---
title: [ENG-223] 产物元信息（buildinfo：版本/依赖清单/环境）怎么设计？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-223：产物元信息怎么设计？
**答**：
- buildinfo 内容：commit/构建时间/工具链版本/依赖清单（SBOM 引用）/环境标识/产物 hash——线上页面可自省「我是谁」（暴露 debug 接口或 meta 标签）。
- 排障价值：用户报障时拿 buildinfo 直接定位版本，秒答「这个问题在 vX.Y 修了」；比问用户「你清缓存了吗」高效得多。
- 元信息注入：构建时注入（ Define/环境变量）+ 运行时接口（window.__BUILD__）+ HTML meta 三通道。
- 版本契约：runtime 与元信息的兼容性检查（新旧 chunk 混载时版本不匹配告警，SCN-SDK 版本管理同源）。
- 追问钩子：为什么要在运行时暴露 buildinfo——线上问题的第一现场是浏览器，值班/客服在用户机器上直接读取 buildinfo 就能完成版本定位，不用等构建日志追溯。

```javascript
// 构建时注入
new DefinePlugin({ __BUILD__: JSON.stringify({
  commit: GIT_SHA, builtAt: SOURCE_DATE_EPOCH, version: pkg.version,
  deps: sbomHash, env: process.env.DEPLOY_ENV }) });
// 运行时排障
console.table(window.__BUILD__);
// HTML meta: <meta name="build" content="v2.3.1-abc1234">
```
