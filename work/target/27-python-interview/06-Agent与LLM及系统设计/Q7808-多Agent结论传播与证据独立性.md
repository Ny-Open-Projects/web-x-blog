---
title: "[Q7808] 多 Agent 的结论传播：三个 Agent 点头为什么等于一个人点头"
date: 2026-11-25
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7808 · 多 Agent 的结论传播：三个 Agent 点头为什么等于一个人点头

难度：P7 ｜ 标签：多 Agent、证据独立性、置信度聚合、provenance、noisy-OR

基线：库知识库外知识卡，用 noisy-OR 与"共享根因"分组模拟多 Agent 置信度聚合的相关性偏差。

**问**：一个投研多 Agent 系统：分析 Agent 给出"看多"置信度 0.6，两个复核 Agent 各自独立复核后给出 0.9，聚合器按 noisy-OR 算到 0.996，直接触发高置信交易建议。事后复盘发现两个复核 Agent 读的是**同一份**分析 Agent 的摘要，并没有独立证据。三个 0.9 为什么不能当三个独立信号？多 Agent 的置信度该怎么聚合？

**答**：

- **结论**：置信度聚合的前提是**证据独立**。两个复核 Agent 的输入都来自同一份摘要/同一批检索结果，它们的"确认"是**相关证据**，不是独立证据；noisy-OR 把它们当独立事件相乘，等于把同一份证据算了三遍，置信度虚高。多 Agent 系统最常见的假独立：共享上下文、共享检索结果、共享上游结论、同一个基座模型（同一种系统性偏差）。聚合前必须做 **provenance 归并**：按 `derived_from` 找到证据根因，同一根因只计一次，或按相关系数折减。
- **取舍**：① 按根因去重后聚合：最保守，能防虚高，但可能低估"多个独立来源确实一致"的强信号；② 保留相关性折扣：`effective_p = 1 - (1-p)^(1/ρ)`，ρ 是有效独立源数，需要估计；③ 要求独立证据：每个 Agent 必须给出"我看了哪些不同来源"，没有独立来源就不计入；④ 只取最高置信度：最简单，但浪费了多源信息。
- **实战**：① 每条结论带 `evidence_ids`（检索文档/工具结果/数据快照），聚合前按证据集合做分组；② 同组内取最大置信度，不同组之间才做 noisy-OR；③ 显式标注"共享上下文"，让聚合器知道哪些 Agent 不独立；④ 高风险决策不只看聚合置信度，还要看"独立证据数"与"反方证据数"；⑤ 回测时对比"聚合置信度"与"实际命中率"的校准曲线，虚高会直接现形。

下面用 noisy-OR 对比：三个 0.9 当独立 → 0.999；识别共享根因后只计一次 → 0.9；再加上分析 Agent 的 0.6 → 0.96 而不是 0.999。

```python
# 置信度聚合: noisy-OR 假设独立; 共享根因必须先按证据分组
def noisy_or(ps):
    prod = 1.0
    for p in ps:
        prod *= (1 - p)
    return 1 - prod


# 三个 Agent 都基于同一份摘要: 不是三个独立证据
naive = noisy_or([0.6, 0.9, 0.9])
print(f"[1] 当独立信号聚合: {naive:.3f}")
assert naive > 0.99
print("    → 实测 同一份证据被算三遍, 置信度冲到 0.996")

# provenance 归并: 按 derived_from 分组, 同组取最大
agents = [
    {"name": "analyst", "p": 0.6, "derived_from": "doc_A"},
    {"name": "reviewer_1", "p": 0.9, "derived_from": "doc_A"},
    {"name": "reviewer_2", "p": 0.9, "derived_from": "doc_A"},
]
groups = {}
for a in agents:
    groups.setdefault(a["derived_from"], []).append(a["p"])
group_scores = [max(ps) for ps in groups.values()]
gated = noisy_or(group_scores)
print(f"[2] 按证据根因归并: 组={ {k: max(v) for k, v in groups.items()} }, 聚合={gated:.3f}")
assert abs(gated - 0.9) < 1e-9

# 真正独立的多源: 两个不同文档各自 0.6/0.7, 才适合 noisy-OR
independent = noisy_or([0.6, 0.7])
print(f"[3] 两个独立来源 0.6/0.7 -> {independent:.3f}")
assert 0.85 < independent < 0.9

# 相关性折扣: 部分共享时用有效独立源数 rho
def correlated_or(ps, rho):
    return 1 - (1 - max(ps)) ** (len(ps) / rho)


print(f"[4] 3 个 0.9, rho=1(独立) -> {correlated_or([0.9]*3, 1):.3f}; "
      f"rho=3(完全相关) -> {correlated_or([0.9]*3, 3):.3f}")
assert correlated_or([0.9] * 3, 1) > 0.99
assert abs(correlated_or([0.9] * 3, 3) - 0.9) < 1e-9

# 决策不能只看置信度: 独立证据数 + 反方证据
decision = {
    "confidence": gated,
    "independent_sources": len(groups),
    "counter_evidence": 1,
}
print(f"[5] 决策输入: {decision}")
assert decision["independent_sources"] == 1 and decision["counter_evidence"] > 0
print("    → 实测 一个独立来源 + 反向证据, 不应触发高置信动作; 置信度必须和证据结构一起看")
```

**追问一**：怎么判断两个 Agent 是否"独立"？—— 看证据链，不看 Agent 名字。如果它们的输入都来自同一批检索文档、同一份上游摘要、同一个数据库快照，就是相关；如果走了不同的数据源、不同的检索 query、不同的工具，才算独立。最实用的做法是让每个结论强制带 `evidence_ids`，按集合交集判断，而不是靠人工声明"我们是独立的"。

**追问二**：同基座模型的不同角色，算独立吗？—— 不算。同一模型的不同 prompt 会共享训练偏差与幻觉模式：一个把"营收增长"读成"利润增长"，另一个很可能犯同样的错。模型多样性（不同厂商/不同规模）比角色多样性更能提供独立信号，但成本更高。至少要意识到"三个角色"不等于"三个证据"。

## 背诵要点

- 置信度聚合的前提是证据独立；共享上下文/检索结果/上游结论会让 noisy-OR 把同一证据算多遍，虚高到 0.99+。
- 按 `evidence_ids`/`derived_from` 分组，同组取最大，跨组才 noisy-OR；部分相关用有效独立源数 ρ 折扣。
- 高风险决策看"独立证据数 + 反方证据"，不能只看聚合置信度；同基座模型的不同角色不算独立。

## 复盘追问

- 如果两个 Agent 的证据集合部分重叠（共享 3 篇、各自独有 2 篇），该怎样分组/折扣？
- 怎样用回测校准"聚合置信度"与真实命中率？校准曲线虚高说明什么？
