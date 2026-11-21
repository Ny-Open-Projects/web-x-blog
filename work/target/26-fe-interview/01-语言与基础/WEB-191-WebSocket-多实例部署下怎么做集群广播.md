---
title: [WEB-191] WebSocket 多实例部署下怎么做集群广播？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-191：WebSocket 多实例部署下怎么做集群广播？
**答**：
- 问题：WS 连接粘在某个实例上，用户 A 连在实例 1，订阅的频道消息却先到实例 2，跨实例无法直达。
- 标准解法：WS 网关无状态化 + Redis Pub/Sub 扇出——发布方 publish，每个实例订阅后把消息投给自己持有的连接。
- 规模升级：按频道分片的专用推送网关，或消息队列（Kafka）兜底可靠投递与回放。
- 前端配合：重连后回传"最后收到的消息 id"，服务端做增量补偿，避免广播间隙丢消息。

```javascript
// Node：ws 网关 + Redis pub/sub 扇出（ioredis）
const Redis = require('ioredis');
const sub = new Redis(), pub = new Redis();
wss.on('connection', (ws, req) => {
  ws.room = new URL(req.url, 'http://x').searchParams.get('room');
  ws.send(JSON.stringify({ t: 'sync' })); // 提示前端回传 lastId 做增量补偿
});
sub.psubscribe('chat:*');                 // 频道通配订阅
sub.on('pmessage', (pattern, channel, msg) => {
  const data = JSON.parse(msg);
  for (const client of wss.clients) {
    if (client.room === data.room && client.readyState === 1) client.send(msg);
  }
});
// 发布方（任意实例或业务服务）
function broadcast(room, payload) {
  pub.publish('chat:*', JSON.stringify({ room, ...payload }));
}
```
