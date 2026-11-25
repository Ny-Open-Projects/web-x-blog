---
title: [RBL-210] Rspack 插件性能怎么剖析定位
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-210：Rspack 插件性能怎么剖析定位

**答**:
- 工具一：`rspack build --profile`（或 experiments.profile）输出各阶段与钩子耗时，直接看到 JS 插件占比
- 工具二：Node 侧 CPU profile（--cpu-prof），插件函数在火焰图中的宽度即其开销
- 手动度量：插件钩子入口出口打点（performance.now），按插件名聚合上报，形成「插件耗时表」
- 优化路径排序：跨边界数据量（缩范围）→ 钩子频率（收敛到低频钩子）→ 算法本身（缓存/增量）；通常第一步就解决 80%

```javascript
// 插件打点装饰器
function timed(hookName, tapFn) {
  return (...args) => {
    const t0 = performance.now()
    tapFn(...args)
    pluginTimes.set(hookName, (pluginTimes.get(hookName) ?? 0) + performance.now() - t0)
  }
}
// done 时输出
compiler.hooks.done.tap('Report', () => {
  console.log([...pluginTimes.entries()].sort((a, b) => b[1] - a[1]))
})
```
