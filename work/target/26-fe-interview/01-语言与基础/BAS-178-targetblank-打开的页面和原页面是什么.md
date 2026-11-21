---
title: [BAS-178] target="_blank" 打开的页面和原页面是什么关系？rel="noopener" 为什么高频？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-178：target="_blank" 打开的页面和原页面是什么关系？rel="noopener" 为什么高频？
**答**：
- window.open 或无 rel 的 target=_blank 打开的窗口，可通过 window.opener 引用回原窗口，跨源下也能把它 location 跳到钓鱼页（Reverse Tabnabbing 攻击）。
- 防御：`rel="noopener"`（切断 opener 引用）；`rel="noreferrer"` 顺带不带 Referer。
- 现代浏览器对 target=_blank 已默认隐式 noopener，但显式写出仍是规范做法，面试答"必须加"。

```html
<!-- 不安全：新页面能拿到 window.opener 反向操控原页面 -->
<a href="https://unknown.example.com" target="_blank">有风险</a>
<!-- 安全写法：noopener 切断引用，noreferrer 连 Referer 一起隐藏 -->
<a href="https://unknown.example.com" target="_blank" rel="noopener noreferrer">安全外链</a>
<!-- window.open 返回的窗口同理：被打开页可通过 window.opener 访问原窗口 -->
```
