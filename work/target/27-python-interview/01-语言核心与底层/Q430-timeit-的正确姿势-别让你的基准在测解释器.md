---
title: [Q430] timeit 的正确姿势:别让你的基准在测解释器噪音
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q430 · timeit 的正确姿势:别让你的基准在测解释器噪音

> 难度:★★★★☆ | 标签:性能, timeit, 基准测试

**问**:为什么"在 REPL 里测出来 A 比 B 快"经常是错的?`timeit` 的 `number`、`repeat`、`globals` 各有什么讲究?GC 和 tracer 对基准的污染怎么排除?最终汇报应该报哪个统计量?

**答**:REPL/脚本测时间的常见错误:一次性计时包含首次执行的自适应特化预热(3.11+ 前几百次调用在解释特化,测的是"冷"路径)、GC 恰好在循环中触发、以及 `time.perf_counter` 手工计时的循环外开销。`timeit` 的对策:禁 GC、重复执行取分布、语句级编译去除外壳。要点:`number` 要调到单次运行 > 0.2s;`repeat=5~7` 后**取最小值**而非均值(min 最接近真实成本,均值被系统抖动污染——这是 pyperf/timeit 官方口径);被测函数在 `globals=globals()` 下要小心名字查找差异;同一进程内先测的用例可能预热缓存影响后者,重要结论换序复测。进阶:3.12+ 可用 `timeit -r` 配合 `--processes`(pyperf)或 `perf` 采样对照,汇报时写明 Python 版本与平台,因为这些微基准结论强绑定 CPython 具体版本。

```python
# file: code/01_语言核心与底层/q430_timeit_bench.py
import timeit

code_a = "sum(range(1000))"
code_b = "sum([i for i in range(1000)])"     # 多一层 list 构建与临时 list

NUMBER = 2_000    # 演示规模缩小保证秒级跑完;真实基准建议调到单次 repeat > 0.2s
REPEAT = 5

def bench(stmt):
    t = timeit.Timer(stmt, globals={"sum": sum, "range": range})
    runs = t.repeat(REPEAT, NUMBER)
    ns = [r / NUMBER * 1e9 for r in runs]    # 统一换算成单次耗时 ns
    return min(ns), ns                        # 汇报取 min 而非均值

best_a, runs_a = bench(code_a)
best_b, runs_b = bench(code_b)
print(f"sum(range)      {best_a:8.0f} ns/op  all runs: {[round(r) for r in runs_a]}")
print(f"sum(listcomp)   {best_b:8.0f} ns/op  all runs: {[round(r) for r in runs_b]}")
print("ratio:", round(best_b / best_a, 2))
print("timeit 默认禁用 GC:", "gc 在 Timer 内部被关闭,避免回收打点污染")
```

**追问**:1) 为什么报 min 不报 mean?——mean 混入 OS 调度、缺页等单向噪声,分布右偏;min 是"最理想机器状态下的真实成本",官方 timeit/pyperf 均此口径。2) 3.11+ 的 adaptive interpreter 对微基准意味着什么?——函数要跑几百次才完成特化,`number` 太小时测的是未特化路径,快慢结论可能整体反转。
