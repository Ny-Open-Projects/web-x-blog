---
title: "[Q7725] 多 Agent 互相等结果：等待图里的环怎么破"
date: 2026-11-23
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7725 · 多 Agent 互相等结果：等待图里的环怎么破

难度：P6 ｜ 标签：多 Agent、死锁、等待图、超时

基线：Python 3.12；多 Agent 编排（消息传递/共享状态）；纯 Python 模拟 wait-for graph。

**问**：三个 Agent 协作写报告：A 等 B 的调研结果，B 等 C 的数据，C 等 A 的大纲。上线后整条流水线卡死，日志里每个 Agent 都显示"waiting for dependency"，没有任何报错，直到超时批量失败。消息队列没丢消息、服务都健康，为什么会出现环形等待？怎么在编排层提前发现？

**答**：
- **结论**：这是**分布式死锁**：每个 Agent 持有一个资源（自己的输出/锁）并等待另一个 Agent 的资源，等待关系形成环（A→B→C→A），没有任何一个能推进。与单机锁不同，这里没有全局锁管理器，消息协议只保证"消息能送达"，不保证"依赖无环"；超时只是兜底，不是检测。必须在编排层维护 **wait-for graph** 并做环检测，或从设计上禁止环。
- **取舍**：环检测能在提交前拒绝/打破环，代价是要集中维护依赖关系、增加协调开销；超时+重试简单，但会把"永久死锁"变成"反复超时重试"，放大成本且掩盖根因。更根本的做法是**依赖单向化**（DAG 编排）、固定资源获取顺序、或把"互相需要"改成由一个协调者串行调度。
- **实战**：① 提交任务前对依赖图做拓扑排序，有环直接拒绝并指出环路径；② 运行中用租约/TTL，等待超时后**取消整个环**而不是各自重试；③ 给每个 Agent 的输出加版本/占位，允许"先返回草稿再补齐"打破强依赖；④ 监控"等待时长分布"，长尾突增是死锁前兆。

```python
"""wait-for graph 环检测：三色标记 DFS，输出环路径。"""
from collections import defaultdict


def find_cycle(graph: dict[str, list[str]]) -> list[str] | None:
    WHITE, GRAY, BLACK = 0, 1, 2
    color = defaultdict(int)
    stack: list[str] = []

    def dfs(node: str) -> list[str] | None:
        color[node] = GRAY
        stack.append(node)
        for nxt in graph.get(node, []):
            if color[nxt] == GRAY:                 # 回到栈上的节点 = 环
                return stack[stack.index(nxt):] + [nxt]
            if color[nxt] == WHITE:
                cycle = dfs(nxt)
                if cycle:
                    return cycle
        stack.pop()
        color[node] = BLACK
        return None

    for node in graph:
        if color[node] == WHITE:
            cycle = dfs(node)
            if cycle:
                return cycle
    return None


if __name__ == "__main__":
    deadlock = {"A": ["B"], "B": ["C"], "C": ["A"]}
    dag = {"A": ["B", "C"], "B": ["C"], "C": []}

    print("环形依赖:", find_cycle(deadlock))
    print("无环 DAG:", find_cycle(dag))

    # 打破环：把 C 对 A 的依赖改成"使用 A 的上一版大纲"
    fixed = {"A": ["B"], "B": ["C"], "C": []}
    print("去掉 C->A 后:", find_cycle(fixed))
    print("结论：提交前拓扑检测，有环就拒绝或改依赖方向")
```

**追问一**：为什么给每个 Agent 加超时重试，反而可能让系统更糟？
→ 解析：死锁的环不会因为重试而解开，重试只会周期性重复同样的等待，消耗 token/CPU/连接；多个 Agent 同时超时重试还会造成"重试风暴"，把本来健康的依赖也拖垮。超时应配合**取消传播**：一个节点超时，沿等待边取消整个环，释放已占资源。

**追问二**：分布式死锁和单机线程死锁的检测难度差在哪？
→ 解析：单机可以维护全局锁表、精确知道谁持有什么；分布式没有全局时钟和共享内存，等待关系要靠消息/心跳拼出来，且可能因网络分区出现"假死"（对端其实已完成但消息未达）。所以分布式更依赖**设计上避免环**（DAG、固定顺序、租约）而不是运行时的精确检测。
