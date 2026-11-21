---
title: [Q7603] 推理模型思考 token 的成本账
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7603 · 推理模型（reasoning）思考 token 的成本账

难度：P6 ｜ 标签：reasoning 模型 / token 计费 / 成本工程

**问**：把一套客服 Agent 从普通模型切到推理模型（reasoning model）后，单请求费用涨了 3 倍，但思考 token（reasoning tokens）既不出现在回复里也常常无法关闭。思考 token 是怎么计费的？什么场景值得用、什么场景是纯浪费？

**答**：
- **结论**：推理模型把"内部草稿推理"生成为思考 token，计入 output 计费（与最终回复同等价格），且通常不可见、不可复用为缓存前缀（或只能被后续轮次的专用缓存机制部分复用）。成本结构变化：普通模型 output = 最终答案；推理模型 output = 思考（常常是答案的 2-10 倍）+ 最终答案。账要这样算：`单请求成本 = input 价 × (prompt + 历史) + output 价 × (思考 token + 回复 token)`，多轮 Agent 里思考 token 默认不跨轮传递（或按模型规则被截断），每轮重新"想一遍"，多轮累积成本线性放大。适配场景：数学/代码/多步规划等"思考提升正确率显著"的任务；浪费场景：格式转换、简单分类、检索改写——这些任务思考几十秒换不来精度，纯烧钱加延迟。
- **取舍**：控制杠杆（以 o-系列/Claude thinking 类参数为准，各厂命名不同）：① 思考预算参数（reasoning_effort/budget_tokens）设档位——低档降本、高档留给难题；② 模型分级路由——简单任务走普通模型，复杂任务走推理模型（配合分类器成本约 1 次小调用）；③ 复用思考缓存——同会话连续轮次若供应商支持思考续传（如 GPT-5 系列的 reasoning reuse），开启后多轮成本大幅下降，但要确认计费口径。延迟是第二笔账：思考 token 按输出速度生成，思考 3000 token ≈ 多等 30-90 秒，交互式场景体验成本可能比 token 成本更高。
- **实战**：步骤：① 切换前用固定评测集测"正确率提升 vs 成本/延迟增幅"，写出每任务的性价比；② 按任务类型设 effort 档位与路由规则；③ 账单按"思考 token 占 output 比例"做指标监控（供应商 usage 里能拆出 reasoning token 数）；④ 复盘项：每季度复核模型价格与能力——推理模型降价与能力上移会让上次的路由分界过时。

```python
# 推理模型成本账计算器（纯标准库）
# 基线：Python 3.9+

def request_cost(
    prompt_tokens: int, answer_tokens: int,
    reasoning_tokens: int = 0,
    in_price: float = 3.0,    # $/1M input
    out_price: float = 15.0,  # $/1M output（思考与回复同价）
) -> dict:
    total_out = answer_tokens + reasoning_tokens
    cost = (prompt_tokens * in_price + total_out * out_price) / 1e6
    return {"cost_usd": round(cost, 4),
            "reasoning_pct_of_output": round(
                reasoning_tokens / max(1, total_out) * 100, 1)}


def multiround_cost(rounds: int, prompt: int, answer: int,
                    reasoning: int, reasoning_reuse: bool = False) -> float:
    """多轮累积：无续传时每轮重新付全额思考 token"""
    total = 0.0
    for r in range(rounds):
        hist = r * (answer + prompt)  # 历史增长
        think = reasoning if not (reasoning_reuse and r > 0) else int(reasoning * 0.2)
        total += request_cost(prompt + hist, answer, think)["cost_usd"]
    return round(total, 4)


def main() -> None:
    plain = request_cost(4000, 400)
    reason = request_cost(4000, 400, reasoning_tokens=2500)
    print("普通:", plain, "推理:", reason)
    # (4000*3 + 400*15)/1e6 = 0.018
    assert plain["cost_usd"] == 0.018
    # (4000*3 + 2900*15)/1e6 = 0.0555
    assert reason["cost_usd"] == 0.0555
    assert reason["cost_usd"] / plain["cost_usd"] > 3  # 约 3 倍
    # 10 轮会话：无续传 vs 有续传
    c1 = multiround_cost(10, 1000, 300, 2000, reasoning_reuse=False)
    c2 = multiround_cost(10, 1000, 300, 2000, reasoning_reuse=True)
    print(f"10轮 无续传 ${c1} / 有续传 ${c2}")
    assert c2 < c1
    print("OK")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么思考 token 通常无法做前缀缓存（prompt cache）复用？
→ 一句话提示：思考内容每次随输入动态变化且供应商一般不回放完整思考文本，缓存系统的"前缀完全一致"前提被破坏；只有支持思考续传的供应商才能在会话内部分复用，计费口径要单独核对。

**追问 2**：怎么从 usage 数据里度量"思考是否物有所值"？
→ 一句话提示：按任务类型分组对比"思考 token 数 × 单价"与"正确率/人工采纳率提升"，算每提升 1 个百分点的边际成本；分界线以下的任务应路由回普通模型或降 effort 档。

## 背诵要点
- 思考 token 计入 output 同价计费，常为答案的 2-10 倍且默认不跨轮复用；多轮 Agent 成本线性放大。
- 成本公式 = input 价 × prompt + output 价 ×（思考 + 回复）；监控"思考占 output 比例"与续传开启与否。
- 用 effort 档位 + 任务分级路由控制；简单任务（改写/分类）走推理模型是纯浪费，延迟是第二笔账。

## 复盘追问
- 为什么"延迟成本"在交互式 Agent 里可能超过 token 成本？提示：思考 3000 token 意味着 30-90 秒首字延迟，会话流失率与用户重试都会上升；体验层的流失要折算进成本账，不能只看 API 账单。
- 模型降价/能力上移后路由分界为什么会过时？提示：半年前"难题才用推理模型"的分界，在新一代模型又便宜又强后可能整体上移一档；路由规则要绑定"价格与能力快照"并定期重新标定，而不是一劳永逸。
