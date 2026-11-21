---
title: [CSS-064] 属性选择器在工程中如何配合 data-* 做状态样式？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-064：属性选择器在工程中如何配合 data-* 做状态样式？

**答**：
- 用 `[data-state="open"]` 表达组件状态，JS 只改 data 属性，样式切换全在 CSS 层。
- 与 class 变体相比语义更清晰，且天然支持枚举校验与 TS 常量约束。
- 布尔态可省略值：`[data-disabled]` 匹配存在即可。
- 多个状态维度正交组合：`[data-variant][data-size]` 互不干扰。
- 可与 CSS 变量联用，把"状态 → token 映射"收敛到一处。

```css
/* 状态样式：JS 只负责 setAttribute，不再拼 className */
.dialog[data-state="open"]    { opacity: 1; visibility: visible; }
.dialog[data-state="closed"]  { opacity: 0; visibility: hidden; }
.dialog[data-variant="modal"] { position: fixed; inset: 0; }

/* 布尔态 + 组合维度 */
.btn[data-disabled] { opacity: 0.5; cursor: not-allowed; }
.btn[data-variant="primary"][data-size="lg"] {
  --btn-pad: 12px 24px;
  --btn-fs: 16px;
}
```

```javascript
// 状态管理侧：只改属性，样式自动跟随
el.dataset.state = visible ? 'open' : 'closed';
```
