---
title: [XP-103] Electron 打包体积优化怎么做？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-103：Electron 打包体积优化怎么做？
**答**：
- 认清大头：**Electron 运行时（Chromium+Node，双平台约 150-200MB 解压后）**是主开销，业务代码通常 <10%；优化重点是"不重复带资源"而非压缩运行时本身。
- 依赖瘦身：`files` 白名单最小化、`asar` 打包业务代码、生产依赖 prune（two-package.json 结构隔离 devDependencies）、排除多语言 locale（`electron-builder` 的 `electronLanguages`）、剔除不需要的平台二进制（原生模块按平台构建）。
- 资源治理：大资源外置（首次启动下载到 userData，模型/字体/皮肤类），图标与素材压缩；`extraResources` 只放必须随包的。
- 分发优化：全量包之外提供 **differential（blockmap）差量更新**；macOS 产物做 universal 或按架构分发取舍（x64+arm64 双包 vs universal 体积翻倍）。
- 门禁：CI 记录安装包/解压后体积趋势，diff 门禁与 XP-116 口径统一；升级 Electron 版本时跑体积对比（版本间差异可达 10MB+）。

```yaml
# electron-builder.yml —— 体积治理配置
appId: com.example.app
asar: true                       # 业务代码 asar 归档（只读，配合白名单）
files:                           # 最小白名单：只打包运行必需
  - build/main.js
  - build/preload.js
  - build/renderer/**            # 渲染层产物（前端构建已 tree-shake）
  - "!**/*.map"                  # sourcemap 不进包，符号表走外置上报（XP-068 同思路）
  - "!**/*.md"
  - "!**/test/**"
asarUnpack:                      # 原生模块与二进制必须 unpack 才能被 require
  - "**/node_modules/better-sqlite3/**"
electronLanguages: [zh-CN, en-US]   # 砍 Chromium locale，省 ~10MB 级
compression: maximum
mac:
  target: { target: dmg, arch: [arm64, x64] }   # 分架构分发（不打 universal）
win:
  target: nsis
nsis:
  differentialPackage: true      # blockmap 差量更新：升级包常 <10% 全量
extraResources:                  # 仅必需随包；模型/大素材走首启动下载到 userData
  - from: assets/icons
    to: icons
# CI 门禁：dmg < 110MB、nsis < 95MB、解压后 diff > 5MB 阻断（口径对齐 XP-116）
```
