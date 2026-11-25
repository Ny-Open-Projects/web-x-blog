---
title: [ARC-285] AB 实验的体验一致性与跨端分桶如何保证？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-285：AB 实验的体验一致性与跨端分桶如何保证？
**答**：
- 跨端一致：用户在 App/H5/小程序要进同一个实验组——分桶因子统一 userId（登录态），未登录用户用设备 ID 并在登录时做"分桶迁移对齐"；服务端下发实验配置（各端 SDK 消费同一配置协议）。
- 体验一致性细节：实验变量在**首次渲染前**确定（服务端注入或配置预取），避免"先看到 A 再闪成 B"；同一会话内分桶结果锁定（防刷新变组）。
- 分桶服务化：AB 判定做成服务端 API（批量取实验值），端上 SDK 只做缓存与消费——跨端一致性天然成立，端上只处理降级（服务不可用时用缓存或全走默认）。
- 登录合并：未登录期间的设备桶与登录后的用户桶，登录瞬间做桶合并（以用户桶为准）并打标，供分析侧清洗"中途变组"用户。

```typescript
// 服务端批量分桶接口
POST /experiments/batch
{ uid: 'u123', exps: ['checkoutB', 'newFeed'] }
→ { checkoutB: 'B', newFeed: 'control', ts: 1699999999 }
// 端上：首次渲染前 await fetchBatch() 注入 SSR HTML；会话锁定：
sessionStorage.setItem('exp-lock', JSON.stringify(vals));   // 同会话不再重新分桶
// 登录合并：onLogin(uid) → server.migrateBucket(deviceId → uid) → 强制刷新分桶上下文
```
