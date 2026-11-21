---
title: "[Q7576] 推理模型 Reasoning Token 的成本账"
date: 2026-11-20
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7576 · 推理模型 Reasoning Token 的成本账

难度：P6 ｜ 标签：成本工程 / reasoning / o系列 / 预算

**问**：团队把简单分类任务也从普通模型切到推理模型（o 系列/思考模型），月成本翻了 8 倍——reasoning token 是不可见的大头。怎么给"要不要用推理模型"定账与路由规则？

**答**：

**结论**：推理模型的账和普通模型结构不同：输出分 answer token 与 reasoning token，reasoning 部分按输出价计费但用户看不见、且不可直接控制长度（部分 API 提供 reasoning effort/budget 参数）。典型账：简单任务（分类、格式转换）reasoning 可能占输出的 90%，单价又贵 3-5 倍，成本放大 10 倍以上而质量增益为零；复杂任务（多步数学、规划）reasoning 换来的是成功率，账反而是省的——重试一次失败的普通模型调用比一次成功的推理调用更贵。路由规则应该按"任务失败重试成本 vs 推理溢价"来定，而不是按任务类型拍脑袋。

**取舍**：三个控制杠杆：① 路由分层——意图分类/路由本身用小模型，判断为"难"才升级推理模型（路由器的错误率要进账：误降级导致重试成本、误升级导致溢价）；② effort/budget 参数——多数推理 API 支持 low/medium/high 或 max_tokens 级预算，默认给 low，按任务实测调；③ 缓存与批处理——推理 token 同样吃 prompt cache 与 batch 折扣，离线任务优先 batch API。隐藏坑：reasoning token 会撑大上下文（部分 API 的 reasoning 留在上下文里参与下一轮计费），多轮 Agent 里要确认框架是否清理。

**实战**：账本化：按任务类型记录 reasoning token 占比分布、单价、成功率、重试率——算出每类任务的"每成功一次总成本"，普通模型含期望重试次数、推理模型含溢价，交叉点即路由阈值。Python 演示这个决策公式。

```python
# 推理模型 vs 普通模型：每成功一次的总成本决策账
# 仅标准库，Python 3.9+
from __future__ import annotations


def cost_per_success(base_out: int, price: float, success_rate: float,
                     reasoning_ratio: float = 0.0,
                     reasoning_price_mult: float = 1.0) -> float:
    """单次成本 = answer token 费 + reasoning token 费；期望成本再除以成功率（重试期望）。"""
    unit_cost = base_out * price * (1 + reasoning_ratio * reasoning_price_mult)
    return unit_cost / success_rate


def main() -> None:
    P_STD, P_RSN = 0.002, 0.005  # $/1k output tokens（推理单价约 2.5x）

    # 简单分类任务：300 token 输出
    std = cost_per_success(300, P_STD, success_rate=0.97)
    rsn = cost_per_success(300, P_RSN, success_rate=0.98,
                           reasoning_ratio=9.0)  # reasoning 占 90%
    print(f"分类任务: 普通 ${std:.4f} vs 推理 ${rsn:.4f} → 用普通模型")
    assert rsn > std * 5

    # 复杂规划任务：普通模型成功率仅 0.10（频繁重试），推理 0.93
    std2 = cost_per_success(1500, P_STD, success_rate=0.10)
    rsn2 = cost_per_success(1500, P_RSN, success_rate=0.93,
                            reasoning_ratio=2.0)
    print(f"规划任务: 普通(含重试) ${std2:.4f} vs 推理 ${rsn2:.4f} → 用推理模型")
    assert rsn2 < std2

    # 路由器本身也有错误成本
    router_err = 0.05
    blended = (1 - router_err) * 0 + router_err * rsn  # 误升级成本
    print(f"路由器误升级率 {router_err:.0%}，误升级单次损失 ${blended:.4f}")
    assert blended >= 0
    print("结论：路由阈值 = 每成功成本交叉点，用账定而不是拍脑袋")


if __name__ == "__main__":
    main()
```

**追问链**：

- 追问 1：为什么"按任务类型路由"不如"按重试成本路由"？——任务类型是代理指标，真实决策变量是"普通模型在该任务上的失败重试期望成本"；同一类型里难度分布不同（有的分类题就很难），成功率数据比类型标签更准。路由器持续收集 per-task 成功率自动收敛阈值。
- 追问 1.1：reasoning token 留在上下文里对多轮 Agent 的影响？——部分 API 的 reasoning 块不计入后续上下文（自动剥离），部分会保留并参与计费与窗口占用；后者让长会话上下文被思考过程撑爆。迁移/混用多家 API 时要逐家确认，账里单列。
- 追问 2：reasoning effort 从 high 降到 low，质量损失怎么评估？——用分层评测集：按任务难度分层看 low effort 的失败率分布，损失应集中在最难层；如果简单层也开始失败说明配错了模型而非 effort 问题。

**背诵要点**：

1. 推理模型账的结构：reasoning token 按输出计费、不可见、占输出 50-90%；简单任务成本放大 5-10 倍零增益。
2. 路由决策 = 每成功一次总成本交叉点：普通模型成本要乘 1/成功率（重试期望），不是按任务类型拍脑袋。
3. 控制杠杆：effort/budget 默认 low 按实测调、离线走 batch 折扣、确认 reasoning 是否驻留上下文参与下一轮计费。

**复盘追问**：

1. 上线推理模型一个月后成本 8 倍，你先查哪三个数据（reasoning 占比/路由误判率/effort 配置）？
2. 如何为路由器收集"普通模型成功率"数据而不让用户承担失败体验？
