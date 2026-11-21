---
title: [NODE-059] PM2 的配置与集群模式如何使用？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-059：PM2 的配置与集群模式如何使用？
**答**：
- 两种模式：`fork`（单进程）与 `cluster`（`exec_mode: 'cluster'`，按 CPU 核数起多个实例共享端口，负载均衡）；`max_memory_restart` 内存超限自动重启；`env_*` 区分环境。
- 核心运维命令：`pm2 start ecosystem.config.js`、`pm2 reload`（**0 秒重启**，逐个 worker 滚动重启，与 `restart` 的硬重启区分）、`pm2 logs/monit/startup`（开机自启）。
- 高频追问：cluster 模式下 0 downtime 重启的原理（master 先起新 worker 再杀旧的，配合 server.close 优雅退出）；`kill_timeout` 给 SIGTERM 处理留时间；PM2 与 Docker/K8s 的关系——容器内一般不用 PM2，交给编排系统管理。

```javascript
// ecosystem.config.js
module.exports = {
  apps: [{
    name: 'bff-server',
    script: './dist/main.js',
    instances: 'max',            // 按 CPU 核数起满；或写死数字
    exec_mode: 'cluster',        // 集群模式：多进程共享 3000 端口
    max_memory_restart: '600M',  // 内存超限自动重启（OOM 防护）
    kill_timeout: 10000,         // SIGTERM 后等 10s 再 SIGKILL，留出优雅退出时间
    wait_ready: false,
    listen_timeout: 8000,
    env_production: {
      NODE_ENV: 'production',
      LOG_LEVEL: 'info',
    },
    out_file: '/var/log/bff/out.log',
    error_file: '/var/log/bff/err.log',
    merge_logs: true,
  }],
};
```

```bash
# 常用运维命令
pm2 start ecosystem.config.js --env production
pm2 reload bff-server          # 0 downtime 滚动重启（发版标准动作）
pm2 reload bff-server --update-env   # 环境变量变更后 reload
pm2 monit                      # 实时 CPU/内存监控面板
pm2 logs bff-server --lines 200
pm2 startup && pm2 save        # 开机自启：生成 systemd 单元并保存进程列表
```
