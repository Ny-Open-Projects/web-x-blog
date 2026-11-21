---
title: [CSS-229] @layer 与 !important 的关系，谁赢
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 架构]
type: 面试题
---

## CSS-229：@layer 与 !important 的关系：谁赢

**答**：
- 反直觉规则：!important 的层序与普通值相反——**早声明层的 !important 赢过晚声明层的 !important**
- 完整优先级序（高→低）：!important 未分层 > !important 早期层 > !important 晚期层 > 未分层普通值 > 晚期层 > 早期层
- 设计动机：!important 的语义是「防御性优先」，reset/框架层（先声明）的 !important 保护其兜底不被 utilities 层打破
- 工程含义：@layer 时代应尽量少用 !important；用层序表达优先级；最后决胜手段是「未分层 !important」
- 面试陷阱题：`@layer a,b` 中 a 层 .x{color:red!important} 与 b 层 .y{color:blue!important}，目标同时命中——红色赢

```css
@layer a, b;
@layer a { #x { color: red !important; } }
@layer b { p { color: blue !important; } }
/* <p id="x"> → red：早层 important 赢 */
```
