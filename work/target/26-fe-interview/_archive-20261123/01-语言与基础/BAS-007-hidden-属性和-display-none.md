---
title: [BAS-007] hidden 属性和 display: none 有什么区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-007：hidden 属性和 display: none 有什么区别？
**答**：
- 效果相同：都不可见且不占空间，但 hidden 的本质是 UA 样式 `[hidden] { display: none }`，特异性很低。
- 经典坑：元素自己写了 `display: flex` 时，hidden 属性会被覆盖而失效。
- 工程建议：组件库统一显式兜底 `.x[hidden] { display: none !important; }`，业务上显隐控制尽量走 class 或 v-show。

```css
.card { display: flex; }          /* 没有下一行兜底时，hidden 属性会失效 */
.card[hidden] { display: none; }  /* 显式兜底，保证 hidden 永远生效 */
```
