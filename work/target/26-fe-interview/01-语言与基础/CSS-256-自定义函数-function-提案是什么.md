---
title: [CSS-256] 自定义函数 @function 提案是什么
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 新特性]
type: 面试题
---

## CSS-256：自定义函数 @function 提案是什么

**答**：
- @function：在 CSS 里定义可复用的计算函数——`--function pow(n, p) { result: calc(n ** p) }` 这类参数化计算
- 价值：复杂 calc 表达式（尺寸换算、色阶计算）抽成函数，一处定义多处调用，可读性质变
- 与 Sass 函数的区别：运行时求值（随 CSS 变量实时变化），Sass 是编译期——配合 @property 能做响应式计算
- 配套特性：tail arguments、命名参数；和 @mixin 提案（条件/循环的样式复用）同属「CSS 程序化」路线
- 现状：Chrome 138+ 实验实现，生产远未成熟；面试讲清「运行时 vs 编译期」的分界即可

```css
@function --pow(--base, --exp) {
  result: calc(var(--base) ** var(--exp));
}
.size-3 {
  width: --pow(2, 8) * 1px;  /* 256px，且 base/exp 为变量时实时重算 */
}
```
