---
title: [CSS-102] CSS 变量主题如何做基础/语义/组件三层 token 分层？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-102：CSS 变量主题如何做基础/语义/组件三层 token 分层？

**答**：
- 基础层 primitive：与业务无关的原始刻度（gray-100、space-4），不直接被组件引用。
- 语义层 semantic：承载业务含义（bg-surface、text-primary、border-strong），组件唯一引用层。
- 组件层 component：组件私有 token（btn-bg、btn-pad），从语义层派生，收敛局部默认值。
- 主题切换只重定义语义层到基础层的映射，组件层与组件代码零改动。
- 三层结构是暗黑模式、多品牌换肤能"低成本扩展"的根本原因。

```css
/* 1. 基础层：原始刻度 */
:root {
  --gray-0: #fff;  --gray-9: #17181a;
  --blue-5: #409eff;
  --space-2: 8px;  --space-4: 16px;
}

/* 2. 语义层：主题切换只动这里 */
:root {
  --bg-surface: var(--gray-0);
  --fg-primary: var(--gray-9);
  --color-accent: var(--blue-5);
  --radius-md: 8px;
}

/* 3. 组件层：从语义层派生 */
.btn {
  --btn-bg: var(--color-accent);
  --btn-pad: var(--space-2) var(--space-4);
  background: var(--btn-bg);
  padding: var(--btn-pad);
  border-radius: var(--radius-md);
}
```
