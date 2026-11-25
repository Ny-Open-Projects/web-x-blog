---
title: [PER-962] 样式重算（Style Recalc）的失效传播机制是怎样的
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-962：样式重算（Style Recalc）的失效传播机制是怎样的

**答**：
- Blink 为每个元素维护 StyleRule 集合，样式变更时计算"失效集合"：从变更节点向上找共同祖先再向下重算受影响子树。
- 代价取决于失效范围而非元素总数：改 body 上的类可能全树重算；改叶子节点通常只影响自身与后代。
-  descendant invalidation（:hover 后代选择器、属性选择器）会让失效集扩大——选择器越复杂，重算越贵。
- 实测方法：DevTools Performance 面板看 Recalculate Style 的"Elements Affected"数量；大量受影响元素说明选择器或 DOM 结构需要治理。

```javascript
// 检测样式失效范围的实验法
const root = document.querySelector('#list');
console.time('style');
root.classList.add('theme-dark');     // 若 CSS 里有 .theme-dark *，全树失效
requestAnimationFrame(() => {
  requestAnimationFrame(() => console.timeEnd('style'));  // 观察耗时
});
// 优化：避免通配后代选择器；用 CSS 自定义属性切换主题，
// 变量更新不触发结构级失效：
root.style.setProperty('--accent', 'red');
```
