---
title: [PER-104] 监控数据的存储与查询怎么设计？标签（tag）如何定才不踩坑？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-104：监控数据的存储与查询怎么设计？标签（tag）如何定才不踩坑？

**答**：
- 选型：指标类进**时序库**（Prometheus/VictoriaMetrics/InfluxDB），日志与错误明细进日志库（ES/ClickHouse），回放与堆栈进对象存储 + 元数据索引。
- 标签设计原则：标签基数（cardinality）必须可控——`page` 用路由模板（`/orders/:id`）而非全量 URL，禁止把 userId、时间戳做成标签（基数爆炸会拖垮时序库）。
- 推荐标签集：app、version、page 模板、device tier、region 五个左右；明细维度（具体 URL、userId）放日志明细里按需关联。
- 查询模式预设计：报表看分位数（P75/P95）用预聚合的 Histogram，排查明细用 traceId/会话 id 串起来。

```yaml
# VictoriaMetrics/Prometheus 指标设计：可控基数的标签
metrics:
  - name: lcp_seconds
    type: histogram
    help: 页面 LCP 分布
    labels:
      app: web                 # 应用名，低基数
      version: "v1.42.0"       # 构建版本，低基数
      page: /orders/:id        # 路由模板，禁止用原始 URL（基数爆炸）
      device_tier: low         # high 与 medium 与 low 三档
    buckets: [0.5, 1, 1.5, 2, 2.5, 4, 8]

  - name: js_errors_total
    type: counter
    labels:
      app: web
      version: "v1.42.0"
      fingerprint: a3f9c2      # 错误指纹哈希，错误种类级别基数
      # 注意：userId、具体 URL、时间戳都不进标签，进日志明细库
```

```sql
-- ClickHouse：错误明细表，与指标库互补
CREATE TABLE js_error_details (
    ts            DateTime,
    app           LowCardinality(String),
    version       LowCardinality(String),
    fingerprint   FixedString(64),   -- 关联指标库的聚合曲线
    message       String,
    stack         String,            -- sourcemap 还原后的堆栈
    session_id    String,            -- 串会话回放与日志
    page_url      String,            -- 明细维度存这里，不进时序标签
    user_id       String
) ENGINE = MergeTree()
PARTITION BY toYYYYMMDD(ts)
ORDER BY (app, version, fingerprint, ts);
```
