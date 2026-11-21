---
title: [CSS-065] :focus-visible 与 :focus-within 有什么区别？各适合什么场景？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-065：:focus-visible 与 :focus-within 有什么区别？各适合什么场景？

**答**：
- `:focus-visible` 由浏览器判断"用户是否应该看到焦点环"：键盘 Tab 导航匹配，鼠标点击通常不匹配。
- `:focus-within` 是自身或任意后代持有焦点即匹配，适合把焦点态映射到容器。
- 自定义 focus 样式一律写在 `:focus-visible` 上，避免鼠标点击出现难看的焦点环。
- 输入框组（前缀图标 + input）用 `:focus-within` 整体高亮。
- 出于可访问性，绝不能只写 `outline: none` 而不提供 `:focus-visible` 替代。

```css
/* 键盘导航才显示焦点环，鼠标点击不打扰视觉 */
.btn:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 2px;
}
.btn:focus:not(:focus-visible) { outline: none; }

/* 输入组：input 获得焦点，整个分组高亮 */
.input-group {
  display: flex; align-items: center;
  border: 1px solid var(--border-color);
}
.input-group:focus-within {
  border-color: var(--brand);
  box-shadow: 0 0 0 3px color-mix(in srgb, var(--brand) 20%, transparent);
}
```
