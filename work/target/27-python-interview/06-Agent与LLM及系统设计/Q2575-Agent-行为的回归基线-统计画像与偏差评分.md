---
title: [Q2575] Agent 行为的回归基线:统计画像与偏差评分
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2575 · Agent 行为的回归基线:统计画像与偏差评分

> 难度:★★★★ | 标签:Agent, 测试, 回归

**问**:端到端断言只能抓确定性错误,LLM 输出带随机性,回归怎么抓"没坏但变了"?

**答**:统计画像基线的思路是不比文本比行为:记录一组正常运行的画像——步数分布、各工具调用频次、状态计数,取均值和标准差。新版本跑同一批种子,算每个指标偏离基线的程度,任何一项超过阈值就告警,阈值常用两三个标准差起步再按误报率调。它抓得住端到端断言抓不住的问题:某工具调用频率翻倍、步数普遍变长,输出可能都对,但成本和时延已经劣化。画像维度要选行为学稳定的量,别放会随正常波动剧烈变化的指标。基线本身要版本化:升级 prompt 或模型后画像重录并审批,否则新基线把漂移洗成正常。

```python
# file: code/06_Agent与LLM及系统设计/q2575_behavior_baseline.py
"""Q2575 Agent 行为的回归基线:统计画像与偏差评分。

金样本指纹只能抓可复现场景;统计画像基线记录步数分布与工具调用
频次的均值方差,新版本跑一批种子,任一指标偏离超阈值就告警,
能抓住"没坏但行为漂移"的隐性回归。
"""
import random
import statistics


def run_agent(seed):
    rng = random.Random(seed)
    steps = rng.randint(6, 9)
    tools = {}
    for _ in range(steps):
        t = rng.choice(["search", "calc", "sum"])
        tools[t] = tools.get(t, 0) + 1
    return {"steps": steps, "tools": tools}


def build_baseline(seeds):
    runs = [run_agent(s) for s in seeds]
    steps = [r["steps"] for r in runs]
    tool_total = {}
    for r in runs:
        for t, c in r["tools"].items():
            tool_total[t] = tool_total.get(t, 0) + c
    n = len(runs)
    return {"steps_mean": statistics.mean(steps),
            "steps_std": max(statistics.pstdev(steps), 1.0),
            "tool_mean": {t: c / n for t, c in tool_total.items()}}


def deviation(profile, run):
    worst = abs(run["steps"] - profile["steps_mean"]) / profile["steps_std"]
    for t, m in profile["tool_mean"].items():
        worst = max(worst, abs(run["tools"].get(t, 0) - m) / max(m, 1.0))
    return worst


def main():
    profile = build_baseline([1, 2, 3, 4, 5])
    normal = run_agent(6)
    weird = {"steps": 30, "tools": {"search": 30}}
    d1, d2 = deviation(profile, normal), deviation(profile, weird)
    assert d1 < 2.0, d1
    assert d2 > 2.0, d2
    print("基线:步数均值", round(profile["steps_mean"], 2),
          "标准差", round(profile["steps_std"], 2))
    print("正常新样本偏差:", round(d1, 2), "通过")
    print("异常新样本偏差:", round(d2, 2), "触发回归告警")


if __name__ == "__main__":
    main()
```

**追问**:
- 追问一:种子决定一切的话,画像不就固定了?答:种子只压住采样噪声,画像捕捉的是分布形态,种子集要覆盖场景多样性而不是单点。
- 追问二:和金样本指纹什么关系?答:金样本抓可复现路径的精确匹配,画像抓统计层面的漂移,一个管正确性一个管健康度,互补。
