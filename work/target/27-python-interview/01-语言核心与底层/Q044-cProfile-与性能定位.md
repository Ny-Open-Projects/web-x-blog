---
title: [Q044] cProfile 与性能定位
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q044 · cProfile 与性能定位

> 难度:★★☆ | 标签:性能

**问**:怀疑代码慢,第一步做什么?cProfile 输出怎么读?

**答**:先测量再优化。cProfile 按函数统计调用次数、总耗时(cumtime)与自身耗时(tottime),排序看 tottime 找热点函数、看 cumtime 找高成本调用链;`pstats` 可编程分析。微观层面用 `timeit` 做可靠的小段计时(自动处理多次采样)。警惕过早优化:profile 证明的热点才值得动。

```python
# file: code/01_语言核心与底层/q044_cprofile.py
import cProfile
import io
import pstats
import timeit

def slow_parts():
    total = 0
    for i in range(200_000):
        total += len(str(i))     # 字符串转换是热点
    data = [x for x in range(100_000)]
    return total, len(data)

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    slow_parts()
    profiler.disable()

    buf = io.StringIO()
    stats = pstats.Stats(profiler, stream=buf).sort_stats("tottime")
    stats.print_stats(3)
    print(buf.getvalue()[:600])

    cost = timeit.timeit("'-'.join(str(n) for n in range(1000))", number=100)
    print(f"join version: {cost:.4f}s for 100 runs")
```

**追问**:1) cProfile 本身有开销吗?——有,函数级插桩会显著放大调用密集代码的时间,关注相对占比而非绝对值;行级精度可用 line_profiler 这类第三方工具。2) tottime 和 cumtime 怎么读?——tottime 是函数自身耗时(不含子调用),用来找算法热点;cumtime 含全部子调用,用来找高成本调用链;排序字段选错结论就错。3) py-spy 和 cProfile 怎么互补?——py-spy 采样式、不插桩、可挂正在运行的生产进程,开销低; cProfile 精确到函数调用数但侵入,适合开发期复现定位。
