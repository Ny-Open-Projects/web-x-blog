---
title: [Q7524] 工具 schema 设计与参数校验自愈循环
date: 2026-11-20
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7524 · 工具 schema 设计与参数校验自愈：模型填错参数，重试还是喂回去？

> 难度:★★★★ | 标签:Agent, 工具调用, schema

**问**：Agent 调工具时模型给的参数缺字段、类型错、日期格式五花八门。直接报错重试几次就放弃。怎么设计工具的 schema 与校验-反馈循环，让"第一次就填对率"尽可能高？

**答**：结论：错误参数的正确处理不是"盲目重试"，而是**结构化反馈自愈**——校验失败时把机器可读的错误（哪个字段、期望什么、实际收到什么）作为 tool 消息喂回模型再生成一次，通常 1-2 轮收敛。而"第一次就填对率"的真正杠杆在 schema 设计本身：字段名用领域词汇而不是缩写、description 写清格式与取值范围、必填最少化、枚举代替自由文本、日期给相对语义（"today+7d"服务端解析）。schema 质量的提升收益远大于重试逻辑的打磨。

机理与实战：
- schema 设计五律：① 必填最少化（可选字段让模型自行判断，必填越多错填越多）；② 枚举优先（status 用 enum 而非 string，约束解码/工具选择都受益）；③ description 带正例与反例（"ISO 8601 如 2026-01-01，不要传时间戳"）；④ 参数扁平化，深嵌套对象是填错重灾区；⑤ 危险参数显式化（amount 金额、target_user 身份字段服务端注入不由模型填——与最小权限构造呼应）。
- 自愈循环的工程细节：校验层用 Pydantic 校验函数入参（版本基线 Pydantic v2），错误信息转成 `{"error": "field 'date': 期望 ISO8601 日期,收到 1706745600"}` 喂回；自愈轮次计入指标（first_call_ok_rate / heal_rate），自愈超过 2 轮视为 schema 设计缺陷信号回改 schema，而不是继续加轮数。
- 失败兜底：自愈仍失败时按错误类分流——缺必填转"向用户澄清"分支；类型不兼容转"换工具或终止"；绝不用默认值静默填充危险参数。

```python
# 基线:Python 3.9+ / Pydantic v2 ;缺库降级:手写校验器演示同一协议
from dataclasses import dataclass, field

try:
    from pydantic import BaseModel, Field, ValidationError
    HAS_PYD = True
except ImportError:
    HAS_PYD = False


if HAS_PYD:
    class PaymentArgs(BaseModel):
        """工具入参:必填最少化 + 枚举 + 格式显式声明。"""
        order_id: str = Field(description="订单号,形如 ORD-20260101-001")
        action: str = Field(description="取值: refund | cancel")
        amount: float | None = Field(None, description="仅 refund 时必填,单位元")


def validate_args(raw: dict) -> tuple[object | None, dict | None]:
    """返回 (成功参数, 结构化错误)。错误可直接喂回模型自愈。"""
    if HAS_PYD:
        try:
            return PaymentArgs(**raw), None
        except ValidationError as e:
            return None, {"error": "invalid_tool_args", "details": [
                {"field": ".".join(map(str, x["loc"])),
                 "issue": x["type"],
                 "msg": x["msg"]} for x in e.errors()]}
    # 降级手写校验:同样的结构化错误协议
    errs = []
    if not isinstance(raw.get("order_id"), str) or not raw["order_id"].startswith("ORD-"):
        errs.append({"field": "order_id", "issue": "format",
                     "msg": "期望 ORD- 开头的订单号"})
    if raw.get("action") not in ("refund", "cancel"):
        errs.append({"field": "action", "issue": "enum",
                     "msg": "取值仅 refund | cancel"})
    if raw.get("action") == "refund" and raw.get("amount") is None:
        errs.append({"field": "amount", "issue": "required",
                     "msg": "refund 必须带金额"})
    if errs:
        return None, {"error": "invalid_tool_args", "details": errs}
    return raw, None


def tool_loop(raw: dict, heal_budget: int = 2) -> dict:
    """自愈循环:校验失败 -> 结构化错误喂回 -> 重新生成(此处模拟)。"""
    for attempt in range(heal_budget + 1):
        args, err = validate_args(raw)
        if args is not None:
            return {"ok": True, "attempts": attempt + 1, "args": args}
        # 真实实现:err 序列化进 tool 消息让模型重生成;此处模拟修正
        print(f"第 {attempt+1} 次校验失败,反馈给模型:", err)
        raw = {"order_id": "ORD-20260101-001", "action": "refund", "amount": 99.0}
    return {"ok": False, "error": err}


def main() -> None:
    bad = {"order_id": 12345, "action": "RE-FUND"}          # 模型首答
    print("自愈结果:", tool_loop(bad))


if __name__ == "__main__":
    main()
```

**追问一**：为什么"自愈超过 2 轮"要当 schema 缺陷信号而不是加轮数？
答：反复同类错误说明模型稳定地误解 schema——例如字段名 `ord` 被理解为其他含义，或 description 缺格式说明。加轮数只是给同一个误解更多机会，边际收益趋零还翻倍成本；改 schema（改名、加正例、拆参数）才是修根因。把 heal_rate 按"字段 × 错误类"聚合，直接指出哪个 description 要重写。

**追问二**：危险参数（金额）为什么不该由模型填？
答：模型对数值的生成不可靠且有被注入引导的风险（"把金额改成 9999"）；金额类参数应由上游业务上下文（订单原始金额）服务端注入，模型只能表达意图（refund）。这与最小权限构造原则一致：身份与资金字段走服务端，不进模型自由度。

**背诵要点**：
- schema 五律：必填最少、枚举优先、description 带正反例、参数扁平、危险字段服务端注入。
- 校验失败喂结构化错误（字段+期望+实际）自愈，2 轮不收敛视为 schema 缺陷。
- 指标 first_call_ok_rate 按"字段×错误类"聚合，直接指导 schema 迭代。

**复盘追问**：
- 自愈消息的 token 成本怎么预算（错误详情是否截断）？
- 多工具场景下"选错工具"与"参数填错"两类失败如何分别治理？

## 背诵要点
- 自愈循环上限 2 轮，超出即回改 schema 而非堆轮数。
- 枚举与最少必填是 first_call_ok_rate 的最大杠杆。
- 金额/身份类参数永远服务端注入，模型只表达意图。

## 复盘追问
- 如何用历史真实调用数据回归"schema 改版前后 first_call_ok_rate"？
- 约束解码（grammar/json schema）与 post 校验自愈的适用边界？
