---
title: [Q269] LLM 应用成本怎么控制
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q269 · LLM 应用成本怎么控制

> 难度:★★★ | 标签:Agent, 成本

**问**:LLM 调用很贵,有哪些系统性的降本手段?

**答**:按收益排序:1) 缓存——语义缓存命中重复问题,前缀缓存降低重复 system 的费用;2) 模型分级——简单任务(分类、改写)用小模型,复杂推理才上大模型,可加一个"路由器";3) 上下文瘦身——检索 top-k 收紧、历史压缩、工具结果裁剪,直接省 input token(占大头);4) 输出约束——要求简洁输出,输出 token 单价通常更高;5) 批处理 API——离线任务用 batch 价(通常五折);6) 架构层——能用规则/RAG 短路就不用 Agent 多轮循环。必须先建成本观测(按用户/功能维度),否则优化无从谈起。

```python
# file: code/06_Agent与LLM及系统设计/q269_cost_control.py
"""成本核算器:按模型分级路由并统计 token 费用,演示分级降本效果。"""

PRICING = {  # 每千 token 价格(演示值)
    "small": {"in": 0.5, "out": 1.5},
    "large": {"in": 5.0, "out": 15.0},
}


class CostTracker:
    def __init__(self):
        self.total = 0.0
        self.by_model: dict[str, float] = {}

    def bill(self, model: str, in_tokens: int, out_tokens: int):
        cost = (in_tokens / 1000 * PRICING[model]["in"]
                + out_tokens / 1000 * PRICING[model]["out"])
        self.total += cost
        self.by_model[model] = self.by_model.get(model, 0) + cost
        return cost


def route(task: str) -> str:
    """简单路由:分类/改写类用小模型,推理类用大模型。"""
    return "small" if task.startswith(("分类", "改写", "打标")) else "large"


def run_tasks(tasks: list[str], tracker: CostTracker):
    for task in tasks:
        model = route(task)
        in_t, out_t = (500, 30) if model == "small" else (2000, 500)
        cost = tracker.bill(model, in_t, out_t)
        print(f"  {task:<8} -> {model:<5} 费用 {cost:.4f}")


if __name__ == "__main__":
    tracker = CostTracker()
    run_tasks(["分类这条评论", "复杂推理解答数学证明", "改写这段文案", "复杂推理写行业分析"], tracker)
    print(f"总费用 {tracker.total:.4f},分布 {tracker.by_model}")
```

**追问**:
- 为什么先建成本观测?——没有按功能/用户维度的成本数据,优化就是盲调;常见结论是 20% 的会话贡献 80% 成本。
- 模型路由怎么做?——规则(长度/任务类型)先行,置信度低再升级大模型;路由错误会伤质量,要有评估兜底。
- input 和 output token 哪个贵?——output 通常 2-4 倍于 input;约束输出长度、避免重复长回答往往比压缩上下文更快见效。
