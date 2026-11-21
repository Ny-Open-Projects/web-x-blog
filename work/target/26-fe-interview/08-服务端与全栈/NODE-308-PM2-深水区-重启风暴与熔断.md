---
title: [NODE-308] PM2 深水区：重启风暴与熔断？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-308：PM2 深水区：重启风暴与熔断？
**答**:
- 风暴场景：代码启动即崩 → PM2 无限重启循环（CPU 空转+日志爆盘）——max_restarts + min_uptime 配置防风暴（连续失败达阈值进入 errored 状态停止重启）。
- 熔断配置：max_restarts: 10 + min_uptime: '30s'（进程活过 30s 才算稳定重启）+ exp_backoff_restart_delay（100 → 300 → 15000ms 递增重启间隔）。
- 告警联动：进程进入 errored 状态 → 立即告警（比"错误率上升"更早暴露）。
- 发布保护：发布前 CI 冒烟启动（本地 node server & sleep 5 & curl health）——把"启动即崩"拦在发布前。

```yaml
# 防风暴配置
apps:
  - name: api
    max_restarts: 10            # 连续 10 次失败 → 停止重启（errored）
    min_uptime: '30s'           # 活过 30s 才重置计数
    exp_backoff_restart_delay: 100   # 重启间隔指数递增（100→200→400...）
# CI 冒烟门禁
smoke:
  cmd: 'node dist/server.js & sleep 5 && curl -sf localhost:3000/health'
  fail: 'exit 1 → 阻止发布'
```
