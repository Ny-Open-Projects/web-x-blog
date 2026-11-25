---
title: [BAS-161] ::selection 伪元素能改什么？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-161：::selection 伪元素能改什么？
**答**：
- 定制文本被选中时的样式，只支持少数属性：color、background-color、background、text-shadow、text-decoration、-webkit-text-stroke 等。
- 不支持字号、字体族等影响布局的属性（防止选区重排）。
- 常见用途：品牌主题色选区、深色模式下的选区可读性修正。

```css
::selection {
  background: #1677ff;
  color: #fff;
  text-shadow: none;   /* 只允许 color/background/text-shadow 等少数属性 */
}
.dark ::selection {    /* 深色模式下避免蓝底黑字看不清 */
  background: #4096ff;
  color: #111;
}
```
