---
title: [NODE-247] PM2 面试高频问题清单？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-247：PM2 面试高频问题清单？
**答**:
- reload vs restart？（NODE-237）——cluster 滚动 vs 全杀；优雅关闭是前提。
- 内存泄漏怎么办？——max_memory_restart 兜底 + heap snapshot 定位（NODE-264）。
- cluster 下状态怎么共享？——外置 Redis（NODE-243），进程内存只做辅助。
- 0-downtime 怎么验证？——reload 期间 autocannon，errors=0 才达标。
- 为什么容器里不用 PM2？——进程管理上移 K8s（NODE-239），单进程容器更符合云原生。
- 收束：PM2 五件套——cluster 扩容、reload 零停机、日志切割、指标监控、deploy 脚本。

```bash
# 面试现场可写出的最小 ecosystem
module.exports = {
  apps: [{
    name: 'api',
    script: 'dist/server.js',
    instances: 'max',
    exec_mode: 'cluster',
    max_memory_restart: '600M',
    kill_timeout: 10000,                    // graceful 等待
    kill_signal: 'SIGTERM',
    out_file: '/var/log/api/out.log',
    error_file: '/var/log/api/err.log',
    merge_logs: true,
  }],
};
```
