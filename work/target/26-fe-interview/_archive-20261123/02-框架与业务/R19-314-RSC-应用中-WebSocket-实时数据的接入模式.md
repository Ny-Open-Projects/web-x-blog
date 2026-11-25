---
title: [R19-314] RSC 应用中 WebSocket 实时数据怎么接入？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-314：RSC 应用中 WebSocket 实时数据怎么接入？
**答**：
- RSC 是请求-响应模型，实时推送必须客户端承载：客户端组件内 WS 连接，收到消息 setState/useOptimistic 更新局部 UI。
- 混合模式：初始数据 RSC 下发（首屏快），增量走 WS；消息去重（RSC 快照与 WS 消息重叠时按 msgId 去重）。
- 广播刷新：服务端事件触发 revalidate（通过队列消费者调用 action 或 route handler），所有在线客户端收到刷新 payload——重数据低频场景适用。
- 连接管理：会话鉴权（WS 握手带 token）、断线重连退避、页面隐藏暂停心跳。
- 口诀：「RSC 管快照、WS 管增量、revalidate 管最终一致」。
