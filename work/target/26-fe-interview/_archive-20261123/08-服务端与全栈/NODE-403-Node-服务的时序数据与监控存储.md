---
title: [NODE-403] Node 服务的时序数据（指标/事件流）存储与查询如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-403：时序数据存储与查询
**答**:
- 选型：Prometheus（指标拉取、告警生态，默认选择）、ClickHouse（超大规模事件明细 + 聚合分析）、InfluxDB/TimescaleDB（PG 生态时序扩展）。业务事件流（用户行为明细）与系统指标分开存。
- 数据建模：指标命名规范（domain_subsystem_metric_unit）、标签基数控制（防基数爆炸拖垮 TSDB——uid 级标签进明细库不进 Prometheus）、预聚合（recording rules 常用查询固化）。
- 保留与降采样：原始 15s 精度保 15 天 → 5m 聚合保 90 天 → 1h 聚合保 1 年（成本阶梯，ARC-356）；业务事件明细按价值分级保留。
- 查询体验：常用面板固化（Grafana dashboard 代码化管理）、SLO 视图（燃烧率）、标签维度可组合下钻。
- 写入保护：远程写入限流（异常基数/速率拒绝）、丢弃规则（低价值高频指标降采样丢弃）。
```yaml
# Prometheus 保留与降采样（Thanos/Mimir 配置示意）
 retention: 15d           # 原始精度
 downsample: [ 5m, 1h ]   # 聚合层
 recording_rules:
   - record: job:http_error_rate:5m
     expr: sum(rate(http_requests_total{status=~"5.."}[5m])) by (job)
           / sum(rate(http_requests_total[5m])) by (job)
```
