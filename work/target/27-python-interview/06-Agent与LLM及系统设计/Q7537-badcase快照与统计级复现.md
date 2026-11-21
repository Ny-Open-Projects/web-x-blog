---
title: [Q7537] badcase 快照与统计级复现：为什么重跑复现不出来
date: 2026-11-20
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7537 · 可重现性工程：用户报了 badcase，重跑却"好了"

> 难度:★★★★ | 标签:可重现性, badcase, 回放器

**问**：用户报了一个错误输出，工程师重跑却复现不出来——"现在看起来没问题"就结案了吗？LLM 输出的可重现性要固定哪些要素？为什么温度 0 也不保证确定？回放器怎么建、工具/检索结果怎么处理？

**答**：结论：复现不出来是因为输入快照不完整 + 采样本身非确定。可重现 = 固定三元组"**输入快照（messages+工具/检索结果+上下文）+ 采样参数 + 模型版本**"，且工程目标应是**统计级复现**（重放 N 次看行为分布），而不是单条 bit 级一致——温度 0 也存在路由/批处理层面的非确定性，供应商还会静默更新模型。

机理与实战：
- **快照五要素**：完整 messages 序列、采样参数（温度/top_p/种子若支持）、模型版本标识（响应头里拿）、工具与检索结果的冻结快照、（Agent 场景）每步的工具 schema——缺任何一维都可能"重跑就好了"。
- **温度 0 的非确定来源**：分布式推理的浮点求和顺序随 batch 组合变化、MoE 路由、供应商负载均衡把请求路由到不同硬件/实例——bit 级复现不可依赖，判定用"重放分布"（多数输出、漂移率）。
- **时间敏感上下文必须冻结**：检索结果、行情、库存变了之后重放，得到的是"今天的答案"——复现的是当时行为就必须用当时的快照；确定性工具（查库）可回放真实调用，非确定工具一律冻结。
- **工程闭环**：badcase 入库带完整快照（Q1213 反馈闭环）→ 回放器重放 N 次给出行为分布 → 修复后把历史 badcase 集合作为回归集重放（"曾经坏过的不能再坏"）。
- **供应商静默更新**：模型版本标识在快照里，回放前先校验版本仍在（或 pin 到快照版本的可复现环境），版本没了要标注"复现环境不可用"而不是硬回放。

```python
# 基线:Python 3.10+;纯标准库实现 badcase 快照捕获与回放器(统计级复现)
# 真实场景:请求快照(messages/参数/工具结果/模型版本)入库;回放 N 次看行为分布
from __future__ import annotations
import random
from dataclasses import dataclass, field


@dataclass
class Snapshot:
    messages: list[dict]
    temperature: float
    model_version: str
    tool_results: dict[str, str] = field(default_factory=dict)   # 冻结的工具快照
    seed: int | None = None


@dataclass
class ReplayReport:
    outputs: list[str]

    def distinct(self) -> int:
        return len(set(self.outputs))

    def majority(self) -> str:
        return max(set(self.outputs), key=self.outputs.count)


class BadcaseStore:
    """badcase 入库:完整快照(缺任何一维都可能导致复现失败)。"""

    def __init__(self) -> None:
        self.cases: list[Snapshot] = []

    def capture(self, snap: Snapshot) -> int:
        assert snap.model_version, "缺模型版本:供应商静默更新会让回放失真"
        assert snap.tool_results is not None, "缺工具/检索快照:时间敏感数据变了无法复现"
        self.cases.append(snap)
        return len(self.cases) - 1


def replay(snap: Snapshot, provider, n: int = 5) -> ReplayReport:
    """回放 N 次:目标是统计级复现(行为分布),不是单条 bit 级一致。"""
    outputs = []
    for i in range(n):
        # 供应商模拟:温度>0 有采样随机性;温度 0 仍有路由级微小差异
        noise = 0.0 if snap.temperature == 0 else random.Random(i).random() * 0.3
        flip = (snap.seed is None and noise > 0.25)      # 无种子时偶发行为漂移
        outputs.append(provider(snap, flip))
    return ReplayReport(outputs)


def mock_provider(snap: Snapshot, flip: bool) -> str:
    base = "结构化JSON输出"
    return base + ("(漂移版)" if flip else "")


def demo() -> None:
    store = BadcaseStore()
    snap = Snapshot(
        messages=[{"role": "user", "content": "把这段话总结成JSON"}],
        temperature=0.7, model_version="gpt-x-2026-03",
        tool_results={"search:合同条款": "v123 快照内容"},   # 冻结检索快照
        seed=42,
    )
    idx = store.capture(snap)
    print(f"badcase #{idx} 入库:快照含 messages/温度/模型版本/工具冻结快照 ✅")

    rep = replay(store.cases[idx], mock_provider, n=5)
    print(f"带种子回放 5 次:distinct={rep.distinct()} 多数输出={rep.majority()} ✅")
    assert rep.distinct() == 1

    unstable = Snapshot(messages=snap.messages, temperature=0.7,
                        model_version=snap.model_version, seed=None)
    rep2 = replay(unstable, mock_provider, n=20)
    print(f"无种子回放 20 次:distinct={rep2.distinct()} -> "
          "统计级复现看行为分布而非单条一致 ✅")

    print("纪律:时间敏感工具结果必须冻结在快照里——重取真实数据复现的是'今天的答案' ✅")


if __name__ == "__main__":
    demo()
```

**追问一**：回放器的成本怎么控制？
答：重放 N 次是 N 倍 token 成本——分层回放：新 badcase 先 N=3 快筛，进入回归集的按"高危高频"分层抽放（每周固定预算）；温度 0 + 种子支持时 N=1-3 即可判定，非确定场景才需要 N≥10 的分布统计。

**追问二**：修复发布后怎么证明"这个 badcase 修好了"？
答：三证齐全——回放分布收敛（漂移率降到阈值下）、黄金集回归无回退（修复没有破坏其他行为）、线上监控该模式再发率下降（7 天窗口）；"重跑一次没问题"不构成任何证据。

## 背诵要点
- 可重现三元组：输入快照（含冻结工具/检索结果）+ 采样参数 + 模型版本；目标是统计级复现（N 次重放看分布）。
- 温度 0 也有非确定性（batch 浮点顺序/MoE 路由/实例路由）；时间敏感上下文必须冻结，重取=复现"今天的答案"。
- badcase 闭环：快照入库 → 回放器分层预算 → 修复后作为回归集；"重跑没问题"不是证据。

## 复盘追问
- 供应商换了模型版本导致历史快照无法回放，回归集怎么办？（提示：快照标注版本可复现性、不可复现样本转入"行为等价性重生成"流程（用新版本重新标注期望），并推动供应商提供版本 pin 能力）
- 回放分布显示 30% 漂移率但都"不算错"，这算 bug 吗？（提示：按行为契约判定——格式/安全/关键事实约束违约才算 bug；风格漂移记为噪声并纳入温度/种子治理决策）
