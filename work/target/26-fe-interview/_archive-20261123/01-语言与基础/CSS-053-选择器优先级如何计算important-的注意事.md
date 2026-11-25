---
title: [CSS-053] 选择器优先级如何计算？!important 的注意事项？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-053：选择器优先级如何计算？!important 的注意事项？

**答**：
- 优先级四元组：内联 style(1,0,0,0) > ID(0,1,0,0) > 类/伪类/属性(0,0,1,0) > 元素/伪元素(0,0,0,1)，高位胜出。
- `!important` 覆盖正常级联；同一声明都带 important 时再比优先级，再比源码顺序。
- `:is()`/`:not()` 取**参数中最高的**优先级，`:where()` 优先级恒为 0。
- 工程规范：禁用 !important，用提高选择器层级或调整加载顺序解决冲突。

```css
/* 优先级对比 */
#nav .item            {}  /* 0,1,1,0 */
.nav .item:hover      {}  /* 0,0,3,0  ID 位更高，上面赢 */
div span              {}  /* 0,0,0,2 */
.item                 {}  /* 0,0,1,0  赢过上一行 */

/* :is 取参数最高优先级 */
:is(#footer, .footer) .link { color: red; }  /* 按 #footer 计算 0,1,1,0 */
:where(#footer, .footer) .link { color: red; } /* 恒为 0,0,1,0 */

/* important 覆盖内联样式，但内联也能加 important */
.text { color: blue !important; }
/* <p class="text" style="color: red"> → blue 生效 */
```
