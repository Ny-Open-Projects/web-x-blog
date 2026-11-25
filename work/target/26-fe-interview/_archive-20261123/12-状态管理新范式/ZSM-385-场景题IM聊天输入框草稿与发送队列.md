---
title: [ZSM-385] 场景题示范：IM 输入区状态（草稿/发送队列/重发）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-385：场景题示范：IM 输入区状态（草稿/发送队列/重发）

**答**:
- 草稿层：每会话草稿独立（切会话保留）、debounce 持久化、带 @ 与引用的复合草稿结构化存储（不是纯字符串）
- 发送队列：发送即入队（状态机：queued→sending→sent/failed），串行发送保序；失败进 failed 态提供「重发」，网络恢复自动重试 failed 队列
- 乐观与确认：入队即乐观上屏（pending 样式），服务端 ack（带真实 id/seq）后换绑；ack 超时转 failed 不直接消失（用户可见可重发）
- 幂等：重发携带同一 clientMsgId，服务端去重——网络抖动导致的重复发送安全

```javascript
function send(text) {
  const msg = { clientMsgId: uuid(), text, status: 'queued' }
  enqueue(msg); optimisticAppend(msg)
  flush().then((ack) => bindRealId(msg.clientMsgId, ack.id))
         .catch(() => markFailed(msg.clientMsgId))     // 可重发，不丢
}
// 重发：同一 clientMsgId → 服务端幂等
retry: (id) => sendQueue.requeue(id)
```
