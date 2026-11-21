---
title: [Q1753] Agent 执行轨迹折叠:近详远略台账
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1753 · Agent 执行轨迹折叠:近详远略台账

> 难度:★★★☆ | 标签:Agent, 轨迹压缩, 上下文

**问**:Agent 跑了几十步,每步的工具结果都要进上下文,越跑越胖,怎么压?

**答**:轨迹压缩用近详远略:最近 N 步保留完整原文,包括完整工具结果,因为模型正在基于它们推理;更早的步骤折叠成一行台账,只留步骤号、动作、参数和"已完成"标记,因为旧结果的信息已经被后续步骤消化。折叠后如果还超预算,再从最旧的台账行开始逐行丢弃,而最近 N 步永不折叠——牺牲最旧信息保最新推理材料。每一级都可独立验证:折了几行、保了几步、最终 token 数,全部进报告可断言。

```python
# file: code/06_Agent与LLM及系统设计/q1753_trajectory_fold.py
"""Agent 轨迹折叠:近 N 步保留原文,更早步骤折叠为一行台账,超预算再丢最旧行。"""
import json


def est_tokens(text):
    return max(1, len(text) // 2)            # 演示用粗估:2 字符 1 token


class TrajectoryFolder:
    """近详远略:verbatim 保留最近 keep_recent 步,旧步骤折叠成单行台账。"""

    def __init__(self, keep_recent=3, budget=10 ** 9):
        self.keep_recent = keep_recent
        self.budget = budget

    def fold(self, steps):
        """steps: [{action, args, result}] 按时间序,返回 (折叠文本, 报告)。"""
        old, recent = steps[:-self.keep_recent], steps[-self.keep_recent:]
        ledger = []
        for i, s in enumerate(old, 1):
            args = ",".join("%s=%s" % kv for kv in s["args"].items())
            ledger.append("步骤%d %s(%s) -> 已完成" % (i, s["action"], args))
        recent_text = [json.dumps(s, ensure_ascii=False) for s in recent]
        while ledger and est_tokens("\n".join(ledger + recent_text)) > self.budget:
            ledger = ledger[1:]                  # 超预算:从最旧的台账行开始丢
        text = "\n".join(ledger + recent_text)
        return text, {"ledger_lines": len(ledger), "verbatim_steps": len(recent)}


if __name__ == "__main__":
    steps = [{"action": "search", "args": {"q": "q%d" % i},
              "result": "结果" * 10} for i in range(8)]

    text, rep = TrajectoryFolder(keep_recent=3).fold(steps)
    assert rep == {"ledger_lines": 5, "verbatim_steps": 3}
    assert "步骤1 search(q=q0) -> 已完成" in text, "旧步骤折叠为台账行"
    assert '"result"' in text, "近 3 步保留完整工具结果"

    text2, rep2 = TrajectoryFolder(keep_recent=3, budget=130).fold(steps)
    assert rep2["ledger_lines"] < rep["ledger_lines"], "超预算时台账逐行丢弃"
    assert rep2["verbatim_steps"] == 3, "最近步骤永不折叠"
    assert est_tokens(text2) <= 130
    print("轨迹折叠通过:5 行台账加 3 步原文,紧预算再丢最旧行,近端永不折叠")
```

**追问**:
- 为什么不把最近几步也摘要掉? 答:最近几步的工具结果是模型当前推理的直接依据,摘要会丢数值与引用,宁丢旧不丢新。
- 台账和对话摘要的关系? 答:台账管工具步骤,对话摘要管自然语言轮次,两者通常在上下文装配器里各占一段预算。
