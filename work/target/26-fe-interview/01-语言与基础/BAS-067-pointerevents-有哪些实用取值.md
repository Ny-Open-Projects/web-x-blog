---
title: [BAS-067] pointer-events 有哪些实用取值？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-067：pointer-events 有哪些实用取值？
**答**：
- `pointer-events: none` 让元素对鼠标/触摸完全"透明"，点击穿透到下层元素；常用于装饰层、提示层。
- 对 HTML 元素基本只用 auto 和 none；SVG 还有 visiblePainted 等精细取值。
- 典型场景：禁用态按钮不再响应也不显手型、canvas 覆盖的提示文案不挡操作、自定义点击穿透。

```css
.overlay-tip {
  position: absolute; inset: 0;
  pointer-events: none;      /* 提示层不拦截点击 */
}
.btn:disabled { pointer-events: none; }  /* 点击直接穿透 */
```
