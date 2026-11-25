---
title: [WCN-205] 自定义元素在 SSR 下的三种策略与取舍？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-205：自定义元素在 SSR 下的三种策略与取舍？
**答**：
- 策略 1：SSR 输出空壳 + 客户端注册后渲染（简单，白屏感）。
- 策略 2：声明式 Shadow DOM（DSD，<template shadowrootmode>）随 HTML 下发——首屏完整且免闪烁，主流方向。
- 策略 3：框架侧预渲染（元素提供 renderToString 静态方法由 SSR 框架调用）——耦合框架。
- DSD 注意：模板内容双倍传输问题（客户端注册后 lit 忽略模板但 DOM 已存在）。

```javascript
<!-- DSD：服务端输出完整首屏 -->
<goods-card sku="A1">
  <template shadowrootmode="open">
    <style>:host { display: block; }</style>
    <div class="price">¥99</div>
  </template>
</goods-card>
r
```
