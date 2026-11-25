---
title: [BLD-233] 模块图到 chunk 的分配算法怎么工作？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-233：chunk 分配算法怎么工作？
**答**：
- 分配输入：模块图 + 入口集 + 分割配置 → 输出 chunk 图——算法目标：共享模块去重（多入口共享不重复打包）+ 加载效率（并行度与请求大小）。
- rollup 分配：动态入口生成 chunk，共享模块归入「被引用最多入口」的公共 chunk 或独立 shared chunk——粒度可控（manualChunks 覆盖）。
- webpack splitChunks：按 cacheGroups 规则（test/enforce/minChunks/priority）匹配模块归属——priority 决定组间冲突归属。
- 分配的约束：chunk 图无环（SCN-BLD-214）+ 加载性能（大 chunk vs 多请求平衡）。
- 追问钩子：为什么「同一模块被 main 和 async 两个 chunk 引用」会被提升——如果不提升，该模块会分别打进两个 chunk（重复 50%）；提升到独立 chunk 后两处引用同一文件（缓存复用）——分配算法的核心目标就是「每个模块在最终产物中恰好出现一次」。

```javascript
// 分配示意
// main: [app, utils]  async: [chart, utils]
// → main: [app], async: [chart], shared: [utils]    // utils 去重提升
// webpack priority 示例
cacheGroups: {
  vendor: { test: /node_modules/, priority: 10 },    // 高优先级先匹配
  common: { minChunks: 2, priority: 5, reuseExistingChunk: true },
}
```
