---
title: [Q1203] 多 Agent 结果聚合:投票与加权
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1203 · 多 Agent 结果聚合:投票与加权

> 难度:★★★☆ | 标签:多 Agent, 可靠性

**问**:三个 Agent 给出不同答案,怎么聚合出最终结论?

**答**:聚合按任务类型选:分类/选择题用多数投票,数值估算用中位数(抗离群),开放生成用 LLM-as-Judge 或"修正-再共识"(把分歧点抛回给 Agent 二轮)。加权投票:权重来自历史准确率或本次置信度。关键工程点:投票要求问题可判等(答案先规范化再比较,"北京/北京市"要归一);平票时不要随机,升级人工或追加一轮带分歧信息的讨论;全员一致的答案也别全信,可能是共同的系统性偏差,抽样人审校准。

```python
# file: code/06_Agent与LLM及系统设计/q1203_result_aggregation.py
"""结果聚合:规范化 + 多数投票/中位数 + 置信度加权 + 平票升级。"""
import statistics


def normalize(ans):
    alias = {"北京市": "北京", "beijing": "北京"}
    return alias.get(ans.strip().lower(), ans.strip())


def majority_vote(answers, weights=None):
    norm = [normalize(a) for a in answers]
    tally = {}
    for a in norm:
        tally[a] = tally.get(a, 0) + 1
    top = max(tally.values())
    winners = [a for a, n in tally.items() if n == top]
    if len(winners) > 1:
        return None, "tie", tally
    return winners[0], "majority", tally


def weighted_vote(answers, confidences):
    tally = {}
    for a, c in zip(answers, confidences):
        tally[normalize(a)] = tally.get(normalize(a), 0) + c
    return max(tally.items(), key=lambda x: x[1])


def aggregate_numeric(values):
    return statistics.median(values)


if __name__ == "__main__":
    # 分类任务:多数投票
    ans = ["北京", "北京市", "上海"]
    result, mode, tally = majority_vote(ans)
    print("投票:", result, mode, tally)
    assert result == "北京", "归一化后北京 2 票胜出"

    # 平票升级
    r2, mode2, _ = majority_vote(["北京", "上海", "北京", "上海"][:3] + ["上海"])
    r2, mode2, _ = majority_vote(["北京", "上海", "广州"])
    assert r2 is None and mode2 == "tie"
    print("平票 -> 升级人工或追加讨论,不随机选")

    # 置信度加权:低置信高票被高置信拉回
    w = weighted_vote(["A", "B", "A"], [0.4, 0.95, 0.4])
    print("加权:", w)
    assert w[0] == "B", "置信度加权纠正低置信多数"

    # 数值聚合:中位数抗离群
    assert aggregate_numeric([10, 12, 11, 100]) == 11.5
    print("离群值 100 被中位数抑制")
```

**追问**:
- Agent 间答案相关性强(都看了同一份材料)投票还有效吗?答:有效性骤降——投票假设独立性,同源材料会导致"共识假象",应让各 Agent 用不同检索源或温度/视角,保持多样性再投票。
- 二轮共识怎么设计?答:把分歧点与各自理由拼成新 prompt 再答一轮,通常 1 轮内收敛;两轮仍分歧说明问题歧义,直接转人工。
