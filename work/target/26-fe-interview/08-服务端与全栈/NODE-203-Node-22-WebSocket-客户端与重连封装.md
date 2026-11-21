---
title: [NODE-203] Node 22 原生 WebSocket 客户端与重连封装？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-203：Node 22 原生 WebSocket 客户端与重连封装？
**答**:
- Node 22 全局 WebSocket（undici 提供）与浏览器事件 API 一致：onopen/onmessage/onclose，服务端做 WS 客户端（对接内部长连接网关）不再引 ws 库。
- 服务端客户端的特有关注：进程退出时的优雅关闭、Node 事件循环退出（无其他活动时 WS 不阻止退出——undici 特性）。
- 重连封装三件套：指数退避+抖动、心跳判死、断线缓冲队列（NODE-229 浏览器端同款逻辑，此处用 Node API）。
- 与 ws 库的取舍：原生足够做客户端；做服务端（需要 permessage-deflate/子协议细节）仍推荐 ws。

```javascript
// Node 22 原生 WebSocket 客户端
class WsClient {
  #ws; #attempt = 0; #queue = [];
  connect() {
    this.#ws = new WebSocket(process.env.GATEWAY_WS);
    this.#ws.onopen = () => { this.#attempt = 0;
      this.#queue.splice(0).forEach(m => this.send(m)); };
    this.#ws.onmessage = ({ data }) => this.handle(JSON.parse(data));
    this.#ws.onclose = () => { if (this.#attempt++ < 10)
      setTimeout(() => this.connect(), Math.min(500 * 2 ** this.#attempt, 30000) * (0.7 + Math.random() * 0.6)); };
  }
  send(msg) { this.#ws.readyState === 1 ? this.#ws.send(JSON.stringify(msg)) : this.#queue.push(msg); }
}
// graceful shutdown：
process.on('SIGTERM', () => { client.close(); server.close(() => process.exit(0)); });
```
