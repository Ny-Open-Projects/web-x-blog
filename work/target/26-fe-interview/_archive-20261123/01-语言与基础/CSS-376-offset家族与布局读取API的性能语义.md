---
title: [CSS-376] offset 家族与布局读取 API 的性能语义
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## CSS-376：offset 家族与布局读取 API 的性能语义

**答**：
- 读取 API 分级：offsetWidth/scrollTop（强制 layout，最贵）、getBoundingClientRect（也强制 layout 但返回 viewport 坐标 + 精确小数）、getClientRects（多行内联元素每行矩形）、ResizeObserver/IntersectionObserver（异步回调，不强制布局）——「能 IO/RO 解决的绝不 offset」
- 强制同步布局触发条件：样式脏 + 读布局属性——同一帧第一次读付全款，后续读免费（直到再次写）；所以「读-写-读-写」交错最贵，批量读再批量写是纪律
- 语义差异陷阱：offsetWidth 含 border 不含 margin、取整丢失小数（getBoundingClientRect 不取整）、display:none 元素全部返回 0（visibility: hidden 有值）——测量逻辑要处理隐藏分支
- 高频读取场景的正确姿势：滚动视差用 rAF 内一次性读 → 计算 → 写；元素可见性用 IntersectionObserver 而不是 scroll 里 getBoundingClientRect
- 新 API：Element.checkVisibility() 判断真实可见性（考虑 display/visibility/content-visibility），替代手写祖先遍历

```javascript
// 反模式: 循环读写交错
rows.forEach(r => r.style.top = r.offsetTop + shift + 'px'); // N 次强制布局
// 正解
const tops = rows.map(r => r.offsetTop);                      // 1 次布局
rows.forEach((r, i) => r.style.top = tops[i] + shift + 'px');
// 可见性: 异步观察
const io = new IntersectionObserver(cb); io.observe(el);
```
