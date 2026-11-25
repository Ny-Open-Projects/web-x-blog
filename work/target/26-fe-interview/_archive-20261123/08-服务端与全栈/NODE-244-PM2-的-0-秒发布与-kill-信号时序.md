---
title: [NODE-244] PM2 的 0 秒发布与 kill 信号时序？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-244：PM2 的 0 秒发布与 kill 信号时序？
**答**:
- 信号链：pm2 reload → master 发 SIGINT（可用 kill_signal 自定义 SIGTERM）到旧 worker → 应用 graceful shutdown（NODE-237）→ worker 'exit' → master fork 新 worker。
- 旧 worker 停止接收新请求的正确姿势：server.close()（停止 accept）而非 process.exit()——在途请求要跑完。
- keep-alive 长连接陷阱：close() 不关闭已有 keep-alive 连接——需设置 server.keepAliveTimeout 或主动 conn.end()（网关复用连接时会悬挂）。
- 健康检查时序：新 worker listen 之后才进流量——load balancer/cluster 的 accept 层自动屏蔽未 listen worker。

```javascript
// 完整时序实现
process.on('SIGINT', () => {
  server.closeIdleConnections?.();          // Node 18.2+：关闭空闲 keep-alive 连接
  server.close(() => process.exit(0));      // 等 active 完成
  setTimeout(() => process.exit(1), 10000); // 兜底
  // WS：主动通知客户端重连
  io.emit('server-restarting'); io.disconnectSockets(true);
});
// PM2 配置：kill_signal: 'SIGTERM', kill_timeout: 10000（强杀等待时长）
```
