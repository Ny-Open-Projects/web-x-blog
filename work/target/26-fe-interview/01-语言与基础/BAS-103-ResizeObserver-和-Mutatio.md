---
title: [BAS-103] ResizeObserver 和 MutationObserver 分别观察什么？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-103：ResizeObserver 和 MutationObserver 分别观察什么？
**答**：
- ResizeObserver 监听元素**自身尺寸**变化，比 window.resize 精细到单个元素，容器自适应场景首选。
- MutationObserver 监听 DOM 树变化（childList/attributes/characterData），回调在微任务时机批量执行；第三方脚本、富文本编辑器常用。
- 还有 IntersectionObserver 监听与视口相交（懒加载、曝光埋点），三者组成替代 scroll 事件的观察器家族。

```javascript
new ResizeObserver((entries) => {
  const { width } = entries[0].contentRect;
  chart.resize(width);                 // 元素变宽就重绘图表
}).observe(box);

new MutationObserver((muts) => {
  console.log(muts[0].type, muts[0].addedNodes);  // childList / attributes / characterData
}).observe(list, { childList: true, subtree: true });
```
