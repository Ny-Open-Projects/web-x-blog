---
title: [Q7634] 输出冗长度（verbosity）的成本账与约束手段
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7634 · 输出冗长度（verbosity）的成本账：max_tokens、指令约束与后处理的取舍

难度：P6 ｜ 标签：成本工程 / 输出治理 / token

**问**：账单分析发现输出 token 占总成本 60%，抽查发现模型回答普遍比需要长 2-3 倍（客服场景一句能说完的回答写三段）。为什么"输出长"这么贵、怎么治理？硬掐 max_tokens 与提示词约束"简洁"各有什么副作用？

**答**：
- **结论**：输出 token 的贵有三重：单价通常高于输入 3-4 倍；输出是**逐 token 串行生成**，直接决定尾部时延与并发吞吐（容量账 Q7586 同源）；且输出里被浪费的部分（客套、重复总结）没有业务价值。治理手段按"约束强度"排序：① **提示词结构化约束**——不是一句"简洁"，而是输出契约（"先一句结论，然后最多 3 个要点，每点 ≤20 字"），可验证可回归；② **max_tokens 硬上限**——防失控尾部，但掐得太短会出现 `finish_reason=length` 静默截断（Q7608/Q1755 同源），解析失败重试反而更贵；③ **后处理裁剪**——输出后按规则删重复段/模板化客套，对计费无效（token 已生成已计费）只优化用户体验；④ **小模型重写/压缩**——额外一次调用换输出缩短，只有当输出超长比例高时划算。账要按"任务结构"算：客服回答的理论输出 ≈ 结论 30 token + 要点 60 token = 90 token，实际均值 400 token → 78% 是浪费 → 治理目标是把均值压到 150 以内（留容错），单条成本降 ~60%。
- **取舍**：max_tokens 设多紧？设为"任务理论输出的 2-3 倍"：足够容纳合理波动，同时真正封死失控（如复读循环）；配合 finish_reason 监控——length 截断率 >2% 说明上限太紧或输出契约没被遵循。提示词"简洁"约束的失效模式：模型对模糊形容词（简洁/简短）遵循度低且不稳定，量化数字（≤20 字）遵循度显著更高——所以输出契约要可数、可断言。
- **实战**：① 每类任务定义输出契约（结构+上限）进 prompt 模板与评测集（冗长度指标：均值/P95）；② max_tokens 按任务分档 + finish_reason=length 率监控；③ 账单按"输出 token/会话"与"理论输出比"两个指标跟踪治理效果；④ 输出截断路径必须有解析兜底（Q1143 部分解析修复），不重试整条。

```python
# 输出成本账: 理论 vs 实际 token; max_tokens=理论x2-3; length截断率监控
# 基线: Python 3.9+ 标准库
from dataclasses import dataclass


@dataclass
class OutputBudget:
    theoretical: int       # 任务理论输出 token
    actual_mean: int
    price_in: float        # $/1k input
    price_out: float       # $/1k output

    def waste_ratio(self) -> float:
        return 1 - self.theoretical / self.actual_mean

    def cap(self, k: float = 2.5) -> int:
        return int(self.theoretical * k)

    def cost_per_call(self, tokens: int) -> float:
        return tokens / 1000 * self.price_out


def main() -> None:
    o = OutputBudget(theoretical=90, actual_mean=400,
                     price_in=0.5, price_out=2.0)
    assert abs(o.waste_ratio() - 0.775) < 1e-9      # 78% 浪费
    assert o.cap() == 225                            # 理论 x2.5
    before = o.cost_per_call(o.actual_mean)
    after = o.cost_per_call(150)                     # 治理后均值
    assert after / before < 0.4                      # 降 ~63%
    # 单价差: 输出贵 4 倍 -> 输出治理优先于输入
    assert o.price_out / o.price_in == 4
    print(f"浪费率 {o.waste_ratio():.0%}; cap={o.cap()} "
          f"(理论x2.5, 防失控不误伤)")
    print(f"输出成本 {before:.4f} -> {after:.4f}/call; "
          f"length截断率>2% 说明 cap 过紧或契约未遵循")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么"简洁"这种模糊指令遵循度低而"≤20 字"高？
→ 一句话提示：模糊形容词没有可判定的边界，模型按训练分布自行解释且方差大；量化契约有明确边界可对齐可评测——输出契约的可数性决定遵循度与可回归性。

**追问 2**：max_tokens 掐断后的正确处理路径是什么，为什么不直接重试？
→ 一句话提示：先看 finish_reason——length 截断走部分解析修复（结构化输出抢救半截 JSON）或降级回答，重试整条大概率再次超限（同样的输出倾向），只加倍成本；截断率高要修输出契约而不是靠重试兜。

## 背诵要点
- 输出 token 三重贵：单价高（约输入 3-4 倍）、串行生成决定时延与吞吐、无业务价值的冗长纯浪费——治理优先级高于输入侧。
- 手段排序：可数输出契约（"≤20 字"）> max_tokens（理论 ×2-3 封失控）> 后处理（不省计费只优体验）> 小模型压缩（超长比例高才划算）。
- 监控三件套：冗长度均值/P95、finish_reason=length 截断率（>2% 即契约问题）、输出 token/会话趋势。

## 复盘追问
- 为什么输出治理的 ROI 常被低估？提示：账单上输出只占"token 数"一半，但单价 ×4 且影响时延容量，实际成本占比可过半；治理收益要按"单价加权"算而不是按 token 量算。
- "输出契约"怎么进回归评测才不会腐化？提示：冗长度作为指标进评测集（均值/P95 卡阈值），prompt 模板变更跑对比；只有可数断言的契约才能在模型/prompt 升级时守住口径。
