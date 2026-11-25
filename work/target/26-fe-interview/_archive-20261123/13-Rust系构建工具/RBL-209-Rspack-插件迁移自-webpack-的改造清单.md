---
title: [RBL-209] webpack 插件迁移到 Rspack 的改造清单
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-209：webpack 插件迁移到 Rspack 的改造清单

**答**:
- 第一步兼容性盘点：只用主流钩子（compilation/processAssets/emit/done）的插件大概率直接可用；用 tapable 高级特性（intercept、Promise.all 并行钩子深依赖）或 webpack 内部 API（Module.buildInfo 细节）的要逐个验证
- 常见改造点：`require('webpack').sources` → `compiler.rspack.sources`； Compilation 缓存 API 差异；fs 相关用 compiler.outputFileSystem
- 行为差异验证：迁移后产物做 byte-level diff（同输入下 hash 是否一致），不一致逐个归因
- 不可迁移的兜底：插件在 Node 子进程里跑 webpack 单独处理那部分产物（双构建器过渡方案），限期收敛

```javascript
// 迁移清单（工程化模板）
const checklist = {
  hooksUsed: ['processAssets', 'done'],                 // 1. 盘点钩子
  webpackInternals: ['Module.buildInfo'],               // 2. 内部 API
  sources: 'compiler.rspack.sources',                   // 3. sources 来源替换
  fs: 'compiler.outputFileSystem',                      // 4. fs 替换
  diff: 'byte-level compare on same fixture',           // 5. 产物一致性验证
}
```
