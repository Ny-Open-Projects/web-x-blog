---
title: [SCN-213] IM 消息可靠投递——从发送到对方已读的全链路？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-213：IM 消息从发送到已读，可靠投递链路怎么设计？

**答**:
- 发送侧三态：发送中（本地立即上屏+待确认标记）→ 已发送（服务端 ack，拿到 serverId）→ 失败（重试入口）；本地先渲染（乐观显示）+ clientMsgId 幂等（重试不产生重复消息）。
- 可靠性机制：发送队列（串行保证会话内有序）、失败重试（指数退避 3 次，超限标失败可手动重发）、超时判定（ack 超时 8s 标失败——不无限等）。
- 接收侧：推送与拉取双通道（WS 推送为主、断线重连后按 lastSeq 拉增量——推送丢失靠拉补齐）、去重（serverId 幂等，重复推送丢弃）、排序（按服务端 seq 排序，本地时钟不可信）。
- 状态回执链：sent（服务端收到）→ delivered（对方在线收到）→ read（对方已读），已读回执批量上报（阅读位置上报，不逐条）——回执丢失不影响消息本身（回执是尽力而为）。

```javascript
async function sendMessage(msg) {
  const clientMsgId = uid();               // 幂等键
  store.append({ ...msg, clientMsgId, status: 'sending' }); // 乐观上屏
  const r = await withRetry(() => imApi.send({
    ...msg, clientMsgId }), { retries: 3, ackTimeout: 8000 });
  if (r.ok) store.update(clientMsgId,
    { status: 'sent', serverId: r.serverId });
  else store.update(clientMsgId, { status: 'failed' });  // 手动重发入口
}
// 接收：ws.on('msg', m => {
//   if (seen.has(m.serverId)) return;      // 去重
//   seen.add(m.serverId);
//   store.insertSorted(m, 'seq');          // seq 排序
//   ackDelivered(m.serverId);
// });
// 重连恢复：imApi.pull({ since: lastSeq }) → 合并去重。
// 已读：readCursor 上报（批量），对端渲染已读分割线。
```
