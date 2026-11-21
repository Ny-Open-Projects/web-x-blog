---
title: [CSS-116] 从 CSS 视角，哪些属性触发重排、重绘或仅合成？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-116：从 CSS 视角，哪些属性触发重排、重绘或仅合成？

**答**：
- 仅合成（走 GPU）：`transform`、`opacity`，动画首选。
- 触发重绘：`color/background/box-shadow/border-radius/visibility/text-decoration` 等外观属性，跳过布局但仍要重新绘制。
- 触发重排：一切几何属性（width/height/margin/padding/top/left/font-size），改动沿文档流向上向下传播，成本最高。
- 排查依据见上方分类图：优先把动画属性迁移到 transform/opacity 轴（如 left 位移改 translateX）。
- 读写交错会强制同步布局（layout thrashing），批量改样式或用 class 切换。

```css
/* 1. 反例：动画 left/top 每帧重排 */
.bad-slide { animation: bad 0.3s; }
@keyframes bad { from { left: -100px; } to { left: 0; } }

/* 2. 正解：改用 transform，仅合成 */
.good-slide { position: relative; animation: good 0.3s both; }
@keyframes good { from { transform: translateX(-100px); } to { transform: translateX(0); } }

/* 3. 宽度动画改为 scaleX，布局零参与 */
.progress-fill { transform-origin: 0 50%; transition: transform 0.3s; }
.progress-fill.is-full { transform: scaleX(1); }
```
