---
title: [NODE-236] PM2 的核心机制与 cluster 模式？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-236：PM2 的核心机制与 cluster 模式？
**答**：
- 架构：pm2 daemon（god daemon）管理应用进程树——daemon 收 CLI 命令，应用进程是 daemon 的子进程；daemon 挂了进程仍在但失去管理能力（pm2 kill 要谨慎）。
- cluster 模式：内部使用 Node cluster（NODE-232）——fork 多个 worker 共享同一端口，master 做请求分发与进程管理。
- fork 模式：单进程多实例场景（每个实例独立端口，配合 Nginx 上游）。
- 进程管理细节：自动重启（异常退出）、max_restarts 防重启风暴、max_memory_restart（内存超限回收——NODE-264 内存泄漏的兜底）。

```javascript
// ecosystem.config.js
module.exports = {
  apps: [{
    name: 'api',
    script: './dist/server.js',
    instances: 'max',              // cluster：按 CPU 核数
    exec_mode: 'cluster',
    max_memory_restart: '600M',    // 内存兜底
    max_restarts: 10, restart_delay: 5000,   // 防风暴
    env: { NODE_ENV: 'production' },
    env_production: { NODE_ENV: 'production' },
  }],
};
// pm2 start ecosystem.config.js --env production
// pm2 reload api       ← 0-downtime 重载（见 NODE-237）
```
