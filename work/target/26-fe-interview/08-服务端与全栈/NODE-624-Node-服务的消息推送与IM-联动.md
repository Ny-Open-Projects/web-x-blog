---
title: [NODE-624] Node 服务的消息推送与 IM 联动（在线直推/离线推送）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-624：消息推送与 IM 联动
**答**:
- 联动逻辑：消息到达 → 接收方在线（WS 直推——毫秒级）→ 离线（Push 通道——NODE-570）→ 端上拉取；过渡状态（WS 断线重连窗口——Push 去重（已推未读 vs 已拉取））。
- 去重与升级：多渠道同消息去重（消息 ID 全渠道唯一——用户只感知一次）、推送升级（低优先级消息（群）聚合、高优先级（单聊@）直推——分级 NODE-453/568）、免打扰与勿扰（会话免打扰不 Push 只进收件箱——状态联动）。
- 端上联动：WS 在线时 Push 已达（端上去重：同 msgId 忽略 Push）、已读后撤回 Push（读水位于 Push 之后——通知栏清理——端上能力差异适配）。
- 可靠性：Push 失败降级（短信兜底（关键消息）——成本分级）、离线消息与 Push 的一致（离线拉取后取消未读 Push——回执联动）。
- 观测：直推率/Push 触发率/到达率/打开率——通道效率看板。
```javascript
async function onMessage(msg) {
  const online = await registry.isOnline(msg.to);
  if (online) await ws.push(msg);                                // 直推
  else await push.dispatch(msg, { dedupeKey: msg.id,
    priority: msg.mention ? 'high' : 'normal' });                // 离线 Push（分级）
  // 端上：WS 已收到同 msgId → 忽略 Push（端上去重）
}
```
