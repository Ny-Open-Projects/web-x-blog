---
title: [CSS-090] 径向渐变如何做出光效？鼠标跟随 spotlight 怎么实现？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-090：径向渐变如何做出光效？鼠标跟随 spotlight 怎么实现？

**答**：
- `radial-gradient(circle at x y, 高光色, 透明)` 定义中心光源，at 位置可用 CSS 变量驱动。
- 按钮高光：叠一层顶部椭圆白光模拟玻璃质感。
- 鼠标跟随 spotlight：JS 只更新 `--mx/--my` 两个变量，光斑位置过渡全交给 CSS。
- 多层背景叠加 radial + linear 可一次声明，注意先写的层在上。

```css
.glow-card {
  background:
    radial-gradient(120px circle at var(--mx, 50%) var(--my, 50%),
      color-mix(in srgb, var(--brand) 25%, transparent), transparent 70%),
    linear-gradient(180deg, var(--bg-elevated), var(--bg-surface));
  border: 1px solid var(--border-color);
}

.btn-glossy {
  background:
    radial-gradient(120% 60% at 50% 0%, rgb(255 255 255 / 0.35), transparent 60%),
    linear-gradient(var(--brand), var(--brand-dark));
}

/* JS 只写变量，无 style 内联动画 */
card.addEventListener('pointermove', (e) => {
  const r = card.getBoundingClientRect();
  card.style.setProperty('--mx', `${e.clientX - r.left}px`);
  card.style.setProperty('--my', `${e.clientY - r.top}px`);
});
```
