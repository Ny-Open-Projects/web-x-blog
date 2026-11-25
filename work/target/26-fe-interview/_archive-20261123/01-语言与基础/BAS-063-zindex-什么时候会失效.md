---
title: [BAS-063] z-index 什么时候会失效？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-063：z-index 什么时候会失效？
**答**：
- 元素不是定位元素（position 为 static）且不参与 flex/grid 布局时，z-index 无效；flex/grid 子项例外，无需定位也能生效。
- 父级创建了层叠上下文后，子元素 z-index 只在父上下文内部比较，跨上下文时由父级整体决定。
- transform、opacity < 1、filter、will-change、isolation 等会隐式创建层叠上下文，导致"z-index 很大却盖不住别人"。

```css
.parent { transform: translateZ(0); }       /* 隐式创建层叠上下文 */
.parent .child { z-index: 9999; }           /* 只在 parent 内部比较 */
.other { position: relative; z-index: 1; }  /* parent 整体 z-index 为 auto，可能被 .other 盖住 */
```
