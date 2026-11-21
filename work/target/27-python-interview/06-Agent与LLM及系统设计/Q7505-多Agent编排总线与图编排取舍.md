---
title: [Q7505] 多 Agent 编排:消息总线 vs 图编排的取舍
date: 2026-11-18
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7505 · 多 Agent 编排:消息总线 vs 图编排(langgraph 思路)的取舍

> 难度:★★★ | 标签:Agent, 架构, 编排

**问**：多 Agent 系统两种流派：消息总线（各 Agent 订阅事件自由协作）和图编排（DAG/状态图显式定义流转）。架构评审时怎么选？各自在可观测性、失败恢复、动态性上的真实短板是什么？

**答**：结论：选型的分水岭是"流程确定性与可审计性要求"。**图编排**把控制流写死在图里：每步输入输出可校验、可重放、失败定位到节点，适合业务流程明确（审批链、多步流水线）与强合规场景；**消息总线**松耦合、可动态加入 Agent，但全局行为不可预测、死信与循环难排查，适合探索型协作（头脑风暴、跨域联查）。经验法则：**生产可交付的 Agent 系统九成该用图编排（或图为主+总线为辅），纯总线架构几乎都会在可观测性上翻车**。

短板与实战：
- 总线的三大真实短板：无全局视图（"这条消息为什么触发了这个 Agent"要靠日志考古）、级联放大（一个事件扇出 N 订阅者，N 又发事件，风暴）、最终一致性（Agent 各自持有状态副本，冲突靠事后仲裁）。
- 图编排的短板同样真实：灵活性差（新增分支要改图+发版）、长流程的图状态膨胀（checkpoint 大）、以及"图复杂到没人看得懂"——节点数超过 30 就该分层拆子图。
- 事故复盘：某总线架构里"总结 Agent"订阅了"检索完成"事件，而另一个 Agent 又会重发该事件，导致总结被触发 4 次、4 份报告覆盖写。修复：事件幂等键（事件 ID + 消费者去重）+ 把固定流程改造成显式图。教训：**只要流程能画出来，就画出来**；总线留给真正动态的多方协作。

```python
# 基线:Python 3.9+ 标准库;两种编排的最小骨架对比(可运行)
from collections import deque

def graph_run(dag: dict[str, list[str]], entry: str) -> list[str]:
    """图编排:拓扑序执行,流程确定、可重放。"""
    order, ready = [], deque([entry])
    while ready:
        node = ready.popleft()
        order.append(node)
        ready.extend(dag.get(node, []))
    return order

class Bus:
    """消息总线:订阅-发布,动态但全局行为不可预测(演示扇出放大)。"""
    def __init__(self) -> None:
        self.subs: dict[str, list[str]] = {}
        self.fired: list[tuple[str, str]] = []
    def subscribe(self, topic: str, agent: str) -> None:
        self.subs.setdefault(topic, []).append(agent)
    def publish(self, topic: str, evt_id: str, depth: int = 0) -> None:
        if depth > 3:
            return                       # 防风暴闸门:总线架构必须自带
        for agent in self.subs.get(topic, []):
            self.fired.append((agent, evt_id))
            self.publish(f"done.{agent}", evt_id, depth + 1)   # 级联扇出

if __name__ == "__main__":
    print(graph_run({"a": ["b", "c"], "b": ["d"], "c": ["d"]}, "a"))
    bus = Bus()
    bus.subscribe("query", "A"); bus.subscribe("done.A", "B")
    bus.publish("query", "e1")
    print(bus.fired)                     # 两次触发:1 次发布 → 2 次 Agent 执行
```

**追问**：
- 一层追问：图编排的 checkpoint/state 怎么设计才能断点恢复？——每节点执行后原子持久化（节点 ID + 输入指纹 + 输出），恢复时按"已完成节点指纹与当前图一致"跳过；图版本变更时指纹不一致的节点重跑，这是 langgraph 式恢复的核心语义。
- 二层追问：混合架构（图 + 总线）的边界怎么划？——图管"必须发生的流程"，总线只承载"通知类"事件（进度上报、审计采集），且总线上不允许再触发业务决策节点——把总线降级为观测通道，规避级联风暴。
- 三层追问：多 Agent 并发写同一共享状态怎么办？——图里用"单写者节点"收敛（写操作集中在一个节点串行执行），或给共享状态加版本化 CAS（写时校验版本号）；多 Agent 自由并发写共享内存是总线架构最难治理的坑。
