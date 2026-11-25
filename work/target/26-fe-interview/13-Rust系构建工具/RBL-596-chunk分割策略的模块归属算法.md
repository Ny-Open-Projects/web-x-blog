---
title: [RBL-596] Chunk 分割策略：模块归属的算法家族与商业场景校准
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-596：Chunk 分割策略：模块归属的算法家族与商业场景校准

**答**：
- 分割算法家族：1) **入口静态分组**（entry 闭包各成一个 chunk，无共享拆分）；2) **共享模块启发式**（被 ≥N 个入口引用才拆出 shared chunk，rollup 的 manualChunks/minShared）；3) **最优二分/图划分**（把「引用相似性」当图划分问题，minCut 拆出公共子图——理论最优但复杂度高，工业上以启发式为主）；4) **路由/动态 import 驱动**（每个 dynamic import 天然是边界，业务最常用）。
- 商业场景校准才是实战重点：电商大促场景要「首页壳极小 + 活动页独立」→ 分割目标偏激进；后台管理场景页面切换频繁 → 反而要「适度合并」（chunk 太碎导致并行请求数爆炸与瀑布依赖）。分割策略是业务权衡，没有数学最优解。
- 关键权衡链：chunk 数量 ↑ → 缓存粒度细但请求多/预加载复杂；chunk 尺寸 ↑ → 请求少但缓存命中率低。经验带宽：初始加载 JS 每页面 ≤200KB 压缩后、chunk 数 ≤20~30 个、单 chunk ≥20KB（低于此合并）。
- 归属判定细节：一个模块只属一个 chunk（复制 vs 引用取舍：小模块多入口引用时**复制进各入口 chunk** 反而更优——省一次网络往返，rollup 的内联策略）；动态 chunk 的预取链（dynamic import 的依赖闭包）要成组归属保证原子加载。
- 追问钩子：为什么 vendor 拆分（node_modules 全拆一个 chunk）是过时经验？——长缓存收益依赖「依赖版本不变」，但现代依赖更新频繁，vendor chunk 失效反而拖累；splitChunks 的 chunks:'all' + cacheGroups 按使用频率分组比一刀切 vendor 更优。

```javascript
// 分割决策流水线
function assignChunks(graph, entries, opts) {
  const owner = new Map();
  // 1) entry 闭包初始化
  for (const e of entries) for (const m of closure(graph, e)) owner.set(m, e);
  // 2) 动态 import 边界
  for (const dyn of graph.dynamicImports()) {
    for (const m of closure(graph, dyn)) owner.set(m, dyn);   // 深层闭包归动态 chunk
  }
  // 3) 共享模块提取：被多个 owner 引用
  const refCount = countBy(owner);
  for (const [m, count] of refCount) {
    if (count >= opts.minShared && sizeOf(m) >= opts.minSize) {
      owner.set(m, makeSharedChunk(m, [...refCount.keys()]));
    } else if (count > 1 && sizeOf(m) < opts.minSize) {
      markInline(m);                       // 小共享模块复制内联（省往返）
    }
  }
  // 4) 带宽校验：过小合并、过大再切
  return rebalance(owner, { maxChunkKB: 200, minChunkKB: 20 });
}
```
