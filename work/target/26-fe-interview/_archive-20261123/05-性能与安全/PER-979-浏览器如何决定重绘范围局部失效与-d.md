---
title: [PER-979] 浏览器如何决定重绘范围？局部失效与 dirty rect 是什么
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-979：浏览器如何决定重绘范围？局部失效与 dirty rect 是什么

**答**：
- 绘制失效是"脏区"模型：变更只标记受影响的绘制区域，Paint 只重出脏区的绘制记录，栅格只重画脏块。
- 失效范围可被放大：祖先的 overflow 可见、will-change 大层、层边界穿越都会扩大脏区。
- 实践：限制溢出（overflow: clip）、让动画元素独立成小层、避免背景随子元素变化。
- 验证：DevTools Rendering 面板开启 Paint flashing，观察绿色重绘块是否远大于实际变更区域。

```javascript
/* 限制脏区扩散 */
.dialog { overflow: clip; contain: paint; }   /* 内部动画不外溢 */
.banner img { will-change: transform; }        /* 动画元素小层化 */
/* Paint flashing 实验：
   未加 contain：hover 触发整页绿色闪烁
   加 contain：仅 dialog 区域闪烁 */
```
