---
title: [RBL-021] 如何对 Rspack 构建做产物分析与诊断？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-021：如何对 Rspack 构建做产物分析与诊断？
**答**：
- 官方工具 Rsdoctor：提供构建时长分析（loader/plugin 各阶段耗时）、产物体积（gzip/原始）、模块依赖链（为什么这个包被打进来）、重复依赖检测，替代 webpack-bundle-analyzer 生态位。
- 原始 stats：rspack build --json 输出 stats.json，可自己写脚本聚合 modules/chunks/assets 三张表，做 CI 体积门禁。
- 体积门禁实战：比对上次产物（size-limit 或自研 manifest diff），超阈值 fail CI，防止" gradual bloat"。
- 构建时长定位：stats.profile 打开 per-module profile，看瓶颈在 loader 转换还是 resolve；Rspack 语境下瓶颈常是 JS loader 与外部 plugin。
- 依赖追溯：用 Rsdoctor 的模块链路功能回答"lodash 全量为什么进来了"，通常是 CJS 副作用导入或 require 导致。
- 追问钩子：分析工具本身会拖慢构建（开 profile），诊断与日常构建要分离。

```javascript
// CI 体积门禁脚本
const fs = require('fs');
const stats = JSON.parse(fs.readFileSync('dist/stats.json'));
const LIMIT = 250 * 1024;
for (const a of stats.assets) {
  if (a.name.endsWith('.js') && a.size > LIMIT) {
    console.error(`超限: ${a.name} ${(a.size / 1024).toFixed(1)}KB > ${LIMIT / 1024}KB`);
    process.exitCode = 1;
  }
}
```
