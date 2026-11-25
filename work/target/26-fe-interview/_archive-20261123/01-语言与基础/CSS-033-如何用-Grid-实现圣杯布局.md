---
title: [CSS-033] 如何用 Grid 实现圣杯布局？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-033：如何用 Grid 实现圣杯布局？

**答**：
- 三行结构：顶部 header、中部三栏（左中右）、底部 footer，中栏自适应。
- 用 `grid-template-areas` 命名比浮动/负 margin 版本简洁一个量级。
- 中栏左右固定宽度，中间 1fr，天然等高（行高由最高列决定）。
- 窄屏时改一下模板字符串即可变单列，无需改 HTML。

```css
.holy-grail {
  display: grid;
  grid-template:
    "header header header" 60px
    "left   main   right"  1fr
    "footer footer footer" 50px
    / 180px 1fr 180px;   /* rows / columns 一次性定义 */
  min-height: 100vh;
}
.holy-grail > header { grid-area: header; }
.holy-grail > .left  { grid-area: left; }
.holy-grail > main   { grid-area: main; }
.holy-grail > .right { grid-area: right; }
.holy-grail > footer { grid-area: footer; }

@media (max-width: 768px) {
  .holy-grail {
    grid-template:
      "header" 60px
      "main"   1fr
      "left"   auto
      "right"  auto
      "footer" 50px
      / 1fr;
  }
}
```

## 六、居中方案
