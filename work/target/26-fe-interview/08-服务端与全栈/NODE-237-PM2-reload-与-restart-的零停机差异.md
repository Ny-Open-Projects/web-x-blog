---
title: [NODE-237] PM2 reload 与 restart 的零停机差异？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-237：PM2 reload 与 restart 的零停机差异？
**答**：
- restart：杀掉全部进程再启动——有 downtime（新进程绑定端口前请求 502）。
- reload（cluster 模式）：滚动重启——逐个 fork 新 worker、旧 worker graceful shutdown 后退出；端口始终有 worker 在听。
- 优雅关闭是前提：应用必须处理 SIGINT/SIGTERM（PM2 发送）——停止收新请求、完成在途、超时强退；否则 reload 也会打断请求。
- fork 模式 reload 不保证零停机（单进程）——需要 Nginx 层摘流配合。

```javascript
// 应用侧：优雅关闭（配合 PM2 reload）
process.on('SIGINT', shutdown);    // PM2 默认发 SIGINT
process.on('SIGTERM', shutdown);
async function shutdown() {
  server.close();                  // 停止接收新连接（NODE-33x SSR 稳定性同款）
  const force = setTimeout(() => process.exit(1), 10000);   // 超时强退
  await Promise.allSettled([drainInflight(), closeDB(), closeRedis()]);
  clearTimeout(force);
  process.exit(0);
}
// 验证零停机：reload 期间压测
// autocannon -c 50 -d 60 → errors 应为 0（requests 重启前完成）
```
