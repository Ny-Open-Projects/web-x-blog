---
title: [CSS-089] conic-gradient 有哪些高级用法？饼图和棋盘格怎么画？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-089：conic-gradient 有哪些高级用法？饼图和棋盘格怎么画？

**答**：
- `conic-gradient(from 角度 at 位置)` 按角度扫色，一段一段写色标即成饼图/圆环。
- 棋盘格：0/90/180/270 度四段双色 + `background-size` 重复平铺，两行代码。
- 圆环进度：conic-gradient 扇形 + `mask` 径向挖洞，配 `@property` 注册角度变量即可动画。
- 相邻色标写成同值即得硬边界分段，无需多元素叠加。

```css
/* 1. 饼图：三段占比 40% / 35% / 25% */
.pie {
  width: 160px; aspect-ratio: 1; border-radius: 50%;
  background: conic-gradient(
    var(--c1) 0 40%,
    var(--c2) 40% 75%,
    var(--c3) 75% 100%
  );
}

/* 2. 圆环进度：扇形 + mask 挖洞 */
.ring {
  border-radius: 50%;
  background: conic-gradient(var(--brand) calc(var(--pct) * 1%), transparent 0);
  mask: radial-gradient(circle, transparent 58%, #000 59%);
}

/* 3. 棋盘格：透明占位背景 */
.checker {
  background: conic-gradient(#eee 0 25%, transparent 0 50%, #eee 0 75%, transparent 0);
  background-size: 24px 24px;
}
```
