---
title: [CSS-266] CSS 求值过程：从样式计算到合成的管线回顾
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## CSS-266：CSS 求值过程：从样式计算到合成的管线

**答**：
- 渲染管线五阶段：解析（HTML/CSS→DOM/CSSOM）→ 样式计算（匹配选择器+级联求计算值）→ 布局（几何）→ 绘制（像素指令/图层）→ 合成（GPU 拼图层）
- 关键概念：计算样式（computed style）≠ 最终样式；重排（layout）必然引发重绘（paint）；重绘不一定重排；合成层变化（transform/opacity）两者都跳过
- 优化落点：把动画约束到合成阶段（transform/opacity）、contain 缩小重算范围、content-visibility 跳过屏幕外
- 布局抖动（thrashing）：同一帧内交替「读布局-写样式」导致强制同步布局——批量读写分离
- 面试话术：能把一条「改 width」与一条「改 transform」走完的管线差异讲清楚，就是扎实的前端

```javascript
// 反例：读写交替 → 每次读都强制 layout
items.forEach(el => { el.style.height = el.offsetWidth + 1 + 'px'; });
// 正例：批量读 → 批量写
const widths = items.map(el => el.offsetWidth);
items.forEach((el, i) => (el.style.height = widths[i] + 1 + 'px'));
```
