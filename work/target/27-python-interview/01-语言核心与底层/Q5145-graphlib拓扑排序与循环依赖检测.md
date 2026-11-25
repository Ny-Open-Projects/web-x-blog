---
title: "[Q5145] graphlib.TopologicalSorter 与循环依赖检测"
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5145 · graphlib.TopologicalSorter 与循环依赖检测

难度：P6 ｜ 标签：graphlib、拓扑排序、3.9+、构建系统

**问**：任务编排系统里用户可以自定义"前置任务"，一次配置错误让调度器死循环后 OOM。如何用 3.9 内置的 `graphlib` 做拓扑排序并在调度前**提前**检测环？`prepare()/get_ready()/done()` 三段式接口为什么这样设计？

**答**：
结论：`graphlib.TopologicalSorter` 是 3.9 内置的拓扑排序 + 环检测器：直接对全图 `list(sorter)` 或先 `prepare()` 后会在存在环时抛 `CycleError`（附带环路径），调度器应该在**接收配置时**就校验，而不是运行到一半 OOM。三段式接口（`prepare` → 反复 `get_ready()` 取零入度节点 → `done(node)` 标记完成）把排序器变成了**流式调度协议**：某批任务执行完 `done` 后才解锁下一批，天然支持动态并行调度，这是"一次性 `list()` 拿全序"给不了的能力。

取舍：`list(sorter)` 简单但只能串行语义；三段式灵活但要自己管理并发完成回调。graphlib 只做 DAG 排序，没有权重/优先级/超时，复杂编排仍需 APScheduler/Celery/DAG 框架，但"前置依赖校验"这一层用标准库就够了。

实战：配置加载处对依赖图先 `prepare()` 抛出带环路径的 `CycleError`，把 "a→b→c→a" 直接返回给用户；执行器用 `get_ready/done` 配线程池，把同批无依赖任务并行跑。

```python
from graphlib import TopologicalSorter, CycleError

graph = {
    "build": ["lint"],
    "test": ["build"],
    "deploy": ["test"],
    "hotfix": ["deploy", "lint"],
}

order = list(TopologicalSorter(graph).static_order())   # 串行全序（内部含 prepare）
print("serial order:", order)

ts = TopologicalSorter(graph)
ts.prepare()                      # 存环时这里抛 CycleError（调度器前置校验）

# 环检测：配置校验阶段直接拒绝
bad = {"a": ["c"], "b": ["a"], "c": ["b"]}
try:
    TopologicalSorter(bad).prepare()
except CycleError as e:
    print("cycle found:", e.args[1])   # 环路径，直接回给用户

# 三段式：模拟并行调度器——同批任务并发，done 后解锁下一批
import concurrent.futures

ts2 = TopologicalSorter(graph)
ts2.prepare()
executed: list[str] = []
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    while True:
        ready = list(ts2.get_ready())          # 当前所有零入度任务
        if not ready:
            break
        for name, delay in pool.map(lambda n: (n, 0.01), ready):
            # 模拟任务执行；done 必须在任务真正完成后调用
            ts2.done(name)
            executed.append(name)
print("parallel order:", executed)
assert set(executed) == set(order)
```

**追问一**：`static_order()` 与 `get_ready/done` 的关系？——`static_order` 内部就是三段式的全自动串行消费；三段式是暴露出中间态让调度器插入并发与重试逻辑，两者共享同一份状态机。

**追问二**：`done()` 漏调或重复调会怎样？——漏调则后续任务永远 `get_ready` 不出来，调度器表现为"卡死"（比 OOM 好排查，但要配 watchdog）；重复调抛 `ValueError`。这两个是调度器自测的必写用例。

**追问三**：如果依赖是运行中动态追加的怎么办？——graphlib 不支持边动态修改；做法是新配置到达时构建新 sorter，与旧图做"剩余子图"迁移，讨论为什么禁止运行中改图（状态机一致性）。

## 背诵要点
- 3.9 内置 `graphlib`：`prepare()` 提前抛 `CycleError`（带环路径），配置校验期拦截，杜绝运行中 OOM。
- `prepare → get_ready（零入度批）→ done` 三段式是并行调度协议；`static_order` 是其串行简化。
- `done` 漏调卡死、重复调抛 ValueError；graphlib 无权重/优先级，复杂编排交给任务框架。

## 复盘追问
- 如何给环路径生成用户可读的"配置项第几行"定位？（建图时携带 source map，CycleError 节点映射回配置位置）
- 两个任务"互为可选依赖"（都能跑但顺序影响结果）如何在 graphlib 语义下建模？（人为加边确定顺序 vs 拆成两阶段图，讨论确定性输出）
