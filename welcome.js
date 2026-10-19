const MODULE_NAME = "zzz_mod_chn";
const LIST_VERSION = 7;

Hooks.once("init", () => {
    game.settings.register(MODULE_NAME, "welcomed", {
        name: "不再显示欢迎信息",
        scope: "client",
        config: false,
        type: Boolean,
        default: false
    });
    game.settings.register(MODULE_NAME, "listver", {
        name: "欢迎信息版本",
        scope: "client",
        config: false,
        type: Number,
        default: 0
    });
});

Hooks.once("ready", async () => {
    const { DialogV2 } = foundry.applications.api;
    const oldModId = "zzzzz_mega_chn";

    if (game.user.isGM && game.modules.get(oldModId)?.active) {
        const disable = await DialogV2.confirm({
            window: { title: "汉化包冲突" },
            content: "<p>同时启用 Mega 翻译整合包和 Mod 翻译包可能导致文本相互覆盖。是否禁用 Mega 翻译整合包并刷新？</p>",
            yes: { label: "禁用并刷新" },
            no: { label: "暂时保留" },
            rejectClose: false
        });
        if (disable) {
            const configuration = { ...game.settings.get("core", "moduleConfiguration") };
            configuration[oldModId] = false;
            await game.settings.set("core", "moduleConfiguration", configuration);
            window.location.reload();
            return;
        }
    }

    const welcomed = game.settings.get(MODULE_NAME, "welcomed");
    const listVersion = game.settings.get(MODULE_NAME, "listver");
    if (welcomed && listVersion >= LIST_VERSION) return;

    const action = await DialogV2.wait({
        window: { title: "Foundry VTT Mod 翻译包" },
        content: `
            <h2>欢迎使用 Mod 翻译包</h2>
            <p>这是面向 Foundry VTT v14 的候选版本。新增译文包含机器翻译，仍需人工校对及实机验证。</p>
            <p>各模块的上游版本、词条覆盖率及未完成项目见仓库中的 v14 适配报告。汉化包不能修复原模块自身的 v14 兼容问题。</p>
            <p><a href="https://github.com/observer1236/fvtt_mod_chn">项目仓库及适配报告</a></p>
        `,
        buttons: [
            { action: "ok", label: "确定", default: true },
            { action: "dismiss", label: "不再显示" }
        ],
        rejectClose: false
    });
    if (action === null) return;
    if (action === "dismiss") await game.settings.set(MODULE_NAME, "welcomed", true);
    await game.settings.set(MODULE_NAME, "listver", LIST_VERSION);
});
