---
title: [BAS-053] meta http-equiv 有哪些常用指令？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-053：meta http-equiv 有哪些常用指令？
**答**：
- http-equiv 让 meta 模拟 HTTP 响应头，常用：refresh（定时刷新/跳转）、X-UA-Compatible（指定 IE 内核）、Content-Security-Policy。
- refresh 支持延迟跳转：`content="3;url=/home"`；现代项目跳转优先用 302 或 JS。
- 能配响应头就不要用 http-equiv，只有静态托管改不了响应头时才用它兜底。

```html
<meta http-equiv="refresh" content="3;url=/home" />
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<meta http-equiv="Content-Security-Policy" content="default-src 'self'" />
```
