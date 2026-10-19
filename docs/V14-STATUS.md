# v14 汉化候选版适配报告

核对日期：2026-10-19。目标：Foundry VTT **14.369**。版本：**14.0.0-beta.1**。

这是一份可供测试和校对的候选更新，不能视为全部 950 个模块均已适配 v14。汉化包不修改各模块的功能代码，也不能使未适配 v14 的原模块正常运行。

| 核对结果 | 数量 |
| --- | ---: |
| 已同步 v14 语言文件（待实机验证） | 532 |
| 未找到官方目录中 Verified 14 的发布版，保留原译 | 318 |
| 上游资源读取失败，保留原译 | 88 |
| v14 清单未声明英文语言文件，保留原译 | 11 |
| 清单兼容范围排除 v14，保留原译 | 1 |

532 份上游英文快照包含 **77,574 个键**，本地对应词条无缺失，变量占位符检查无错误。实际更新 176 个模块中的 **14,467 条译文**；其余可获取模块沿用仍有效的原译。键覆盖完整不等于译文质量或运行兼容性已完成验证。

此次处理记录含 2,596 条已有或上游中文译文复用、11,872 条机器翻译候选、21 条手工处理、2 条非翻译元数据。11,872 是按模块/键计数，包含多个模块复用同一英文字符串的情况。机器翻译由 Google Translate 生成，应用了 FVTT/5e 术语表、占位符和标记保护，仍需人工逐条校对。已有英文专名、URL、代码及本轮未变化的旧译可能仍包含英文；本轮没有声称对全部旧译进行重新人工校对。

## 来源与核对规则

- 从 Foundry 官方模块目录逐一核对全部 950 个顶层模块目录（共有 951 个 cn.json，包含原仓库一个嵌套目录）。选择目录中最新的 Verified 14 发布记录，并读取对应清单及语言文件。
- 记录目录版本与实际清单版本。少数上游链接指向 latest 或可变分支，二者可能不同；报告保留两者和实际英文 SHA-256，以明确本次使用的快照。
- 上游自带中文仅用于本轮需要补充/更新的条目；其余保留原译。保留不妨碍新结构的旧键以支持原有词条引用；清理一处阻碍新对象结构的旧标量键。
- 88 项读取失败包括失效页面/下载、未公开或付费资源。没有绕过登录、付费或访问限制。318 项只表示未找到官方 Verified 14 记录，不等于已证明该模块完全不能在 v14 运行。
- 清理了原始 JSON 中 57 个重复成员，保留 JSON 解析器原本生效的最后一个值；另规范了 danger-zone 中重复表达的点号/嵌套键。

## 运行与打包改动

- 欢迎窗口使用 foundry.applications.api.DialogV2，设置命名空间与实际安装 ID zzz_mod_chn 一致。
- Mega 汉化冲突窗口只有明确确认后才更改模块配置；取消、关闭窗口或普通玩家连接不会禁用模块。
- 统一展开点号与嵌套语言键；合并时优先采用本次 v14 英文快照中存在的键，避免旧别名覆盖新版译文。707 次不同值的共享键冲突及取舍见 merge-conflicts.json。共享命名空间仍可能产生语义差异，需结合实际启用的模块检查。
- 清单指向此 fork 的候选版本下载地址；只有正式创建对应 GitHub Release 并上传附件后，清单安装链接才可使用。当前本地压缩包可手动安装。
- compatibility.minimum 设为 14，未填写 verified。完成真实 Foundry 会话验证之前，不宣称已经过实机验证。

## 验证结果与待办

已通过：1,883 份语言/模块 JSON 的解析及重复键检查、950 个目录清单完整性、532 份英文快照哈希、77,574 个上游键对应词条和占位符、本轮处理译文的 HTML/URL/行内代码保留、5 项 Python 测试和 7 项 JavaScript API 模拟测试。

尚未完成：在真实 Foundry 14.369 世界中启动验证；对 11,872 条机器翻译逐条人工校对；解决剩余 418 个模块的上游版本或资源限制；对模块共享命名空间冲突进行实际组合测试。本轮没有运行世界迁移或测试原模块功能代码。

建议实机验收：中文环境启动并检查控制台；打开已启用模块设置页；抽测 Midi-QOL、DAE、Dice So Nice、Tidy5e Sheet 等实际使用的模块；验证取消冲突提示和“不再显示”；确认没有出现原始语言键、插值变量或布局损坏。

## 维护与复现

构建安装包：`python scripts/build_release.py`。

离线检查：`python -m unittest discover -s tests -p "test_*.py"`、`node --test tests/welcome.test.mjs`、`python scripts/validate_v14.py`。validate_v14.py 需要先生成根目录 cn.json。

重新查询上游：`python scripts/audit_v14.py`；需要忽略本机代理时增加 `--direct`。公开资源缓存至 .cache/upstream，该只读命令不会自动覆盖已提交的快照或译文。后续更新应比较快照、人工复核变更，再同步更新 v14-audit.json 中的哈希与校对记录。

机器翻译待审键和本轮处理方式见 v14-translation-review.json。逐模块来源、错误及哈希见 v14-audit.json。

## 全部模块

| 模块目录 | 官方目录版本 / 实际清单版本 | 上游键 | 更新译文 | 机器翻译待审 | 状态 |
| --- | --- | ---: | ---: | ---: | --- |
| [3d-to-iso](https://foundryvtt.com/packages/3d-to-iso) | 0.5.0 / 0.5.0 | 74 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [44s-vso](https://foundryvtt.com/packages/44s-vso) | 0.1.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [5e-spellblock-importer](https://foundryvtt.com/packages/5e-spellblock-importer) | 1.14.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [5e-statblock-sheet](https://foundryvtt.com/packages/5e-statblock-sheet) | 1.4.4 / 1.4.4 | 13 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [5edndnpc](https://foundryvtt.com/packages/5edndnpc) | v1.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [_chatcommands](https://foundryvtt.com/packages/_chatcommands) | 2.0.6 / 2.0.6 | 34 | 7 | 7 | 已同步 v14 语言文件（待实机验证） |
| [about-face](https://foundryvtt.com/packages/about-face) | 3.30.0 / 3.30.0 | 43 | 2 | 2 | 已同步 v14 语言文件（待实机验证） |
| [about-time](https://foundryvtt.com/packages/about-time) | 14.0.1 / 14.0.1 | 38 | 2 | 0 | 已同步 v14 语言文件（待实机验证） |
| [about-time-next](https://foundryvtt.com/packages/about-time-next) | 14.0.0.0 / 14.0.0.0 | 47 | 2 | 2 | 已同步 v14 语言文件（待实机验证） |
| [acd-talking-actors](https://foundryvtt.com/packages/acd-talking-actors) | 1.0.5 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [acdc](https://foundryvtt.com/packages/acdc) | 14.365.1 / 14.365.1 | 33 | 29 | 21 | 已同步 v14 语言文件（待实机验证） |
| [action-pack-enhanced](https://foundryvtt.com/packages/action-pack-enhanced) | 1.4.2 / 1.4.2 | 161 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [action-tracker](https://foundryvtt.com/packages/action-tracker) | 14.0.1 / 14.0.1 | 68 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [active-character-portrait](https://foundryvtt.com/packages/active-character-portrait) | 1.5 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [ActiveAuras](https://foundryvtt.com/packages/ActiveAuras) | 0.12.7 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [activity-macro](https://foundryvtt.com/packages/activity-macro) | 1.2.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [actor-browser](https://foundryvtt.com/packages/actor-browser) | 1.5.0 / 1.5.0 | 49 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [actor-export](https://foundryvtt.com/packages/actor-export) | 2026.9.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [actor-journal-helper](https://foundryvtt.com/packages/actor-journal-helper) | v1.1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [actor-token-portraits](https://foundryvtt.com/packages/actor-token-portraits) | 1.0.1 / 1.0.1 | 10 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [actually-private-rolls](https://foundryvtt.com/packages/actually-private-rolls) | 1.6.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [adaptive-audio](https://foundryvtt.com/packages/adaptive-audio) | 0.1.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [adv-reminder](https://foundryvtt.com/packages/adv-reminder) | 5.1.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [advanced-macros](https://foundryvtt.com/packages/advanced-macros) | 2.4.0 / 2.4.0 | 8 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [adventure-bundler](https://foundryvtt.com/packages/adventure-bundler) | 0.2.6 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [aedifs-compendium-search](https://foundryvtt.com/packages/aedifs-compendium-search) | 2.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [aedifs-snap-me-maybe](https://foundryvtt.com/packages/aedifs-snap-me-maybe) | 2.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [aedifs-tactical-grid](https://foundryvtt.com/packages/aedifs-tactical-grid) | 2.6.2 / 2.6.2 | 76 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [afk-tavern](https://foundryvtt.com/packages/afk-tavern) | 1.1.1 / 1.1.1 | 298 | 33 | 32 | 已同步 v14 语言文件（待实机验证） |
| [agnostic-light](https://foundryvtt.com/packages/agnostic-light) | 2.0.02 / 2.0.02 | 49 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [albo-image-viewer](https://foundryvtt.com/packages/albo-image-viewer) | 1.2.0 / 1.2.0 | 37 | 2 | 2 | 已同步 v14 语言文件（待实机验证） |
| [alignment-tracker](https://foundryvtt.com/packages/alignment-tracker) | v1.0.4 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [alpha-5](https://foundryvtt.com/packages/alpha-5) | 3.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [alter-ego](https://foundryvtt.com/packages/alter-ego) | 1.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [alternative-rotation](https://foundryvtt.com/packages/alternative-rotation) | 2.3.4 / 2.3.4 | 14 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [always-chat](https://foundryvtt.com/packages/always-chat) | 1.0.3 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [always-hp](https://foundryvtt.com/packages/always-hp) | 14.01 / 14.01 | 59 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [anonymous](https://foundryvtt.com/packages/anonymous) | 1.6.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [apsj-styles](https://foundryvtt.com/packages/apsj-styles) | 4.0.0 / 4.0.0 | 144 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [arcane-warding](https://foundryvtt.com/packages/arcane-warding) | 1.2.27 / 1.2.27 | 61 | 3 | 2 | 已同步 v14 语言文件（待实机验证） |
| [archive-tab](https://foundryvtt.com/packages/archive-tab) | 0.1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [archivist-sync](https://foundryvtt.com/packages/archivist-sync) | 2.0.5 / 2.0.5 | 243 | 2 | 2 | 已同步 v14 语言文件（待实机验证） |
| [archon](https://foundryvtt.com/packages/archon) | 1.2.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [argas-dice-roller](https://foundryvtt.com/packages/argas-dice-roller) | 14.2.1 / 14.2.1 | 325 | 51 | 50 | 已同步 v14 语言文件（待实机验证） |
| [arms-reach](https://foundryvtt.com/packages/arms-reach) | 14.0.0 / 14.0.0 | 180 | 1 | 1 | 已同步 v14 语言文件（待实机验证） |
| [asset-auditor](https://foundryvtt.com/packages/asset-auditor) | 2.0.3 / 2.0.3 | 17 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [asset-librarian](https://foundryvtt.com/packages/asset-librarian) | 1.4.6 / 1.4.6 | 270 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [asset-preview](https://foundryvtt.com/packages/asset-preview) | 0.1.2 / 0.1.2 | 7 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [audio-tagger](https://foundryvtt.com/packages/audio-tagger) | 1.5.4 / 1.5.4 | 119 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [auraeffects](https://foundryvtt.com/packages/auraeffects) | 2.2.3 / 2.2.3 | 54 | 4 | 4 | 已同步 v14 语言文件（待实机验证） |
| [autoanimations](https://foundryvtt.com/packages/autoanimations) | 7.1.8 / 7.1.8 | 717 | 2 | 2 | 已同步 v14 语言文件（待实机验证） |
| [autocomplete-inline-properties](https://foundryvtt.com/packages/autocomplete-inline-properties) | 3.3.0 / 3.3.0 | 5 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [autocomplete-mentions](https://foundryvtt.com/packages/autocomplete-mentions) | 2.4.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [automated-animations-for-all](https://foundryvtt.com/packages/automated-animations-for-all) | 0.0.3 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [automated-conditions-5e](https://foundryvtt.com/packages/automated-conditions-5e) | 14.606.4 / 14.606.4 | 496 | 248 | 224 | 已同步 v14 语言文件（待实机验证） |
| [automated-crafted-creations](https://foundryvtt.com/packages/automated-crafted-creations) | 0.0.13 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [automated-evocations](https://foundryvtt.com/packages/automated-evocations) | 6.0.0 / 6.0.0 | 42 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [automated-polymorpher](https://foundryvtt.com/packages/automated-polymorpher) | 1.1.12 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [avclient-livekit](https://foundryvtt.com/packages/avclient-livekit) | 0.6.6 / 0.6.8 | 84 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [aztecs-rdy-set-go](https://foundryvtt.com/packages/aztecs-rdy-set-go) | 1.1.0 / 1.1.0 | 121 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [babele](https://foundryvtt.com/packages/babele) | 2.9.1 / 2.9.1 | 102 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [babonus](https://foundryvtt.com/packages/babonus) | 12.5.8 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [background-volume](https://foundryvtt.com/packages/background-volume) | 1.7.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [backpack](https://foundryvtt.com/packages/backpack) | 2.0.1 / 2.0.1 | — | — | — | 上游资源读取失败，保留原译 |
| [bakana-action-display](https://foundryvtt.com/packages/bakana-action-display) | 1.3.0 / 1.3.0 | 195 | 152 | 132 | 已同步 v14 语言文件（待实机验证） |
| [banestorm-name-generator](https://foundryvtt.com/packages/banestorm-name-generator) | 0.0.3 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [bank-module](https://foundryvtt.com/packages/bank-module) | 3.0.1 / 3.0.1 | — | — | — | 上游资源读取失败，保留原译 |
| [barbrawl](https://foundryvtt.com/packages/barbrawl) | 1.9.4 / 1.9.4 | 95 | 5 | 4 | 已同步 v14 语言文件（待实机验证） |
| [bases](https://foundryvtt.com/packages/bases) | 14.367.1 / 14.367.1 | 15 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [batch-media-optimizer](https://foundryvtt.com/packages/batch-media-optimizer) | 1.4.0 / 1.4.0 | 78 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [battle-transitions](https://foundryvtt.com/packages/battle-transitions) | 2.0.14 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [bbh](https://foundryvtt.com/packages/bbh) | 13.533.4 / 13.533.4 | 105 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [bbmm](https://foundryvtt.com/packages/bbmm) | 1.4.11 / 1.4.11 | 525 | 1 | 1 | 已同步 v14 语言文件（待实机验证） |
| [bd-tiles](https://foundryvtt.com/packages/bd-tiles) | 1.0.3 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [beavers-crafting](https://foundryvtt.com/packages/beavers-crafting) | 4.7.0 / 4.7.0 | 122 | 15 | 12 | 已同步 v14 语言文件（待实机验证） |
| [beavers-gamepad](https://foundryvtt.com/packages/beavers-gamepad) | 3.1.0 / 3.1.0 | 53 | 43 | 40 | 已同步 v14 语言文件（待实机验证） |
| [beavers-mobile](https://foundryvtt.com/packages/beavers-mobile) | 3.0.1 / 3.0.1 | 6 | 6 | 5 | 已同步 v14 语言文件（待实机验证） |
| [beavers-system-interface](https://foundryvtt.com/packages/beavers-system-interface) | 2.3.5 / 2.3.5 | 25 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [beneos-module](https://foundryvtt.com/packages/beneos-module) | 14.4.10 / 14.4.10 | 2462 | 47 | 44 | 已同步 v14 语言文件（待实机验证） |
| [better-turn-markers](https://foundryvtt.com/packages/better-turn-markers) | 1.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [betterroofs](https://foundryvtt.com/packages/betterroofs) | 4.0.2 / 4.0.2 | 7 | 2 | 2 | 已同步 v14 语言文件（待实机验证） |
| [bg3-hud-core](https://foundryvtt.com/packages/bg3-hud-core) | 0.8.0 / 0.8.0 | 267 | 18 | 18 | 已同步 v14 语言文件（待实机验证） |
| [bg3-hud-dnd5e](https://foundryvtt.com/packages/bg3-hud-dnd5e) | 0.8.0 / 0.8.0 | 173 | 3 | 3 | 已同步 v14 语言文件（待实机验证） |
| [bg3-inspired-hotbar](https://foundryvtt.com/packages/bg3-inspired-hotbar) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [bing-bong](https://foundryvtt.com/packages/bing-bong) | 0.1.3 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [blind-death-saves](https://foundryvtt.com/packages/blind-death-saves) | 14.1 / 14.1 | 4 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [blind-skill-rolls](https://foundryvtt.com/packages/blind-skill-rolls) | 1.4.2 / 1.4.2 | 156 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [boss-beat](https://foundryvtt.com/packages/boss-beat) | 1.9.1 / 1.9.1 | 41 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [boss-loot-assets-free](https://foundryvtt.com/packages/boss-loot-assets-free) | 2.4.9 / 2.4.9 | 131 | 1 | 1 | 已同步 v14 语言文件（待实机验证） |
| [boss-loot-assets-premium](https://foundryvtt.com/packages/boss-loot-assets-premium) | 3.5.4 / 3.5.4 | — | — | — | 上游资源读取失败，保留原译 |
| [boss-loot-monster-tools](https://foundryvtt.com/packages/boss-loot-monster-tools) | 1.0.0 / 1.0.0 | 102 | 2 | 0 | 已同步 v14 语言文件（待实机验证） |
| [boss-loot-token-manager](https://foundryvtt.com/packages/boss-loot-token-manager) | 1.1.3 / 1.1.3 | 32 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [boss-splash](https://foundryvtt.com/packages/boss-splash) | 1.2.3 / 1.2.3 | 45 | 1 | 0 | 已同步 v14 语言文件（待实机验证） |
| [bossbar](https://foundryvtt.com/packages/bossbar) | 5.0.1 / 5.0.1 | 40 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [bottlecap](https://foundryvtt.com/packages/bottlecap) | v3.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [bounty-board](https://foundryvtt.com/packages/bounty-board) | 1.1.0 / 1.1.0 | 61 | 6 | 6 | 已同步 v14 语言文件（待实机验证） |
| [breaktime](https://foundryvtt.com/packages/breaktime) | 14.01 / 14.01 | 47 | 4 | 4 | 已同步 v14 语言文件（待实机验证） |
| [bsa-dnd5e](https://foundryvtt.com/packages/bsa-dnd5e) | 2.2.0 / 2.2.0 | 8 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [bugbears-harvester](https://foundryvtt.com/packages/bugbears-harvester) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [bugs](https://foundryvtt.com/packages/bugs) | 13.5330.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [bulk-tasks](https://foundryvtt.com/packages/bulk-tasks) | 0.6.4 / 0.6.4 | 30 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [bx-factions](https://foundryvtt.com/packages/bx-factions) | 0.3.9 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [calendaria](https://foundryvtt.com/packages/calendaria) | 1.4.5 / 1.4.5 | — | — | — | v14 清单未声明英文语言文件，保留原译 |
| [campaign-builder](https://foundryvtt.com/packages/campaign-builder) | 1.10.6 / 1.10.6 | 942 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [campaign-codex](https://foundryvtt.com/packages/campaign-codex) | 6.9.971 / 6.9.971 | 775 | 192 | 159 | 已同步 v14 语言文件（待实机验证） |
| [canvas-layers](https://foundryvtt.com/packages/canvas-layers) | 2.0.0 / 2.0.0 | 60 | 1 | 1 | 已同步 v14 语言文件（待实机验证） |
| [card-deck-initiative](https://foundryvtt.com/packages/card-deck-initiative) | 1.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [card-hands-list](https://foundryvtt.com/packages/card-hands-list) | 2.2.7 / 2.2.7 | 31 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [cascade-folder-permissions](https://foundryvtt.com/packages/cascade-folder-permissions) | 0.1.5 / 0.1.5 | 7 | 1 | 1 | 已同步 v14 语言文件（待实机验证） |
| [CautiousGamemastersPack](https://foundryvtt.com/packages/CautiousGamemastersPack) | 1.12.1 / 1.12.1 | 22 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [celebrate](https://foundryvtt.com/packages/celebrate) | v1.6.4 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [challenge-tracker](https://foundryvtt.com/packages/challenge-tracker) | 3.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [change-log](https://foundryvtt.com/packages/change-log) | 1.4.1 / 1.4.1 | 78 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [character-chat-selector](https://foundryvtt.com/packages/character-chat-selector) | 3.5.1 / 3.5.1 | 129 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [character-tracker](https://foundryvtt.com/packages/character-tracker) | 1.1.0 / 1.1.0 | 21 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [charlemos-camera-layout](https://foundryvtt.com/packages/charlemos-camera-layout) | 2.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [chat-images](https://foundryvtt.com/packages/chat-images) | 3.3 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [chat-media](https://foundryvtt.com/packages/chat-media) | 14.0.1 / 14.0.1 | 17 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [chat-portrait](https://foundryvtt.com/packages/chat-portrait) | 13.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [chat-select](https://foundryvtt.com/packages/chat-select) | 1.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [chat-tabs](https://foundryvtt.com/packages/chat-tabs) | 1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [chat-timestamp](https://foundryvtt.com/packages/chat-timestamp) | 0.2.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [chat-trimmer](https://foundryvtt.com/packages/chat-trimmer) | 2.1.1 / 2.1.1 | 85 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [chatedit-new](https://foundryvtt.com/packages/chatedit-new) | v0.0.45 / 0.0.45 | 22 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [chatgpt-item-generator](https://foundryvtt.com/packages/chatgpt-item-generator) | 2.3.3 / 2.3.3 | 7 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [chatlog-prune](https://foundryvtt.com/packages/chatlog-prune) | 1.1.11 / 1.1.11 | 14 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [chess](https://foundryvtt.com/packages/chess) | 1.0.4 / 1.0.4 | — | — | — | 上游资源读取失败，保留原译 |
| [chris-premades](https://foundryvtt.com/packages/chris-premades) | 1.5.50 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [chronicle-keeper](https://foundryvtt.com/packages/chronicle-keeper) | v1.1.4 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [cinematic-cut-ins](https://foundryvtt.com/packages/cinematic-cut-ins) | 2.0.8 / 2.0.8 | — | — | — | 上游资源读取失败，保留原译 |
| [classic-ui](https://foundryvtt.com/packages/classic-ui) | 2.0.8 / 2.0.8 | 14 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [cleaner-sheet-title-bar](https://foundryvtt.com/packages/cleaner-sheet-title-bar) | 2.0 / 2.0 | 2 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [clock-works](https://foundryvtt.com/packages/clock-works) | 1.5.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [ClueBook](https://foundryvtt.com/packages/ClueBook) | 2.0.1 / 2.0.1 | 592 | 202 | 158 | 已同步 v14 语言文件（待实机验证） |
| [colorsettings](https://foundryvtt.com/packages/colorsettings) | 3.0.4 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [combat-chat](https://foundryvtt.com/packages/combat-chat) | 2.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [combat-enhancements](https://foundryvtt.com/packages/combat-enhancements) | 1.3.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [combat-exhaustion](https://foundryvtt.com/packages/combat-exhaustion) | 1.7.0 / 1.7.0 | 40 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [combat-hp-display](https://foundryvtt.com/packages/combat-hp-display) | 1.6.0 / 1.6.0 | 19 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [combat-spell-timer](https://foundryvtt.com/packages/combat-spell-timer) | 2.3.0 / 2.3.0 | 100 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [combat-stats](https://foundryvtt.com/packages/combat-stats) | 4.0.0 / 4.0.0 | 157 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [combat-theme-expansion-pack](https://foundryvtt.com/packages/combat-theme-expansion-pack) | 0.3.1 / 0.3.1 | 9 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [combat-tracker-dock](https://foundryvtt.com/packages/combat-tracker-dock) | 5.0.2 / 5.0.2 | 133 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [combat-tracker-extensions](https://foundryvtt.com/packages/combat-tracker-extensions) | 1.4 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [combatbooster](https://foundryvtt.com/packages/combatbooster) | 6.0.1 / 6.0.1 | 53 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [compact-scene-navigation](https://foundryvtt.com/packages/compact-scene-navigation) | 1.0.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [complete-card-management](https://foundryvtt.com/packages/complete-card-management) | 3.0.3 / 3.0.3 | 101 | 1 | 1 | 已同步 v14 语言文件（待实机验证） |
| [condition-lab-triggler](https://foundryvtt.com/packages/condition-lab-triggler) | 2.1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [conditional-visibility](https://foundryvtt.com/packages/conditional-visibility) | 1.1.1 / 1.1.1 | 1 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [connected-permission](https://foundryvtt.com/packages/connected-permission) | 1.0.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [connection-monitor](https://foundryvtt.com/packages/connection-monitor) | 1.8.0 / 1.8.0 | 3 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [consent-form](https://foundryvtt.com/packages/consent-form) | 3.2.2 / 3.2.2 | 480 | 167 | 157 | 已同步 v14 语言文件（待实机验证） |
| [console](https://foundryvtt.com/packages/console) | 1.9.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [conversation-hud](https://foundryvtt.com/packages/conversation-hud) | 6.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [cooking-pot](https://foundryvtt.com/packages/cooking-pot) | 1.5.5 / 1.5.5 | — | — | — | 上游资源读取失败，保留原译 |
| [critically-fumbled](https://foundryvtt.com/packages/critically-fumbled) | 1.1.1 / 1.1.1 | 67 | 58 | 52 | 已同步 v14 语言文件（待实机验证） |
| [crlngn-ui](https://foundryvtt.com/packages/crlngn-ui) | 4.6.0 / 4.6.0 | 579 | 93 | 4 | 已同步 v14 语言文件（待实机验证） |
| [crunch-my-party](https://foundryvtt.com/packages/crunch-my-party) | 14.1.0 / 14.1.0 | 85 | 5 | 5 | 已同步 v14 语言文件（待实机验证） |
| [crux](https://foundryvtt.com/packages/crux) | 2.2.5 / 2.2.5 | 140 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [cs-click-to-scene](https://foundryvtt.com/packages/cs-click-to-scene) | 2.0.3 / 2.0.3 | 4 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [csv-importer](https://foundryvtt.com/packages/csv-importer) | 1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [cursed-energy](https://foundryvtt.com/packages/cursed-energy) | 1.0.0 / 1.0.0 | 96 | 84 | 84 | 已同步 v14 语言文件（待实机验证） |
| [cursor-hider](https://foundryvtt.com/packages/cursor-hider) | 1.3.4 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [custom-browser-tab](https://foundryvtt.com/packages/custom-browser-tab) | 1.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [custom-character-sheet-sections](https://foundryvtt.com/packages/custom-character-sheet-sections) | 2.1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [custom-chat-tabs](https://foundryvtt.com/packages/custom-chat-tabs) | 1.1.3 / 1.1.3 | 35 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [custom-css](https://foundryvtt.com/packages/custom-css) | 2.4.4 / 2.4.4 | 17 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [custom-dnd5e](https://foundryvtt.com/packages/custom-dnd5e) | 5.6.0 / 5.6.0 | 1436 | 680 | 592 | 已同步 v14 语言文件（待实机验证） |
| [custom-fields](https://foundryvtt.com/packages/custom-fields) | 0.0.5 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [custom-group-initiative](https://foundryvtt.com/packages/custom-group-initiative) | 14.361.1 / 14.361.1 | 6 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [cutin-manager](https://foundryvtt.com/packages/cutin-manager) | 1.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [dae](https://foundryvtt.com/packages/dae) | 14.0.18 / 14.0.18 | 1513 | 50 | 42 | 已同步 v14 语言文件（待实机验证） |
| [damage-log](https://foundryvtt.com/packages/damage-log) | 1.33.0 / 1.33.0 | 67 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [danger-zone](https://foundryvtt.com/packages/danger-zone) | 2.1.1 / 2.1.1 | 899 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [data-inspector](https://foundryvtt.com/packages/data-inspector) | 5.4.0 / 5.4.0 | 94 | 10 | 5 | 已同步 v14 语言文件（待实机验证） |
| [data-storage](https://foundryvtt.com/packages/data-storage) | 1.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [day-night-theme](https://foundryvtt.com/packages/day-night-theme) | 1.0.0 / 1.0.0 | 8 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [dchat](https://foundryvtt.com/packages/dchat) | 1.7.3 / 1.7.3 | 66 | 66 | 51 | 已同步 v14 语言文件（待实机验证） |
| [ddb-importer](https://foundryvtt.com/packages/ddb-importer) | 7.5.8 / 7.5.8 | 560 | 367 | 310 | 已同步 v14 语言文件（待实机验证） |
| [ddb-sync](https://foundryvtt.com/packages/ddb-sync) | 0.0.6 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [deadly-encounter-benchmark](https://foundryvtt.com/packages/deadly-encounter-benchmark) | v3.0.1 / 3.0.1 | 12 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [death-effects](https://foundryvtt.com/packages/death-effects) | 1.1.1 / 1.1.1 | 229 | 1 | 1 | 已同步 v14 语言文件（待实机验证） |
| [depruner-chat-message-remover](https://foundryvtt.com/packages/depruner-chat-message-remover) | 2.0.4 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [deyzerias-equipment-slots](https://foundryvtt.com/packages/deyzerias-equipment-slots) | 1.4.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [df-active-lights](https://foundryvtt.com/packages/df-active-lights) | 2.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [df-architect](https://foundryvtt.com/packages/df-architect) | 5.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [df-chat-enhance](https://foundryvtt.com/packages/df-chat-enhance) | 5.1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [df-curvy-walls](https://foundryvtt.com/packages/df-curvy-walls) | 13.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [df-flag-edit](https://foundryvtt.com/packages/df-flag-edit) | 13.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [df-logger](https://foundryvtt.com/packages/df-logger) | 13.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [df-qol](https://foundryvtt.com/packages/df-qol) | 2.0.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [df-scene-enhance](https://foundryvtt.com/packages/df-scene-enhance) | 4.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [df-settings-clarity](https://foundryvtt.com/packages/df-settings-clarity) | 13.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [df-templates](https://foundryvtt.com/packages/df-templates) | 2.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [dfreds-chat-pins](https://foundryvtt.com/packages/dfreds-chat-pins) | 6.1.2 / 6.1.2 | 16 | 2 | 2 | 已同步 v14 语言文件（待实机验证） |
| [dfreds-clipboard](https://foundryvtt.com/packages/dfreds-clipboard) | 3.1.3 / 3.1.3 | — | — | — | 上游资源读取失败，保留原译 |
| [dfreds-comprehensive-keybinds](https://foundryvtt.com/packages/dfreds-comprehensive-keybinds) | 2.1.0 / 2.1.0 | — | — | — | 上游资源读取失败，保留原译 |
| [dfreds-convenient-effects](https://foundryvtt.com/packages/dfreds-convenient-effects) | 9.2.7 / 9.2.7 | 508 | 54 | 24 | 已同步 v14 语言文件（待实机验证） |
| [dfreds-droppables](https://foundryvtt.com/packages/dfreds-droppables) | 6.2.1 / 6.2.1 | 39 | 6 | 6 | 已同步 v14 语言文件（待实机验证） |
| [dfreds-effects-panel](https://foundryvtt.com/packages/dfreds-effects-panel) | 6.2.3 / 6.2.3 | 68 | 4 | 4 | 已同步 v14 语言文件（待实机验证） |
| [dfreds-effects-to-chat](https://foundryvtt.com/packages/dfreds-effects-to-chat) | 3.0.0 / 3.0.0 | 18 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [dfreds-hidden-token-effects](https://foundryvtt.com/packages/dfreds-hidden-token-effects) | 2.0.1 / 2.0.1 | 3 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [dfreds-obvious-settings](https://foundryvtt.com/packages/dfreds-obvious-settings) | 3.0.0 / 3.0.0 | 2 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [dfreds-picky-ui](https://foundryvtt.com/packages/dfreds-picky-ui) | 2.1.0 / 2.1.0 | — | — | — | 上游资源读取失败，保留原译 |
| [dfreds-select-tool](https://foundryvtt.com/packages/dfreds-select-tool) | 2.0.4 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [dfreds-status-effects](https://foundryvtt.com/packages/dfreds-status-effects) | 3.2.4 / 3.2.4 | — | — | — | 上游资源读取失败，保留原译 |
| [dh-666f78-quicknames](https://foundryvtt.com/packages/dh-666f78-quicknames) | 1.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [dice-calculator](https://foundryvtt.com/packages/dice-calculator) | 4.0.6 / 4.0.6 | 63 | 9 | 7 | 已同步 v14 语言文件（待实机验证） |
| [dice-oracles](https://foundryvtt.com/packages/dice-oracles) | 1.0.0 / 1.0.0 | 182 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [dice-so-nice](https://foundryvtt.com/packages/dice-so-nice) | 6.4.4 / 6.4.4 | 597 | 323 | 281 | 已同步 v14 语言文件（待实机验证） |
| [dice-stats](https://foundryvtt.com/packages/dice-stats) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [did-you-hear-that](https://foundryvtt.com/packages/did-you-hear-that) | 1.1.2 / 1.1.2 | 14 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [diploglass](https://foundryvtt.com/packages/diploglass) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [disable-mouse-wheel-sliders](https://foundryvtt.com/packages/disable-mouse-wheel-sliders) | 3.0.0 / 3.0.0 | 6 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [disposition-initiative](https://foundryvtt.com/packages/disposition-initiative) | 1.0.0 / 1.0.0 | 9 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [distance-calculator](https://foundryvtt.com/packages/distance-calculator) | — / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [dlopen](https://foundryvtt.com/packages/dlopen) | 1.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [dm-whisper-monitor](https://foundryvtt.com/packages/dm-whisper-monitor) | 1.0.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [dnd-easy-reference](https://foundryvtt.com/packages/dnd-easy-reference) | 3.0.5 / 3.0.5 | 108 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [dnd-randomizer](https://foundryvtt.com/packages/dnd-randomizer) | 1.14.01 / 1.14.01 | 2 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [dnd5e-animations](https://foundryvtt.com/packages/dnd5e-animations) | 3.3.0 / 3.3.0 | 29 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [dnd5e-buff-on-trigger](https://foundryvtt.com/packages/dnd5e-buff-on-trigger) | 1.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [dnd5e-combat-difficulty](https://foundryvtt.com/packages/dnd5e-combat-difficulty) | 2.1.1 / 2.1.1 | 19 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [dnd5e-custom-skills](https://foundryvtt.com/packages/dnd5e-custom-skills) | 1.5.23 / 1.5.23 | 21 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [dnd5e-follow-up-save](https://foundryvtt.com/packages/dnd5e-follow-up-save) | 1.2.0 / 1.2.0 | 4 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [dnd5e-item-resources](https://foundryvtt.com/packages/dnd5e-item-resources) | 1.3.00 / 1.3.00 | 24 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [dnd5e-point-buy](https://foundryvtt.com/packages/dnd5e-point-buy) | 0.9.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [dnd5e-print-sheet](https://foundryvtt.com/packages/dnd5e-print-sheet) | 2.8.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [dnd5e-scriptlets](https://foundryvtt.com/packages/dnd5e-scriptlets) | 13.0.6 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [dnd5e-sheet-notes](https://foundryvtt.com/packages/dnd5e-sheet-notes) | 1.2.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [dnd5e-spellpoints](https://foundryvtt.com/packages/dnd5e-spellpoints) | 3.3.15 / 3.3.15 | 101 | 3 | 3 | 已同步 v14 语言文件（待实机验证） |
| [dnd5e-system-customizer](https://foundryvtt.com/packages/dnd5e-system-customizer) | 4.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [Dnd5eItemGenerator](https://foundryvtt.com/packages/Dnd5eItemGenerator) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [DnD5eNpcMaker](https://foundryvtt.com/packages/DnD5eNpcMaker) | 3.5.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [document-tagger](https://foundryvtt.com/packages/document-tagger) | 1.1.0 / 1.1.0 | 16 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [dont-forget](https://foundryvtt.com/packages/dont-forget) | 2.3.1 / 2.3.1 | — | — | — | v14 清单未声明英文语言文件，保留原译 |
| [door-sounds](https://foundryvtt.com/packages/door-sounds) | 14.006 / 14.006 | 29 | 4 | 4 | 已同步 v14 语言文件（待实机验证） |
| [dorman-lakely-cartography](https://foundryvtt.com/packages/dorman-lakely-cartography) | 1.1.3 / 1.1.3 | 55 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [dorman-lakelys-crit-fumble-tables](https://foundryvtt.com/packages/dorman-lakelys-crit-fumble-tables) | 2.0.2 / 2.0.2 | 89 | 15 | 14 | 已同步 v14 语言文件（待实机验证） |
| [dorman-lakelys-npc-generator](https://foundryvtt.com/packages/dorman-lakelys-npc-generator) | 1.5.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [downtime-dnd5e](https://foundryvtt.com/packages/downtime-dnd5e) | 13.0.9 / 13.0.9 | 170 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [downtime-manager](https://foundryvtt.com/packages/downtime-manager) | 1.1 / 1.1.0 | 720 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [dragonbane-item-browser](https://foundryvtt.com/packages/dragonbane-item-browser) | 2,6 / 2.6 | 85 | 5 | 5 | 已同步 v14 语言文件（待实机验证） |
| [drama-director](https://foundryvtt.com/packages/drama-director) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [dramatic-rolls](https://foundryvtt.com/packages/dramatic-rolls) | 3.2.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [droplet](https://foundryvtt.com/packages/droplet) | 3.0.3 / 3.0.3 | 28 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [dscryb](https://foundryvtt.com/packages/dscryb) | 6.1.3 / 6.1.3 | 2 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [duelyst-sprites](https://foundryvtt.com/packages/duelyst-sprites) | 1.1.1 / 1.1.1 | — | — | — | 上游资源读取失败，保留原译 |
| [dungeon-draw](https://foundryvtt.com/packages/dungeon-draw) | 5.0.0 / 5.0.0 | 160 | 13 | 12 | 已同步 v14 语言文件（待实机验证） |
| [dynamic-soundscapes](https://foundryvtt.com/packages/dynamic-soundscapes) | 4.0.0 / 4.0.0 | — | — | — | 上游资源读取失败，保留原译 |
| [dynamic-tokens](https://foundryvtt.com/packages/dynamic-tokens) | 1.2.3 / 1.2.3 | 24 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [ear](https://foundryvtt.com/packages/ear) | 14.4.0 / 14.4.0 | 30 | 30 | 28 | 已同步 v14 语言文件（待实机验证） |
| [earth-calendar](https://foundryvtt.com/packages/earth-calendar) | 0.1.1 / 0.1.1 | 10 | 2 | 1 | 已同步 v14 语言文件（待实机验证） |
| [easy-macro-execution](https://foundryvtt.com/packages/easy-macro-execution) | 1.0.1 / 1.0.1 | 7 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [easy-phasey](https://foundryvtt.com/packages/easy-phasey) | 1.1.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [easy-regions](https://foundryvtt.com/packages/easy-regions) | 2.1.3 / 2.1.3 | 34 | 1 | 1 | 已同步 v14 语言文件（待实机验证） |
| [easy-target](https://foundryvtt.com/packages/easy-target) | 4.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [easy-token](https://foundryvtt.com/packages/easy-token) | 2.4.1 / 2.4.1 | 39 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [effect-hider](https://foundryvtt.com/packages/effect-hider) | 1.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [effectivetray-ng](https://foundryvtt.com/packages/effectivetray-ng) | 14.361.5.3.3.1 / 14.361.5.3.3.1 | 23 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [effectmacro](https://foundryvtt.com/packages/effectmacro) | 14.0.1 / 14.0.1 | 49 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [elevationruler](https://foundryvtt.com/packages/elevationruler) | 13.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [elfreys-item-price](https://foundryvtt.com/packages/elfreys-item-price) | 1.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [elliptical-token-shape](https://foundryvtt.com/packages/elliptical-token-shape) | 1.14.0 / 1.14.0 | 4 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [em-tile-utilities](https://foundryvtt.com/packages/em-tile-utilities) | 3.0.1 / 3.0.1 | 862 | 500 | 439 | 已同步 v14 语言文件（待实机验证） |
| [emojify](https://foundryvtt.com/packages/emojify) | 3.0.0 / 3.0.0 | 8 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [emphasis-roll](https://foundryvtt.com/packages/emphasis-roll) | 1.2.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [encounter-forge](https://foundryvtt.com/packages/encounter-forge) | v2.3.0 / 2.3.0 | 265 | 1 | 1 | 已同步 v14 语言文件（待实机验证） |
| [encounter-stats](https://foundryvtt.com/packages/encounter-stats) | 2.12.3 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [enhanced-region-behavior](https://foundryvtt.com/packages/enhanced-region-behavior) | 1.5.0 / 1.5.0 | 78 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [enhancedcombathud](https://foundryvtt.com/packages/enhancedcombathud) | 5.0.1 / 5.0.1 | 151 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [enhancedcombathud-dnd5e](https://foundryvtt.com/packages/enhancedcombathud-dnd5e) | 5.2.3 / 5.2.3 | 100 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [epic-rolls-5e](https://foundryvtt.com/packages/epic-rolls-5e) | 6.0.0 / 6.0.0 | — | — | — | 上游资源读取失败，保留原译 |
| [equipment-selector](https://foundryvtt.com/packages/equipment-selector) | 1.1.closing / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [errors-and-echoes](https://foundryvtt.com/packages/errors-and-echoes) | 0.2.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [eskie-macros](https://foundryvtt.com/packages/eskie-macros) | 1.2.12 / 1.2.12 | 186 | 21 | 19 | 已同步 v14 语言文件（待实机验证） |
| [ethereal-plane](https://foundryvtt.com/packages/ethereal-plane) | 3.3.0 / 3.3.0 | 111 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [ethereal-tokens](https://foundryvtt.com/packages/ethereal-tokens) | 1.0.0 / 1.0.0 | 2 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [eventide-speech-mannerisms](https://foundryvtt.com/packages/eventide-speech-mannerisms) | 14.0.0 / 14.0.0 | 18 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [eventide-teleporter](https://foundryvtt.com/packages/eventide-teleporter) | 14.0.0 / 14.0.0 | 22 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [expedition-tracker](https://foundryvtt.com/packages/expedition-tracker) | 2026.04.10 / 2026.04.10 | 175 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [export-markdown](https://foundryvtt.com/packages/export-markdown) | 1.0.0 / 1.0.0 | 9 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [exportjournals](https://foundryvtt.com/packages/exportjournals) | 1.0.4 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [ez-glide](https://foundryvtt.com/packages/ez-glide) | 1.0.0 / 1.0.0 | 12 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [fa-battlemaps](https://foundryvtt.com/packages/fa-battlemaps) | — / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [fabricate](https://foundryvtt.com/packages/fabricate) | 1.9.10 / 1.9.10 | 5468 | 3213 | 2661 | 已同步 v14 语言文件（待实机验证） |
| [fabulous-drag-ruler](https://foundryvtt.com/packages/fabulous-drag-ruler) | 1.2.0 / 1.2.0 | 54 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [fameosity](https://foundryvtt.com/packages/fameosity) | 14.3.0 / 14.3.0 | 251 | 52 | 47 | 已同步 v14 语言文件（待实机验证） |
| [fancy-ui-5e](https://foundryvtt.com/packages/fancy-ui-5e) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [farchievements](https://foundryvtt.com/packages/farchievements) | 14.2.1 / 14.2.1 | 131 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [farkledice](https://foundryvtt.com/packages/farkledice) | 1.1.0 / 1.1.0 | 63 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [fast-flip](https://foundryvtt.com/packages/fast-flip) | 5.0.4 / 5.0.4 | 31 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [feature-organizer](https://foundryvtt.com/packages/feature-organizer) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [file-manager-dungeons-lab](https://foundryvtt.com/packages/file-manager-dungeons-lab) | 0.7.0 / 0.7.0 | 165 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [filepicker-memory](https://foundryvtt.com/packages/filepicker-memory) | 1.1.0 / 1.1.0 | 3 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [filepicker-plus](https://foundryvtt.com/packages/filepicker-plus) | 6.0.1 / 6.0.1 | — | — | — | 上游资源读取失败，保留原译 |
| [financial-system](https://foundryvtt.com/packages/financial-system) | 2.0.8 / 2.0.8 | — | — | — | 上游资源读取失败，保留原译 |
| [find-and-replace](https://foundryvtt.com/packages/find-and-replace) | 14.0.0.0 / 14.0.0.0 | 16 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [find-the-culprit](https://foundryvtt.com/packages/find-the-culprit) | 3.3.0 / 3.3.0 | 88 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [fit](https://foundryvtt.com/packages/fit) | V1.2.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [flash-rolls-5e](https://foundryvtt.com/packages/flash-rolls-5e) | 1.30.8 / 1.30.8 | 1030 | 434 | 327 | 已同步 v14 语言文件（待实机验证） |
| [fog-weaver](https://foundryvtt.com/packages/fog-weaver) | 1.0.6 / 1.0.6 | 39 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [follow-me-if-you-can](https://foundryvtt.com/packages/follow-me-if-you-can) | v1.4.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [follow-the-leader](https://foundryvtt.com/packages/follow-the-leader) | 1.0.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [force-client-controls](https://foundryvtt.com/packages/force-client-controls) | 1.2.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [force-client-settings](https://foundryvtt.com/packages/force-client-settings) | 2.6.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [forien-ammo-swapper](https://foundryvtt.com/packages/forien-ammo-swapper) | 0.4.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [forien-copy-environment](https://foundryvtt.com/packages/forien-copy-environment) | 4.0.0 / v4.0.0 | 30 | 7 | 7 | 已同步 v14 语言文件（待实机验证） |
| [forien-easy-polls](https://foundryvtt.com/packages/forien-easy-polls) | 2.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [forien-quest-log](https://foundryvtt.com/packages/forien-quest-log) | 0.9.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [forien-ui-tweaks](https://foundryvtt.com/packages/forien-ui-tweaks) | 0.4.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [foundry-ai](https://foundryvtt.com/packages/foundry-ai) | 1.3.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [foundry-audiolog](https://foundryvtt.com/packages/foundry-audiolog) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [foundry-beams](https://foundryvtt.com/packages/foundry-beams) | 1.5.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [foundry-familiar](https://foundryvtt.com/packages/foundry-familiar) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [foundry-graph](https://foundryvtt.com/packages/foundry-graph) | 0.14.4 / 0.14.4 | 338 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [foundry-markdown-sheets](https://foundryvtt.com/packages/foundry-markdown-sheets) | 0.1.3 / 0.1.3 | 73 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [foundry-mcp-bridge](https://foundryvtt.com/packages/foundry-mcp-bridge) | 0.8.5 / 0.8.5 | 31 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [foundry-rest-api](https://foundryvtt.com/packages/foundry-rest-api) | 3.4.1 / 3.4.1 | 8 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [foundry-tables-to-items](https://foundryvtt.com/packages/foundry-tables-to-items) | 1.1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [foundry-tube](https://foundryvtt.com/packages/foundry-tube) | 1.4.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [foundrystreamoverlay](https://foundryvtt.com/packages/foundrystreamoverlay) | 5.0.0 / 5.0.0 | 3 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [foundrytodiscord](https://foundryvtt.com/packages/foundrytodiscord) | 4.0.1 / 4.0.1 | 127 | 1 | 1 | 已同步 v14 语言文件（待实机验证） |
| [foundryvtt-actor-studio](https://foundryvtt.com/packages/foundryvtt-actor-studio) | 2.10.5 / 2.10.5 | 450 | 1 | 1 | 已同步 v14 语言文件（待实机验证） |
| [foundryvtt-dnd5e-aoe-secondary](https://foundryvtt.com/packages/foundryvtt-dnd5e-aoe-secondary) | 0.1.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [foundryvtt-dnd5e-jump-calculator](https://foundryvtt.com/packages/foundryvtt-dnd5e-jump-calculator) | 1.3.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [foundryvtt-journal-to-pdf](https://foundryvtt.com/packages/foundryvtt-journal-to-pdf) | 2.1.2 / 2.1.2 | 5 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [foundryvtt-simple-calendar](https://foundryvtt.com/packages/foundryvtt-simple-calendar) | 2.4.18 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [foundryvtt-simple-calendar-compat](https://foundryvtt.com/packages/foundryvtt-simple-calendar-compat) | 0.4.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [foundryvtt-simple-calendar-reborn](https://foundryvtt.com/packages/foundryvtt-simple-calendar-reborn) | 2.6.1 / 2.6.1 | 504 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [fox-burble](https://foundryvtt.com/packages/fox-burble) | 2.1.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [fq-card-engine](https://foundryvtt.com/packages/fq-card-engine) | 3.0.0 / 3.0.0 | 1119 | 877 | 806 | 已同步 v14 语言文件（待实机验证） |
| [friendship-dice](https://foundryvtt.com/packages/friendship-dice) | 1.1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [fullsearch](https://foundryvtt.com/packages/fullsearch) | 3.0.0 / 3.0.0 | 22 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [fumble-switch](https://foundryvtt.com/packages/fumble-switch) | 0.2.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [furu-sc](https://foundryvtt.com/packages/furu-sc) | 1.2.3 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [fuzzy-foundry](https://foundryvtt.com/packages/fuzzy-foundry) | 5.0.2 / 5.0.2 | 25 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [fvtt-challenge-calculator](https://foundryvtt.com/packages/fvtt-challenge-calculator) | 2.6.0 / 2.6.0 | 23 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [fvtt-delayed-teleport-region](https://foundryvtt.com/packages/fvtt-delayed-teleport-region) | 2.0.4 / 2.0.4 | 5 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [fvtt-module-automated-combat-notes](https://foundryvtt.com/packages/fvtt-module-automated-combat-notes) | 1.2.0 / — | — | — | — | 上游资源读取失败，保留原译 |
| [fvtt-paper-doll-ui](https://foundryvtt.com/packages/fvtt-paper-doll-ui) | 3.0.0 / 3.0.0 | — | — | — | 上游资源读取失败，保留原译 |
| [fvtt-party-resources](https://foundryvtt.com/packages/fvtt-party-resources) | 1.9.1 / 1.9.1 | 64 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [fvtt-party-sheet](https://foundryvtt.com/packages/fvtt-party-sheet) | 3.0.3 / 3.0.3 | 75 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [fvtt-perf-optim](https://foundryvtt.com/packages/fvtt-perf-optim) | 0.12.9 / 0.12.9 | 46 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [fvtt-player-achievements](https://foundryvtt.com/packages/fvtt-player-achievements) | 2.0.0 / 2.0.0 | 89 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [fvtt-player-initiative](https://foundryvtt.com/packages/fvtt-player-initiative) | 2.0.5 / 2.0.5 | 4 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [fvtt-tabbed-chatlog](https://foundryvtt.com/packages/fvtt-tabbed-chatlog) | 1.0.5 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [fvtt-token-targeting](https://foundryvtt.com/packages/fvtt-token-targeting) | 2.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [fvtt-youtube-player](https://foundryvtt.com/packages/fvtt-youtube-player) | 4.0.1 / 4.0.1 | — | — | — | 上游资源读取失败，保留原译 |
| [fxmaster](https://foundryvtt.com/packages/fxmaster) | 8.4.1 / 8.4.1 | 1341 | 210 | 187 | 已同步 v14 语言文件（待实机验证） |
| [gambits-premades](https://foundryvtt.com/packages/gambits-premades) | 2.1.44 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [gambitsEmoteBar](https://foundryvtt.com/packages/gambitsEmoteBar) | 3.1.1 / 3.1.1 | 114 | 1 | 1 | 已同步 v14 语言文件（待实机验证） |
| [gambitsTemplatePreviewer](https://foundryvtt.com/packages/gambitsTemplatePreviewer) | 2.1.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [game-faces](https://foundryvtt.com/packages/game-faces) | 1.1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [game_time_clock](https://foundryvtt.com/packages/game_time_clock) | 2.1.2 / 2.2.5 | 28 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [gatherer](https://foundryvtt.com/packages/gatherer) | 5.0.3 / 5.0.3 | — | — | — | 上游资源读取失败，保留原译 |
| [geanos-carriage-shake](https://foundryvtt.com/packages/geanos-carriage-shake) | 2.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [geanos-scene-rotation](https://foundryvtt.com/packages/geanos-scene-rotation) | 2.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [genga](https://foundryvtt.com/packages/genga) | 1.3.6 / 1.3.6 | 4 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [gg-calendar](https://foundryvtt.com/packages/gg-calendar) | v1.2.0 / 1.2.0 | 55 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [gg-encounter-lens](https://foundryvtt.com/packages/gg-encounter-lens) | v0.3.1 / 0.3.4 | 110 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [gg-fog-scout](https://foundryvtt.com/packages/gg-fog-scout) | v1.0.0 / 1.0.1 | 32 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [gg-nameforge](https://foundryvtt.com/packages/gg-nameforge) | 2.3.2 / 2.3.2 | 118 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [gg-sheet-export](https://foundryvtt.com/packages/gg-sheet-export) | 1.12.0 / 1.12.0 | 149 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [ghorin-light-on](https://foundryvtt.com/packages/ghorin-light-on) | 3.1.0 / 3.1.0 | 41 | 33 | 27 | 已同步 v14 语言文件（待实机验证） |
| [ghorin-toolbar](https://foundryvtt.com/packages/ghorin-toolbar) | 2.0.0 / 2.0.0 | 64 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [giffyglyph-monster-maker-continued](https://foundryvtt.com/packages/giffyglyph-monster-maker-continued) | Latest Stable / 2.1.0.2 | 1166 | 266 | 228 | 已同步 v14 语言文件（待实机验证） |
| [ginzzzu-music-deck](https://foundryvtt.com/packages/ginzzzu-music-deck) | 1.1.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [ginzzzu-portraits](https://foundryvtt.com/packages/ginzzzu-portraits) | 2.1.6 / 2.1.6 | 242 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [glitchsmith-lib](https://foundryvtt.com/packages/glitchsmith-lib) | 0.13.0 / 0.13.0 | 109 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [global-progress-clocks](https://foundryvtt.com/packages/global-progress-clocks) | 1.3.3 / 1.3.3 | 46 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [gm-notes](https://foundryvtt.com/packages/gm-notes) | 12.0 / 12.0 | 20 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [gm-only-tables](https://foundryvtt.com/packages/gm-only-tables) | v1.1.1 / 1.1.1 | 1 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [gm-runic-items](https://foundryvtt.com/packages/gm-runic-items) | v1.4.0 / 1.4.0 | 608 | 17 | 16 | 已同步 v14 语言文件（待实机验证） |
| [gm-screen](https://foundryvtt.com/packages/gm-screen) | 6.2.3 / 6.2.3 | 53 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [gm-vision](https://foundryvtt.com/packages/gm-vision) | 2.0.5 / 2.0.5 | 1 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [greybearded-tokens](https://foundryvtt.com/packages/greybearded-tokens) | 0.2.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [grid-aware-auras](https://foundryvtt.com/packages/grid-aware-auras) | 0.5.7 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [grid-inch-zoom](https://foundryvtt.com/packages/grid-inch-zoom) | 1.0.1 / 1.0.1 | 6 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [grouproll](https://foundryvtt.com/packages/grouproll) | 0.13.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [gunslingers](https://foundryvtt.com/packages/gunslingers) | 1.2.1 / 1.2.1 | — | — | — | 上游资源读取失败，保留原译 |
| [hand-mini-bar](https://foundryvtt.com/packages/hand-mini-bar) | 1.7.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [handout-ping-viewer](https://foundryvtt.com/packages/handout-ping-viewer) | 1.0.1 / 1.0.1 | 6 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [hasterolls5e](https://foundryvtt.com/packages/hasterolls5e) | 1.2.0 / 1.2.0 | 6 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [health-monitor](https://foundryvtt.com/packages/health-monitor) | 3.1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [healthEstimate](https://foundryvtt.com/packages/healthEstimate) | 35.2.2 / 35.2.2 | 149 | 16 | 11 | 已同步 v14 语言文件（待实机验证） |
| [heart-containers](https://foundryvtt.com/packages/heart-containers) | 14.0.0 / 14.0.0 | 14 | 2 | 2 | 已同步 v14 语言文件（待实机验证） |
| [hero-mancer](https://foundryvtt.com/packages/hero-mancer) | 3.3.1 / 3.3.1 | — | — | — | v14 清单未声明英文语言文件，保留原译 |
| [hero-villain-points](https://foundryvtt.com/packages/hero-villain-points) | 1.5 / 1.4.0 | 55 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [hex-size-support](https://foundryvtt.com/packages/hex-size-support) | 5.7 / 5.7 | 46 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [hex-support](https://foundryvtt.com/packages/hex-support) | 1.2.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [hexploration](https://foundryvtt.com/packages/hexploration) | 1.1.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [hexplorer](https://foundryvtt.com/packages/hexplorer) | 3.0.3 / 3.0.3 | — | — | — | 上游资源读取失败，保留原译 |
| [hey-wait](https://foundryvtt.com/packages/hey-wait) | 0.7.7 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [Hidden-Items](https://foundryvtt.com/packages/Hidden-Items) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [hide-icons-vault](https://foundryvtt.com/packages/hide-icons-vault) | 2.0.2 / 2.0.2 | 22 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [hide-npc-names](https://foundryvtt.com/packages/hide-npc-names) | 1.4.1 / 1.4.1 | 46 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [hide-party-hp](https://foundryvtt.com/packages/hide-party-hp) | 2.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [hide-player-ui](https://foundryvtt.com/packages/hide-player-ui) | 1.9.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [hot-pan](https://foundryvtt.com/packages/hot-pan) | 14.0.1 / 14.0.1 | 80 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [how-unfortunate-are-you--dice-counting](https://foundryvtt.com/packages/how-unfortunate-are-you--dice-counting) | 1.1.2 / 1.1.12 | 6 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [hurry-up](https://foundryvtt.com/packages/hurry-up) | 4.0.0 / 4.0.0 | 47 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [illandril-npc-quick-actions](https://foundryvtt.com/packages/illandril-npc-quick-actions) | 2.3.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [illandril-third-pact](https://foundryvtt.com/packages/illandril-third-pact) | 4.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [illandril-token-hud-scale](https://foundryvtt.com/packages/illandril-token-hud-scale) | 4.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [illandril-token-tooltips](https://foundryvtt.com/packages/illandril-token-tooltips) | 4.2.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [image-tagger](https://foundryvtt.com/packages/image-tagger) | 0.2.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [image-z00m](https://foundryvtt.com/packages/image-z00m) | 1.2.0 / 1.2.0 | 3 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [imp-counter](https://foundryvtt.com/packages/imp-counter) | 1.0.13 / 1.0.13 | 37 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [imp-theater](https://foundryvtt.com/packages/imp-theater) | 0.1.15 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [improved-player-list](https://foundryvtt.com/packages/improved-player-list) | v2.0.2 / 2.0.2 | 1 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [indy-dice-stats](https://foundryvtt.com/packages/indy-dice-stats) | 1.1.7 / 1.1.7 | 174 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [indy-fx](https://foundryvtt.com/packages/indy-fx) | 1.2.6 / 1.2.6 | 2 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [indy-regions](https://foundryvtt.com/packages/indy-regions) | 0.5 / 0.5 | 84 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [indy-walls](https://foundryvtt.com/packages/indy-walls) | 1.1.7 / 1.1.7 | 175 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [initiative-double-click](https://foundryvtt.com/packages/initiative-double-click) | 1.8.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [inlinewebviewer](https://foundryvtt.com/packages/inlinewebviewer) | 3.4.8 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [insania-et-perturbatio-animi](https://foundryvtt.com/packages/insania-et-perturbatio-animi) | 1.0.0-beta.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [inspect-statblock](https://foundryvtt.com/packages/inspect-statblock) | 1.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [instant-range](https://foundryvtt.com/packages/instant-range) | 3.0.2 / 3.0.2 | 6 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [intelligent-npcs](https://foundryvtt.com/packages/intelligent-npcs) | 1.14.1 / 1.14.1 | 1 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [interactive-light](https://foundryvtt.com/packages/interactive-light) | 1.2.2 / v1.2.2 | 22 | 1 | 1 | 已同步 v14 语言文件（待实机验证） |
| [intoterica](https://foundryvtt.com/packages/intoterica) | v1.5.1 / 1.5.1 | 2 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [inventory-containers](https://foundryvtt.com/packages/inventory-containers) | 0.0.5 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [ionrift-respite](https://foundryvtt.com/packages/ionrift-respite) | 4.3.0 / 4.3.0 | 2 | 1 | 1 | 已同步 v14 语言文件（待实机验证） |
| [ionrift-waterline](https://foundryvtt.com/packages/ionrift-waterline) | 1.0.5 / 1.0.5 | 28 | 19 | 18 | 已同步 v14 语言文件（待实机验证） |
| [ipdip](https://foundryvtt.com/packages/ipdip) | 3.0 / 3.0 | 17 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [ironsworn-impacts](https://foundryvtt.com/packages/ironsworn-impacts) | 1.1.0 / 1.1.0 | 164 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [isometric-perspective](https://foundryvtt.com/packages/isometric-perspective) | v14.0.5 / 14.0.5 | 91 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [item-browser](https://foundryvtt.com/packages/item-browser) | 1.3.2 / 1.3.2 | 93 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [item-delete-check](https://foundryvtt.com/packages/item-delete-check) | 14.1.0 / 14.1.0 | 38 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [item-piles](https://foundryvtt.com/packages/item-piles) | 3.3.4 / 3.3.4 | 745 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [itemacro](https://foundryvtt.com/packages/itemacro) | 3.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [itemcollection](https://foundryvtt.com/packages/itemcollection) | 11.3.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [items-with-spells-5e](https://foundryvtt.com/packages/items-with-spells-5e) | 13.0.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [jd-easytimekeeping](https://foundryvtt.com/packages/jd-easytimekeeping) | v1.6.1 / v1.6.1 | 152 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [journal-backlinks-extended](https://foundryvtt.com/packages/journal-backlinks-extended) | 0.13.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [journal-cues](https://foundryvtt.com/packages/journal-cues) | 0.2.4 / 0.2.4 | 88 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [journal-icon-numbers](https://foundryvtt.com/packages/journal-icon-numbers) | v1.10.2 / v1.10.2 | 62 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [journal-styler](https://foundryvtt.com/packages/journal-styler) | 1.4 / 1.4 | 97 | 51 | 32 | 已同步 v14 语言文件（待实机验证） |
| [journal-wod](https://foundryvtt.com/packages/journal-wod) | v1.1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [karma](https://foundryvtt.com/packages/karma) | 2.4.0 / 2.4.0 | 47 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [kill-tracker](https://foundryvtt.com/packages/kill-tracker) | 1.0.4 / 1.0.4 | 5 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [koboldworks-ready-up](https://foundryvtt.com/packages/koboldworks-ready-up) | 1.1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [koboldworks-rolltable-sheet](https://foundryvtt.com/packages/koboldworks-rolltable-sheet) | 1.2.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [lame-messenger](https://foundryvtt.com/packages/lame-messenger) | 4.6.2 / 4.6.2 | 32 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [languages-rp](https://foundryvtt.com/packages/languages-rp) | v1.5.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [last-scene-view](https://foundryvtt.com/packages/last-scene-view) | 1.4.00 / 1.4.00 | 16 | 3 | 3 | 已同步 v14 语言文件（待实机验证） |
| [launchmacro](https://foundryvtt.com/packages/launchmacro) | 3.0.1 / 3.0.1 | 5 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [layer-hotkeys](https://foundryvtt.com/packages/layer-hotkeys) | 2.8.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [ld-hydez](https://foundryvtt.com/packages/ld-hydez) | v 2.3.9 / 2.3.11 | 85 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [ld-triggerz](https://foundryvtt.com/packages/ld-triggerz) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [lead-the-way](https://foundryvtt.com/packages/lead-the-way) | 1.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [less-chat](https://foundryvtt.com/packages/less-chat) | 2.0.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [levels](https://foundryvtt.com/packages/levels) | 7.0.3 / 7.0.3 | 153 | 6 | 6 | 已同步 v14 语言文件（待实机验证） |
| [levels-3d-preview](https://foundryvtt.com/packages/levels-3d-preview) | 9.0.36 / 9.0.36 | 1444 | 24 | 24 | 已同步 v14 语言文件（待实机验证） |
| [levels-layer-effects](https://foundryvtt.com/packages/levels-layer-effects) | 3.0.0 / 3.0.0 | — | — | — | 上游资源读取失败，保留原译 |
| [levelsautocover](https://foundryvtt.com/packages/levelsautocover) | 4.0.1 / 4.0.1 | — | — | — | 上游资源读取失败，保留原译 |
| [levelsvolumetrictemplates](https://foundryvtt.com/packages/levelsvolumetrictemplates) | 4.0.7 / 4.0.7 | — | — | — | 上游资源读取失败，保留原译 |
| [lib-df-buttons](https://foundryvtt.com/packages/lib-df-buttons) | 13.1.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [lib-dfreds-migrations](https://foundryvtt.com/packages/lib-dfreds-migrations) | 1.0.4 / 1.0.4 | 2 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [lib-dfreds-ui-extender](https://foundryvtt.com/packages/lib-dfreds-ui-extender) | 2.5.0 / 2.5.0 | 41 | 8 | 4 | 已同步 v14 语言文件（待实机验证） |
| [lib-item-select-dialog](https://foundryvtt.com/packages/lib-item-select-dialog) | 1.0.3 / 1.0.3 | 2 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [lib-wrapper](https://foundryvtt.com/packages/lib-wrapper) | 1.13.5.1 / 1.13.5.1 | 74 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [lightmask](https://foundryvtt.com/packages/lightmask) | 0.9.3 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [limited-attenuation-wall](https://foundryvtt.com/packages/limited-attenuation-wall) | 1.0.3 / 1.0.3 | 4 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [limits](https://foundryvtt.com/packages/limits) | 3.0.0 / 3.0.0 | 24 | 1 | 1 | 已同步 v14 语言文件（待实机验证） |
| [linemap](https://foundryvtt.com/packages/linemap) | 0.13.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [link-item-resource-5e](https://foundryvtt.com/packages/link-item-resource-5e) | 2.1.3 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [loaded-dice-roll](https://foundryvtt.com/packages/loaded-dice-roll) | 2.4.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [loading-screen](https://foundryvtt.com/packages/loading-screen) | 2.3.2 / 2.3.2 | 69 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [lobowerewolf-hub](https://foundryvtt.com/packages/lobowerewolf-hub) | 5.1.1 / 5.1.1 | 23 | 18 | 12 | 已同步 v14 语言文件（待实机验证） |
| [lock-the-sheets](https://foundryvtt.com/packages/lock-the-sheets) | 14.0.2 / 14.0.2 | 72 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [LocknKey](https://foundryvtt.com/packages/locknkey) | 5.1.3 / 5.1.3 | 411 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [LockView](https://foundryvtt.com/packages/LockView) | 2.1.0 / 2.1.0 | 209 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [loot-parcels](https://foundryvtt.com/packages/loot-parcels) | 0.26.0 / 0.26.0 | 5 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [lootforge](https://foundryvtt.com/packages/lootforge) | 0.6.3 / 0.6.4 | 129 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [lootsheet-simple](https://foundryvtt.com/packages/lootsheet-simple) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [loremaster](https://foundryvtt.com/packages/loremaster) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [low-code-macro](https://foundryvtt.com/packages/low-code-macro) | 0.1.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [lyynix-more-journal-enrichers](https://foundryvtt.com/packages/lyynix-more-journal-enrichers) | 13.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [macro-keybinds](https://foundryvtt.com/packages/macro-keybinds) | 2.3.1 / 2.3.1 | — | — | — | v14 清单未声明英文语言文件，保留原译 |
| [macro-trigger](https://foundryvtt.com/packages/macro-trigger) | 1.0.3 / 1.0.3 | — | — | — | 上游资源读取失败，保留原译 |
| [macro-wheel](https://foundryvtt.com/packages/macro-wheel) | 4.0.0 / 4.0.0 | — | — | — | 上游资源读取失败，保留原译 |
| [magical-beans](https://foundryvtt.com/packages/magical-beans) | 1.1.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [magicitems](https://foundryvtt.com/packages/magicitems) | 5.0.0-beta.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [maleficar-manoeuvres](https://foundryvtt.com/packages/maleficar-manoeuvres) | 1.18.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [mana-system](https://foundryvtt.com/packages/mana-system) | 3.0.1 / 3.0.1 | — | — | — | 上游资源读取失败，保留原译 |
| [map-coords](https://foundryvtt.com/packages/map-coords) | v1.2.0 / v1.2.0 | 22 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [markdown-paste](https://foundryvtt.com/packages/markdown-paste) | 0.3.1 / 0.3.1 | 44 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [mastercrafted](https://foundryvtt.com/packages/mastercrafted) | 6.0.5 / 6.0.5 | — | — | — | 上游资源读取失败，保留原译 |
| [materialdeck-dnd5e](https://foundryvtt.com/packages/materialdeck-dnd5e) | 2.1.0 / 2.1.0 | 41 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [md-to-journal](https://foundryvtt.com/packages/md-to-journal) | 0.0.6 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [media-binder](https://foundryvtt.com/packages/media-binder) | 1.3.1 / 1.3.1 | — | — | — | 上游资源读取失败，保留原译 |
| [media-optimizer](https://foundryvtt.com/packages/media-optimizer) | 6.0.1 / 6.0.1 | — | — | — | 上游资源读取失败，保留原译 |
| [micro-map](https://foundryvtt.com/packages/micro-map) | 1.3.0 / 1.3.0 | 106 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [midi-item-showcase-community](https://foundryvtt.com/packages/midi-item-showcase-community) | 2.0.2 / 2.0.2 | 8 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [midi-qol](https://foundryvtt.com/packages/midi-qol) | 14.0.15 / 14.0.15 | 1903 | 161 | 131 | 已同步 v14 语言文件（待实机验证） |
| [mini-uploader](https://foundryvtt.com/packages/mini-uploader) | 3.5 / 3.5 | 31 | 2 | 2 | 已同步 v14 语言文件（待实机验证） |
| [minimal-ui](https://foundryvtt.com/packages/minimal-ui) | 1.7.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [mission-board](https://foundryvtt.com/packages/mission-board) | 1.3.6 / 1.3.6 | — | — | — | 上游资源读取失败，保留原译 |
| [mkah-compendium-importer](https://foundryvtt.com/packages/mkah-compendium-importer) | 3.1.6 / 3.1.6 | 29 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [mob-attack-tool](https://foundryvtt.com/packages/mob-attack-tool) | 0.19.0 / 0.19.0 | 152 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [mobile-companion-dnd5e](https://foundryvtt.com/packages/mobile-companion-dnd5e) | 0.25.1-light / 0.25.1-light | 53 | 4 | 3 | 已同步 v14 语言文件（待实机验证） |
| [mobile-improvements](https://foundryvtt.com/packages/mobile-improvements) | 2.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [module-credits](https://foundryvtt.com/packages/module-credits) | 2.2.3 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [module-list-export](https://foundryvtt.com/packages/module-list-export) | 1.0.4 / 1.0.4 | 6 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [module-profiles](https://foundryvtt.com/packages/module-profiles) | 1.1.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [monks-active-tiles](https://foundryvtt.com/packages/monks-active-tiles) | 14.01 / 14.01 | 516 | 1 | 1 | 已同步 v14 语言文件（待实机验证） |
| [monks-bloodsplats](https://foundryvtt.com/packages/monks-bloodsplats) | 14.01 / 14.01 | 35 | 3 | 3 | 已同步 v14 语言文件（待实机验证） |
| [monks-chat-timer](https://foundryvtt.com/packages/monks-chat-timer) | 14.01 / 14.01 | 9 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [monks-combat-details](https://foundryvtt.com/packages/monks-combat-details) | 14.03 / 14.03 | 157 | 9 | 6 | 已同步 v14 语言文件（待实机验证） |
| [monks-common-display](https://foundryvtt.com/packages/monks-common-display) | 14.01 / 14.01 | 76 | 6 | 5 | 已同步 v14 语言文件（待实机验证） |
| [monks-enhanced-journal](https://foundryvtt.com/packages/monks-enhanced-journal) | 14.01 / 14.01 | 763 | 3 | 3 | 已同步 v14 语言文件（待实机验证） |
| [monks-hotbar-expansion](https://foundryvtt.com/packages/monks-hotbar-expansion) | 14.01 / 14.01 | 19 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [monks-little-details](https://foundryvtt.com/packages/monks-little-details) | 14.01 / 14.01 | 117 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [monks-player-settings](https://foundryvtt.com/packages/monks-player-settings) | 14.01 / 14.01 | 4 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [monks-scene-navigation](https://foundryvtt.com/packages/monks-scene-navigation) | 14.02 / 14.02 | 45 | 4 | 4 | 已同步 v14 语言文件（待实机验证） |
| [monks-sound-enhancements](https://foundryvtt.com/packages/monks-sound-enhancements) | 14.01 / 14.01 | 35 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [monks-tokenbar](https://foundryvtt.com/packages/monks-tokenbar) | 14.01 / 14.01 | 270 | 7 | 1 | 已同步 v14 语言文件（待实机验证） |
| [monks-wall-enhancement](https://foundryvtt.com/packages/monks-wall-enhancement) | 14.01 / 14.01 | 38 | 2 | 2 | 已同步 v14 语言文件（待实机验证） |
| [more-activities](https://foundryvtt.com/packages/more-activities) | 1.9.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [more-dynamic-token-rings](https://foundryvtt.com/packages/more-dynamic-token-rings) | 2.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [more-manual-dice-rolls](https://foundryvtt.com/packages/more-manual-dice-rolls) | 14.364.2 / 14.364.2 | 12 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [more-messages-options](https://foundryvtt.com/packages/more-messages-options) | 2.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [mortal-needs](https://foundryvtt.com/packages/mortal-needs) | 3.0.3 / 3.0.3 | 906 | 130 | 111 | 已同步 v14 语言文件（待实机验证） |
| [moulinette](https://foundryvtt.com/packages/moulinette) | 2.3.1 / 2.3.1 | 270 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [moulinette-soundboards](https://foundryvtt.com/packages/moulinette-soundboards) | 14.0.3 / 14.0.3 | 70 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [move-that-for-you](https://foundryvtt.com/packages/move-that-for-you) | 4.0.0 / 4.0.0 | 21 | 3 | 3 | 已同步 v14 语言文件（待实机验证） |
| [movement-approval](https://foundryvtt.com/packages/movement-approval) | 1.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [mrkb-background-display](https://foundryvtt.com/packages/mrkb-background-display) | 1.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [mrkb-chat-enhancements](https://foundryvtt.com/packages/mrkb-chat-enhancements) | 1.3.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [mrkb-sidebar-resizer](https://foundryvtt.com/packages/mrkb-sidebar-resizer) | 1.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [mrkb-ui-improvements](https://foundryvtt.com/packages/mrkb-ui-improvements) | 1.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [multi-hit-spell-lvl-scaler](https://foundryvtt.com/packages/multi-hit-spell-lvl-scaler) | 0.1.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [multi-token-edit](https://foundryvtt.com/packages/multi-token-edit) | 3.3.8 / 3.3.8 | 150 | 1 | 0 | 已同步 v14 语言文件（待实机验证） |
| [multiface-tiles](https://foundryvtt.com/packages/multiface-tiles) | 14.001 / 14.001 | 6 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [multilevel-tokens](https://foundryvtt.com/packages/multilevel-tokens) | 14.1.2 / 14.1.5 | 83 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [multiple-chat-tabs](https://foundryvtt.com/packages/multiple-chat-tabs) | 1.2.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [multiple-document-selection](https://foundryvtt.com/packages/multiple-document-selection) | 14.01 / 14.01 | 6 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [my-names-jeff](https://foundryvtt.com/packages/my-names-jeff) | v1.1.3 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [narrator-tools](https://foundryvtt.com/packages/narrator-tools) | 2.0.6 / 2.0.6 | 24 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [natural-roll](https://foundryvtt.com/packages/natural-roll) | 1.5.6 / 1.5.6 | 26 | 9 | 9 | 已同步 v14 语言文件（待实机验证） |
| [niks-dnd5e-tweaks](https://foundryvtt.com/packages/niks-dnd5e-tweaks) | 14.46.5 / 14.46.5 | 124 | 42 | 40 | 已同步 v14 语言文件（待实机验证） |
| [niks-dynamic-roll-area](https://foundryvtt.com/packages/niks-dynamic-roll-area) | 14.0.0 / 14.0.0 | 2 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [niks-settings-locks](https://foundryvtt.com/packages/niks-settings-locks) | 14.1.0 / 14.1.0 | 66 | 1 | 1 | 已同步 v14 语言文件（待实机验证） |
| [niks-shared-npc-initiative](https://foundryvtt.com/packages/niks-shared-npc-initiative) | 14.2.0 / 14.2.0 | 6 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [niks-show-and-tell](https://foundryvtt.com/packages/niks-show-and-tell) | 14.8.8 / 14.8.8 | 37 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [niks-token-tags](https://foundryvtt.com/packages/niks-token-tags) | 14.1.6 / 14.1.6 | 23 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [no-token-vision-animation](https://foundryvtt.com/packages/no-token-vision-animation) | 14.0.0 / 14.0.0 | 5 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [no-update-pips](https://foundryvtt.com/packages/no-update-pips) | 1.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [nomina-names](https://foundryvtt.com/packages/nomina-names) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [notebook](https://foundryvtt.com/packages/notebook) | 3.0.2 / 3.0.2 | 74 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [notelicker](https://foundryvtt.com/packages/notelicker) | 1.1.0 / 1.1.0 | 26 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [NotYourTurn](https://foundryvtt.com/packages/NotYourTurn) | 4.1.0 / 4.1.0 | 42 | 2 | 2 | 已同步 v14 语言文件（待实机验证） |
| [npc-button-5e](https://foundryvtt.com/packages/npc-button-5e) | 1.0.7 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [npc-dialogue-bubbles](https://foundryvtt.com/packages/npc-dialogue-bubbles) | 1.1.0 / v1.1.0 | 19 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [objection](https://foundryvtt.com/packages/objection) | 1.2.3 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [obs-utils](https://foundryvtt.com/packages/obs-utils) | 5.3.1 / 5.3.1 | 517 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [ofm-blastzone](https://foundryvtt.com/packages/ofm-blastzone) | 0.3.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [ofm-shared-world](https://foundryvtt.com/packages/ofm-shared-world) | 0.0.3 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [oft](https://foundryvtt.com/packages/oft) | 1.5.1 / 1.5.1 | — | — | — | 上游资源读取失败，保留原译 |
| [old-crt-effects](https://foundryvtt.com/packages/old-crt-effects) | 3.0 / 3.0 | — | — | — | v14 清单未声明英文语言文件，保留原译 |
| [omnipresence](https://foundryvtt.com/packages/omnipresence) | 0.9.0 / 0.9.0 | 78 | 16 | 11 | 已同步 v14 语言文件（待实机验证） |
| [omniscient-die](https://foundryvtt.com/packages/omniscient-die) | 2.2 / 2.2 | 65 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [one-journal-handouts](https://foundryvtt.com/packages/one-journal-handouts) | 2.14.0 / 2.14.0 | 19 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [orcnog-card-viewer](https://foundryvtt.com/packages/orcnog-card-viewer) | 0.4.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [oronder](https://foundryvtt.com/packages/oronder) | 1.2.1 / 1.2.1 | 97 | 5 | 4 | 已同步 v14 语言文件（待实机验证） |
| [osr-character-builder](https://foundryvtt.com/packages/osr-character-builder) | 0.5.0 / 0.5.0 | 153 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [particule-fx](https://foundryvtt.com/packages/particule-fx) | 2.7.0 / 2.7.0 | 61 | 18 | 18 | 已同步 v14 语言文件（待实机验证） |
| [party-monitor-dock](https://foundryvtt.com/packages/party-monitor-dock) | 4.0.4 / 4.0.4 | — | — | — | 上游资源读取失败，保留原译 |
| [party-overview](https://foundryvtt.com/packages/party-overview) | 2.20.3 / 2.20.3 | 37 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [patrol](https://foundryvtt.com/packages/patrol) | 5.0.10 / 5.0.10 | 55 | 54 | 51 | 已同步 v14 语言文件（待实机验证） |
| [pause-icon](https://foundryvtt.com/packages/pause-icon) | 14.001 / 14.001 | 43 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [pause-text](https://foundryvtt.com/packages/pause-text) | v3.3.1 / 3.3.1 | 82 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [pause-tweaks](https://foundryvtt.com/packages/pause-tweaks) | 1.0.5 / 1.0.5 | 20 | 2 | 2 | 已同步 v14 语言文件（待实机验证） |
| [pazaak-fvtt](https://foundryvtt.com/packages/pazaak-fvtt) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [pazindor-dev-essentials](https://foundryvtt.com/packages/pazindor-dev-essentials) | 1.0.0 / 1.0.0 | 83 | 2 | 1 | 已同步 v14 语言文件（待实机验证） |
| [pazindor-gm-tools](https://foundryvtt.com/packages/pazindor-gm-tools) | 1.0.0 / 1.0.0 | 175 | 63 | 54 | 已同步 v14 语言文件（待实机验证） |
| [pazindor-quick-notes](https://foundryvtt.com/packages/pazindor-quick-notes) | 1.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [pazindor-token-hotbar](https://foundryvtt.com/packages/pazindor-token-hotbar) | 1.0.0 / 1.0.0 | 152 | 59 | 42 | 已同步 v14 语言文件（待实机验证） |
| [pbta-manager](https://foundryvtt.com/packages/pbta-manager) | 0.13.1 / 0.13.1 | 310 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [pdf-pager](https://foundryvtt.com/packages/pdf-pager) | 14.1.0 / 14.1.0 | 114 | 6 | 4 | 已同步 v14 语言文件（待实机验证） |
| [pdf-sheet](https://foundryvtt.com/packages/pdf-sheet) | 0.24.15 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [pdf-sheets](https://foundryvtt.com/packages/pdf-sheets) | 0.0.8 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [perceived-reality](https://foundryvtt.com/packages/perceived-reality) | 1.2.0 / 1.2.0 | 436 | 218 | 186 | 已同步 v14 语言文件（待实机验证） |
| [perceptive](https://foundryvtt.com/packages/perceptive) | 6.0.9 / 6.0.9 | 460 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [persistent-zones](https://foundryvtt.com/packages/persistent-zones) | 0.2.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [pf2e-reactive-token-ring](https://foundryvtt.com/packages/pf2e-reactive-token-ring) | 3.0.0 / 3.0.0 | 105 | 2 | 2 | 已同步 v14 语言文件（待实机验证） |
| [pf2e-tokener](https://foundryvtt.com/packages/pf2e-tokener) | 2.1.7 / 2.1.7 | 109 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [phantomtokens](https://foundryvtt.com/packages/phantomtokens) | 4.0.0 / 4.0.0 | 12 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [phils-ai-assistant](https://foundryvtt.com/packages/phils-ai-assistant) | 1.5.0 / 1.5.0 | 85 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [phils-art-replacer](https://foundryvtt.com/packages/phils-art-replacer) | 1.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [phils-day-night-cycle](https://foundryvtt.com/packages/phils-day-night-cycle) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [phils-foundry-ui-tweaks](https://foundryvtt.com/packages/phils-foundry-ui-tweaks) | 1.2.0 / 1.2.0 | 41 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [phils-map-migrator](https://foundryvtt.com/packages/phils-map-migrator) | 1.4.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [phils-quest-tracker](https://foundryvtt.com/packages/phils-quest-tracker) | 2.0.3 / 2.0.3 | 158 | 67 | 61 | 已同步 v14 语言文件（待实机验证） |
| [phils-random-names](https://foundryvtt.com/packages/phils-random-names) | 3.0.0 / 3.0.0 | 123 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [phils-random-quests](https://foundryvtt.com/packages/phils-random-quests) | 1.2.4 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [phils-token-studio](https://foundryvtt.com/packages/phils-token-studio) | 1.6.4 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [physical-dice-rolls](https://foundryvtt.com/packages/physical-dice-rolls) | 1.3.0 / 1.3.0 | 39 | 2 | 2 | 已同步 v14 语言文件（待实机验证） |
| [physics-tools](https://foundryvtt.com/packages/physics-tools) | 1.3.0 / 1.3.0.0 | 67 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [pick-up-stix](https://foundryvtt.com/packages/pick-up-stix) | 5.0.0 / 5.0.0 | 273 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [pickyadventurer](https://foundryvtt.com/packages/pickyadventurer) | 2.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [pin-cushion](https://foundryvtt.com/packages/pin-cushion) | 13.0.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [pings](https://foundryvtt.com/packages/pings) | 1.4.3 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [pinned-chat-message](https://foundryvtt.com/packages/pinned-chat-message) | 2.4.0 / 2.4.0 | 21 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [pixie-border](https://foundryvtt.com/packages/pixie-border) | 1.3.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [player-approval](https://foundryvtt.com/packages/player-approval) | 1.0.4 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [player-pilot](https://foundryvtt.com/packages/player-pilot) | 0.3.3 / 0.3.3 | 29 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [playerStatus](https://foundryvtt.com/packages/playerStatus) | 5.0.0 / 5.0.0 | 16 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [playlist-group](https://foundryvtt.com/packages/playlist-group) | 5.0.1 / 5.0.1 | 6 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [playlist_import](https://foundryvtt.com/packages/playlist_import) | 13.0.4 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [playlistenchantment](https://foundryvtt.com/packages/playlistenchantment) | 2.0.3 / 2.0.3 | 246 | 227 | 200 | 已同步 v14 语言文件（待实机验证） |
| [playtime-tracker](https://foundryvtt.com/packages/playtime-tracker) | 1.3 / 1.3 | 29 | 28 | 22 | 已同步 v14 语言文件（待实机验证） |
| [poi-teleport](https://foundryvtt.com/packages/poi-teleport) | 14.1.1 / 14.3.0 | 82 | 3 | 3 | 已同步 v14 语言文件（待实机验证） |
| [pointer](https://foundryvtt.com/packages/pointer) | 13.2.6 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [polmap](https://foundryvtt.com/packages/polmap) | 2.1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [polyglot](https://foundryvtt.com/packages/polyglot) | 2.10.4 / 2.10.4 | 137 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [popout](https://foundryvtt.com/packages/popout) | v2.24 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [popout-resizer](https://foundryvtt.com/packages/popout-resizer) | 1.6.2 / 1.6.2 | 7 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [portal-lib](https://foundryvtt.com/packages/portal-lib) | 4.0.0 / 4.0.0 | 18 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [potato-or-not](https://foundryvtt.com/packages/potato-or-not) | 0.9.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [power-select-toolkit](https://foundryvtt.com/packages/power-select-toolkit) | 1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [precise-drawing-tools](https://foundryvtt.com/packages/precise-drawing-tools) | 1.6.3 / 1.6.3 | 31 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [precision-grid-aligner](https://foundryvtt.com/packages/precision-grid-aligner) | 13.351 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [preload-tracker](https://foundryvtt.com/packages/preload-tracker) | 2.2.2 / 2.2.2 | 54 | 15 | 14 | 已同步 v14 语言文件（待实机验证） |
| [prime-psionics](https://foundryvtt.com/packages/prime-psionics) | 3.1.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [progress-tracker](https://foundryvtt.com/packages/progress-tracker) | 3.0.0 / 3.0.0 | — | — | — | 上游资源读取失败，保留原译 |
| [property-inspector](https://foundryvtt.com/packages/property-inspector) | 1.00 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [proximity-voice-chat](https://foundryvtt.com/packages/proximity-voice-chat) | 1.1.0 / 1.1.0 | 22 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [put-a-ring-on-it](https://foundryvtt.com/packages/put-a-ring-on-it) | 0.1.1 / 0.1.1 | 79 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [puzzle-locks](https://foundryvtt.com/packages/puzzle-locks) | 4.0.2 / 4.0.2 | — | — | — | 上游资源读取失败，保留原译 |
| [quartermaster](https://foundryvtt.com/packages/quartermaster) | 0.1.11 / 0.1.11 | 84 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [quick-battlemap-importer](https://foundryvtt.com/packages/quick-battlemap-importer) | 1.5.12 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [quick-combat](https://foundryvtt.com/packages/quick-combat) | 0.5.9 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [quick-display-change](https://foundryvtt.com/packages/quick-display-change) | 3.0.0 / 3.0.0 | — | — | — | 上游资源读取失败，保留原译 |
| [quick-draw](https://foundryvtt.com/packages/quick-draw) | 1.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [quick-encounters](https://foundryvtt.com/packages/quick-encounters) | 12.1.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [quick-grid-align](https://foundryvtt.com/packages/quick-grid-align) | 1.3.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [quick-insert](https://foundryvtt.com/packages/quick-insert) | 3.7.8 / 3.7.8 | 155 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [quick-journal-page-back](https://foundryvtt.com/packages/quick-journal-page-back) | 1.0.4 / 1.0.4 | 10 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [quick-journal-page-clipboard](https://foundryvtt.com/packages/quick-journal-page-clipboard) | 1.2.4 / 1.2.4 | 64 | 6 | 6 | 已同步 v14 语言文件（待实机验证） |
| [quick-journal-page-sort](https://foundryvtt.com/packages/quick-journal-page-sort) | 1.3.0 / 1.3.0 | 11 | 7 | 7 | 已同步 v14 语言文件（待实机验证） |
| [quick-module-enable](https://foundryvtt.com/packages/quick-module-enable) | 1.4.2 / 1.4.2 | 5 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [quick-scenes](https://foundryvtt.com/packages/quick-scenes) | 1.4.1 / 1.4.1 | 40 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [quick-status-select](https://foundryvtt.com/packages/quick-status-select) | 1.9.0 / 2.0.3 | 2 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [quickbrush](https://foundryvtt.com/packages/quickbrush) | — / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [quickscale](https://foundryvtt.com/packages/quickscale) | 1.7.0 / 1.7.0 | 17 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [raise-my-hand](https://foundryvtt.com/packages/raise-my-hand) | 3.0.0 / 3.0.0 | 93 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [rando](https://foundryvtt.com/packages/rando) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [random-loot-generator](https://foundryvtt.com/packages/random-loot-generator) | 14.0.1 / 14.0.1 | 108 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [random-target](https://foundryvtt.com/packages/random-target) | 4.8.1 / 4.8.1 | 65 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [random-token-names](https://foundryvtt.com/packages/random-token-names) | 1.1.0 / 1.1.0 | 2 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [rarity-colors](https://foundryvtt.com/packages/rarity-colors) | 12.0.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [reactionn-combat-rules](https://foundryvtt.com/packages/reactionn-combat-rules) | 1.3.0 / 1.3.0 | 114 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [ready-for-the-stage](https://foundryvtt.com/packages/ready-for-the-stage) | 2.0.4 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [ready-to-use-cards](https://foundryvtt.com/packages/ready-to-use-cards) | 1.16.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [real-fow](https://foundryvtt.com/packages/real-fow) | 0.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [recipe-book](https://foundryvtt.com/packages/recipe-book) | 1.01 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [recycle-bin](https://foundryvtt.com/packages/recycle-bin) | 4.0.0 / 4.0.0 | — | — | — | 上游资源读取失败，保留原译 |
| [refresh-scenes](https://foundryvtt.com/packages/refresh-scenes) | v1.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [region-active-effects](https://foundryvtt.com/packages/region-active-effects) | 2.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [region-attacher](https://foundryvtt.com/packages/region-attacher) | 1.11.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [regional-deck-draw](https://foundryvtt.com/packages/regional-deck-draw) | 1.1 / 1.1 | 19 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [regionba](https://foundryvtt.com/packages/regionba) | 1.5.3 / 1.5.3 | 216 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [regionenchantment](https://foundryvtt.com/packages/regionenchantment) | 1.2.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [relations-tracker](https://foundryvtt.com/packages/relations-tracker) | 2.0.2 / 2.0.2 | — | — | — | 上游资源读取失败，保留原译 |
| [remote-action](https://foundryvtt.com/packages/remote-action) | 0.2.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [remote-highlight-ui](https://foundryvtt.com/packages/remote-highlight-ui) | 2.3.6 / 2.3.6 | 24 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [resize-sidebar](https://foundryvtt.com/packages/resize-sidebar) | 0.2.1 / 0.2.1 | 8 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [rest-recovery](https://foundryvtt.com/packages/rest-recovery) | 6.0.0 / 6.0.0 | 410 | 3 | 1 | 已同步 v14 语言文件（待实机验证） |
| [revolutionary-piratenames](https://foundryvtt.com/packages/revolutionary-piratenames) | v2.0.0 / 2.0.0 | 51 | 22 | 11 | 已同步 v14 语言文件（待实机验证） |
| [rhym](https://foundryvtt.com/packages/rhym) | 1.0.2 / 1.0.2 | 30 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [ric](https://foundryvtt.com/packages/ric) | 1.0.4 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [rich-info-tooltips](https://foundryvtt.com/packages/rich-info-tooltips) | 3.0.0 / 3.0.0 | — | — | — | 上游资源读取失败，保留原译 |
| [Rideable](https://foundryvtt.com/packages/rideable) | 5.0.22 / 5.0.22 | 299 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [rmu-lighting-vision](https://foundryvtt.com/packages/rmu-lighting-vision) | 2.2.0 / 2.2.0 | 77 | 6 | 6 | 已同步 v14 语言文件（待实机验证） |
| [rnk-illumination](https://foundryvtt.com/packages/rnk-illumination) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [rnk-lobby](https://foundryvtt.com/packages/rnk-lobby) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [rnk-runar](https://foundryvtt.com/packages/rnk-runar) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [rnk-vintage-ui](https://foundryvtt.com/packages/rnk-vintage-ui) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [rolecall-sync](https://foundryvtt.com/packages/rolecall-sync) | 0.1.1 / 0.1.1 | 80 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [roll-new-character-stats](https://foundryvtt.com/packages/roll-new-character-stats) | 3.2.3 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [roll-table-importer](https://foundryvtt.com/packages/roll-table-importer) | 2.0.2 / 2.0.2 | 0 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [roll-toast](https://foundryvtt.com/packages/roll-toast) | 1.2.3 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [roll-tracker](https://foundryvtt.com/packages/roll-tracker) | 2.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [rollgroups](https://foundryvtt.com/packages/rollgroups) | 12.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [rollies](https://foundryvtt.com/packages/rollies) | 0.4.2 / 0.4.2 | — | — | — | v14 清单未声明英文语言文件，保留原译 |
| [rolltable-requester](https://foundryvtt.com/packages/rolltable-requester) | 1.6.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [rotate-camera-8d](https://foundryvtt.com/packages/rotate-camera-8d) | 1.1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [rpgm-forge](https://foundryvtt.com/packages/rpgm-forge) | 2.3.3 / 2.3.3 | 57 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [rpgx-loot-crate](https://foundryvtt.com/packages/rpgx-loot-crate) | v1.2.2 / 1.2.2 | 25 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [rpgx-quest-log](https://foundryvtt.com/packages/rpgx-quest-log) | v2.2.0 / 2.2.0 | 58 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [rpgx-shops-traders](https://foundryvtt.com/packages/rpgx-shops-traders) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [runware-imagegen](https://foundryvtt.com/packages/runware-imagegen) | 1.4.0 / 1.4.0 | 51 | 51 | 0 | 已同步 v14 语言文件（待实机验证） |
| [safety-tools](https://foundryvtt.com/packages/safety-tools) | 14.0.0 / 14.0.0 | — | — | — | 清单兼容范围排除 v14，保留原译 |
| [salvage-yard](https://foundryvtt.com/packages/salvage-yard) | 1.2.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [save-tray-5e](https://foundryvtt.com/packages/save-tray-5e) | 1.1.1 / 1.1.1 | 4 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [sc-conditional-activities](https://foundryvtt.com/packages/sc-conditional-activities) | 6.1.7 / 6.1.7 | 35 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [sc-conditional-ae](https://foundryvtt.com/packages/sc-conditional-ae) | 0.3.0 / 0.3.0 | 226 | 137 | 126 | 已同步 v14 语言文件（待实机验证） |
| [sc-more-activities](https://foundryvtt.com/packages/sc-more-activities) | 0.13.0 / 0.13.0 | 1086 | 241 | 205 | 已同步 v14 语言文件（待实机验证） |
| [sc-simple-sockets](https://foundryvtt.com/packages/sc-simple-sockets) | 2.0.26 / 2.0.26 | 783 | 192 | 174 | 已同步 v14 语言文件（待实机验证） |
| [scene-darkness-tools](https://foundryvtt.com/packages/scene-darkness-tools) | v1.0.1 / 1.0.1 | 26 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [scene-defaults](https://foundryvtt.com/packages/scene-defaults) | 3.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [scene-express](https://foundryvtt.com/packages/scene-express) | 0.14.1 / 0.14.1 | 24 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [scene-fog-alpha](https://foundryvtt.com/packages/scene-fog-alpha) | 0.0.5 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [scene-link-view](https://foundryvtt.com/packages/scene-link-view) | 1.0.1 / 1.0.1 | 11 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [scene-loading-screens](https://foundryvtt.com/packages/scene-loading-screens) | v1.3.0 / 1.3.0 | 83 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [scene-packer](https://foundryvtt.com/packages/scene-packer) | 2.8.13 / 2.8.13 | 457 | 1 | 1 | 已同步 v14 语言文件（待实机验证） |
| [scene-pins](https://foundryvtt.com/packages/scene-pins) | 1.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [scene-transitions](https://foundryvtt.com/packages/scene-transitions) | 14.0.0 / 14.0.0 | 62 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [scene-viewer](https://foundryvtt.com/packages/scene-viewer) | 1.1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [sceneMacros](https://foundryvtt.com/packages/sceneMacros) | 1.2.1 / 1.2.1 | 19 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [scenery](https://foundryvtt.com/packages/scenery) | 3.0.0 / 3.0.0 | 73 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [scenes-library](https://foundryvtt.com/packages/scenes-library) | 1.4.0 / 1.4.0 | 89 | 1 | 1 | 已同步 v14 语言文件（待实机验证） |
| [sch-customize](https://foundryvtt.com/packages/sch-customize) | 1.2.3 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [Scifi-Battle](https://foundryvtt.com/packages/Scifi-Battle) | V1.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [seasons-and-stars](https://foundryvtt.com/packages/seasons-and-stars) | 0.26.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [seasons-and-stars-calendar-builder](https://foundryvtt.com/packages/seasons-and-stars-calendar-builder) | 0.5.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [segue](https://foundryvtt.com/packages/segue) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [sense-players](https://foundryvtt.com/packages/sense-players) | 1.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [sephrals-content-backup-restore](https://foundryvtt.com/packages/sephrals-content-backup-restore) | 1.0.3 / 1.0.3 | 74 | 15 | 14 | 已同步 v14 语言文件（待实机验证） |
| [sephrals-file-commander](https://foundryvtt.com/packages/sephrals-file-commander) | 1.0.2 / 1.0.2 | 91 | 21 | 18 | 已同步 v14 语言文件（待实机验证） |
| [sephrals-image-paste-drop](https://foundryvtt.com/packages/sephrals-image-paste-drop) | 1.0.5 / 1.0.5 | 136 | 72 | 70 | 已同步 v14 语言文件（待实机验证） |
| [sephrals-module-loadouts](https://foundryvtt.com/packages/sephrals-module-loadouts) | 1.0.3 / 1.0.3 | 117 | 45 | 40 | 已同步 v14 语言文件（待实机验证） |
| [sephrals-player-notes](https://foundryvtt.com/packages/sephrals-player-notes) | 1.0.3 / 1.0.3 | 174 | 8 | 5 | 已同步 v14 语言文件（待实机验证） |
| [sephrals-roll-breakdown](https://foundryvtt.com/packages/sephrals-roll-breakdown) | 1.0.5 / 1.0.5 | 46 | 13 | 12 | 已同步 v14 语言文件（待实机验证） |
| [sephrals-roll-triggers](https://foundryvtt.com/packages/sephrals-roll-triggers) | 1.0.5 / 1.0.5 | 339 | 126 | 96 | 已同步 v14 语言文件（待实机验证） |
| [sequencer](https://foundryvtt.com/packages/sequencer) | 4.3.0 / 4.3.0 | 145 | 3 | 3 | 已同步 v14 语言文件（待实机验证） |
| [settings-hotkeys](https://foundryvtt.com/packages/settings-hotkeys) | 1.3.0 / 1.3.0 | 8 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [settings-world-client-swap](https://foundryvtt.com/packages/settings-world-client-swap) | 1.0.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [settlement-sheets](https://foundryvtt.com/packages/settlement-sheets) | 1.1.0 / 1.1.0 | 50 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [shadows-and-secrets](https://foundryvtt.com/packages/shadows-and-secrets) | 1.2.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [share-media](https://foundryvtt.com/packages/share-media) | 3.14.3 / 3.14.3 | 115 | 26 | 19 | 已同步 v14 语言文件（待实机验证） |
| [shareddice](https://foundryvtt.com/packages/shareddice) | 2.3.0 / 2.3.0 | 83 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [sheet-export](https://foundryvtt.com/packages/sheet-export) | 0.14.8 / 0.14.8 | 43 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [sheet-only](https://foundryvtt.com/packages/sheet-only) | 2.4.4 / 2.4.4 | 32 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [show-actor-art](https://foundryvtt.com/packages/show-actor-art) | 2.1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [show-image](https://foundryvtt.com/packages/show-image) | 4.6.1 / 4.6.1 | 17 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [show-token-art](https://foundryvtt.com/packages/show-token-art) | 1.3.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [shr1mps-character-monitor](https://foundryvtt.com/packages/shr1mps-character-monitor) | 1.1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [side-initiative](https://foundryvtt.com/packages/side-initiative) | v1.3.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [simbuls-cover-calculator](https://foundryvtt.com/packages/simbuls-cover-calculator) | 2.1.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [simbuls-creature-aide](https://foundryvtt.com/packages/simbuls-creature-aide) | 1.2.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [simbuls-template-scaling](https://foundryvtt.com/packages/simbuls-template-scaling) | 1.1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [simple-cinematic-pan](https://foundryvtt.com/packages/simple-cinematic-pan) | 1.1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [simple-countdown](https://foundryvtt.com/packages/simple-countdown) | 1.2.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [simple-dice-roller](https://foundryvtt.com/packages/simple-dice-roller) | 14.0.0 / 14.0.0 | 5 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [simple-dice-roller-deluxe](https://foundryvtt.com/packages/simple-dice-roller-deluxe) | 3.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [simple-message-window](https://foundryvtt.com/packages/simple-message-window) | 2.1.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [simple-mindmap](https://foundryvtt.com/packages/simple-mindmap) | 1.5.0 / 1.4.0 | 73 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [simple-negotiation-tracker](https://foundryvtt.com/packages/simple-negotiation-tracker) | 0.4.0 / 0.4.0 | 68 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [simple-nutrition-5e](https://foundryvtt.com/packages/simple-nutrition-5e) | 1.1.0 / 1.1.0 | 86 | 28 | 21 | 已同步 v14 语言文件（待实机验证） |
| [simple-portrait-organizer](https://foundryvtt.com/packages/simple-portrait-organizer) | 1.4.4 / 1.4.4 | 26 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [simple-quest](https://foundryvtt.com/packages/simple-quest) | 5.1.7 / 5.1.7 | — | — | — | 上游资源读取失败，保留原译 |
| [simple-requests](https://foundryvtt.com/packages/simple-requests) | 1.0.9 / 1.0.9 | 61 | 14 | 14 | 已同步 v14 语言文件（待实机验证） |
| [simple-searchbar](https://foundryvtt.com/packages/simple-searchbar) | 0.1.1 / 0.1.1 | 18 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [simple-session-scheduler](https://foundryvtt.com/packages/simple-session-scheduler) | 0.1.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [simple-shop-craft-5e](https://foundryvtt.com/packages/simple-shop-craft-5e) | 1.0.1 / 1.0.1 | 424 | 257 | 225 | 已同步 v14 语言文件（待实机验证） |
| [simple-stardate](https://foundryvtt.com/packages/simple-stardate) | 1.0.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [simple-timekeeping](https://foundryvtt.com/packages/simple-timekeeping) | 2.0.3 / 2.0.3 | — | — | — | 上游资源读取失败，保留原译 |
| [simple-timer](https://foundryvtt.com/packages/simple-timer) | 2.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [simple-vistas](https://foundryvtt.com/packages/simple-vistas) | 0.2.4 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [simple-weather](https://foundryvtt.com/packages/simple-weather) | 2.2.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [simplecover5e](https://foundryvtt.com/packages/simplecover5e) | 2.2.4 / 2.2.4 | 146 | 62 | 58 | 已同步 v14 语言文件（待实机验证） |
| [simplefog](https://foundryvtt.com/packages/simplefog) | 1.5.10 / 1.5.10 | 51 | 19 | 14 | 已同步 v14 语言文件（待实机验证） |
| [simpler-quests](https://foundryvtt.com/packages/simpler-quests) | v0.4.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [simraki-character-monitor](https://foundryvtt.com/packages/simraki-character-monitor) | 2.0.0 / 2.0.0 | 86 | 12 | 0 | 已同步 v14 语言文件（待实机验证） |
| [simraki-cursed-items](https://foundryvtt.com/packages/simraki-cursed-items) | 0.2.1 / 0.2.1 | 18 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [simraki-radial-effects](https://foundryvtt.com/packages/simraki-radial-effects) | 2.1.0 / 2.1.0 | 57 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [simulacrum](https://foundryvtt.com/packages/simulacrum) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [simultaneous-cards](https://foundryvtt.com/packages/simultaneous-cards) | 3.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [sketch-tiles](https://foundryvtt.com/packages/sketch-tiles) | 1.0.7 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [skill-tree](https://foundryvtt.com/packages/skill-tree) | 3.0.0 / 3.0.0 | — | — | — | 上游资源读取失败，保留原译 |
| [smalltalk](https://foundryvtt.com/packages/smalltalk) | 4.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [smalltime](https://foundryvtt.com/packages/smalltime) | 2.0.5 / 2.0.5 | 47 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [smart-doors](https://foundryvtt.com/packages/smart-doors) | 1.8.0 / 1.8.0 | 19 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [smartphone-browser-app](https://foundryvtt.com/packages/smartphone-browser-app) | 1.0.0 / 1.0.3 | 7 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [smartphone-chirp-app](https://foundryvtt.com/packages/smartphone-chirp-app) | 1.1.1 / 1.1.1 | — | — | — | 上游资源读取失败，保留原译 |
| [smartphone-id-card](https://foundryvtt.com/packages/smartphone-id-card) | 1.1.4 / 1.1.4 | — | — | — | 上游资源读取失败，保留原译 |
| [smartphone-macro-app](https://foundryvtt.com/packages/smartphone-macro-app) | 1.0.2 / 1.0.2 | — | — | — | 上游资源读取失败，保留原译 |
| [smartphone-taxi-app](https://foundryvtt.com/packages/smartphone-taxi-app) | 1.1.0 / 1.1.1 | 20 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [smartphone-widget](https://foundryvtt.com/packages/smartphone-widget) | 2.5.0 / 2.5.0 | — | — | — | 上游资源读取失败，保留原译 |
| [smartphone-widget-scanner](https://foundryvtt.com/packages/smartphone-widget-scanner) | 1.1.0 / 1.1.0 | — | — | — | 上游资源读取失败，保留原译 |
| [smarttarget](https://foundryvtt.com/packages/smarttarget) | 4.0.2 / 4.0.2 | 73 | 1 | 1 | 已同步 v14 语言文件（待实机验证） |
| [smooth-pause-transition](https://foundryvtt.com/packages/smooth-pause-transition) | 1.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [smooth-tile-transition](https://foundryvtt.com/packages/smooth-tile-transition) | 1.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [snoot](https://foundryvtt.com/packages/snoot) | 1.4 / 1.4 | — | — | — | v14 清单未声明英文语言文件，保留原译 |
| [sounds-player](https://foundryvtt.com/packages/sounds-player) | 1.1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [soundscape](https://foundryvtt.com/packages/soundscape) | 1.2.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [soundscape-adventure](https://foundryvtt.com/packages/soundscape-adventure) | 6.0.4 / 6.0.4 | 25 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [sp-resizer](https://foundryvtt.com/packages/sp-resizer) | 1.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [spell-book](https://foundryvtt.com/packages/spell-book) | 2.5.3 / 2.5.3 | — | — | — | v14 清单未声明英文语言文件，保留原译 |
| [splash](https://foundryvtt.com/packages/splash) | 1.2.0 / 1.2.0 | 487 | 139 | 108 | 已同步 v14 语言文件（待实机验证） |
| [splatter](https://foundryvtt.com/packages/splatter) | 6.0.2 / 6.0.2 | 39 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [spotlight-omnisearch](https://foundryvtt.com/packages/spotlight-omnisearch) | 4.0.3 / 4.0.3 | 93 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [sprite-animations](https://foundryvtt.com/packages/sprite-animations) | 2.1.2 / 2.1.2 | 81 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [sprite-shadows](https://foundryvtt.com/packages/sprite-shadows) | 2.1.8 / 2.1.8 | 106 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [stairways](https://foundryvtt.com/packages/stairways) | 0.12.0 / 0.12.0 | 55 | 2 | 2 | 已同步 v14 语言文件（待实机验证） |
| [stat-tracker](https://foundryvtt.com/packages/stat-tracker) | 1.0.3 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [statuscounter](https://foundryvtt.com/packages/statuscounter) | 3.1.3 / 3.1.3 | 41 | 10 | 7 | 已同步 v14 语言文件（待实机验证） |
| [stealthy](https://foundryvtt.com/packages/stealthy) | 14.0.0 / 14.0.0 | 85 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [stickynotes](https://foundryvtt.com/packages/stickynotes) | 1.4.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [stop-hitting-yourself](https://foundryvtt.com/packages/stop-hitting-yourself) | 1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [story-teller-x](https://foundryvtt.com/packages/story-teller-x) | 1.2.1 / 1.2.1 | 30 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [storyflow-dungeons-lab](https://foundryvtt.com/packages/storyflow-dungeons-lab) | 0.1.532 / 0.1.532 | 2536 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [storyframe](https://foundryvtt.com/packages/storyframe) | 3.1.2 / 3.1.2 | 505 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [storyteller-cinema](https://foundryvtt.com/packages/storyteller-cinema) | 1.1.1 / 1.1.1 | 28 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [storyteller2](https://foundryvtt.com/packages/storyteller2) | 1.0.5 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [stresspoints-rest](https://foundryvtt.com/packages/stresspoints-rest) | 2.0.0 / 2.0.2 | 120 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [stroud-dnd-helpers](https://foundryvtt.com/packages/stroud-dnd-helpers) | 13.5.13 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [student-card](https://foundryvtt.com/packages/student-card) | 1.1.18 / 1.1.18 | 112 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [stylish-action-hud](https://foundryvtt.com/packages/stylish-action-hud) | 2.7.5 / 2.7.5 | — | — | — | 上游资源读取失败，保留原译 |
| [stylish-relationship-tracker](https://foundryvtt.com/packages/stylish-relationship-tracker) | 1.5.2 / 1.5.2 | — | — | — | 上游资源读取失败，保留原译 |
| [stylish-shop](https://foundryvtt.com/packages/stylish-shop) | 2.0.1 / 2.0.1 | — | — | — | 上游资源读取失败，保留原译 |
| [sunder](https://foundryvtt.com/packages/sunder) | 4.0.2 / 4.0.2 | 85 | 3 | 2 | 已同步 v14 语言文件（待实机验证） |
| [suppress-loading-message](https://foundryvtt.com/packages/suppress-loading-message) | 1.0.0 / 1.0.0 | 4 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [swapper](https://foundryvtt.com/packages/swapper) | 14.1.0 / 14.0.1 | 31 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [swarm](https://foundryvtt.com/packages/swarm) | 14.0.4 / 14.0.4 | 16 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [sweetnothings](https://foundryvtt.com/packages/sweetnothings) | 2.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [swipe-vtt](https://foundryvtt.com/packages/swipe-vtt) | 2.12.3 / 2.12.3 | 912 | 312 | 243 | 已同步 v14 语言文件（待实机验证） |
| [swtextcrawl](https://foundryvtt.com/packages/swtextcrawl) | 1.2.2 / 1.2.2 | 26 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [syrinscape-control](https://foundryvtt.com/packages/syrinscape-control) | 1.1.0 / 1.1.0 | 43 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [tabbed-journals](https://foundryvtt.com/packages/tabbed-journals) | 1.0.1 / 1.0.1 | 13 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [tabbed-whispers](https://foundryvtt.com/packages/tabbed-whispers) | 2.1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [table-safety](https://foundryvtt.com/packages/table-safety) | latest / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [target-direction-pointer](https://foundryvtt.com/packages/target-direction-pointer) | v1.2.0 / 1.2.0 | 36 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [target-tree](https://foundryvtt.com/packages/target-tree) | 3.0.0 / 3.0.0 | — | — | — | 上游资源读取失败，保留原译 |
| [tcal](https://foundryvtt.com/packages/tcal) | 1.2.0 / 1.2.0 | 2 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [team-box](https://foundryvtt.com/packages/team-box) | V1.1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [templatemacro](https://foundryvtt.com/packages/templatemacro) | 11.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [terrain-height-tools](https://foundryvtt.com/packages/terrain-height-tools) | 0.7.5 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [terrainmapper](https://foundryvtt.com/packages/terrainmapper) | 14.0.1 / 14.0.1 | 72 | 18 | 17 | 已同步 v14 语言文件（待实机验证） |
| [the-gold-box](https://foundryvtt.com/packages/the-gold-box) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [the-horses-encumbrance-controls](https://foundryvtt.com/packages/the-horses-encumbrance-controls) | 1.0.7 / 1.1.0 | 9 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [the-lockpicker](https://foundryvtt.com/packages/the-lockpicker) | 1.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [theatre](https://foundryvtt.com/packages/theatre) | v3.4.2 / v3.4.2 | 202 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [theripper-premium-hub](https://foundryvtt.com/packages/theripper-premium-hub) | 6.0.1 / 6.0.1 | 33 | 1 | 1 | 已同步 v14 语言文件（待实机验证） |
| [three-actor-portrait](https://foundryvtt.com/packages/three-actor-portrait) | 4.0.0 / 4.0.0 | — | — | — | 上游资源读取失败，保留原译 |
| [tidbits](https://foundryvtt.com/packages/tidbits) | 4.0.1 / 4.0.1 | — | — | — | 上游资源读取失败，保留原译 |
| [tidy5e-sheet](https://foundryvtt.com/packages/tidy5e-sheet) | 14.2.0 / 14.2.0 | 377 | 377 | 95 | 已同步 v14 语言文件（待实机验证） |
| [tile-scroll](https://foundryvtt.com/packages/tile-scroll) | 5.0.0 / 5.0.0 | 10 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [tile-zoom-fader](https://foundryvtt.com/packages/tile-zoom-fader) | 1.0.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [time-magic](https://foundryvtt.com/packages/time-magic) | 1.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [timeline](https://foundryvtt.com/packages/timeline) | 3.0.0 / 3.0.0 | — | — | — | 上游资源读取失败，保留原译 |
| [times-up](https://foundryvtt.com/packages/times-up) | 13.1.9 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [toggle-snap-to-grid](https://foundryvtt.com/packages/toggle-snap-to-grid) | 13.0.0 / 13.0.0 | 8 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [token-action-hud-core](https://foundryvtt.com/packages/token-action-hud-core) | 2.1.2 / 2.1.2 | 200 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [token-action-hud-dnd5e](https://foundryvtt.com/packages/token-action-hud-dnd5e) | 2.2.0 / 2.2.0 | 87 | 2 | 2 | 已同步 v14 语言文件（待实机验证） |
| [token-attacher](https://foundryvtt.com/packages/token-attacher) | 4.6.12 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [token-color-marker](https://foundryvtt.com/packages/token-color-marker) | 6.0.0 / 6.0.0 | 41 | 2 | 2 | 已同步 v14 语言文件（待实机验证） |
| [token-damage](https://foundryvtt.com/packages/token-damage) | 0.0.4 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [token-defaults](https://foundryvtt.com/packages/token-defaults) | 1.0.6 / 1.0.6 | 14 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [token-ease](https://foundryvtt.com/packages/token-ease) | 1.3.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [token-elevation-shadows](https://foundryvtt.com/packages/token-elevation-shadows) | 2.2.0 / 2.2.0 | 20 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [token-elevator](https://foundryvtt.com/packages/token-elevator) | 1.5.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [token-factions](https://foundryvtt.com/packages/token-factions) | 12.0.3 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [token-hud-wildcard](https://foundryvtt.com/packages/token-hud-wildcard) | 4.1.0 / 4.1.0 | 21 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [token-lean](https://foundryvtt.com/packages/token-lean) | 2.3.0 / 2.3.0 | 22 | 4 | 4 | 已同步 v14 语言文件（待实机验证） |
| [token-loot](https://foundryvtt.com/packages/token-loot) | 1.2.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [token-mirror-button](https://foundryvtt.com/packages/token-mirror-button) | 14.0.1 / 14.0.1 | 7 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [token-mold](https://foundryvtt.com/packages/token-mold) | 2.24.0 / 2.24.0 | 77 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [token-movement](https://foundryvtt.com/packages/token-movement) | 0.1.7 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [token-movement-settings](https://foundryvtt.com/packages/token-movement-settings) | 1.1.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [token-nameplates](https://foundryvtt.com/packages/token-nameplates) | 1.3.8 / 1.3.8 | 134 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [token-note-hover](https://foundryvtt.com/packages/token-note-hover) | 4.1.5 / 4.1.5 | 72 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [token-notes](https://foundryvtt.com/packages/token-notes) | 4.0.0 / 4.0.0 | — | — | — | 上游资源读取失败，保留原译 |
| [token-presets](https://foundryvtt.com/packages/token-presets) | v0.20.0 / 0.20.0 | 127 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [token-reaction-tracker](https://foundryvtt.com/packages/token-reaction-tracker) | 1.3 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [token-resize](https://foundryvtt.com/packages/token-resize) | 3.0.0 / 3.0.0 | — | — | — | 上游资源读取失败，保留原译 |
| [token-says](https://foundryvtt.com/packages/token-says) | 1.13.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [token-tooltip-alt](https://foundryvtt.com/packages/token-tooltip-alt) | 3.3.6 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [token-variants](https://foundryvtt.com/packages/token-variants) | 6.1.3 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [token-z](https://foundryvtt.com/packages/token-z) | 3.0.0 / 3.0.0 | 3 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [tokencover](https://foundryvtt.com/packages/tokencover) | 0.10.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [tokenflip](https://foundryvtt.com/packages/tokenflip) | 5.0.1 / 5.0.1 | — | — | — | 上游资源读取失败，保留原译 |
| [tokenizer-2](https://foundryvtt.com/packages/tokenizer-2) | 2.1.0 / 2.1.0 | 2007 | 1485 | 1231 | 已同步 v14 语言文件（待实机验证） |
| [tokenlightcondition](https://foundryvtt.com/packages/tokenlightcondition) | 1.3.1 / 1.3.1 | — | — | — | v14 清单未声明英文语言文件，保留原译 |
| [tokenmagic](https://foundryvtt.com/packages/tokenmagic) | 0.8.4 / 0.8.4 | 90 | 9 | 7 | 已同步 v14 语言文件（待实机验证） |
| [tokenmagic-automatic-wounds](https://foundryvtt.com/packages/tokenmagic-automatic-wounds) | 1.1.27 / 1.1.27 | 24 | 4 | 4 | 已同步 v14 语言文件（待实机验证） |
| [tokenprofile](https://foundryvtt.com/packages/tokenprofile) | 1.3.0 / 1.3.0 | 61 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [tokenvisibility](https://foundryvtt.com/packages/tokenvisibility) | 14.0.0 / 14.0.0 | 92 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [tokenwarp](https://foundryvtt.com/packages/tokenwarp) | 14.365.4.1 / 14.365.4.1 | 48 | 13 | 12 | 已同步 v14 语言文件（待实机验证） |
| [torch](https://foundryvtt.com/packages/torch) | 3.3.0 / 3.3.0 | 27 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [touch-vtt](https://foundryvtt.com/packages/touch-vtt) | 2.3.13 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [transform-cleanup](https://foundryvtt.com/packages/transform-cleanup) | 14.361.5.3.3.1 / 14.361.5.3.3.1 | 2 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [translate-all](https://foundryvtt.com/packages/translate-all) | 2.1.10 / 2.1.10 | 50 | 28 | 25 | 已同步 v14 语言文件（待实机验证） |
| [trap-automator](https://foundryvtt.com/packages/trap-automator) | 1.0.7 / 1.0.7 | 2 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [travel-pace](https://foundryvtt.com/packages/travel-pace) | 5.3.1 / 5.3.1 | — | — | — | v14 清单未声明英文语言文件，保留原译 |
| [traveller-toolkit](https://foundryvtt.com/packages/traveller-toolkit) | 0.7.1-light / 0.7.1-light | 11 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [trigger-engine](https://foundryvtt.com/packages/trigger-engine) | 1.36.0 / 1.36.0 | 577 | 199 | 147 | 已同步 v14 语言文件（待实机验证） |
| [uiscaler](https://foundryvtt.com/packages/uiscaler) | 1.6.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [unboxing-mystery](https://foundryvtt.com/packages/unboxing-mystery) | 1.5.0 / 1.5.0 | — | — | — | 上游资源读取失败，保留原译 |
| [universal-animations](https://foundryvtt.com/packages/universal-animations) | 0.4.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [unkenny](https://foundryvtt.com/packages/unkenny) | 2.1.0 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [update-your-password](https://foundryvtt.com/packages/update-your-password) | 4.0.0 / 4.0.0 | 12 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [vauxs-archives](https://foundryvtt.com/packages/vauxs-archives) | 2.1.3 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [vf-5e-sheet-addons](https://foundryvtt.com/packages/vf-5e-sheet-addons) | 1.0.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [vgmusic](https://foundryvtt.com/packages/vgmusic) | 1.4.2 / 1.4.2 | — | — | — | v14 清单未声明英文语言文件，保留原译 |
| [video-scaler](https://foundryvtt.com/packages/video-scaler) | 1.0.1 / 1.0.1 | 2 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [visage](https://foundryvtt.com/packages/visage) | 5.12.0 / 5.12.0 | 665 | 263 | 237 | 已同步 v14 语言文件（待实机验证） |
| [vision-5e](https://foundryvtt.com/packages/vision-5e) | 3.2.3 / 3.2.3 | 23 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [vision-blur](https://foundryvtt.com/packages/vision-blur) | 1.4.0 / 1.4.0 | 27 | 10 | 10 | 已同步 v14 语言文件（待实机验证） |
| [vision-toolkit](https://foundryvtt.com/packages/vision-toolkit) | 2.1.13 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [visual-active-effects](https://foundryvtt.com/packages/visual-active-effects) | 14.0.3 / 14.0.3 | 21 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [visual-novel-maker](https://foundryvtt.com/packages/visual-novel-maker) | 1.4.2 / 1.4.2 | — | — | — | 上游资源读取失败，保留原译 |
| [vtta-tokenizer](https://foundryvtt.com/packages/vtta-tokenizer) | 5.0.3 / 5.0.3 | 207 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [vueport](https://foundryvtt.com/packages/vueport) | 1.2 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [wall-height](https://foundryvtt.com/packages/wall-height) | 7.0.8 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [walledtemplates](https://foundryvtt.com/packages/walledtemplates) | 0.9.6 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [walls-have-ears](https://foundryvtt.com/packages/walls-have-ears) | 3.14.2 / 3.14.2 | 16 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [walls-resize-buttons](https://foundryvtt.com/packages/walls-resize-buttons) | 1.0.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [wanted-level](https://foundryvtt.com/packages/wanted-level) | v1.0.1 / 1.0.1 | 4 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [wayfinder](https://foundryvtt.com/packages/wayfinder) | 14.1.3 / 14.1.3 | 4 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [wayfinder-auto-grid](https://foundryvtt.com/packages/wayfinder-auto-grid) | 1.1.2 / 1.1.2 | 46 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [wayfinder-core](https://foundryvtt.com/packages/wayfinder-core) | 1.1.1 / 1.1.1 | 38 | 4 | 3 | 已同步 v14 语言文件（待实机验证） |
| [wgtgm-mini-calendar](https://foundryvtt.com/packages/wgtgm-mini-calendar) | 10.2.2 / 10.2.2 | 26 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [wgtgm-mini-player](https://foundryvtt.com/packages/wgtgm-mini-player) | 14.0.6 / 14.0.6 | 119 | 2 | 2 | 已同步 v14 语言文件（待实机验证） |
| [wgtngm-light-switch](https://foundryvtt.com/packages/wgtngm-light-switch) | 1.2.1 / 1.2.1 | 44 | 8 | 7 | 已同步 v14 语言文件（待实机验证） |
| [wgtngm-mini-edit](https://foundryvtt.com/packages/wgtngm-mini-edit) | 0.7.7 / 0.7.7 | 15 | 4 | 4 | 已同步 v14 语言文件（待实机验证） |
| [whisper-as](https://foundryvtt.com/packages/whisper-as) | 3.0.4 / 3.0.4 | 22 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [wild-magic-surge-5e](https://foundryvtt.com/packages/wild-magic-surge-5e) | 7.4.0 / 7.4.0 | 88 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [wildharvest](https://foundryvtt.com/packages/wildharvest) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [window-controls-next](https://foundryvtt.com/packages/window-controls-next) | 14.0.1.0 / 14.0.1.0 | 59 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [wizzlethorpe-labs](https://foundryvtt.com/packages/wizzlethorpe-labs) | — / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [wm5e](https://foundryvtt.com/packages/wm5e) | 14.606.1 / 14.606.1 | 43 | 24 | 22 | 已同步 v14 语言文件（待实机验证） |
| [world-explorer](https://foundryvtt.com/packages/world-explorer) | 2.2.1 / 2.2.1 | 43 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [world-lock](https://foundryvtt.com/packages/world-lock) | 0.1.0 / 0.1.0 | 5 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [world-scripter](https://foundryvtt.com/packages/world-scripter) | 1.1.0 / 1.1.0 | 5 | 4 | 2 | 已同步 v14 语言文件（待实机验证） |
| [world-setting-sync](https://foundryvtt.com/packages/world-setting-sync) | 3.0.0 / 3.0.0 | — | — | — | 上游资源读取失败，保留原译 |
| [yakuza-fy](https://foundryvtt.com/packages/yakuza-fy) | v1.2.1 / — | — | — | — | 未找到官方目录中 Verified 14 的发布版，保留原译 |
| [yendors-scene-actors](https://foundryvtt.com/packages/yendors-scene-actors) | 3.0.1 / 3.0.1 | 64 | 1 | 1 | 已同步 v14 语言文件（待实机验证） |
| [yendors-user-passwords](https://foundryvtt.com/packages/yendors-user-passwords) | 1.0.0 / 1.0.0 | 39 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [your-flavor](https://foundryvtt.com/packages/your-flavor) | 5.0.1 / 5.0.1 | 1863 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [your-turn](https://foundryvtt.com/packages/your-turn) | 1.4.11 / 1.4.11 | 6 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [youtube-sync](https://foundryvtt.com/packages/youtube-sync) | 1.0.3 / 1.0.3 | 21 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [yt-jukebox](https://foundryvtt.com/packages/yt-jukebox) | 0.5.5 / 0.5.5 | 13 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [yugen-criticals](https://foundryvtt.com/packages/yugen-criticals) | 1.0.14 / 1.0.14 | 111 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [yugen-downtime](https://foundryvtt.com/packages/yugen-downtime) | 1.0.4 / 1.0.4 | 21 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [yugen-merchant](https://foundryvtt.com/packages/yugen-merchant) | 1.0.4 / 1.0.4 | 49 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [yugen-modifiers](https://foundryvtt.com/packages/yugen-modifiers) | 1.0.4 / 1.0.4 | 55 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [yugen-party](https://foundryvtt.com/packages/yugen-party) | — / — | — | — | — | 上游资源读取失败，保留原译 |
| [yugen-tracker](https://foundryvtt.com/packages/yugen-tracker) | 1.0.6 / 1.0.6 | 99 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [yugen-utils](https://foundryvtt.com/packages/yugen-utils) | 1.0.4 / 1.0.4 | 1 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [yuuko-chat-interface-overhaul](https://foundryvtt.com/packages/yuuko-chat-interface-overhaul) | 1.1.6 / 1.1.6 | 176 | 44 | 0 | 已同步 v14 语言文件（待实机验证） |
| [z-scatter](https://foundryvtt.com/packages/z-scatter) | 2.3.0 / 2.3.0 | 17 | 2 | 2 | 已同步 v14 语言文件（待实机验证） |
| [zipperinitiative](https://foundryvtt.com/packages/zipperinitiative) | 14.0.0 / 14.0.0 | 16 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [zone-movement](https://foundryvtt.com/packages/zone-movement) | 1.4.5 / 1.4.5 | 33 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
| [zoom-pan-options](https://foundryvtt.com/packages/zoom-pan-options) | 2.2.1 / 2.2.1 | 30 | 0 | 0 | 已同步 v14 语言文件（待实机验证） |
