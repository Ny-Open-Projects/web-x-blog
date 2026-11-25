---
title: [MFW-584] SSR 性能 profiling：渲染树火焰图的构建与解读
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-584：SSR 渲染火焰图

**答**:
- 渲染火焰图的构建：RSC 渲染的 async 组件树天然是「调用树」——trace span 树（RBL-542）转火焰图（宽度 = 耗时、层级 = 组件嵌套）；「span 树 → 火焰图」的数据变换（RBL-728 的可视化层）。
- 火焰图的解读：1) **宽而浅的叶子**（单组件慢——fetch 慢：数据优化）；2) **串行阶梯**（兄弟组件顺序执行——并行化机会：Promise.all）；3) **深嵌套窄条**（组件层层 await——数据依赖链：重构数据获取）；4) Suspense 边界间的间隙（等待窗口——数据未就绪的空转）。
- 与 client 火焰图的差异：SSR 火焰图的主力是 IO（fetch/db）而非 JS 计算——「IO 瀑布」是 SSR 性能的头号问题（JS 执行在 server 侧通常 <50ms）。
- 追问钩子：为什么 SSR 火焰图里「串行阶梯」比「单条慢查询」更常见且更值得修？——单条慢查询（800ms）是 DB 问题（索引/缓存）；串行阶梯（3 个 200ms 顺序查询 = 600ms）是代码结构问题（await 链）——并行化零风险（无依赖时 Promise.all = 600ms → 200ms）；「结构性优化（并行）优先于物理优化（索引）」：收益大、风险低——SSR 性能优化的第一课。

```javascript
// span 树 → 火焰图数据（RBL-844 规范）
function spansToFlame(span) {
  return {
    name: span.name,
    value: span.durationMs,
    children: span.children.map(spansToFlame),
  };
}
// 渲染树示例
// rsc:page (900ms)
// ├── Header (5ms)
// ├── ProductView (820ms)           ← 宽叶：数据慢
// │   ├── getProduct (600ms)        ← 单条慢查询
// │   └── getReviews (400ms)        ← 串行阶梯！与 getProduct 无依赖
// │       └── db.reviews (200ms)
// └── Footer (3ms)
// 修复：Promise.all([getProduct, getReviews]) → 820ms → 620ms
// Suspense 间隙：ProductView 在边界内 → 600ms 等待窗口 = 用户看骨架的时间
```
