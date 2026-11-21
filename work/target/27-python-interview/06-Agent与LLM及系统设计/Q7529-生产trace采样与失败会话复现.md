---
title: [Q7529] 生产 trace 采样与失败会话复现
date: 2026-11-20
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7529 · 失败会话复现：从生产 trace 重建一次 Agent 任务的完整执行

> 难度:★★★★ | 标签:Agent, 可观测性, 复现

**问**：线上 Agent 任务失败，用户只报了"结果不对"。如何用生产 trace 在测试环境重建这次执行（同输入、同工具响应），把 bug 复现出来？全量 trace 存不起，采样怎么设计？

**答**：结论：可复现的前提是 trace 记录了**重建所需的最小完备集**：每步的输入快照（prompt 组装结果全文）、工具响应全文、随机种子、模型/工具版本号。复现 = 按序回放这些输入——模型响应用录制回放（或重调真模型验证行为），工具响应用录制桩，整链在测试环境重跑并 diff 每步输出与生产 trace 的差异。采样策略决定"想复现时有没有货"：失败任务全量保、成功任务按流量采（1-5%）、金样本永久保；配合 TTL 分层（7 天热、90 天冷、金样本永久）控制成本。

机理与实战：
- 完备性检查是关键工程点：trace 落盘时跑一遍"重建校验"——按 trace 逐字段核对是否存在缺失（工具响应截断、prompt 快照缺失、版本号缺），缺则标 `replayable=false`。没有这个闸门，采样保下来的 trace 一半不可复现，出了事故才发现白存。
- 非确定性的驯服：重跑要 diff 的是"逻辑路径"（步骤序列、工具调用参数、状态转移）而不是逐字节响应（模型温度下响应必然漂移）。diff 口径按 step kind 分层：工具调用参数用归一化指纹比对，模型输出用语义层（抽取的结构化字段）比对。漂移大但路径一致 = 行为类问题，转评估归因。
- 复现产物的归属：复现会话应能一键升级为评估集条目（输入 + 期望输出入库），这是 badcase → 标注 → 回归闭环的管道入口；复现不闭环进评估集，排障的价值只停留在单次救火。

```python
# 基线:Python 3.9+ 纯标准库 ;演示 trace 完备性闸门与重放 diff
import re
from dataclasses import dataclass, field


@dataclass
class StepRecord:
    seq: int
    kind: str                     # model_call / tool_call
    input_snapshot: str | None = None
    output_snapshot: str | None = None
    version: str | None = None
    replayable: bool = True


def completeness_gate(trace: list[StepRecord]) -> list[str]:
    """落盘前重建校验:缺任一快照/版本即标不可复现。"""
    problems = []
    for s in trace:
        missing = [k for k in ("input_snapshot", "output_snapshot", "version")
                   if getattr(s, k) is None]
        if missing:
            s.replayable = False
            problems.append(f"step{s.seq}({s.kind}) 缺 {missing}")
    return problems


def norm_fp(s: str | None) -> str:
    if s is None:
        return ""
    s = re.sub(r"\d{4}-\d{2}-\d{2}T[\d:]+", "<TS>", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def replay_diff(prod: list[StepRecord], replayed: list[StepRecord]) -> list[str]:
    """重放 diff:只比逻辑路径(指纹),不比逐字节响应。"""
    issues = []
    for p, r in zip(prod, replayed):
        if p.kind != r.kind:
            issues.append(f"step{p.seq} 路径分叉: {p.kind} vs {r.kind}")
            break
        if norm_fp(p.output_snapshot) != norm_fp(r.output_snapshot):
            issues.append(f"step{p.seq}({p.kind}) 输出语义漂移,转评估归因")
    return issues


def main() -> None:
    prod = [
        StepRecord(0, "model_call", "plan prompt 2026-01-01T10:00", "调用 search",
                   "gpt-x-2026-01"),
        StepRecord(1, "tool_call", "search: kw", "3 条结果", "tool-v5"),
        StepRecord(2, "tool_call", "export: {order}", None, "tool-v5"),  # 截断丢失
    ]
    print("完备性闸门:", completeness_gate(prod))
    print("step2 可复现:", prod[2].replayable)

    ok_prod = [StepRecord(0, "model_call", "p", "调用 search", "v1"),
               StepRecord(1, "tool_call", "kw", "3 条结果", "v1")]
    replayed = [StepRecord(0, "model_call", "p", "调用 search 工具", "v1"),
                StepRecord(1, "tool_call", "kw", "3 条结果", "v1")]
    print("重放 diff:", replay_diff(ok_prod, replayed))


if __name__ == "__main__":
    main()
```

**追问一**：prompt 快照存全文成本高，能不能只存模板 + 变量？
答：能，且推荐——快照存 (template_id + 版本 + 变量 dict)，重建时本地渲染。前提是模板版本化管理严格（模板删除要延迟到所有引用 trace 过期之后），否则老 trace 无法重建。全文快照只给金样本与失败高价值样本。

**追问二**：重跑时真模型响应与生产必然不同，"复现"还成立吗？
答：复现的目标分两层：确定层（编排逻辑、工具行为、schema 解析）必须逐位一致，漂移即 bug；生成层（模型文本）只要求语义一致，漂移转评估。工程上先把确定层跑成可复现，这层通常就覆盖了 80% 的线上故障（工具版本变化、上下文组装错、缓存污染）。

**背诵要点**：
- 可复现最小集：每步输入/输出快照（模板+变量优先）+ 随机种子 + 版本号。
- 采样分层：失败全量、成功 1-5%、金样本永久，落盘前跑完备性闸门标 replayable。
- 重放 diff 按层分治：确定层逐位比，生成层比语义指纹。

**复盘追问**：
- 模板删除与 trace 保留期的冲突如何用"引用计数过期"策略解决？
- 复现会话升级为评估集条目的准入标准是什么？

## 背诵要点
- 完备性闸门让采样存储不变成"不可复现的废料堆"。
- 工具版本号是常被漏记的复现关键：工具升级会让老 trace 不可重建。
- badcase → 复现 → 评估集的闭环是排障价值的放大器。

## 复盘追问
- 冷热分层的存储成本模型（元数据/全文/金样本三档单价）怎么估？
- 如何在压测流量里自动注入"可复现采样标记"验证链路？
