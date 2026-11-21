---
title: [Q7522] Agent 工具调用链 trace 与失败归因
date: 2026-11-20
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7522 · Agent 工具调用链 trace 与失败归因：一次失败任务怎么在 5 分钟内定位？

> 难度:★★★★ | 标签:Agent, 可观测性, trace

**问**：Agent 执行一次任务要调 12 次工具、2 次模型，线上报障"结果不对但不知道哪步错的"。Agent 系统的 trace 该记什么？失败归因怎么从"人工翻日志"变成"结构化定位"？

**答**：结论：Agent trace 的最小单元不是"请求"，而是**步骤（step）**——每次模型调用（含完整 prompt 快照、token 用量、耗时）与每次工具调用（入参、出参、错误、重试次数）都记一个带序号的 span，串在 task_id 下。失败归因的关键是把失败**分类**：模型层（幻觉、超长截断、schema 解析失败）、工具层（超时、权限拒绝、返回格式变化）、编排层（步数熔断、取消）。每类失败有独立的计数指标，报警时直接给出"哪一类、第几步"，定位从翻日志变成看分布。

机理与实战：
- trace 记录的字段纪律：prompt/响应全文另存对象存储，span 里放引用与哈希——既支持事后复盘，又不让 trace 存储被大文本打爆。工具入参要脱敏后再记录（凭证字段掩码），否则 trace 系统自己变成敏感数据泄露面。
- 归因的结构化实现：每个 step 记 `step_kind`（model_call/tool_call/decision）、`outcome`（ok/retryable_failed/fatal）、`error_class`（枚举而非自由文本）。自由文本错误日志没法聚合，枚举才能出"今天 40% 失败集中在 payment_tool 超时"这种可行动结论。
- 金样本对比：把成功任务的 trace 序列作为"金样本"，失败任务 trace 与之 diff（第一次分叉的步骤就是归因起点），这是从"人工看"到"机器定位"的跃迁。

```python
# 基线:Python 3.9+ 纯标准库 ;演示 step 级 trace 记录与失败归因 diff
import hashlib
import json
import time
from dataclasses import dataclass, field, asdict


@dataclass
class Step:
    seq: int
    kind: str                    # model_call / tool_call
    name: str
    outcome: str = "ok"          # ok / retryable_failed / fatal
    error_class: str | None = None   # timeout / schema_parse / permission ...
    duration_ms: int = 0
    payload_hash: str = ""       # 大文本存哈希,全文外置


class TaskTrace:
    def __init__(self, task_id: str) -> None:
        self.task_id = task_id
        self.steps: list[Step] = []

    def record(self, kind: str, name: str, outcome: str = "ok",
               error_class: str | None = None, duration_ms: int = 0,
               payload: dict | None = None) -> Step:
        h = hashlib.sha256(json.dumps(payload, sort_keys=True,
                                      ensure_ascii=False).encode()).hexdigest()[:12] if payload else ""
        s = Step(len(self.steps), kind, name, outcome,
                 error_class, duration_ms, h)
        self.steps.append(s)
        return s

    def attribute_failure(self) -> str:
        """归因:找第一个非 ok 步骤,按 error_class 映射到层。"""
        LAYER = {"timeout": "工具层", "schema_parse": "模型层",
                 "permission": "工具层", "max_steps": "编排层"}
        for s in self.steps:
            if s.outcome != "ok":
                return f"第{s.seq}步 {s.name}: {LAYER.get(s.error_class, '未知')}失败({s.error_class})"
        return "无失败步骤(结果质量类问题,转评估归因)"


def golden_diff(task: TaskTrace, golden: list[str]) -> str | None:
    """与金样本序列 diff,返回第一次分叉的步骤名。"""
    for s, g in zip(task.steps, golden):
        if s.name != g:
            return f"第{s.seq}步分叉: 期望 {g} 实际 {s.name}"
    if len(task.steps) < len(golden):
        return f"序列中断: 金样本还需 {golden[len(task.steps):]},实际在第{len(task.steps)}步终止"
    if len(task.steps) > len(golden):
        extra = [s.name for s in task.steps[len(golden):]]
        return f"多余步骤: {extra}"
    return None


def main() -> None:
    golden = ["plan", "search_doc", "payment_tool", "compose"]
    t = TaskTrace("t-1001")
    t.record("model_call", "plan", duration_ms=800, payload={"p": "plan prompt"})
    t.record("tool_call", "search_doc", duration_ms=120, payload={"q": "keyword"})
    t.record("tool_call", "payment_tool", outcome="fatal", error_class="timeout",
             duration_ms=5000, payload={"req": "pay req"})
    print("失败归因:", t.attribute_failure())
    print("金样本分叉:", golden_diff(t, golden))
    # 指标聚合口径:按 error_class 计数才能出分布
    from collections import Counter
    print("错误类分布:", dict(Counter(s.error_class for s in t.steps if s.outcome != "ok")))


if __name__ == "__main__":
    main()
```

**追问一**：模型层失败里"幻觉导致调错工具"怎么归因？它 error_class 该是什么？
答：这类失败在 trace 里表现为"步骤成功但结果错"，静态归因抓不到。两层补救：运行时校验（工具入参 schema + 业务规则校验，把"调错"转化为显式 schema_parse/invalid_params 失败类）；离线评估用标注集判定幻觉率，与 trace 关联（badcase 入库）。原则：能运行时显式化的失败绝不留在"结果不对"这种模糊类里。

**追问二**：trace 的采样策略怎么定？全量存成本高不高？
答：模型调用占比成本大头的是 prompt 全文，span 元数据本身很便宜。策略：元数据全量（支持聚合与报警），全文按"失败 100% + 成功采样 5%"存对象存储；金样本任务的 trace 永久保留。存储预算按"每任务平均 20 步 × 1KB 元数据"估，单日 10 万任务约 2GB 元数据，可行。

**背诵要点**：
- trace 单元是 step（model_call/tool_call），大文本外置只存哈希与引用。
- 失败归因 = error_class 枚举 + 第一分叉定位 + 金样本 diff，拒绝自由文本。
- 元数据全量、全文按失败 100%/成功 5% 采样，金样本永久保留。

**复盘追问**：
- 工具入参脱敏在 trace 层怎么实现才不会破坏"复盘时能看懂上下文"？
- 跨多轮会话的 task_id 串联怎么做（会话级与任务级两层 trace）？

## 背诵要点
- 归因三层：模型层（解析/幻觉）、工具层（超时/权限）、编排层（熔断/取消）。
- 运行时显式化失败（schema 校验）优先于离线归因。
- 指标必须按枚举聚合，分布结论（哪类失败占比）才是可行动的。

## 复盘追问
- "结果不对但每步都 ok"的任务，如何用评估集自动归因到具体 prompt 环节？
- trace 元数据 schema 演进（加字段）如何兼容旧数据查询？
