---
title: [CSS-056] :has() 选择器能做什么？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-056：:has() 选择器能做什么？

**答**：
- `:has()` 是“父级/前向”选择器：根据**后代或后续兄弟**是否存在来匹配当前元素。
- 典型应用：包含图片的卡片加特殊样式、表单某项非法时高亮整个 fieldset。
- 可与 :not 组合，如 `div:not(:has(p))`。
- 注意性能与兼容基线，避免在大范围选择器上滥用。

```css
/* 含图的卡片：横向布局 */
.card:has(img) { flex-direction: row; }

/* 表单联动：有 invalid 输入时整组标红 */
fieldset:has(input:invalid) {
  border-color: #f56c6c;
}
fieldset:has(input:invalid) .hint { display: block; }

/* 兄弟联动：勾选后展开面板 */
.expand:has(+ .panel) .arrow { transform: rotate(90deg); }

/* 无段落时隐藏容器 */
.section:not(:has(p)) { display: none; }
```

## 十一、CSS 工程化与性能
