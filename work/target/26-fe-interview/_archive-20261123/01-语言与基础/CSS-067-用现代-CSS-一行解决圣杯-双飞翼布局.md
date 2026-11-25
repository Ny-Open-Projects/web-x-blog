---
title: [CSS-067] 用现代 CSS 一行解决圣杯/双飞翼布局？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-067：用现代 CSS 一行解决圣杯/双飞翼布局？

**答**：
- 传统圣杯/双飞翼靠 float + 负 margin + padding hack，中列 DOM 顺序还要提前。
- Grid 用 `grid-template-areas` 一次声明三区，行高 `100vh`，天然顺序分离。
- 中列写 `minmax(0, 1fr)` 防止长内容把布局撑爆（对应 flex 的 min-width: 0 问题）。
- 响应式降级只需重写 areas，无需改 DOM。

```css
.holy-grail {
  display: grid;
  grid-template-areas: "header header header" "aside main extra" "footer footer footer";
  grid-template-columns: 200px minmax(0, 1fr) 200px;
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
}
.holy-grail > header { grid-area: header; }
.holy-grail > aside  { grid-area: aside; }
.holy-grail > main   { grid-area: main; }
.holy-grail > .extra { grid-area: extra; }
.holy-grail > footer { grid-area: footer; }

@media (max-width: 768px) {
  .holy-grail {
    grid-template-areas: "header" "main" "aside" "extra" "footer";
    grid-template-columns: minmax(0, 1fr);
  }
}
```
