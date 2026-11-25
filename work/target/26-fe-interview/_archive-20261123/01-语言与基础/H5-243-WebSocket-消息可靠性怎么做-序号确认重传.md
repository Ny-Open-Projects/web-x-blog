---
title: [H5-243] WebSocket 消息可靠性怎么做：序号-确认-重传
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, WebSocket]
type: 面试题
---

## H5-243：WebSocket 消息可靠性怎么做：序号-确认-重传

**答**：
- WS 本身基于 TCP，字节流可靠，但「连接断开瞬间在途消息」会丢——应用层可靠性仍要做
- 协议设计：每条业务消息带自增 seq，接收方回 ACK(seq) 或「已收最大连续 seq」；发送方保留未确认消息，重连后重发
- 幂等消费：接收方按 seq 去重（重发会导致重复投递），存储「已处理的最大 seq」实现断点续传
- 顺序保证：发送按 seq 递增，接收按序入队；乱序到达时缓冲等待空洞补齐
- 取舍话术：实时聊天要可靠+有序；游戏状态用最新值覆盖旧值（丢旧帧无所谓），不必完整可靠

```javascript
let seq = 0; const unacked = new Map();
function send(payload) {
  const msg = { seq: ++seq, payload };
  unacked.set(seq, msg);
  ws.send(JSON.stringify(msg));
}
ws.onmessage = (e) => {
  const { ack } = JSON.parse(e.data);
  unacked.delete(ack);           // 确认后删除
};
ws.onopen = () => unacked.forEach(m => ws.send(JSON.stringify(m))); // 重连补发
```
