---
title: [BAS-152] inherit、initial、unset、revert 分别是什么效果？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-152：inherit、initial、unset、revert 分别是什么效果？
**答**：
- inherit：强制继承父元素的值，即使该属性默认不继承。
- initial：回到 CSS 规范定义的属性初始值（注意 display:initial 是 inline，不是浏览器默认的 block）。
- unset：可继承属性当 inherit，不可继承属性当 initial；revert：回退到浏览器默认样式表（user-agent），比 initial 更接近"撤销作者样式"。

```css
a { color: red; }
.reset a {
  color: inherit;   /* 强制继承父级颜色 */
  border: initial;  /* 属性规范初始值 none */
  margin: unset;    /* margin 不可继承 → 等价 initial */
  padding: revert;  /* 回退到浏览器 UA 样式表 */
}
```
