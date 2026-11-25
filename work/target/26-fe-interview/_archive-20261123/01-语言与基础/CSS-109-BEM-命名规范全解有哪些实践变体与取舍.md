---
title: [CSS-109] BEM 命名规范全解？有哪些实践变体与取舍？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-109：BEM 命名规范全解？有哪些实践变体与取舍？

**答**：
- 结构 `block__element--modifier`：block 独立语义单元，element 是 block 内组成部分，modifier 表状态或外观。
- 禁止 element 再嵌 element（`.block__el1__el2` 错误），层级关系只体现在 DOM，不体现在类名。
- modifier 两种用法：单独挂 `.btn--disabled`，或组合挂 `.btn.btn--disabled`（配合块级选择器提升稳定性）。
- SASS 的 `&__el {}`、`&--mod {}` 嵌套生成可保持源码结构清晰。
- 取舍：类名冗长但零冲突、可预测；与 SUIT/AMCSS（data 属性）等变体可按团队混用。

```scss
// SASS 中的 BEM 书写
.card {
  background: var(--bg-surface);
  border-radius: var(--radius-md);

  &__header { padding: var(--space-4); }

  &__body  { padding: 0 var(--space-4); }

  &--featured {
    border-color: var(--color-accent);
  }

  // 组合式 modifier：确保只作用于 .card 自身
  &.is-selected {
    outline: 2px solid var(--color-accent);
  }
}
```

```html
<div class="card card--featured is-selected">
  <div class="card__header">标题</div>
  <div class="card__body">内容</div>
</div>
```
