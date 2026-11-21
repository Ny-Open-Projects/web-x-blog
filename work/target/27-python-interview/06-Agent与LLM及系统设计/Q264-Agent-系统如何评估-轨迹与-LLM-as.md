---
title: [Q264] Agent 系统如何评估:轨迹与 LLM-as-Judge
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q264 · Agent 系统如何评估:轨迹与 LLM-as-Judge

> 难度:★★★★ | 标签:Agent, 评估

**问**:RAG 可以评检索命中率,那 Agent 这种多步动态行为怎么量化评估?

**答**:分两个层面。结果层:任务是否完成——最终答案与参考答案的匹配度,可用 LLM-as-Judge 按评分细则(rubric)打 1-5 分,或做 A/B 两两对比(注意 judge 的位置偏差和"偏爱自己输出"问题,可用双评委+交换顺序缓解)。轨迹层:过程是否合理——工具选择正确率(该调的调了、不该调的没调)、步骤效率(冗余调用次数)、是否死循环。轨迹评估是 Agent 独有的:结果对但过程绕了三大圈,说明成本有问题;结果错但轨迹合理,定位到具体哪一步。评估集来源:线上 badcase 回流是最高价值的,配合人工构造的典型任务,每次改动 prompt/工具后跑回归。线上指标:任务完成率、人工接管率、平均步数与成本。

```python
# file: code/06_Agent与LLM及系统设计/q264_agent_eval.py
"""Agent 评估:工具轨迹正确率 + LLM-as-Judge 打分(stub 评委),输出回归报告。"""

GOLD = {  # 任务 -> (期望工具序列, 参考答案要点)
    "查北京天气": (["get_weather"], "北京 晴"),
    "对比两地天气": (["get_weather", "get_weather", "compare"], "北京晴 上海雨"),
}


def judge(answer: str, reference: str) -> int:
    """stub 评委:按参考答案要点覆盖率打 1-5 分(真实实现用强模型 + rubric)。"""
    points = reference.split()
    hits = sum(1 for p in points if p in answer)
    return min(5, 1 + int(hits / len(points) * 4))


def evaluate(cases: dict, traces: dict) -> float:
    passed, total = 0, 0
    for task, (gold_tools, reference) in cases.items():
        tools, answer = traces[task]
        extra = max(0, len(tools) - len(gold_tools))           # 冗余调用
        aligned = sum(1 for t, g in zip(tools, gold_tools) if t == g)
        tool_acc = aligned / len(gold_tools)
        score = judge(answer, reference)
        ok = tool_acc == 1.0 and extra == 0 and score >= 4
        passed += ok
        total += 1
        print(f"  {task}: 工具正确率={tool_acc:.0%} 冗余={extra} "
              f"评委分={score} {'PASS' if ok else 'FAIL'}")
    rate = passed / total
    print(f"回归通过率 {passed}/{total}")
    return rate


if __name__ == "__main__":
    traces = {
        "查北京天气": (["get_weather"], "北京 晴 12 度"),
        # 轨迹有冗余(calc 不在计划中),结果要点齐全:结果层满分、轨迹层扣分
        "对比两地天气": (["get_weather", "calc", "compare"], "北京晴 上海雨"),
    }
    evaluate(GOLD, traces)
```

**追问**:
- judge 偏爱自己输出的偏差怎么缓解?——双评委+交换顺序+多数决;judge 用不同家族的模型,同源偏差更小。
- 轨迹评估的工具成功率的口径?——(该调的调了+不该调的没调)/应判定总数;把「误调用」也算错,不然刷调用率就行。
- badcase 回流的机制?——线上负反馈/低分样本自动入评估集,修复后作为回归用例;评估集是活的资产不是一次性交付。
