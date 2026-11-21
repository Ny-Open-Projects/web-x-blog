---
title: [BAS-153] width 的 max-content、min-content、fit-content 分别什么效果？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-153：width 的 max-content、min-content、fit-content 分别什么效果？
**答**：
- max-content：内容完全不换行时的理想宽度（一整行长句撑开）。
- min-content：按最宽的不可拆分单元（最长单词/图片）收缩到最窄。
- fit-content(上限)：先用 max-content，超了就收缩，但不超过给定上限；三者都可用 min()/max-content 系列做自适应卡片。

```css
.button { width: max-content; }        /* 按文本总宽撑开，不换行 */
.tag { width: min-content; }           /* 收缩到最长单词的宽度 */
.card { width: fit-content(320px); }   /* 内容宽优先，最大不超过 320px */
/* 三者都是 intrinsic sizing，常用于按钮、标签、聊天气泡 */
```
