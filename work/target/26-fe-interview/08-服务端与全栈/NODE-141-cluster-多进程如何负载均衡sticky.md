---
title: [NODE-141] cluster 多进程如何负载均衡？sticky session 怎么实现？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-141：cluster 多进程如何负载均衡？sticky session 怎么实现？
**答**：
- cluster 默认**轮询分发**（Linux 上主进程 accept 后轮流转交 worker，或 OS 竞争），对无状态 HTTP 完美；但**进程内存中的 session/WS 连接要求同一用户固定落同一 worker**。
- sticky 本质：主进程按 IP/cookie 哈希选 worker，把 socket 句柄转交（`pauseOnConnect` 下主进程不读数据，只转发）。
- 更省心的替代：session 放 Redis（NODE-033）消除状态依赖，或网关层做 ip_hash/cookie sticky。
- worker 崩溃由 cluster 重新 fork；配合优雅退出（NODE-060）实现滚动重启不丢单。

```javascript
const cluster = require('cluster');
const http = require('http');
const net = require('net');
const crypto = require('crypto');
const NUM = 4;

if (cluster.isPrimary) {
  const workers = [];
  for (let i = 0; i < NUM; i++) workers.push(cluster.fork());
  cluster.on('exit', (w) => {                       // 崩溃自愈：重新拉起
    const idx = workers.indexOf(w);
    workers[idx] = cluster.fork();
  });
  // 主进程只做"哈希选路"，不处理业务
  net.createServer({ pauseOnConnect: true }, (socket) => {
    socket.pause();                                  // 不读数据，仅转发句柄
    const ip = socket.remoteAddress || '';
    const idx = crypto.createHash('md5').update(ip).digest()[0] % NUM;
    workers[idx].send('sticky', socket);             // IP 哈希固定 worker
  }).listen(3000);
} else {
  const server = http.createServer((req, res) => res.end(`worker ${process.pid}`));
  process.on('message', (msg, socket) => {
    if (msg !== 'sticky') return;
    server.emit('connection', socket);               // 连接交给本 worker 处理
    socket.resume();
  });
}
// WS 场景同理：同一用户的心跳与消息必须落在持有其连接的 worker
```
