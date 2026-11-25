---
title: [Q7643] 思考 token 吃掉 max_tokens 导致静默空输出的复盘
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7643 · 推理模型的思考 token 吃掉 max_tokens 导致静默空输出的复盘

难度：P6 ｜ 标签：事故复盘 / 推理模型 / 参数治理

**问**：接入推理模型（o 系列 / DeepSeek-R1 类）后，部分请求返回的可见内容为空或被截断，`finish_reason` 是 length，但没报任何错。排查发现 max_tokens 没变，推理预算（thinking budget）却远超它。这类"思考 token 与输出 token 共享预算"的坑怎么理解、怎么防？

**答**：
- **结论**：推理模型的 token 计费与长度限制通常把**思考 token（reasoning tokens）和最终回答 token 放进同一个输出预算**：`max_tokens`（或 `max_output_tokens`）= 思考 + 回答。模型遇到难题思考了 4800 token，而 `max_tokens=512` 的配置还是旧参数——思考耗尽预算，可见回答一个 token 都没生成，`finish_reason=length`，客户端拿到空内容。静默性是事故核心：不报错、只返回空/截断，客户端若不做 finish_reason 校验（Q7608 的截断问题在推理模型上的变体）就会把空字符串入库。防线：① **参数联动**：设置推理预算上限（如 `reasoning_effort`/`max_completion_tokens` 显式分账），max_tokens 至少 = 预期思考量 × 安全系数 + 回答上限；② **finish_reason 门禁**：length 一律视为失败（重试提预算或降难度），绝不静默接受空输出；③ **监控分账**：分别统计思考/回答 token 分布（Q7603 成本账的数据源），思考占比异常升高 = 提示词难度异常或模型行为漂移。
- **取舍**：思考预算调大（贵、慢但答案全）vs 调小（便宜但推理质量下降甚至答不完）；按任务分级——简单分类任务关思考/低预算，复杂推理给足预算。另一层取舍：客户端重试加预算 vs 提示词降难度：重试是双倍成本，降难度是质量问题，日志里要区分"预算不足"与"题目本身超纲"。
- **实战**：① 上线推理模型时把 `max_completion_tokens` 与 `reasoning_effort` 写进网关默认参数矩阵（Q7610 网关覆盖参数事故的姊妹问题）；② 空输出（可见内容为空 + finish_reason=length）做独立告警指标，占比 > 0.5% 即参数配置事故；③ 评测集覆盖高难度题，验证预算上限下"能答完"而非只验证"答得对"。

```python
# 推理模型输出预算分账: 思考 token + 回答 token 共享 max_tokens
# 基线: Python 3.9+ 标准库 (语义模型, 生产核对各厂商 reasoning 参数)
from dataclasses import dataclass


@dataclass
class ReasoningBudget:
    max_output_tokens: int        # 输出总预算 (思考+回答共享)
    effort_factor: float          # 思考量随题目难度放大

    def simulate(self, difficulty: float) -> tuple[int, int, str]:
        """返回 (思考token, 回答token, finish_reason)。"""
        think = int(self.effort_factor * difficulty)
        budget_left = self.max_output_tokens - think
        if budget_left <= 0:                     # 思考吃光预算
            return think, 0, "length"            # 可见内容为空!
        answer = min(400, budget_left)
        return think, answer, "length" if answer < 400 else "stop"


def gate(think: int, answer: int, reason: str) -> str:
    """客户端门禁: length 且空输出 -> 禁止静默入库。"""
    if reason == "length" and answer == 0:
        return "REJECT: 空输出(思考吃光预算), 提预算重试或降难度"
    if reason == "length":
        return "RETRY+Budget: 回答被截断"
    return "OK"


def main() -> None:
    tight = ReasoningBudget(max_output_tokens=512, effort_factor=1000)
    think, answer, reason = tight.simulate(difficulty=6.0)   # 难题: 思考 6000
    assert think == 6000 and answer == 0 and reason == "length"
    assert gate(think, answer, reason).startswith("REJECT")
    # 预算充足: 思考 3000 + 回答 400 = stop
    loose = ReasoningBudget(max_output_tokens=8192, effort_factor=500)
    think2, answer2, reason2 = loose.simulate(6.0)
    assert think2 == 3000 and reason2 == "stop"
    # 分账监控: 思考占比异常 (>80%) 告警
    ratio = think2 / (think2 + answer2)
    assert 0.8 < ratio < 0.9                 # 3000/3400 ≈ 0.88
    print(f"tight: think={think} answer=0 -> {gate(think, answer, reason)[:20]}")
    print(f"loose: think={think2} answer={answer2} 占比 {ratio:.0%}")
    print("OK: finish_reason=length 门禁 + 思考/回答分账监控")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么这类事故不报错却比报错更危险？
→ 一句话提示：异常有堆栈会触发告警，空输出是"合法响应"——直接入库/返回给用户，污染数据或造成用户侧困惑；静默失败只能靠业务指标（空输出率）监控。

**追问 2**：`reasoning_effort` 与 `max_completion_tokens` 该由谁定？
→ 一句话提示：网关默认矩阵按任务分级（Q7610 反例是网关覆盖了不该覆盖的参数——正确做法是"按任务预设 + 调用方可显式覆盖 + 覆盖留审计"），禁止全局一刀切。

## 背诵要点
- 推理模型输出预算 = 思考 + 回答共享：难题思考可能吃光 max_tokens，可见回答为空，finish_reason=length，零报错。
- 防线：finish_reason=length 门禁（空输出拒绝入库）、参数分账（reasoning_effort / max_completion_tokens）、思考占比监控告警（>80% 异常）。
- 预算分级：简单任务低预算/关思考，复杂推理足额预算；重试提预算是双倍成本，先区分"预算不足"还是"题目超纲"。

## 复盘追问
- 如何区分"预算不足"与"模型推理不出"？提示：提预算重试一次——能答完是预算问题，仍失败或答案质量差是能力问题；两者处置不同（前者改参数，后者改提示/换模型）。
- 思考占比监控的基线怎么建立？提示：按任务难度分层统计思考/回答 token 分布，上线后对比基线偏移；占比突增常见于提示词混入复杂上下文或模型版本变化。
