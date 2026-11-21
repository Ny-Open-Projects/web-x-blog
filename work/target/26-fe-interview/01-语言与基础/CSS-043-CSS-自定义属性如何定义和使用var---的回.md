---
title: [CSS-043] CSS 自定义属性如何定义和使用？var() 的回退值怎么写？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-043：CSS 自定义属性如何定义和使用？var() 的回退值怎么写？

**答**：
- 以 `--` 开头声明，`var(--name)` 读取；声明和读取都遵循级联与继承。
- `var(--name, fallback)` 提供回退值，fallback 里还可以再嵌套 var。
- 自定义属性可以被 JS 读写（`getPropertyValue` / `setProperty`），是运行时主题的基础。
- 作用域：`:root` 全局，组件内局部覆盖，子元素继承。

```css
:root {
  --brand: #409eff;
  --gap: 12px;
}
.btn {
  color: var(--brand);
  padding: 8px var(--gap);
  /* 回退值 */
  border-color: var(--btn-border, currentColor);
}
.btn--danger {
  /* 局部覆盖 */
  --brand: #f56c6c;
}

:root {
  /* 嵌套回退 */
  --line: var(--line-strong, var(--brand, #ccc));
}
```

```javascript
// JS 动态读写 CSS 变量
const root = document.documentElement;
root.style.setProperty('--brand', '#67c23a');
console.log(getComputedStyle(root).getPropertyValue('--brand'));
```
