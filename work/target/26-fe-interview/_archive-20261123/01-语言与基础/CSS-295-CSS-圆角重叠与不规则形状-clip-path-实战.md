---
title: [CSS-295] CSS 圆角重叠与不规则形状：clip-path 实战
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 效果]
type: 面试题
---

## CSS-295：圆角重叠与不规则形状：clip-path 实战

**答**：
- 常见问题：嵌套圆角「内圆角与外圆角不同心」——内半径 = 外半径 - 边距 才视觉一致（border-radius 数学关系）
- clip-path 基础：circle/ellipse/inset/polygon/path()——polygon 画多边形，path() 画任意贝塞尔
- 不规则形状案例：斜切按钮（polygon 切角）、聊天气泡（path 带尾巴）、步骤条箭头
- 动画：clip-path 同形状（相同顶点数）间可过渡——形状变形动画；path() 之间也可插值（同指令数）
- 与 mask 分工：clip 硬裁剪、mask 软过渡；两者可叠加

```css
.cut-btn { clip-path: polygon(8px 0, 100% 0, 100% calc(100% - 8px), calc(100% - 8px) 100%, 0 100%, 0 8px); }
.bubble { clip-path: path('M0,20 Q0,0 20,0 H200 Q220,0 220,20 V80 Q220,100 200,100 H60 L20,130 V100 H20 Q0,100 0,80 Z'); }
/* 内外圆角同心 */
.outer { border-radius: 16px; padding: 8px; }
.inner { border-radius: 8px; }  /* 16 - 8 = 8 */
```
