---
title: [Q840] CPU 打满复盘:py-spy 与火焰图
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q840 · CPU 打满复盘:py-spy 与火焰图

> 难度:★★★★ | 标签:CPU, 性能分析

**问**:CPU 100% 但 QPS 没涨,怎么在线上无侵入地定位热点?

**答**:`py-spy top/dump` **无侵入采样**正在运行的进程,直接看热点栈——不用改代码不用重启;火焰图(speedscope 火焰格式)可视化聚合调用占比。CPU 打满常见根因:低效算法(O(n²) 随数据量增长)、正则灾难性回溯、序列化大对象、 GC 压力、死循环。区分**单请求热点**(优化代码)与**容量不足**(扩容+限流)。开发态可用 cProfile 精确复现,但线上优先采样器(开销低、无停机)。

```python
# file: code/03_Web后端开发/q840_cpu_triage.py
import cProfile
import io
import pstats

def hot_loop(n: int) -> int:
    total = 0
    for i in range(n):
        total += i * i
    return total

profiler = cProfile.Profile()
profiler.enable()
hot_loop(200000)
profiler.disable()
buf = io.StringIO()
pstats.Stats(profiler, stream=buf).sort_stats("cumulative").print_stats(3)
print("\n".join(buf.getvalue().splitlines()[:8]))
```

**追问**:
- 正则回溯为什么危险?——嵌套量词在部分输入上指数级回溯,单条请求能打满一个核,防御是限制输入长度与改写模式。
- py-spy 的 dump 和 top 区别?——dump 打印当前所有线程栈快照(卡死分析),top 持续采样按占比排序(热点分析)。
