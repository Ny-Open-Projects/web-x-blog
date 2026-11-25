---
title: [NODE-238] PM2 日志与指标体系？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-238：PM2 日志与指标体系？
**答**:
- 日志：pm2 logs 聚合 stdout/stderr（--merge 合并多实例）；rotate 依赖 pm2-logrotate 模块（按大小/时间切割）——避免日志盘爆（NODE-081 配合）。
- 结构化日志优先：应用内 pino 输出 JSON → PM2 只做透传（不要依赖 PM2 的日志管理做检索）。
- 指标：pm2 monit（CPU/内存/restart 次数）；pm2.io（付费面板）或自建 Prometheus exporter（pm2-prometheus）。
- restart 次数告警：持续增长说明内存泄漏或崩溃循环——进告警规则。

```yaml
# pm2-logrotate
pm2 install pm2-logrotate
pm2 set pm2-logrotate:max_size 100M
pm2 set pm2-logrotate:retain 14
pm2 set pm2-logrotate:compress true
# 应用侧（pino 结构化）
const log = pino({ level: process.env.LOG_LEVEL ?? 'info' });   // JSON → stdout → pm2 透传 → ES
# Prometheus：pm2PrometheusExporter() → /metrics 挂到统一采集（NODE-36x trace 配套）
```
