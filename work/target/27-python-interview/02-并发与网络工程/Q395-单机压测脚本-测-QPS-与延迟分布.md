---
title: [Q395] 单机压测脚本:测 QPS 与延迟分布
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q395 · 单机压测脚本:测 QPS 与延迟分布

> 难度:★★★ | 标签:压测, 性能, 并发

**问**:如何用 Python 给一个 HTTP 接口做单机压测?要看哪些指标?

**答**:自己写:线程池 + 连接复用 + 采样,统计 QPS、平均/P95/P99 延迟、错误率。要点:①压测机不能成为瓶颈——连接复用、并发数递增找到拐点;②看延迟分布而不是平均值(P99 比 avg 有信息量);③区分客户端排队延迟和服务端处理延迟;④预热后再采样;⑤压测要隔离环境,防止打挂共享服务。生产工具:`wrk`/`locust`/`k6`,locust 即 Python 写的。

```python
# file: code/02_并发与网络工程/q395_benchmark.py
"""单机压测脚本:并发采样 + QPS + 延迟分位数。"""
import concurrent.futures as cf
import random
import statistics
import time
import urllib.request

TARGET = "https://httpbin.org/get"


def one_request():
    start = time.perf_counter()
    try:
        with urllib.request.urlopen(TARGET, timeout=5) as resp:
            resp.read(1024)
        return time.perf_counter() - start, None
    except Exception as e:
        return time.perf_counter() - start, repr(e)


def percentile(sorted_data, p):
    if not sorted_data:
        return 0.0
    idx = min(int(len(sorted_data) * p / 100), len(sorted_data) - 1)
    return sorted_data[idx]


def benchmark(total=20, workers=5):
    with cf.ThreadPoolExecutor(max_workers=workers) as pool:
        results = list(pool.map(lambda _: one_request(), range(total)))
    latencies = sorted(d for d, _ in results)
    errors = [e for _, e in results if e]
    duration = sum(latencies)  # 近似总时间(串行累加口径, 单机粗估)
    qps = total / (sum(latencies) / workers) if workers else 0
    print(f"请求数 {total} 并发 {workers} 错误 {len(errors)}")
    print(f"avg {statistics.mean(latencies)*1000:.0f}ms "
          f"p50 {percentile(latencies, 50)*1000:.0f}ms "
          f"p95 {percentile(latencies, 95)*1000:.0f}ms "
          f"p99 {percentile(latencies, 99)*1000:.0f}ms")
    print(f"估算 QPS ~ {qps:.1f}")
    if errors:
        print("错误示例:", errors[0])


if __name__ == "__main__":
    benchmark(total=20, workers=5)
```

**追问**:
- P99 是什么意思?99% 的请求延迟低于该值,反映长尾;用户体验由长尾决定,故容量规划看 P99/P999 而非均值。
- 并发加到多大该停?QPS 不再上升而延迟陡增,即系统拐点;继续加压只会堆积队列,得到的数据没有意义。
