---
title: [MFW-245] 元框架的灰度路由与实验框架整合
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## MFW-245：灰度路由与实验框架整合

**答**:
- 分桶位置：Middleware 做实验分桶（读实验配置 KV + hash uid → 桶）→ 请求头带 x-exp-variant 下传——RSC 与客户端组件统一可读（headers() 单源）
- 与产物级灰度的边界：UI 实验用桶（同产物不同分支渲染）；构建级实验（新依赖/重构）用产物双版本（RBL-462 双跑）——两层实验别混
- SSR 一致性：桶在服务端定 → 首屏即正确变体（无 CLS 闪变）——客户端分桶会水合不一致
- 归因闭环：埋点自动带桶（headers 下传 → 上报层统一注入）——实验数据可信的前提

```javascript
// middleware：服务端分桶 → 头下传
const variant = expClient.assign(uid, 'new-cart')           // sticky hash
res.headers.set('x-exp-cart', variant)
// RSC/Client 统一读
const variant = headers().get('x-exp-cart') ?? 'control'
```
