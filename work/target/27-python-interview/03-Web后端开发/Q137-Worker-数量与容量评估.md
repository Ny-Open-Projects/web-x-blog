---
title: [Q137] Worker 数量与容量评估
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q137 · Worker 数量与容量评估

> 难度:★★★ | 标签:部署, 容量

**问**:生产环境 worker 和线程数如何估算?内存与 CPU 如何权衡?

**答**:经典起点:CPU-bound 应用 `workers = CPU 核数`(避免争抢),IO-bound 用 `核数*2+1` 再加线程或换异步 worker;内存受限时用 `workers = 可用内存 / 单 worker 内存` 反推。线程模型下 `threads = workers * 每进程线程数`,受 GIL 限制线程只对 IO 等待有效。压测才是最终依据:用 wrk/locust 找到吞吐拐点与 p99 延迟达标配置,并给数据库连接池留余量(每 worker 连接数 × workers ≤ DB max_connections)。

```python
# file: code/03_Web后端开发/q137_worker_sizing.py
def estimate_workers(cpu_cores: int, per_worker_mb: int,
                     total_mb: int, io_bound: bool = True) -> dict:
    by_cpu = cpu_cores * 2 + 1 if io_bound else cpu_cores
    by_mem = max(total_mb // per_worker_mb, 1)
    workers = min(by_cpu, by_mem)
    return {
        'recommended_workers': workers,
        'limited_by': 'cpu' if by_cpu <= by_mem else 'memory',
        'note': '最终以压测 p99 与吞吐拐点为准',
    }

# 4 核 8G,单 worker 约 400MB 的 IO 密集服务
print(estimate_workers(cpu_cores=4, per_worker_mb=400, total_mb=8192))
# {'recommended_workers': 9, 'limited_by': 'memory', ...}
```

**追问**:
- 为什么是「核数*2+1」而不是更多?——IO 等待期间线程切换让 CPU 保持忙;线程过多上下文切换开销反噬,经验值来自实测拐点。
- 数据库连接数怎么算余量?——每 worker 连接池 × workers ≤ DB max_connections 的 70-80%,给运维与批处理留头寸。
- 压测要看哪些指标定容?——吞吐拐点、P99、错误率、CPU/内存;单看 QPS 会选到延迟爆炸的配置。
