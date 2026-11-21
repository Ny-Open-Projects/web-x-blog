---
title: [Q248] Agent 辩论模式如何提升质量
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q248 · Agent 辩论模式如何提升质量

> 难度:★★★ | 标签:Agent, 多Agent

**问**:多 Agent 辩论为什么能减少错误?代价是什么?

**答**:辩论模式让多个 Agent 独立作答,再互相看到对方的答案进行批驳或修正,迭代若干轮后由裁判(或投票)取收敛结论。它有效的原理:独立作答的错误往往不同,互相挑错相当于引入了"交叉验证",也能暴露单个 Agent 的思考盲区。代价:每轮成本 = Agent 数 × 轮数倍增,延迟同步放大,一般只用于高风险决策(审核、重要推理)。判据:答案收敛才停,否则到最大轮数取裁判裁决。

```python
# file: code/06_Agent与LLM及系统设计/q248_debate.py
"""辩论模式:三个 Agent 独立作答、互相批驳并修订答案,裁判按收敛度裁决。"""
from collections import Counter


class Debater:
    def __init__(self, name, answer, policy):
        self.name, self.answer, self.policy = name, answer, policy

    def revise(self, others: list[str]) -> str:
        """看到对方答案后按策略修订自己的结论(真实场景由 LLM 完成)。"""
        self.answer = self.policy(others)
        return self.answer


def run_debate(debaters: list[Debater], judge, max_rounds: int = 3):
    for round_no in range(1, max_rounds + 1):
        for d in debaters:
            others = [x.answer for x in debaters if x is not d]
            print(f"  第{round_no}轮 {d.name} 修订为:{d.revise(others)}")
        votes = Counter(d.answer for d in debaters)
        if votes.most_common(1)[0][1] == len(debaters):
            print(f"  第{round_no}轮 全体收敛,提前结束")
            break
    return judge({d.name: d.answer for d in debaters})


def judge(answers: dict) -> str:
    return f"多数派结论:{Counter(answers.values()).most_common(1)[0][0]}"


if __name__ == "__main__":
    ds = [Debater("A", "方案1", lambda o: "方案1"),
          Debater("B", "方案1", lambda o: "方案1"),
          Debater("C", "方案2", lambda o: "方案1" if o.count("方案1") >= 2 else "方案2")]
    print(run_debate(ds, judge))
```

**追问**:
- 裁判模型的位置偏差是什么?——倾向选第一个/最后一个答案;缓解:交换顺序评两次、双评委取一致。
- 收敛判据怎么定?——语义相似度阈值或评委一致性;到上限仍不收敛取多数/裁判,并记录为「低置信」样本回流。
- 辩论和 ensemble 的区别?——ensemble 聚合独立答案(投票),辩论引入交互式批驳;后者能修正推理过程,前者只聚合结论。
