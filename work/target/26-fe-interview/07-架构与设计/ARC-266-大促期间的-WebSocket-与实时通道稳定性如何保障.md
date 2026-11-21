---
title: [ARC-266] 大促期间的 WebSocket 与实时通道稳定性如何保障？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-266：大促期间的 WebSocket 与实时通道稳定性如何保障？
**答**：
- 实时通道故障模式：连接建不起来（网关过载）、频繁断连（LB 踢连接）、消息延迟堆积、假在线（TCP 半开）。
- 保障手段：心跳+假死检测（30s 心跳，2 次超时判死并重连）；重连策略指数退避+抖动，防重连风暴；**降级到 HTTP 轮询**（WS 不可用时拉状态接口，轮询间隔随负载自适应）；多通道冗余（WS 为主，SSE/轮询备用）。
- 大促专项：非关键消息（氛围弹幕）可丢弃（客户端直接不消费），关键消息（库存变化/成团状态）带序号做补拉对账；网关侧连接数预热扩容提前完成。
- 监控：连接成功率、重连次数分布、消息端到端延迟（消息带发送时间戳）。

```typescript
function connect() {
  const ws = new WebSocket(wssUrl);
  let alive = false;
  ws.onopen = () => { alive = true; heartbeat(); };
  ws.onclose = () => { if (alive) scheduleReconnect(expBackoff(jitter)); else degradeToPolling(); };
  setTimeout(() => { if (!alive) degradeToPolling(); }, 5000);   // 5s 建不起 → 轮询兜底
}
function heartbeat() {                                            // 假死检测
  ping(); setTimeout(() => { if (!pongReceived) { ws.close(); scheduleReconnect(); } }, 10000);
}
// 消息对账：msg.seq 不连续 → GET /messages?since=lastSeq 补拉
```
