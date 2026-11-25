---
title: [CSS-063] 如何用 ::part 穿透 Shadow DOM 给 Web Components 做主题？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-063：如何用 ::part 穿透 Shadow DOM 给 Web Components 做主题？

**答**：
- Shadow DOM 内部样式与外部完全隔离，外部选择器无法直接命中内部节点。
- 组件作者在内部元素上声明 `part="foo"`，外部用 `.host::part(foo)` 定向覆盖。
- `::part()` 不能继续写后代组合器，需要暴露多个 part，或用 `exportparts` 向外转发。
- `::theme` 已被规范废弃，不要在生产中使用。
- 主题化第三方 Web Components（设计系统组件库）时这是官方推荐的唯一通道。

```html
<!-- 组件内部：标记可定制部分并对外转发 -->
<template id="tpl">
  <style>/* 组件私有样式，外部不可见 */</style>
  <div part="card" exportparts="card: outer-card">
    <h3 part="title">标题</h3>
    <p part="body">内容</p>
  </div>
</template>
```

```css
/* 外部页面：定向覆盖组件暴露的 part */
fancy-card::part(card) {
  border: 1px solid var(--border-color);
  border-radius: 12px;
}
fancy-card::part(title) { font-size: 18px; }
fancy-card:hover::part(title) { color: var(--brand); }
```
