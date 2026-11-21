---
title: [CSS-259] will-change 的正确用法与常见误用
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## CSS-259：will-change 的正确用法与常见误用

**答**：
- 语义：向浏览器提前声明「此属性将变化」，让浏览器预备优化（提升合成层、分配内存）——是提示不是开关
- 正确用法：交互即将发生前加（如 hover 前）、用后移除（JS 加 class 再移除）；常变化的元素可常驻
- 误用一：全站元素挂 will-change: transform——每个都建合成层，内存爆炸反而更慢
- 误用二：以为 will-change「加速」——它只是预先优化，本身不减少绘制量；真正的优化是把动画限制在 transform/opacity
- 判断标准：加前后用 Performance 面板对比，没收益就删

```css
.modal { transition: transform .3s; }
/* 只在打开前提升 */
.modal.about-to-open { will-change: transform; }
.modal.open { transform: translateY(0); }
/* 打开完成后 JS 移除 about-to-open */
```
