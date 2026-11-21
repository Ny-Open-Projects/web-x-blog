---
title: [Q2634] graphlib.TopologicalSorter:依赖排序与循环检测
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2634 · graphlib.TopologicalSorter:依赖排序与循环检测

> 难度:★★★☆☆ | 标签:graphlib, 拓扑排序, 3.9 新特性

**问**:标准库能做依赖排序吗?检测到循环依赖会怎样?

**答**:3.9 的 `graphlib.TopologicalSorter` 是标准答案:传入「节点 -> 前置集合」的字典,`static_order()` 一次给出合法顺序;存在环时抛 `CycleError`,环本身可以用 `exception.args[1]` 拿到(3.9 起提供参与环的节点)。做并行调度时用增量 API 更合适:`prepare()` 锁定图,循环 `get_ready()` 拿当前可执行节点、`done(node)` 标记完成,天然表达「就绪即可并发」;同一层的就绪集合可以放心丢给线程/进程池。图必须是有向无环的,`static_order` 内部先 `prepare` 再逐层输出,重复调用会报错,要保存结果列表。

```python
# file: code/01_语言核心与底层/q2634_graphlib_topo.py
"""graphlib:拓扑排序、并发就绪层与环检测。"""
from graphlib import CycleError, TopologicalSorter

deps = {
    "install": set(),
    "migrate": {"install"},
    "test": {"migrate"},
    "deploy": {"test"},
    "docs": {"install"},
}

if __name__ == "__main__":
    sorter = TopologicalSorter(deps)
    print("线性顺序:", list(sorter.static_order()))

    # 增量 API:按就绪层输出,适合并行调度
    sorter = TopologicalSorter(deps)
    sorter.prepare()
    layer = 0
    while sorter.is_active():
        ready = sorter.get_ready()
        print(f"第 {layer} 层可并发:", sorted(ready))
        for node in ready:
            sorter.done(node)
        layer += 1

    try:
        TopologicalSorter({"a": {"b"}, "b": {"a"}}).prepare()
    except CycleError as exc:
        print("环检测:", exc)
```

**追问**:1) get_ready 返回的节点顺序稳定吗?——不保证,集合语义,业务上要确定性就自行 sorted,图的输出顺序本就不唯一。2) TopologicalSorter 的用法要点?——prepare() 检环(循环引用抛 CycleError 并给出环);get_ready()/done() 流水式并行执行;static_order() 一次性顺序。3) 与任务调度的结合?——get_ready 返回的并行批次交给线程池/异步任务,done 后继续;这是「依赖图调度器」的标准骨架(构建系统、DAG 工作流)。4) 生产陷阱?——不清 done 导致卡死;环检测后才报错(入口要 prepare);顺序依赖未 sorted 的输出;并行批次共享状态竞态。
