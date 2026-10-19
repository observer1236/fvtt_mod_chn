import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import vm from "node:vm";
import test from "node:test";

const source = readFileSync(new URL("../welcome.js", import.meta.url), "utf8");
function fixture({ mega = false, gm = true, confirm = false, action = "ok", welcomed = false, version = 0 } = {}) {
    const callbacks = new Map();
    const values = new Map([["zzz_mod_chn.welcomed", welcomed], ["zzz_mod_chn.listver", version]]);
    const config = { zzzzz_mega_chn: true, other: true };
    const writes = [];
    const dialogs = [];
    let reloads = 0;
    vm.runInNewContext(source, {
        Hooks: { once: (name, fn) => callbacks.set(name, fn) },
        game: {
            user: { isGM: gm },
            modules: new Map([["zzzzz_mega_chn", { active: mega }]]),
            settings: {
                register: (namespace, key) => assert.equal(namespace, "zzz_mod_chn"),
                get: (ns, key) => ns === "core" ? config : values.get(`${ns}.${key}`),
                set: async (ns, key, value) => { writes.push([ns, key, value]); values.set(`${ns}.${key}`, value); }
            }
        },
        foundry: { applications: { api: { DialogV2: {
            confirm: async options => { dialogs.push(["confirm", options]); return confirm; },
            wait: async options => { dialogs.push(["wait", options]); return action; }
        } } } },
        window: { location: { reload: () => reloads++ } }
    });
    return { callbacks, values, config, writes, dialogs, get reloads() { return reloads; } };
}
test("registers installed id and uses DialogV2", async () => {
    const f = fixture();
    f.callbacks.get("init")();
    await f.callbacks.get("ready")();
    assert.equal(f.dialogs[0][0], "wait");
    assert.equal(f.values.get("zzz_mod_chn.listver"), 7);
});
test("dismiss persists preference; subsequent launch stays quiet", async () => {
    const f = fixture({ action: "dismiss" });
    await f.callbacks.get("ready")();
    assert.equal(f.values.get("zzz_mod_chn.welcomed"), true);
    const quiet = fixture({ welcomed: true, version: 7 });
    await quiet.callbacks.get("ready")();
    assert.equal(quiet.dialogs.length, 0);
});
test("closing welcome does not write preferences", async () => {
    const f = fixture({ action: null });
    await f.callbacks.get("ready")();
    assert.equal(f.writes.length, 0);
});
for (const confirm of [false, null]) {
    test(`declining/closing conflict dialog (${confirm}) keeps configuration`, async () => {
        const f = fixture({ mega: true, confirm });
        await f.callbacks.get("ready")();
        assert.equal(f.reloads, 0);
        assert.equal(f.writes.filter(w => w[0] === "core").length, 0);
        assert.equal(f.config.zzzzz_mega_chn, true);
    });
}
test("confirmation changes only Mega flag then reloads", async () => {
    const f = fixture({ mega: true, confirm: true });
    await f.callbacks.get("ready")();
    const [ns, key, value] = f.writes[0];
    assert.equal(ns, "core");
    assert.equal(key, "moduleConfiguration");
    assert.equal(value.zzzzz_mega_chn, false);
    assert.equal(value.other, true);
    assert.equal(f.config.zzzzz_mega_chn, true);
    assert.equal(f.reloads, 1);
    assert.equal(f.dialogs.length, 1);
});
test("players never change module configuration", async () => {
    const f = fixture({ mega: true, gm: false, confirm: true });
    await f.callbacks.get("ready")();
    assert.equal(f.dialogs.some(d => d[0] === "confirm"), false);
    assert.equal(f.writes.some(w => w[0] === "core"), false);
});
