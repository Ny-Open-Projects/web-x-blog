---
title: [HW-200] 手写 SPA 路由 View Transition——旧页快照/新页渲染/命名元素跨页插值
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-200：手写 SPA 路由 View Transition——旧页快照/新页渲染/命名元素跨页插值
**答**：SPA 路由过渡：navigate 后 startViewTransition 内完成路由渲染（旧页快照 → 新页渲染 → 交叉淡入）；命名元素（商品图从列表到详情的位置插值——view-transition-name 相同的元素跨页自动动画）；数据加载与过渡协调（数据就绪才 startViewTransition，防快照期空白）。

```javascript
async function navigateWithTransition(path) {
  const data = prefetcher.get(path);                      // 数据预取（HW-189）：就绪才过渡
  if (!document.startViewTransition) return router.render(path, await data);   // 降级：直接渲染
  const t = document.startViewTransition(async () => {
    updateDOM(await data);                                // 回调内异步渲染（VT 会等 promise）
  });
  await t.finished;
}
```
```css
/* 命名元素跨页插值：列表缩略图 → 详情大图 位置/尺寸自动动画 */
.product-thumb { view-transition-name: product-hero; }    /* 唯一：同屏只能有一个该 name */
.product-detail .hero { view-transition-name: product-hero; }
::view-transition-old(root) { animation: fade-out 150ms; }
::view-transition-new(root) { animation: fade-in 150ms; }
@media (prefers-reduced-motion: reduce) { ::view-transition-group(*), ::view-transition-old(root),
  ::view-transition-new(root) { animation: none; } }
```
```javascript
// 要点：
// 1. 数据就绪才 startViewTransition —— 快照期渲染空页 = 闪白（时序是最大坑）
// 2. view-transition-name 唯一性（同屏两个同 name = 报错或错乱）—— 列表多元素只能给"焦点元素"命名
// 3. 回调可以返回 Promise（VT 等 DOM 更新完成才交叉）
// 4. reduced-motion 直接禁动画（HW-151/489）
```

**评分点**：
- 数据就绪才 startViewTransition 的时序——本题核心（快照期空白是大坑）。
- 命名元素跨页插值（列表→详情缩略图动画）与唯一性约束。
- 回调返回 Promise 的异步渲染支持。
- reduced-motion 尊重与降级链（HW-151/190 FLIP）。
