---
title: [NODE-404] Node 服务的告警规则设计（分级/抑制/收敛）如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-404：Node 服务的告警规则设计
**答**:
- 告警基于 SLO 燃烧率而非绝对阈值：快速燃烧（1h 烧掉 5% 预算，因子 14.4）→ P0 立即响应；慢速燃烧（6h 烧 10%，因子 6）→ P1；趋势类（磁盘 7 天内满）→ 工单。绝对阈值告警只用于无 SLO 的资源。
- 多窗口判定防抖：错误率告警用双窗口（5m 即时 + 1h 确认），瞬时毛刺不告警；for duration 让指标持续超阈值才触发。
- 分级与路由：P0 电话+IM、P1 IM、P2 日报；值班路由（按服务 owner 转发）；升级规则（30 分钟未认领升级 TL）。
- 收敛与抑制（ARC-353）：同指纹聚合计数、发布窗口静默（NODE-370 灰度期抑制版本相关告警）、依赖抑制（DB 挂抑制全部依赖 DB 的告警，只留根因告警）。
- 质量运营：告警→事故转化率、零行动告警删除、每值班周期告警数预算（疲劳指标）。
```yaml
# Prometheus 告警规则（燃烧率 + 多窗口）
- alert: ApiSloFastBurn
  expr: (sum(rate(http_5xx[5m])) / sum(rate(http_total[5m]))) > 14.4 * 0.001
    and (sum(rate(http_5xx[1h])) / sum(rate(http_total[1h]))) > 14.4 * 0.001
  labels: { severity: P0 }        # SLO 99.9%，14.4 倍快速燃烧
  annotations: { runbook: 'https://runbooks/api/5xx' }
```
