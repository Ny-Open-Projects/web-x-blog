---
title: [NODE-592] Node 服务的客服会话（排队/分配/上下文）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-592：客服会话服务
**答**:
- 会话流：进入（机器人先答——转人工条件：机器人无法解决/用户要求）、排队（队列位置/预计等待——按客服负载估算）、分配（空闲客服/技能匹配/会话上限）、会话（消息链路 ARC-526 服务端）、结束（评价/转工单）。
- 分配策略：负载均衡（活跃会话数限制/技能权重）、会话保持（同一问题回访优先原客服——上下文延续）、高峰策略（排队上限 → 留资回调）。
- 上下文：用户上下文注入（客服端可见：订单/浏览轨迹/历史工单——权限脱敏）、机器人上下文传递（转人工带对话摘要）。
- 可靠性：消息可靠性（ARC-526/392 协议）、会话中断恢复（客服端掉线——会话重分配）、排队公平性。
- 观测：排队时长/会话时长/解决率/转人工率（机器人效果指标）——客服运营看板。
```javascript
// 排队与分配
async function toHuman(session) {
  const ctx = { summary: await robot.summarize(session), userCtx: await userSnapshot(session) };
  const pos = await queue.push({ ...ctx, skill: classify(ctx) });
  emit(session, { queuePos: pos, eta: estimateEta(pos) });       // 排队反馈
  dispatcher.onFree(async (agent) => { const t = await queue.pop(agent.skills); bind(t, agent); });
}
```
