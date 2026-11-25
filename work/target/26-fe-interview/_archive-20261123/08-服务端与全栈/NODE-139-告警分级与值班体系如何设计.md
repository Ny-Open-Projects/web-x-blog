---
title: [NODE-139] 告警分级与值班体系如何设计？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-139：告警分级与值班体系如何设计？
**答**：
- 分级本质是**响应时效**承诺：P0 电话强提醒 15 分钟内响应（服务全挂）、P1 IM 30 分钟（错误率/性能劣化）、P2 工作时段（前兆指标）、P3 转工单排期。
- 规则设计三防抖：`for` 持续时长（防毛刺）、连续 N 次满足才触发、恢复必须通知（闭环）。
- 值班配套：升级链（15 分钟未认领升级 TL）、静默窗口（发布期间 P2/P3 静默）、每条告警必须带 runbook 链接。
- 反模式自查：告警太多没人看（治理到"每条告警都可行动"）、只有错误没前兆（池排队/复制延迟这类 leading indicator 要配）。

```yaml
# alerts.yaml —— 分级 + 路由 + 静默
alerts:
  - name: service-down
    expr: up == 0                       # 实例全挂
    for: 30s
    severity: P0                        # 电话，15 分钟响应
    runbook: https://wiki/runbook/p0-down
  - name: error-rate-high
    expr: rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.05
    for: 2m
    severity: P1
  - name: eventloop-lag-p99
    expr: nodejs_eventloop_lag_p99_seconds > 0.5
    for: 5m
    severity: P1
  - name: db-pool-enqueue               # 前兆指标：池开始排队
    expr: rate(db_pool_enqueue_total[10m]) > 10
    for: 10m
    severity: P2
  - name: disk-80-percent
    expr: disk_used_percent > 80
    severity: P3                         # 转工单

routing:
  P0: [oncall-phone, im-critical]        # 升级链：15 分钟未认领 → TL
  P1: [oncall-im]
  P2: [team-channel]
  P3: [ticket]
quiet_hours:
  P2: "22:00-09:00"                      # 夜间静默，P0 永不打烊
  P3: "19:00-10:00"
```

---

## 十七、高并发与稳定性
