---
title: "[Q7575] 工具结果压缩的 token 成本账"
date: 2026-11-20
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7575 · 工具结果压缩与摘要的 token 成本账

难度：P6 ｜ 标签：成本工程 / Agent / token / 工具结果

**问**：Agent 每轮把工具返回的整页 JSON/HTML 塞进上下文，单会话成本 0.8 美元，其中 70% 是工具结果 token。怎么设计"结果瘦身"并用账本验证收益与质量代价？

**答**：

**结论**：工具结果膨胀是 Agent 成本第一大头，且是多轮复利——每轮历史都带着之前所有工具结果，第 n 轮的成本随轮数平方级增长。瘦身四法按性价比排序：① 字段裁剪（工具返回只取任务需要的字段，schema 级裁剪零质量损失）；② 结构化摘要（大文本交给便宜模型摘要成要点 + 引用 ID，需要细节时按 ID 取原文）；③ 分页/截断加"还有更多"信号（Agent 决定要不要翻页，而不是一次吞下 500 行）；④ 历史压缩（前轮工具结果在后续轮替换为摘要占位符）。质量风险集中在摘要层：丢了关键细节会导致下游步数增多（重试/重复调用），总成本可能不降反升——所以必须用"端到端账"评估：成本 + 任务成功率 + 步数，不是单看 token 数。

**取舍**：压缩率与质量是滑杆：字段裁剪和分页几乎无质量代价（优先做满）；摘要压缩率最高（80-90%）但引入信息损失与一次额外 LLM 调用成本。决策依据是"结果在后续步骤被精确引用的概率"：代码执行结果、检索评分要精确值 → 不摘要；网页正文、日志 → 摘要。另一个账：历史压缩让第 n 轮成本从平方级回到近似线性，这是长期会话唯一有效的成本曲线改写。

**实战**：实现要点：瘦身放在工具执行层统一收口（工具注册时声明 result_policy：whitelist 字段/max bytes/摘要器），业务代码零改动；摘要调用用便宜模型 + 短超时，摘要失败降级为截断不阻塞主流程。账本追踪三个维度：每步 input/output token、瘦身前后对比、任务级成本分布（P50/P95），上线用 A/B：瘦身组 vs 对照组比端到端成本与成功率。

```python
# 工具结果瘦身账：多轮成本平方级 → 线性化的模拟
# 仅标准库，Python 3.9+
from __future__ import annotations


def session_cost(tool_result_tokens: int, turns: int,
                 overhead_tokens: int = 500, price_per_1k: float = 0.003) -> float:
    """每轮 = overhead + 累积的所有历史工具结果（无瘦身）。"""
    total = 0
    for t in range(1, turns + 1):
        ctx = overhead_tokens + (t - 1) * tool_result_tokens  # 历史累积
        total += ctx + tool_result_tokens
    return total * price_per_1k / 1000


def session_cost_compressed(tool_result_tokens: int, turns: int,
                            summary_tokens: int = 80,
                            overhead_tokens: int = 500,
                            price_per_1k: float = 0.003) -> float:
    """历史里的工具结果被替换为摘要占位符 + 一次摘要调用成本。"""
    total = 0
    for t in range(1, turns + 1):
        ctx = overhead_tokens + (t - 1) * summary_tokens
        total += ctx + tool_result_tokens
    total += turns * (200 + summary_tokens)  # 摘要调用（便宜模型）
    return total * price_per_1k / 1000


def main() -> None:
    cost_raw = session_cost(3000, 12)
    cost_cmp = session_cost_compressed(3000, 12)
    print(f"裸奔 12 轮: ${cost_raw:.3f} / 摘要瘦身: ${cost_cmp:.3f} "
          f"(省 {1 - cost_cmp / cost_raw:.0%})")
    assert cost_cmp < cost_raw * 0.5

    # 轮数敏感：40 轮长会话差距拉大（平方 vs 近线性）
    r40 = session_cost(3000, 40) / session_cost_compressed(3000, 40)
    r12 = cost_raw / cost_cmp
    print(f"12 轮省 {r12:.1f}x，40 轮省 {r40:.1f}x → 越长收益越大")
    assert r40 > r12

    # 质量守门：精确引用场景不做摘要（评分、代码结果）
    NO_SUMMARY = {"eval_score", "code_output"}
    assert "eval_score" in NO_SUMMARY
    print("结论：瘦身分层——字段裁剪/分页无脑做，摘要只用于低引用概率结果")


if __name__ == "__main__":
    main()
```

**追问链**：

- 追问 1：为什么无瘦身时成本随轮数平方增长？——第 t 轮的上下文包含前 t-1 轮所有工具结果，单轮成本线性涨、总成本求和即平方级；摘要把历史项压成常数 → 总成本近似线性。这是长会话 Agent 成本优化的核心公式。
- 追问 1.1：摘要失败降级为截断，截断的风险？——截断可能砍掉结果末尾的关键字段（JSON 尾部的状态/错误码），Agent 拿到半截数据继续推理产生错误结论；降级截断要保结构（JSON 按 schema 截数组保标量、文本按段落截）并给 Agent "truncated" 信号。
- 追问 2：A/B 验证瘦身时，"步数增多抵消 token 节省"怎么量化？——任务级账：总 token、总步数、成功率三指标同看；定义"成本效率 = 成功率 / 任务成本"，若瘦身组成功率跌 3% 而成本省 50%，多数业务仍划算；若步数涨 40% 导致成本只省 10%，就不值。

**背诵要点**：

1. 工具结果未瘦身时成本随轮数平方增长；历史摘要化让曲线回线性，长会话收益 2-5 倍。
2. 瘦身四法按性价比：schema 字段裁剪 > 分页截断带信号 > 摘要（低引用概率结果专用）> 历史占位压缩。
3. 评估用端到端账（成本+成功率+步数），摘要截断必须保结构并给 truncated 信号，瘦身统一收口在工具执行层。

**复盘追问**：

1. 上线瘦身 3 个月后某类任务成功率悄悄跌了 2%，你怎么定位是摘要丢了哪类信息？
2. 便宜模型摘要本身引入的延迟与失败率，如何在账里定价？
