---
title: [RBL-041] 笔试：手写构建耗时分段统计插件（多阶段打点）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-041：笔试：手写构建耗时分段统计插件（多阶段打点）
**答**：实现 StageTimingPlugin：1) 分别统计 resolve 前后（thisCompilation→make）、make→finishModules、emit 前后、总时长四段；2) watch 模式每次 rebuild 重新统计；3) 输出 JSON 到 stdout；4) 使用 performance.now 保证精度；5) done 钩子里输出并区分单次构建/重建标签。

```javascript
class StageTimingPlugin {
  apply(compiler) {
    const now = () => performance.now();
    let t = {};
    // compilation 钩子在每次 rebuild 都触发 → 天然支持 watch 重新统计
    compiler.hooks.compilation.tap('StageTimingPlugin', (c) => {
      t.compilationStart = now();
      c.hooks.finishModules.tap('StageTimingPlugin', () => {
        t.buildModules = now() - t.compilationStart;
      });
    });
    compiler.hooks.make.tap('StageTimingPlugin', () => { t.makeStart = now(); });
    compiler.hooks.beforeCompile.tap('StageTimingPlugin', () => { t.before = now(); });
    compiler.hooks.emit.tap('StageTimingPlugin', () => { t.emitStart = now(); });
    compiler.hooks.done.tap('StageTimingPlugin', (stats) => {
      console.log(JSON.stringify({
        watchRebuild: stats.compilation !== compiler.lastCompilation || !!compiler.watching,
        buildModulesMs: +(t.buildModules || 0).toFixed(1),
        totalMs: +stats.endTime && stats.endTime - stats.startTime,
      }));
      t = {};
    });
  }
}
module.exports = StageTimingPlugin;
```
**评分点**：
- compilation 钩子注册统计（watch 下自动重置）——关键点。
- 使用 performance.now 而非 Date.now（精度）。
- done 里用 stats.startTime/endTime 拿权威总时长。
- 分段含义讲清楚：finishModules=模块构建完成、emit=产物写出前。
- 能指出：Rspack 场景该插件用于对比 JS 钩子开销 vs Rust 内核开销。
