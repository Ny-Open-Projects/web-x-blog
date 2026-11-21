---
title: [Q7544] Agent 长任务并发容量账：工具并发与下游配额联动
date: 2026-11-20
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7544 · 容量规划：Agent 平台的并发上限不是实例数，是下游工具配额的函数

> 难度:★★★★ | 标签:容量规划, Agent 编排, 配额联动

**问**：一个 Agent 平台要支撑 500 并发会话，每个会话平均 30% 时间在调工具（搜索 API 配额 50 QPS、内部 DB 连接池 100、LLM 网关 TPM 200 万）。容量瓶颈怎么找？为什么"按 CPU/内存给容器扩容"解决不了这类系统的并发上限？全链路配额联动怎么设计？

**答**：结论：Agent 系统的并发容量 = **min(各下游配额换算的并发数)**——瓶颈在工具与 LLM 的配额，不在算力。换算公式：每个活跃会话的下游占用 = 工具调用频率 × 单调用资源占用；本例搜索 50 QPS ÷ (0.3 会话调用密度) 决定能撑的会话数远小于 500。扩容实例只会把瓶颈移到更脆弱的下游（触发 429/连接池打满），正确做法是**配额联动准入**：按下游剩余配额控制"可进入活跃态的会话数"，超出的会话排队而不是并发执行。

机理与实战：
- **逐下游换算**：设每活跃会话每秒 0.3 次工具调用：搜索配额 50 QPS → 撑 166 活跃会话；LLM TPM 200 万 ÷ 每会话 4000 tok/请求 × 2 请求/分钟 → 250 会话；DB 连接池 100 ÷ 每会话峰值 1 连接 → 100 会话。瓶颈 = 100（DB）→ 全系统活跃会话上限 100，其余必须排队。这是三个 min 的最小值，任一下游扩配额都可能改变瓶颈归属。
- **准入控制**：会话状态机 idle→active（领取全局配额信号量）→idle（释放）；每个下游一个信号量，任一不足则会话不能进入 active。信号量按"预估占用"发放，释放按"实际归还"，误差用 10-20% 的安全余量吸收。
- **延迟型配额的陷阱**：TPM/RPM 是滚动窗口配额不是绝对并发——排队解决不了"所有人挤在同一分钟"的问题，需要速率整形（令牌桶按分钟窗口放行）；而连接池是绝对并发配额，排队有效。两类配额要分开建模，混用会导致"明明排队了还是 429"。
- **容量验证**：用影子会话（合成负载）按目标并发跑 30 分钟，观测各下游的水位与错误率；容量报告要写清"瓶颈在谁、下一个瓶颈是谁"（瓶颈转移预测），扩容决策才有方向。

```python
# 基线:Python 3.10+;纯标准库,Agent 并发容量推算:下游配额换算 + 准入信号量
from __future__ import annotations
from dataclasses import dataclass, field
import math


@dataclass
class Quota:
    name: str
    kind: str          # rate(速率窗口) / pool(绝对并发)
    capacity: float    # QPS / TPM / 连接数
    per_session: float  # 每活跃会话占用速率或连接数


@dataclass
class Platform:
    quotas: list[Quota]
    safety_margin: float = 0.15
    semaphores: dict[str, int] = field(default_factory=dict)

    def __post_init__(self) -> None:
        usable = {q.name: math.floor(q.capacity * (1 - self.safety_margin) / q.per_session)
                  for q in self.quotas}
        self.max_active = min(usable.values())
        self.bottleneck = min(usable, key=usable.get)
        self.semaphores = dict(usable)

    def admit(self, session_id: str) -> bool:
        """准入:占用各下游 1 单位;任一不足则拒绝(排队)。"""
        if min(self.semaphores.values()) < 1:
            return False
        for k in self.semaphores:
            self.semaphores[k] -= 1
        return True

    def release(self) -> None:
        for k, v in self.semaphores.items():
            cap = math.floor(next(q.capacity * (1 - self.safety_margin) / q.per_session
                                  for q in self.quotas if q.name == k))
            self.semaphores[k] = min(cap, v + 1)


def demo() -> None:
    quotas = [
        Quota("search-api", "rate", capacity=50, per_session=0.3),    # 50QPS
        Quota("llm-gateway", "rate", capacity=2_000_000, per_session=8000),  # TPM, 每会话 8000 tok/min
        Quota("db-pool", "pool", capacity=100, per_session=1),
    ]
    p = Platform(quotas)
    print(f"各下游可撑活跃会话: {[math.floor(q.capacity * 0.85 / q.per_session) for q in quotas]}")
    print(f"全系统活跃上限: {p.max_active} (瓶颈: {p.bottleneck})")
    assert p.max_active == 85 and p.bottleneck == "db-pool"
    # 准入控制:最多 max_active 个会话同时活跃
    admitted = sum(p.admit(f"s{i}") for i in range(200))
    assert admitted == p.max_active
    print(f"准入结果: 200 会话请求,放行 {admitted},其余排队")
    p.release()
    assert p.admit("next")
    # 扩容 DB 后瓶颈转移预测:db 200 -> search-api 成新瓶颈
    quotas2 = [Quota("db-pool", "pool", 200, 1)] + quotas[:2]
    p2 = Platform(quotas2)
    assert p2.bottleneck == "search-api"
    print(f"扩容 DB 200 后瓶颈转移 -> {p2.bottleneck} (上限 {p2.max_active})")
    print("Agent 容量 = min(下游配额换算);准入信号量控制活跃会话,排队而非硬闯 ✅")


if __name__ == "__main__":
    demo()
```

**追问一**：为什么"工具调用并发"和"会话并发"要分开建模？
答：一个活跃会话不等于一个工具并发——会话大部分时间在等 LLM 生成（无工具占用），工具并发是脉冲式的（会话内串行，跨会话叠加）。按会话数配工具池会超配，按工具峰值配会欠配；正确建模是"每活跃会话的调用频率×单次占用"，即把会话并发换算成下游的资源速率。这也是准入信号量按"每会话占用"发放的原因。

**追问二**：容量报告里"瓶颈转移预测"为什么重要？
答：扩容瓶颈下游后，系统上限变成次小值——如果只解决 DB 而不知道 LLM TPM 是下一个瓶颈，扩容投入换不来等比例的并发提升，甚至把压力转移到更贵的资源上。容量规划的产出不是"要不要扩"而是"按什么顺序扩、每步能换来多少会话上限"，这需要瓶颈链的完整推算。

## 背诵要点
- Agent 并发上限 = min(各下游配额 ÷ 每活跃会话占用)，瓶颈在工具/LLM 配额不在算力；容器扩容只会转移瓶颈。
- 准入控制：每个下游一个信号量，按预估占用发放、按实际归还、留 15% 安全余量；超出的会话排队不硬闯。
- 速率型配额（RPM/TPM）要令牌桶整形，绝对并发型（连接池）才适合排队；容量报告必须含瓶颈转移预测。

## 复盘追问
- 为什么压测 100 并发通过了、上线 150 并发就雪崩？（提示：压测用的是合成会话（调用模式均匀），真实会话的工具调用是突发聚集（如早高峰批处理）；容量要用真实调用分布建模，安全余量就是为分布不确定性买的保险）
- 多个 Agent 平台共享同一个 LLM 网关时，容量账怎么合并？（提示：配额是共享资源，各平台的"每会话占用"要加权汇总后统一准入；否则各平台各自按自己的余量放行，总和超配——共享配额的治理等于引入"平台间协调"，通常由网关侧集中准入解决）
