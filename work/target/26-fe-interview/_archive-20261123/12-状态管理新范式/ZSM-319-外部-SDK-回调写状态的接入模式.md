---
title: [ZSM-319] 外部 SDK（支付/地图/客服）回调怎么安全写入状态
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-319：外部 SDK（支付/地图/客服）回调怎么安全写入状态

**答**:
- SDK 回调在 React 生命周期之外（全局对象/iframe/定时器），直接 setState 组件态会踩「卸载后更新」；正解是回调只写全局 store（vanilla），组件订阅派生
- 适配层模式：SDK 事件 → 规范化为内部 DTO → 写 store；SDK 生命周期与应用生命周期对齐（卸载时 destroy + 解绑回调）
- 竞态与重复：SDK 可能重复回调（网络重试），写入侧按事件 id/业务键幂等去重
- 类型安全：SDK 的回调签名与内部状态结构用适配函数显式转换，不让 SDK 原始对象渗进 store

```javascript
// 支付 SDK 适配层
paySdk.onSuccess((raw) => {
  const order = normalizeOrder(raw)          // SDK DTO → 内部 DTO
  queryClient.setQueryData(['order', order.id], order)   // 写缓存而非组件 state
})
// 组件卸载安全：回调目标是全局层，组件只 useQuery 订阅
```
