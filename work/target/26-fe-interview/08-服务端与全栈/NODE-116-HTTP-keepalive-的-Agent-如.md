---
title: [NODE-116] HTTP keep-alive 的 Agent 如何调优（maxSockets 是高频压轴）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-116：HTTP keep-alive 的 Agent 如何调优（maxSockets 是高频压轴）？
**答**：
- Node 客户端**默认 Agent 不保活**：每次请求新建 TCP，高 QPS 下大量 TIME_WAIT、每次多一个 RTT 握手。
- 三个核心参数：`maxSockets`（每 host 并发上限——过小自我排队 TTFB 升高，过大压垮下游）、`maxFreeSockets`（空闲保留数）、`keepAliveMsecs`（保活时长）。
- `scheduling: 'lifo'` 优先复用最近活跃的连接，被服务端空闲掐断的概率最低。
- 排查口诀：大量 TIME_WAIT → 没开 keepAlive；下游不慢但 TTFB 高 → maxSockets 太小在排队；下游 CPU 打满 → maxSockets 太大。

```javascript
const http = require('http');
const agent = new http.Agent({
  keepAlive: true,
  keepAliveMsecs: 60_000,
  maxSockets: 50,        // 每 host:port 并发上限 —— 核心参数
  maxFreeSockets: 10,
  scheduling: 'lifo',
});

function callUpstream(path) {
  return new Promise((resolve, reject) => {
    const req = http.get({ host: 'user-service', path, agent, timeout: 2000 }, (res) => {
      res.resume();                       // 不读 body 也要消费完，连接才能复用
      res.on('end', resolve); res.on('error', reject);
    });
    req.on('error', reject);
    req.on('timeout', () => req.destroy(new Error('upstream timeout')));
  });
}

// 监控 sockets/freeSockets：free 长期为 0 且 sockets 打满 → 扩 maxSockets
setInterval(() => {
  metrics.gauge('agent_busy', Object.values(agent.sockets).flat().length);
  metrics.gauge('agent_free', Object.values(agent.freeSockets).flat().length);
}, 5000).unref();
// 注意：axios/got/node-fetch 底层都走 http.Agent，调参是同一个位置
```
