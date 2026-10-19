"""Read the official package registry; cache public manifests and language files.
Never execute downloaded code and never change translations automatically.
"""
import concurrent.futures as cf
import hashlib
import html
import json
import re
import threading
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / '.cache' / 'upstream'
CACHE.mkdir(parents=True, exist_ok=True)
DIRECT = False
LOCAL = threading.local()

def get(url):
    if not url.startswith(('https://', 'http://')):
        raise ValueError('Unsupported URL')
    if not hasattr(LOCAL, 'opener'):
        LOCAL.opener = urllib.request.build_opener(urllib.request.ProxyHandler({}) if DIRECT else urllib.request.ProxyHandler())
    req = urllib.request.Request(url, headers={'User-Agent': 'fvtt-mod-chn-v14-localization-audit/1.0'})
    with LOCAL.opener.open(req, timeout=20) as response:
        data = response.read(12_000_000)
        return data.decode('utf-8-sig'), response.url

def flat(obj, prefix=''):
    result = {}
    for key, value in obj.items():
        key = f'{prefix}.{key}' if prefix else key
        if isinstance(value, dict):
            result.update(flat(value, key))
        else:
            result[key] = value
    return result

def major(v):
    try:
        return int(str(v).split('.')[0])
    except (ValueError, TypeError):
        return 0

def run(folder):
    out = CACHE / folder.name
    out.mkdir(exist_ok=True)
    record = {'id': folder.name, 'package_url': f'https://foundryvtt.com/packages/{urllib.parse.quote(folder.name)}', 'status': 'unresolved'}
    try:
        try:
            page, url = get(record['package_url'])
        except urllib.error.HTTPError as exc:
            if exc.code != 404 or folder.name == folder.name.lower():
                raise
            page, url = get(f'https://foundryvtt.com/packages/{urllib.parse.quote(folder.name.lower())}')
        record['package_url'] = url
        (out / 'page.html').write_text(page, encoding='utf-8')
        chunks = re.findall(r'<li class="package-version[^>]*>(.*?)</li>', page, re.S)
        candidates = []
        for chunk in chunks:
            ver = re.search(r'package-title[^>]*>Version\s+([^<]+)', chunk)
            compat = re.search(r'Foundry Version\s+([^<\n]+)', chunk)
            manifest = re.search(r'href="([^"]+)"\s+title="Manifest Installation URL"', chunk)
            if manifest and compat:
                candidates.append({'version': html.unescape(ver[1]).strip() if ver else '', 'registry_compatibility': html.unescape(compat[1]).strip(), 'manifest_url': html.unescape(manifest[1])})
        record['latest'] = candidates[0] if candidates else None
        eligible = [c for c in candidates if re.search(r'Verified 14(?:[.)])', c['registry_compatibility'])]
        if not eligible:
            record['status'] = 'no_v14_verified_release'
            return record
        # The registry lists newest releases first; use newest explicitly verified v14.
        record.update(eligible[0])
        canonical = record['manifest_url']
        canonical = re.sub(r'https://github.com/([^/]+/[^/]+)/blob/', r'https://raw.githubusercontent.com/\1/', canonical)
        manifest_text, _ = get(canonical)
        manifest_url = canonical
        manifest = json.loads(manifest_text)
        (out / 'module.json').write_text(manifest_text, encoding='utf-8')
        record['manifest_url'] = manifest_url
        record['manifest_version'] = manifest.get('version')
        record['manifest_id'] = manifest.get('id', manifest.get('name'))
        record['compatibility'] = manifest.get('compatibility', {})
        if major(manifest.get('compatibility', {}).get('minimum')) > 14 or (manifest.get('compatibility', {}).get('maximum') and major(manifest['compatibility']['maximum']) < 14):
            record['status'] = 'manifest_excludes_v14'
            return record
        langs = manifest.get('languages', [])
        english = [l for l in langs if l.get('lang','').lower() in ('en', 'en-us', 'en-ca', 'en-gb')]
        english.sort(key=lambda l: l.get('lang') != 'en')
        if not english:
            record['status'] = 'no_english_language_in_manifest'
            return record
        # Relative paths are resolved against the same release, never default branch.
        source = urllib.parse.urljoin(manifest_url, english[0]['path'])
        try:
            en_text, source = get(source)
            en = json.loads(en_text)
        except Exception as exc:
            # A public source file in the SAME release tag is another valid source.
            release = re.search(r'https://github.com/([^/]+/[^/]+)/releases/download/([^/]+)/', canonical)
            recovered = False
            if release:
                for prefix in ('', 'module/'):
                    try:
                        raw = f'https://raw.githubusercontent.com/{release[1]}/{release[2]}/{prefix}{english[0]["path"]}'
                        en_text, source = get(raw)
                        en = json.loads(en_text)
                        recovered = True
                        break
                    except Exception:
                        pass
            # Release assets sit beside module.json in the zip, not on the web.
            download = manifest.get('download', '')
            if not recovered and not download:
                raise exc
            if not recovered:
                import io, zipfile
                with LOCAL.opener.open(download, timeout=40) as response:
                    archive_data = response.read(180_000_000)
                with zipfile.ZipFile(io.BytesIO(archive_data)) as archive:
                    name = english[0]['path'].lstrip('./')
                    matches = [n for n in archive.namelist() if n == name or n.endswith('/' + name)]
                    if len(matches) != 1:
                        raise ValueError(f'Ambiguous/missing archive language: {matches}')
                    if archive.getinfo(matches[0]).file_size > 12_000_000:
                        raise ValueError('Language file too large')
                    en_text = archive.read(matches[0]).decode('utf-8-sig')
                    en = json.loads(en_text)
                    source = download + '#' + matches[0]
        if not isinstance(en, dict):
            raise ValueError('English language is not an object')
        (out / 'en.json').write_text(en_text, encoding='utf-8')
        record.update({'status': 'source_ready', 'english_url': source, 'english_sha256': hashlib.sha256(en_text.encode()).hexdigest(), 'english_keys': len(flat(en))})
        native = [l for l in langs if l.get('lang','').lower() in ('cn', 'zh-cn', 'zh')]
        if native:
            try:
                cn_text, cn_source = get(urllib.parse.urljoin(manifest_url, native[0]['path']))
                json.loads(cn_text)
                (out / 'cn.json').write_text(cn_text, encoding='utf-8')
                record['native_chinese_url'] = cn_source
            except Exception:
                pass
    except Exception as exc:
        record['error'] = f'{type(exc).__name__}: {exc}'
        record['status'] = 'fetch_failed'
    finally:
        (out / 'record.json').write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding='utf-8')
    return record

if __name__ == '__main__':
    import argparse, collections
    parser = argparse.ArgumentParser()
    parser.add_argument('--direct', action='store_true', help='Ignore configured network proxies')
    parser.add_argument('--retry', action='store_true')
    parser.add_argument('--workers', type=int, default=10)
    args = parser.parse_args()
    DIRECT = args.direct
    folders = sorted(p for p in (ROOT / 'fvtt mod汉化').iterdir() if p.is_dir())
    if args.retry:
        folders = [p for p in folders if not (CACHE/p.name/'record.json').exists() or json.loads((CACHE/p.name/'record.json').read_text(encoding='utf-8'))['status'] in ('fetch_failed','unresolved')]
    print(f'Auditing {len(folders)} packages', flush=True)
    counter = collections.Counter()
    with cf.ThreadPoolExecutor(max_workers=args.workers) as pool:
        for i, r in enumerate(pool.map(run, folders), 1):
            counter[r['status']] += 1
            if i % 25 == 0 or i == len(folders):
                print(f'{i}/{len(folders)} {dict(counter)}', flush=True)
    records = [json.loads(p.read_text(encoding='utf-8')) for p in sorted(CACHE.glob('*/record.json'))]
    (CACHE/'audit.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
