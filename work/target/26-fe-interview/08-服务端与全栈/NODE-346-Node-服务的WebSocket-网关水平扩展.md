---
title: [NODE-346] Node 服务的 WebSocket 网关水平扩展如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-346：Node 服务的 WebSocket 网关水平扩展
**答**:
- 核心问题：连接有状态（用户 ↔ 实例绑定），多实例间广播与定向推送不能假设同进程。方案：实例注册表 + 共享通道——连接归属记录到 Redis（uid → instance），消息经 Redis Pub/Sub 或 MQ 广播，各实例只推给自己的连接。
- 会话粘性与迁移：LB 层 ip hash/一致性哈希只能优化不能依赖（实例重启连接会重建）；重连协议带 lastSeq 增量补拉（ARC-416）保证不丢。
- 心跳与回收：LB 空闲超时与心跳周期对齐（心跳 < 空闲超时）；实例优雅下线（先停止接收新连接 → 通知客户端重连 → 等存量断开）。
- 容量模型：单实例连接数（Node 单进程 ~5万 C1000K 需 ulimit/内核调优）、内存（每连接 ~10KB × 连接数）、广播扇出（大房间用房间分片或聚合消息降低 O(n) 写）。
- 观测：连接数分布（是否倾斜）、消息端到端延迟、重连率。
```javascript
// Redis Pub/Sub 扩展
sub.subscribe('ws:broadcast');
sub.on('message', (ch, msg) => {
  const { topic, payload, target } = JSON.parse(msg);
  for (const ws of localConnectionsOf(target ?? topic)) ws.send(payload);  // 只推本地连接
});
function publish(topic, payload) {
  redis.publish('ws:broadcast', JSON.stringify({ topic, payload }));
}
// 定向：注册表 redis.hset('conn', uid, instanceId) → publish({target: instanceId})
```
