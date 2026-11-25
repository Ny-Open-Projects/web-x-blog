---
title: "[Q7772] 半截 JSON 崩了下游：finish_reason=length 的分层降级链"
date: 2026-11-24
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7772 · 半截 JSON 崩了下游：finish_reason=length 的分层降级链

难度：P6 ｜ 标签：finish_reason、输出截断、max_tokens、降级链、结构化输出

基线：Python 3.12；模拟 token 预算不足时的截断生成与三层降级链（加预算重试 → 精简模式 → 显式失败），全标准库实跑。

**问**：模型返回的 JSON 解析报错，查日志才发现 `finish_reason=length`——输出被 max_tokens 掐断了。截断是错误吗？拿到截断响应的正确处理顺序是什么？为什么"半截 JSON 绝不透传给下游"？预算该配多少？

**答**：
- **结论**：`finish_reason=length` 不是模型出错，是**输出预算不够**的显式信号——模型还可以继续，但 max_tokens 到了。它的危险性在于"返回码是 200"：应用层如果只看 HTTP 状态不看 finish_reason，半截 JSON 就当成功返回，下游解析崩掉或更糟（半截数据静默入库）。处理顺序是**分层降级链**：① **加预算重试**：max_tokens 翻倍/三倍重试一次——大多数截断是预算拍脑袋配小了，一次重试即愈；② **精简模式回退**：预算翻倍还不够（或成本不允许），切换系统提示要求"只输出最短合法 JSON、省略可选字段"——用信息量换完整性；③ **显式失败**：两招都不行，返回带明确原因的错误（"输出预算不足，已重试两档"），**绝不把半截产物透传**——半截数据进入下游的代价（脏库、错误决策）远高于一次失败请求。预算配置的正解：按评测集分布配 P95 输出长度 × 安全系数（1.5），并监控截断率——截断率上升说明提示膨胀或任务变难（Q7690 超窗截断的输入侧姊妹题）。
- **取舍**：① 预算配大（比如 4k）省心但烧钱：每次调用按最大输出计费的服务（部分厂商按输出实算则相反），长预算还拖 P99 延迟——按任务分级配预算是成本基本功（Q7731 token 估算的姊妹账）；② 精简回退的信息损失：timeline/remarks 被砍掉，下游要能容忍"核心字段齐全、可选字段缺失"的 schema——**降级链的每一级都要有对应的 schema 兼容**，否则精简模式照样崩下游；③ 流式场景的截断处理不同：流已经发出去了没法"重试"，只能靠前端展示"生成中断"标记（Q7555 半截语法渲染的兜底）——非流式才能走本卡的完整降级链。
- **实战**：① 网关层统一封装：所有 LLM 调用强制检查 finish_reason，非 stop 的走降级链——一处实现，业务方永远拿到"完整或明确失败"二选一；② 监控三指标：截断率、降级链触发分布（L1 vs L2 vs L3）、预算命中率——L2 频繁触发说明默认预算配置错了；③ 结构化任务的保险丝：JSON 模式（response_format）+ 语义完整性校验（必填字段齐全）双闸门；④ 压测覆盖"最长输出任务"（长 timeline、长代码）的预算校验。

```python
"""Q7772 finish_reason=length 截断: 输出预算分层降级链, 而不是把半截 JSON 直接回给调用方。"""
import json

MAX_TOKENS_L1 = 100         # 第一档预算


def fake_model(prompt_len: int, max_tokens: int, concise: bool = False) -> tuple[str, str]:
    """模拟生成: 返回 (文本, finish_reason). 完整答案需要 ~180 tokens, 精简 ~30."""
    needed = 30 if concise else 180
    if prompt_len + needed <= max_tokens:
        body = '{"order_id":"O1","status":"shipped"}' if concise else \
               '{"order_id":"O1","status":"shipped","timeline":[{"ts":"...","event":"packed"},' \
               '{"ts":"...","event":"shipped"}],"eta":"...","carrier":"...","remarks":"..."}'
        return body, "stop"
    # 预算不够: 生成到 max_tokens 被截断(半截 JSON)
    cut = '{"order_id":"O1","status":"shipped","timel'
    return cut, "length"


def handle(prompt_len: int, budget: int) -> tuple[str, str]:
    """降级链: L1 加预算重试 -> L2 精简模式 -> L3 明确失败(不透传半截)."""
    text, reason = fake_model(prompt_len, budget)
    if reason == "stop":
        json.loads(text)                       # 完整且合法
        return text, "ok"
    # L1: 预算翻 3 倍重试
    text, reason = fake_model(prompt_len, budget * 3)
    if reason == "stop":
        return text, "ok_after_budget_retry"
    # L2: 精简模式(系统提示切换, 输出最短合法 JSON)
    text, reason = fake_model(prompt_len, budget * 3, concise=True)
    if reason == "stop":
        return text, "ok_concise_fallback"
    return "", "failed_with_clear_error"


if __name__ == "__main__":
    # 反例: 不看 finish_reason 直接 json.loads -> 崩
    text, reason = fake_model(20, 60)
    try:
        json.loads(text)
        parsed = "ok"
    except json.JSONDecodeError as e:
        parsed = f"JSONDecodeError: {e}"
    print(f"截断响应 ({reason}) 直接解析: {parsed}")

    r1, s1 = handle(20, MAX_TOKENS_L1)         # 加预算重试成功
    r2, s2 = handle(20, 5)                     # 预算小到精简也放不下 -> 显式失败
    print(f"预算 {MAX_TOKENS_L1}: {s1}")
    print(f"预算 5      : {s2} -> 不透传任何半截数据, 返回明确错误")
    ok = ("JSONDecodeError" in parsed and s1 == "ok_after_budget_retry"
          and s2 == "failed_with_clear_error" and json.loads(r1)["order_id"] == "O1")
    print(f"校验: 截断检测 + 三层降级链 + 终态显式失败 -> {'通过' if ok else '异常'}")
    print("结论：finish_reason=length 不是错误, 是'输出预算不够'的信号;")
    print("      处理顺序: 加预算重试 > 精简模式回退 > 显式失败; 半截 JSON 绝不透传给下游")
```

**追问一**：为什么"半截 JSON"比"请求失败"危险得多？在什么链路上会造成资损？

→ 解析：失败请求自带可见性——调用方拿到 error 会重试或报警，损害被窗口化。半截 JSON 的危险在于它**伪装成成功**：① 解析失败的下游抛异常——这还算幸运，问题暴露在离事故最近的地方；② 宽松解析的下游（`errors="ignore"` 式的 JSON 修复器、正则抠字段）会**抽出半截语义继续用**：`"status":"shipped` 被修复成 shipped，"退款已发起"的 timeline 缺了最后一笔，财务对账把截断前看到的金额当全量——**截断在语义上等于谎报**。资损链路：计费摘要、风控结论、结算明细任何一类被截断，下游基于"看起来完整的结构"做出的决策都是错的且无告警。所以纪律必须是：**finish_reason != stop 的响应在网关层就地终结**，错误码带原因透传，让"失败"保持失败的可见性。这与 Q7769 增量解码"宽松错误策略把字节问题洗成数据质量问题"是同一哲学：崩掉修代码，好过脏数据入库洗不掉。

**追问二**：流式输出已经把半截内容发给用户了，截断怎么处理？这和非流式的降级链有什么本质差异？

→ 解析：流式截断（token 预算耗尽、用户中断、连接断开）**不可重试**——前半段已经渲染在用户屏幕上，重试意味着重复计费与重复展示。所以流式的处理不是降级链而是**中断语义的显式表达**：① 尾部事件：SSE 发 `event: interrupted`（带 finish_reason=length 与已产出 token 数），前端渲染"…生成中断"占位（Q7555 半截语法兜底是它的子问题——Markdown 半截语法渲染成乱样式）；② 数据层：落库的内容带"不完整"标记，不参与后续的统计与评测（半截样本进评测集会污染分数）；③ 计费：按已产出 token 实算，但要与"业务上这算不算一次成功服务"解耦——计费完成 ≠ 任务完成（Q7508 取消时已消耗内容的语义账）。本质差异：非流式可以在"返回之前"做完所有质量闸门（降级、校验、重试），流式的闸门只能前置（预算预检、精简模式预选）——事后补救的空间被"已发送"这个事实消灭了。所以流式架构的第一课：**所有需要完整性的决策都必须发生在第一个 token 发出去之前**。
