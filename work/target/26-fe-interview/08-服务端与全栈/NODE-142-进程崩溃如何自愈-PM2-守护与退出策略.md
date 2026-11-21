---
title: [NODE-142] 进程崩溃如何自愈（PM2 守护与退出策略）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-142：进程崩溃如何自愈（PM2 守护与退出策略）？
**答**：
- 哲学：**崩溃优于带病运行**——uncaughtException 后进程状态不可信，记录日志立即退出，交给守护进程拉起。
- PM2 自愈四参：`min_uptime`（多快退出算启动失败）、`max_restarts`（防疯狂重启）、`exp_backoff_restart_delay`（指数退避，给依赖恢复留时间）、`kill_timeout`（优雅退出窗口）。
- 退出码语义化：正常退出 0、业务致命 1，守护进程按码决定是否重启与告警。
- 内存兜底：`max_memory_restart` 防 OOM 前先自愈；泄漏根因仍要靠 heap snapshot 治理（NODE-138）。

```yaml
# ecosystem.yaml —— 自愈三板斧：崩溃即拉起、退避重启、优雅超时
apps:
  - name: bff
    script: dist/server.js
    instances: 2
    exec_mode: cluster
    max_memory_restart: 1G           # 内存超限自动重启（泄漏兜底）
    min_uptime: 10s                  # 启动 10s 内退出视为启动失败
    max_restarts: 10                 # 连续失败 10 次停止拉起并告警
    exp_backoff_restart_delay: 100   # 退避：100/200/400ms 递增
    kill_timeout: 8000               # 给优雅退出 8s，超时强杀
    env:
      NODE_ENV: production
```

```javascript
// 退出策略与守护配合
process.on('uncaughtException', (err) => {
  logger.fatal({ stack: err.stack }, 'fatal, exiting for restart');
  process.exit(1); // 非零退出码 → PM2 按退避策略拉起
});
process.on('SIGTERM', () => gracefulShutdown()); // 优雅退出排空连接（NODE-060）
```
