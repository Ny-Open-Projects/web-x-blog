---
title: [RBL-201] Rspack 插件的完整生命周期钩子有哪些
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-201：Rspack 插件的完整生命周期钩子有哪些

**答**:
- 核心钩子按阶段：`compiler.hooks`（environment/afterEnvironment/thisCompilation/emit/afterEmit/done）与 `compilation.hooks`（processAssets/succeedModule/chunkAsset/optimizeChunks）
- 与 webpack 一致的命名让 webpack 插件低改造成本迁移；但部分钩子是 Rspack 特有（如 processAssets 的 stage 细分更严格）
- 钩子类型：SyncHook/SyncBailHook/AsyncSeriesHook/AsyncParallelHook——bail 型返回非 undefined 中断后续
- 关键实践：资源处理统一走 `compilation.hooks.processAssets`（带 stage：PROCESS_ASSETS_STAGE_ADDITIONS→REPORT），不要在 emit 里直接改 assets

```javascript
class MyPlugin {
  apply(compiler) {
    compiler.hooks.thisCompilation.tap('MyPlugin', (compilation) => {
      compilation.hooks.processAssets.tap(
        { name: 'MyPlugin', stage: compilation.constructor.PROCESS_ASSETS_STAGE_OPTIMIZE_SIZE },
        (assets) => {
          for (const [name, source] of Object.entries(assets)) {
            // 只读分析或用 compilation.updateAsset 修改
          }
        })
    })
    compiler.hooks.done.tap('MyPlugin', (stats) => console.log('build done', stats.toJson().time))
  }
}
```
