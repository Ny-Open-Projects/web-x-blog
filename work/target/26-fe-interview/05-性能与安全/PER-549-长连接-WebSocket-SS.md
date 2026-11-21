---
title: [PER-549] 长连接（WebSocket/SSE）在性能测试里怎么压？和普通 HTTP 压测有什么不同？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-549：长连接（WebSocket/SSE）在性能测试里怎么压？和普通 HTTP 压测有什么不同？

**答**：
- 差异在于**会话态**：HTTP 压测是一次请求一次结论，长连接是长期会话——要压连接建立速率、稳态消息吞吐、心跳保活下的连接存活率、断线重连风暴四个维度，漏一个维度都会漏事故。
- 典型事故模式：网关重发（服务重启）导致几万客户端同时重连（thundering herd），压测必须模拟"批量断线-指数退避重连"剧本验证退避策略生效。
- 前端关注点：心跳间隔与服务端 idle 超时匹配（心跳太密浪费流量，太疏被网关断）；消息洪泛时前端渲染是否节流（批量合并渲染，不能一条消息一次 setState）。
- 指标口径：消息端到端延迟 p95（发方打时间戳收方算差）、客户端 CPU 占用随消息速率的曲线。

```javascript

// WS 压测客户端：连接风暴 + 洪泛接收 + 延迟采样
function wsLoadTest(url, { clients = 2000, flood = 50 } = {}) {
  const stats = { connected: 0, reconnects: 0, latencies: [] };
  for (let i = 0; i < clients; i++) {
    setTimeout(() => {                                    // 错峰建连，模拟自然到达
      const ws = new WebSocket(url);
      ws.onopen = () => stats.connected++;
      ws.onclose = () => {
        stats.reconnects++;
        setTimeout(() => ws.reconnect?.(), Math.random() * 30000); // 指数+抖动退避
      };
      ws.onmessage = (e) => {
        const { t } = JSON.parse(e.data);
        stats.latencies.push(performance.now() - t);      // 端到端延迟样本
      };
    }, Math.random() * 10000);
  }
  // 洪泛剧本：服务端广播 50msg/s，前端断言渲染节流（10s 一批合并）
  setInterval(() => {
    const a = stats.latencies.slice().sort((x, y) => x - y);
    console.log({ connected: stats.connected, reconnects: stats.reconnects,
      p95: a[Math.floor(a.length * 0.95)] ?? -1 });
    stats.latencies = [];
  }, 10000);
  return stats;
}
```
