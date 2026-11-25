---
title: [CSS-062] :has() 有哪些高级用法？表单联动怎么做？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-062：:has() 有哪些高级用法？表单联动怎么做？

**答**：
- 父选择器能力：根据后代/后续兄弟的状态选中祖先，如 `.card:has(img)` 只给带图的卡片加布局。
- 表单联动：`label:has(+ input:user-invalid)` 让错误提示随输入状态显隐，纯 CSS 无 JS。
- 兄弟联动：`.form-item:has(input:focus)` 高亮整个表单项容器。
- 性能注意：`:has()` 会让祖先参与匹配，避免在文档根节点上写大范围 `:has()` 扫描。
- 用 `@supports selector(:has(*))` 做渐进增强，不支持时 JS 兜底加类。

```css
/* 1. 表单联动：输入不合法时，前面的 label 变红并显示提示 */
.field { display: flex; flex-direction: column; gap: 4px; }
.field .error { display: none; color: var(--color-danger); }
.field:has(input:user-invalid) .error { display: block; }
.field:has(input:user-invalid) label { color: var(--color-danger); }

/* 2. 父选择器：卡片内没有图片时用紧凑布局 */
.card:has(> img) .card-body { padding: 16px; }
.card:not(:has(> img)) { grid-template-rows: auto; }

/* 3. 全局暗色开关：勾选后影响整页 */
body:has(#dark-toggle:checked) { --bg: #111; --fg: #eee; }
```
