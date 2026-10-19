#!/usr/bin/env python3
"""Build cn.json without mixed dotted/nested key loss.

For shared keys, a translation matching an audited v14 English snapshot takes
precedence over a legacy alias. Equal-priority entries retain the historical
folder-name order (last wins). Every conflicting value is recorded for review.
"""
import json
from pathlib import Path
from localization import expand, flatten, read_json

ROOT = Path(__file__).resolve().parent.parent

# Build inputs: modules whose current English snapshots target Foundry v14.
V14_MODULE_IDS = frozenset("""
3d-to-iso 5e-statblock-sheet _chatcommands about-face about-time about-time-next
acdc action-pack-enhanced action-tracker actor-browser actor-token-portraits advanced-macros
aedifs-tactical-grid afk-tavern agnostic-light albo-image-viewer alternative-rotation always-hp
apsj-styles arcane-warding archivist-sync argas-dice-roller arms-reach asset-auditor
asset-librarian asset-preview audio-tagger auraeffects autoanimations autocomplete-inline-properties
automated-conditions-5e automated-evocations avclient-livekit aztecs-rdy-set-go babele bakana-action-display
barbrawl bases batch-media-optimizer bbh bbmm beavers-crafting
beavers-gamepad beavers-mobile beavers-system-interface beneos-module betterroofs bg3-hud-core
bg3-hud-dnd5e blind-death-saves blind-skill-rolls boss-beat boss-loot-assets-free boss-loot-monster-tools
boss-loot-token-manager boss-splash bossbar bounty-board breaktime bsa-dnd5e
bulk-tasks campaign-builder campaign-codex canvas-layers card-hands-list cascade-folder-permissions cat
CautiousGamemastersPack change-log character-chat-selector character-tracker chris-premades chat-media chat-trimmer
chatedit-new chatgpt-item-generator chatlog-prune classic-ui cleaner-sheet-title-bar ClueBook
combat-exhaustion combat-hp-display combat-spell-timer combat-stats combat-theme-expansion-pack combat-tracker-dock
combatbooster complete-card-management conditional-visibility connection-monitor consent-form critically-fumbled
crlngn-ui crunch-my-party crux cs-click-to-scene cursed-energy custom-chat-tabs
custom-css custom-dnd5e custom-group-initiative dae damage-log danger-zone
data-inspector day-night-theme dchat ddb-importer deadly-encounter-benchmark death-effects
dfreds-chat-pins dfreds-convenient-effects dfreds-droppables dfreds-effects-panel dfreds-effects-to-chat dfreds-hidden-token-effects
dfreds-obvious-settings dice-calculator dice-oracles dice-so-nice did-you-hear-that disable-mouse-wheel-sliders
disposition-initiative dnd-easy-reference dnd-randomizer dnd5e-animations dnd5e-combat-difficulty dnd5e-custom-skills
dnd5e-follow-up-save dnd5e-item-resources dnd5e-spellpoints document-tagger door-sounds dorman-lakely-cartography
dorman-lakelys-crit-fumble-tables downtime-dnd5e downtime-manager dragonbane-item-browser droplet dscryb
dungeon-draw dynamic-tokens ear earth-calendar easy-macro-execution easy-regions
easy-token effectivetray-ng effectmacro elliptical-token-shape em-tile-utilities emojify
encounter-forge enhanced-region-behavior enhancedcombathud enhancedcombathud-dnd5e eskie-macros ethereal-plane
ethereal-tokens eventide-speech-mannerisms eventide-teleporter expedition-tracker export-markdown ez-glide
fabricate fabulous-drag-ruler fameosity farchievements farkledice fast-flip
file-manager-dungeons-lab filepicker-memory find-and-replace find-the-culprit flash-rolls-5e fog-weaver
forien-copy-environment foundry-graph foundry-markdown-sheets foundry-mcp-bridge foundry-rest-api foundrystreamoverlay
foundrytodiscord foundryvtt-actor-studio foundryvtt-journal-to-pdf foundryvtt-simple-calendar-reborn fq-card-engine fullsearch
fuzzy-foundry fvtt-challenge-calculator fvtt-delayed-teleport-region fvtt-party-resources fvtt-party-sheet fvtt-perf-optim
fvtt-player-achievements fvtt-player-initiative fxmaster gambitsEmoteBar game_time_clock genga
gg-calendar gg-encounter-lens gg-fog-scout gg-nameforge gg-sheet-export ghorin-light-on
ghorin-toolbar giffyglyph-monster-maker-continued ginzzzu-portraits glitchsmith-lib global-progress-clocks gm-notes
gm-only-tables gm-runic-items gm-screen gm-vision grid-inch-zoom handout-ping-viewer
hasterolls5e healthEstimate heart-containers hero-villain-points hex-size-support hide-icons-vault
hide-npc-names hot-pan how-unfortunate-are-you--dice-counting hurry-up image-z00m imp-counter
improved-player-list indy-dice-stats indy-fx indy-regions indy-walls instant-range
intelligent-npcs interactive-light intoterica ionrift-respite ionrift-waterline ipdip
ironsworn-impacts isometric-perspective item-browser item-delete-check item-piles jd-easytimekeeping
journal-cues journal-icon-numbers journal-styler karma kill-tracker lame-messenger
last-scene-view launchmacro ld-hydez levels levels-3d-preview lib-dfreds-migrations
lib-dfreds-ui-extender lib-item-select-dialog lib-wrapper limited-attenuation-wall limits loading-screen
lobowerewolf-hub lock-the-sheets LocknKey LockView loot-parcels lootforge
map-coords markdown-paste materialdeck-dnd5e micro-map midi-item-showcase-community midi-qol
mini-uploader mkah-compendium-importer mob-attack-tool mobile-companion-dnd5e module-list-export monks-active-tiles
monks-bloodsplats monks-chat-timer monks-combat-details monks-common-display monks-enhanced-journal monks-hotbar-expansion
monks-little-details monks-player-settings monks-scene-navigation monks-sound-enhancements monks-tokenbar monks-wall-enhancement
more-manual-dice-rolls mortal-needs moulinette moulinette-soundboards move-that-for-you multi-token-edit
multiface-tiles multilevel-tokens multiple-document-selection narrator-tools natural-roll niks-dnd5e-tweaks
niks-dynamic-roll-area niks-settings-locks niks-shared-npc-initiative niks-show-and-tell niks-token-tags no-token-vision-animation
notebook notelicker NotYourTurn npc-dialogue-bubbles obs-utils omnipresence
omniscient-die one-journal-handouts oronder osr-character-builder particule-fx party-overview
patrol pause-icon pause-text pause-tweaks pazindor-dev-essentials pazindor-gm-tools
pazindor-token-hotbar pbta-manager pdf-pager perceived-reality perceptive pf2e-reactive-token-ring
pf2e-tokener phantomtokens phils-ai-assistant phils-foundry-ui-tweaks phils-quest-tracker phils-random-names
physical-dice-rolls physics-tools pick-up-stix pinned-chat-message player-pilot playerStatus
playlist-group playlistenchantment playtime-tracker poi-teleport polyglot popout-resizer
portal-lib precise-drawing-tools preload-tracker proximity-voice-chat put-a-ring-on-it quartermaster
quick-insert quick-journal-page-back quick-journal-page-clipboard quick-journal-page-sort quick-module-enable quick-scenes
quick-status-select quickscale raise-my-hand random-loot-generator random-target random-token-names
reactionn-combat-rules regional-deck-draw regionba remote-highlight-ui resize-sidebar rest-recovery
revolutionary-piratenames rhym Rideable rmu-lighting-vision rolecall-sync roll-table-importer
rpgm-forge rpgx-loot-crate rpgx-quest-log runware-imagegen save-tray-5e sc-conditional-activities
sc-conditional-ae sc-more-activities sc-simple-sockets scene-darkness-tools scene-express scene-link-view
scene-loading-screens scene-packer scene-transitions sceneMacros scenery scenes-library
sephrals-content-backup-restore sephrals-file-commander sephrals-image-paste-drop sephrals-module-loadouts sephrals-player-notes sephrals-roll-breakdown
sephrals-roll-triggers sequencer settings-hotkeys settlement-sheets share-media shareddice
sheet-export sheet-only show-image simple-dice-roller simple-mindmap simple-negotiation-tracker
simple-nutrition-5e simple-portrait-organizer simple-requests simple-searchbar simple-shop-craft-5e simplecover5e
simplefog simraki-character-monitor simraki-cursed-items simraki-radial-effects smalltime smart-doors
smartphone-browser-app smartphone-taxi-app smarttarget soundscape-adventure splash splatter
spotlight-omnisearch sprite-animations sprite-shadows stairways statuscounter stealthy
story-teller-x storyflow-dungeons-lab storyframe storyteller-cinema stresspoints-rest student-card
sunder suppress-loading-message swapper swarm swipe-vtt swtextcrawl
syrinscape-control tabbed-journals target-direction-pointer tcal terrainmapper the-horses-encumbrance-controls
theatre theripper-premium-hub tidy5e-sheet tile-scroll toggle-snap-to-grid token-action-hud-core
token-action-hud-dnd5e token-color-marker token-defaults token-elevation-shadows token-hud-wildcard token-lean
token-mirror-button token-mold token-nameplates token-note-hover token-presets token-z
tokenizer-2 tokenmagic tokenmagic-automatic-wounds tokenprofile tokenvisibility tokenwarp
torch transform-cleanup translate-all trap-automator traveller-toolkit trigger-engine
update-your-password video-scaler visage vision-5e vision-blur visual-active-effects
vtta-tokenizer walls-have-ears wanted-level wayfinder wayfinder-auto-grid wayfinder-core
wgtgm-mini-calendar wgtgm-mini-player wgtngm-light-switch wgtngm-mini-edit whisper-as wild-magic-surge-5e
window-controls-next wm5e world-explorer world-lock world-scripter yendors-scene-actors
yendors-user-passwords your-flavor your-turn youtube-sync yt-jukebox yugen-criticals
yugen-downtime yugen-merchant yugen-modifiers yugen-tracker yugen-utils yuuko-chat-interface-overhaul
z-scatter zipperinitiative zone-movement zoom-pan-options
""".split())

def merge_files(mod_dir, records=None):
    current = V14_MODULE_IDS if records is None else {r["id"] for r in records if r["status"] == "source_ready"}
    merged, owners, priorities, sequence = {}, {}, {}, {}
    collisions = []
    files = sorted(mod_dir.rglob("cn.json"), key=lambda p: p.relative_to(mod_dir).as_posix())
    if not files:
        raise ValueError("No module cn.json files found")
    for order, path in enumerate(files):
        relative = path.relative_to(mod_dir)
        module_id = relative.parts[0]
        data = read_json(path)
        if not isinstance(data, dict):
            raise ValueError(f"Not a JSON object: {path}")
        source = mod_dir / module_id / "en.json"
        fresh = flatten(read_json(source)) if module_id in current and len(relative.parts) == 2 and source.exists() else {}
        for key, value in flatten(data).items():
            rank = int(key in fresh)
            wins = key not in merged or rank >= priorities[key]
            if key in merged and merged[key] != value:
                collisions.append({"key": key, "previous": owners[key], "incoming": relative.as_posix(), "winner": relative.as_posix() if wins else owners[key]})
            if wins:
                merged[key], owners[key], priorities[key] = value, relative.as_posix(), rank
                sequence[key] = order
    # A v14 object can replace a legacy scalar (or vice versa). JSON cannot
    # represent both at the same property, so apply the same priority rule.
    removed = set()
    for key in sorted(merged):
        if key in removed:
            continue
        parts = key.split(".")
        for end in range(1, len(parts)):
            parent = ".".join(parts[:end])
            if parent not in merged or parent in removed:
                continue
            child_wins = (priorities[key], sequence[key]) >= (priorities[parent], sequence[parent])
            winner, loser = (key, parent) if child_wins else (parent, key)
            collisions.append({"key": key, "parent_key": parent, "type": "parent_child", "previous": owners[parent], "incoming": owners[key], "winner": owners[winner]})
            removed.add(loser)
            if not child_wins:
                break
    for key in removed:
        del merged[key]
    return expand(merged), collisions, len(files)

def main():
    audit = ROOT / ".cache" / "v14-audit" / "v14-audit.json"
    records = read_json(audit)["modules"] if audit.exists() else None
    merged, collisions, count = merge_files(ROOT / "fvtt mod汉化", records)
    (ROOT / "cn.json").write_text(json.dumps(merged, ensure_ascii=False, indent="\t", sort_keys=True) + "\n", encoding="utf-8")
    report = ROOT / ".cache" / "v14-audit" / "merge-conflicts.json"
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(json.dumps(collisions, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Merged {count} files; {len(flatten(merged))} keys; {len(collisions)} shared-key conflicts recorded")

if __name__ == "__main__":
    main()
