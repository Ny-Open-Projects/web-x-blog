---
title: [CSS-228] @layer 的顺序规则详解：reset→framework→local
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 架构]
type: 面试题
---

## CSS-228：@layer 的顺序规则详解：reset → framework → local

**答**：
- 层的优先级由「声明顺序」决定：后声明的层赢，与选择器权重无关——`@layer a, b` 中 b 层任何选择器都赢过 a 层
- 标准分层配方：`@layer reset, base, components, utilities;`——utilities 永远赢，reset 永远垫底
- 层外样式（未分层）永远赢过分层样式——一条「逃生通道」：临时覆盖不用 !important
- 追加层：后续 `@layer components { … }` 按名字合并到已有层（顺序不变）；同层内仍按权重比较
- 对第三方样式：把引入的库样式放进低优先层（import 时指定），业务样式随意覆盖

```css
@layer reset, framework, components, utilities;

@import url('bootstrap.css') layer(framework);
@import url('reset.css') layer(reset);

@layer components { .btn { padding: 8px 16px; } }
@layer utilities { .mt-8 { margin-top: 8px !important; } } /* 赢过 components */
```
