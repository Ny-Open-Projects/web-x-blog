# 1511 Prometheus 四类指标类型全景（深挖）

> 分类：监控 / Prometheus | 难度：L4 | 题型：体系题 | 频率：高 | 关键词：**四指标类型**/**Counter**/**Gauge**/**Histogram**/**Summary**
> 原文锚点：第 6~58 段「四种指标类型」全景

## 思路与架构
本卡把 Prometheus 指标类型按「**标量类 → 分布类 → 模型层**」串起 `1511-counter-gauge`（Counter 只增/Gauge 可变）、`1511-histogram-summary`（Histogram buckets/服务端分位、Summary 客户端分位）、`1511-metric-model-promql`（时序模型/labels/PromQL 函数）三张主卡，并显式划边界。

- **标量类**：Counter（累积、rate/irate 算 QPS）；Gauge（瞬时、set/inc/dec）。
- **分布类**：Histogram（buckets+_sum/_count、服务端 histogram_quantile）；Summary（客户端算分位、查询快、不可跨实例聚合）。
- **模型层**：metric=带 labels 时序；监控四原则；sum/rate/irate/histogram_quantile。

## 方案取舍
| 类型 | 可减？ | 分位计算 | 可跨实例聚合 | 典型用途 |
| --- | --- | --- | --- | --- |
| Counter | 否 | — | 是(rate) | 请求数/处理量 |
| Gauge | 是 | — | 是 | 内存/磁盘 |
| Histogram | 计数是 | 服务端 | 是(buckets sum) | 延迟分布 p90/p99 |
| Summary | — | 客户端 | 否 | 单实例分位 |

- 选型主线：累积量→Counter，状态量→Gauge，要分位且需聚合→Histogram，单实例分位要性能→Summary。
- 与「长尾」的呼应：平均值掩盖长尾，故分布类指标用 buckets/分位暴露 p99 而非均值。

## 答题技巧
- **四类型必背**：Counter→Gauge→Histogram→Summary，顺序由标量到分布。
- **Counter 铁律**：只增不减，QPS 必须 rate/irate，绝不能对 Gauge 算速率。
- **分位差异一句话**：Histogram 服务端算(可聚合/耗资源)、Summary 客户端算(快/不可聚合)。
- **显式边界**：告警链路与 Alertmanager、Grafana 可视化不在本卡范围（课程后续章/运维体系）；本卡只讲指标类型与 PromQL 取数，不重画告警路由。

## 细节与核心 API

**四类指标（Go client_golang 落地）：**

```go
// Counter：只增，QPS 必须 rate/irate
requests := prometheus.NewCounterVec(
    prometheus.CounterOpts{Name: "http_requests_total"}, []string{"svc", "code"})
requests.WithLabelValues("orders", "200").Inc()

// Gauge：瞬时，set/inc/dec（内存/磁盘/Goroutine 数）
mem := prometheus.NewGauge(prometheus.GaugeOpts{Name: "mem_bytes"})

// Histogram：分位用 histogram_quantile 服务端算（可跨实例聚合）
dur := prometheus.NewHistogramVec(prometheus.HistogramOpts{
    Name: "req_duration_seconds",
    Buckets: []float64{.01, .05, .1, .5, 1, 5},
}, []string{"svc"})
dur.WithLabelValues("orders").Observe(0.12)
// PromQL: histogram_quantile(0.99, rate(req_duration_seconds_bucket[5m]))

// Summary：客户端算分位，查询快但不可跨实例聚合（单实例分位场景）
```

**选型口诀：累积量→Counter，状态量→Gauge，要分位且需聚合→Histogram，单实例分位要性能→Summary。平均值掩盖长尾，故用分位暴露 p99。**
