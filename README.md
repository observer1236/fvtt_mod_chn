# Foundry VTT Mod 翻译包（v14 候选版）

本分支面向 Foundry VTT 14.369，版本为 14.0.0-beta.1。已核对原仓库全部 950 个模块目录，取得并同步 532 份 v14 英文语言快照；176 个模块共更新 14,467 条译文。

**本次更新包含 11,872 条待人工校对的机器翻译，尚未进行真实 Foundry 会话测试。其余 418 个模块保留原译；不能视为全部模块已完成 v14 适配。**

详细范围、每个模块的版本和未完成项目见 [v14 适配报告](docs/V14-STATUS.md)。来源和校对记录见 [版本清单](docs/v14-audit.json)、[翻译校对队列](docs/v14-translation-review.json)。

## 手动安装

构建或取得候选安装包 mod_chn.zip，将包内文件解压到 Foundry 用户数据的 `Data/modules/zzz_mod_chn/`，确认该目录下直接包含 module.json、cn.json 和 welcome.js。重新启动 Foundry，选用中文并在世界中启用 Translation: 中文 [Mod]。

仓库清单中的候选 Release 下载地址需待发布对应附件后才可使用。v13 用户请继续使用上游的 13.99 版本；本候选包要求 v14。

如同时启用 Mega 汉化包，会提示是否禁用冲突模块。取消或关闭提示不会更改模块配置。

## 构建及验证

需要 Python 3.12+；JavaScript 模拟测试使用 Node.js 22+。

```text
python -m unittest discover -s tests -p "test_*.py"
node --test tests/welcome.test.mjs
python scripts/build_release.py
```

build_release.py 会合并译文、校验并生成根目录 mod_chn.zip。构建不需要网络或第三方 Python 包。

查询公开上游版本可运行 `python scripts/audit_v14.py`，可选 `--direct` 忽略代理；不会自动覆盖已提交译文。

原始汉化来源：[Memorize-Remix/fvtt_mod_chn](https://github.com/Memorize-Remix/fvtt_mod_chn)。本 fork：[observer1236/fvtt_mod_chn](https://github.com/observer1236/fvtt_mod_chn)。原作者信息保留在 module.json 中。
