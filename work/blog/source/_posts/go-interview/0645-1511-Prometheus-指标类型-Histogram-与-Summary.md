---
disableNunjucks: true
title: "1511 Prometheus 指标类型：Histogram 与 Summary"
date: 2026-10-08 15:42:45
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：监控 / Prometheus | 难度：L3 | 题型：概念题 | 频率：高 | 关键词：**Histogram**/**Summary**/**分位数**/**bucket**/**_sum/_count**
> 原文锚点：第 37~58 段「Histogram / Summary + 分位数计算差异」

## 一句话总述
Histogram 与 Summary 都描述样本**分布**，解决「平均值掩盖长尾」问题：Histogram 把度量值按区间 **buckets** 计数，并暴露 `_sum`/`_count` 后缀 counter，分位数由**服务端** `histogram_quantile` 计算（耗资源）；Summary 把分位数在**客户端**直接算好存储，查询性能好但无法跨实例聚合。

## 面试官视角
- 考察意图：是否理解两类分布指标的区别，尤其「分位数在服务端还是客户端算」这一核心差异。
- 分档：P5 知两者都看分布；P6 知 Histogram 用 buckets、Summary 存分位；P7 知 Histogram 服务端算分位（可聚合、耗资源）、Summary 客户端算（查询快、不可聚合）。
- 红旗答案：以为 Summary 也能 `histogram_quantile`；或不知道 Histogram 暴露 _sum/_count。
- 惊艳点：点出「Histogram 可跨多个实例用 sum 聚合后再算分位；Summary 的分位数已固化、sum 后无意义」。

## 主问答
**Q（面试官原话）：** Histogram 和 Summary 有什么区别？分位数怎么算？
**A：**
1. **Histogram（区间计数）**：把度量值划分成连续区间 buckets 并计数落入数；同时暴露 `_sum`（总和 counter）与 `_count`（总数 counter）后缀指标；分位数用服务端函数 `histogram_quantile(0.9, ...)` 算 p90/p99，取 `histogram_quantile(0.99, ...)` 得 p99。
2. **Summary（客户端分位）**：类似 Histogram 也描述分布，但**直接在客户端计算并存储分位数**，只暴露 `_sum`/`_count` 两个后缀 counter；查询时不必再算，性能好。
3. **核心差异（分位计算位置）**：Histogram 的分位数在**服务端** PromQL 算（可先 sum 跨实例聚合再算，但耗计算资源）；Summary 的分位数在**客户端**已算好（查询快，但分位数无法再跨实例聚合）。
4. **选型**：要跨实例聚合分位、接受服务端开销 → Histogram；只关心单实例分位、要查询性能 → Summary；两者都需 `_sum`/`_count` 配合算平均。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 两者都干嘛？ | 基础 | 描述分布 | P5 |
| L2 | Histogram 暴露啥？ | 细节 | _sum/_count/buckets | P6 |
| L3 | 分位在哪算？ | 关键 | Histogram 服务端/Summary 客户端 | P6 |
| L4 | 为何 Histogram 可聚合？ | 深度 | buckets 可 sum | P7 |
| L5 | 怎么选？ | 进阶 | 聚合需求定 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| Prometheus 全版本 | 无 | Histogram/Summary 行为跨版本一致 |

## 关键代码
```go
// client_golang 定义 Histogram（带 buckets）与 Summary
var (
	reqLatency = prometheus.NewHistogramVec(prometheus.HistogramOpts{
		Name:    "http_request_duration_seconds",
		Buckets: []float64{0.01, 0.05, 0.1, 0.5, 1}, // 区间计数
	}, []string{"method"}),
	reqSum = prometheus.NewSummary(prometheus.SummaryOpts{
		Name: "http_request_duration_summary", // 客户端算好分位
	}),
)
func observe(d float64) {
	reqLatency.WithLabelValues("GET").Observe(d)
	reqSum.Observe(d)
}
```

## 总结与追问预判
四类型（Counter/Gauge/Histogram/Summary）构成 Prometheus 数据模型。指标模型与 PromQL 常用函数下一张。

## ⚠️ 原文纠错
1. 事实核校： [经验] Histogram 用 buckets+_sum/_count、histogram_quantile 服务端算分位；Summary 客户端算分位、查询性能好、不可跨实例聚合——均正确。
2. 崩坏词归一：源码将若干 Prometheus/监控专有名词音译为崩坏词，本卡统一为规范术语。
