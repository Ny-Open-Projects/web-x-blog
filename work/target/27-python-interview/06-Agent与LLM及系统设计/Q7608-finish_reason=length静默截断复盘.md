---
title: [Q7608] finish_reason=length 静默截断导致 JSON 解析失败事故复盘
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7608 · finish_reason=length 静默截断导致 JSON 解析失败事故复盘

难度：P6 ｜ 标签：事故复盘 / 结构化输出 / 截断

**问**：一个"模型输出 JSON→解析入库"的服务，某天解析失败率从 0.3% 涨到 8%，日志里全是 `json.JSONDecodeError: Expecting ',' delimiter`。排查发现上游供应商把默认 `max_tokens` 生效口径改了。为什么截断会"静默"发生？怎么设计防线？

**答**：
- **结论**：`finish_reason` 有 `stop`（正常结束）、`length`（撞到 max_tokens 被截断）、`tool_calls` 等取值。事故链：输出长度随输入增长（新数据源让 prompt 变长 → 生成内容变长），`max_tokens` 用了 API 默认值没显式设置；截断发生时 JSON 恰好断在字符串/嵌套中间，解析失败；服务只捕了异常重试，重试同样截断，失败率被放大。**"静默"的根源是没有把 finish_reason 当作合同的一部分**——只检查拿到了响应，不检查响应是否完整。这是上下文超限截断（Q7543）的姊妹事故：那边截输入，这边截输出。
- **取舍**：防线分层：① **合同层**：显式设置 `max_tokens`（按输出模板实测 P99 长度 ×2 预留），每次响应校验 `finish_reason == "stop"`，否则进入明确分支（不是重试同参数，而是报错/走补全长度的 fallback）；② **结构层**：结构化输出优先用 JSON mode/structured outputs（语法约束下截断率大降）+ `response_format` schema 校验；③ **重试层**：截断重试要带指数——第一次失败把 max_tokens 翻倍重试，而不是原参数重试；④ **观测层**：finish_reason 分布做成指标，`length` 占比 >1% 告警——它是输出预算失配的先行指标；⑤ 截断的 JSON 尝试"补全修复"（补引号/括号）属于赌博，只在缓存类可容忍场景用。
- **实战**：事故剧本：① 统计失败样本的 finish_reason，确认全部是 length；② 从响应 usage 的 completion_tokens 看 P99 与 max_tokens 的关系，重设预算；③ 加 finish_reason 校验分支 + 指标；④ 对长输出场景（逐条长清单）改分页生成（一次生成 N 条 → 多次调用），把单次输出长度压回预算内；⑤ 复盘项：所有模型调用的 SDK 封装强制要求显式 max_tokens 与 finish_reason 校验，缺参数在 code review 门禁拦截。

```python
# finish_reason 合同校验 + 截断重试指数（标准库模拟 SDK 封装）
# 基线：Python 3.9+；真实实现 openai>=1.x（response.choices[0].finish_reason）

import json
from dataclasses import dataclass


@dataclass
class FakeResponse:
    content: str
    finish_reason: str          # stop / length / tool_calls
    completion_tokens: int


def call_model(content: str, max_tokens: int, truncate_at: int | None = None) -> FakeResponse:
    """模拟供应商：输出超 max_tokens 即截断且 finish_reason=length"""
    text = content if truncate_at is None else content[:truncate_at]
    return FakeResponse(text, "length" if truncate_at is not None else "stop",
                        len(text.split()))


def robust_json_call(prompt_content: str, max_tokens: int = 64) -> dict:
    """带 finish_reason 合同校验与长度翻倍重试的调用封装"""
    limit = max_tokens
    for attempt in range(3):
        resp = call_model(prompt_content, limit,
                          truncate_at=40 if attempt < 2 else None)  # 模拟前两次截断
        if resp.finish_reason != "stop":
            if resp.finish_reason == "length":
                limit *= 2                   # 截断重试必须翻倍预算，原参数重试无效
                continue
            raise RuntimeError(f"异常 finish_reason: {resp.finish_reason}")
        try:
            return json.loads(resp.content)
        except json.JSONDecodeError as e:
            raise ValueError(f"finish_reason=stop 但解析失败: {e}") from e
    raise RuntimeError("重试耗尽仍截断：输出预算与任务失配，需人工介入")


def main() -> None:
    payload = json.dumps({"city": "Beijing", "weather": "sunny", "temp": 25})
    # 反面教材：只 try 解析不查 finish_reason
    bad = call_model(payload, max_tokens=16, truncate_at=40)
    try:
        json.loads(bad.content)
        raise AssertionError("should fail")
    except json.JSONDecodeError as e:
        print(f"静默截断现场: {e}")

    result = robust_json_call(payload)
    assert result["city"] == "Beijing"
    print("OK: finish_reason 合同校验 + 翻倍重试兜住截断")


if __name__ == "__main__":
    main()
```

**追问 1**：structured outputs（JSON schema 约束）为什么能大幅降低截断伤害？
→ 一句话提示：约束解码保证每个 token 都符合 schema，截断断点也只能落在结构合法附近（且许多实现会在到达长度时输出可解析的截断态）；但约束不改变"长度预算失配"本身，finish_reason 校验仍不可省。

**追问 2**：finish_reason 有哪些取值容易漏处理？
→ 一句话提示：`tool_calls`（要求继续喂工具结果）、`content_filter`（内容策略拦截）、`function_call`（旧接口）——每种的续接语义不同，封装层应该把"未知 finish_reason"也当异常处理，防止供应商加新值时静默走错分支。

## 背诵要点
- 响应合同三要素：finish_reason == stop、max_tokens 显式设置、usage 长度监控；只 try 解析 JSON 不查 finish_reason 是事故根源。
- 截断重试必须翻倍输出预算（原参数重试必然复现截断）；length 占比 >1% 是输出预算失配的告警线。
- 结构化输出（schema 约束）降低截断伤害但替代不了 finish_reason 校验；长清单改分页生成压预算。

## 复盘追问
- 怎么在 SDK 封装层把"漏检查"变成编译期/评审期错误？提示：封装不返回裸 content，只返回"校验过合同的结果对象"，想在底层拿原始响应要走 escape hatch——让正确用法是唯一顺手的用法。
- usage 里哪几个字段要进监控？提示：completion_tokens 的 P99 与 max_tokens 的比值（预算水位）、total_tokens 趋势、以及按 finish_reason 分桶的占比——水位线告警比失败率告警更早。
