---
title: [Q1107] Prometheus 指标类型与暴露格式
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1107 · Prometheus 指标类型与暴露格式

> 难度:★★★☆ | 标签:Prometheus, metrics

**问**:Prometheus 的四种指标类型分别什么语义?/metrics 的文本长什么样?

**答**:四类:Counter 单调递增(请求数、错误数,查询时用 rate 取速率)、Gauge 可增可减(队列长度、内存)、Histogram 分桶延迟分布(可聚合)、Summary 客户端分位数(不可聚合,基本被 Histogram 取代)。暴露格式是文本协议:`metric_bucket{le="0.1"} 42`,带 HELP/TYPE 注释,HTTP GET 供抓取。工程要点:命名带单位与总数后缀(`_seconds`、`_total`);Counter 重启回退由 rate 处理;抓取是拉模型,服务只需暴露端点。

```python
# file: code/05_数据分析与工程化/q1107_prometheus_types.py

BUCKETS = [0.005, 0.01, 0.05, 0.1, 0.5, 1.0]
LATENCIES = [0.003, 0.008, 0.02, 0.12, 0.6]

def hist_counts(values):
    counts = [0] * (len(BUCKETS) + 1)   # 最后一位是 +Inf
    for v in values:
        placed = False
        for i, b in enumerate(BUCKETS):
            if v <= b:
                counts[i] += 1
                placed = True
                break
        if not placed:
            counts[-1] += 1
    return counts

def render(name, counts):
    lines = [f"# HELP {name} request duration", f"# TYPE {name} histogram"]
    cum = 0
    for b, c in zip(BUCKETS, counts[:-1]):
        cum += c
        lines.append(f'{name}_bucket{{le="{b}"}} {cum}')
    lines.append(f'{name}_bucket{{le="+Inf"}} {sum(counts)}')
    return "\n".join(lines)

if __name__ == "__main__":
    print(render("http_request_duration_seconds", hist_counts(LATENCIES)))
    print("# gauge 示例: queue_depth 42")
    print("# counter 示例: http_requests_total 1024")
```

**追问**:
- 追问 1:为什么用 rate(counter) 而不是直接画 counter?—— counter 只单调增,增速才有业务含义;rate 处理重启回退与采样窗口。
- 追问 2:Histogram 怎么估 P99?—— 找到累计计数超过总数 99% 的最小桶,用桶内线性插值近似,精度受桶边界限制。
