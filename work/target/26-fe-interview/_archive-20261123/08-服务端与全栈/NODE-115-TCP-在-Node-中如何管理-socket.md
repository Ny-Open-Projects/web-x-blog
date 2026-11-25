---
title: [NODE-115] TCP 在 Node 中如何管理 socket（backlog、保活、优雅关闭）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-115：TCP 在 Node 中如何管理 socket（backlog、保活、优雅关闭）？
**答**：
- `net.createServer({ backlog })` 的 backlog 是内核**全连接队列**长度：accept 消费不过来时新连接排队甚至被拒（EMFILE），高并发短连接服务要关注。
- 必做四件套：`setKeepAlive` 死链探测、`setNoDelay` 关 Nagle（低延迟）、空闲超时 destroy、监听 `error`（ECONNRESET 不监听直接崩进程）。
- 服务端 socket 生命周期：三次握手完成入全连接队列 → accept 事件转交业务 → end（FIN，半关闭）→ close（彻底释放）。
- 优雅关闭：`server.close()` 停止 accept + 逐个 `socket.end()` 排空，超时未退 `destroy`（对齐 NODE-060）。

```javascript
const net = require('net');
const sockets = new Set();

const server = net.createServer({ backlog: 1024 }, (socket) => {
  sockets.add(socket);
  socket.setKeepAlive(true, 30_000);  // 死链探测：30s 无数据发探活包
  socket.setNoDelay(true);            // 关 Nagle，小包立即发
  socket.setTimeout(120_000, () => socket.destroy()); // 空闲超时强杀
  socket.on('data', (buf) => socket.write(buf));      // echo 示例
  socket.on('close', () => sockets.delete(socket));
  socket.on('error', () => sockets.delete(socket));   // 必须监听，否则崩进程
});
server.listen(3000);
server.on('connection', () => metrics.inc('tcp_conn'));
console.log('当前连接数', sockets.size);

// 优雅关闭：停止 accept → 通知排空 → 超时强杀
async function drain() {
  server.close();
  const deadline = Date.now() + 10_000;
  for (const s of sockets) s.end();
  while (sockets.size && Date.now() < deadline) await new Promise((r) => setTimeout(r, 200));
  for (const s of sockets) s.destroy();
}
```
