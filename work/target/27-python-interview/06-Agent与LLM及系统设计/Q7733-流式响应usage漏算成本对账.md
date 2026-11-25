---
title: "[Q7733] 流式响应没有 usage：成本报表少算了 40%"
date: 2026-11-24
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7733 · 流式响应没有 usage：成本报表少算了 40%

难度：P6 ｜ 标签：SSE、流式、usage 计量、成本对账

基线：Python 3.12；OpenAI 兼容 `stream_options={"include_usage": true}`；SSE 分块解析。

**问**：非流式调用能拿到 `usage.prompt_tokens/completion_tokens`；改成 SSE 流式后响应里只有 delta，最后也没有 usage，成本报表只能按字符数估算，月度对账差了 40%。流式到底能不能拿到 token 用量？

**答**：
- **结论**：多数 OpenAI 兼容实现**默认不在流式响应里返回 usage**。OpenAI 需要显式传 `stream_options={"include_usage": True}`，此时最后一个 chunk 的 `choices` 是**空数组**、只带 `usage` 字段，位置在 `data: [DONE]` 之前。不传就永远拿不到。部分供应商不支持该参数，传了会 400，需要按供应商能力降级。
- **取舍**：流式改善首 token 体验，但把**计量信息拆散**：要么开启 include_usage（解析器必须容忍 `choices == []`），要么本地估算（不准），要么在网关按字符/字节记账（只能做相对比较）。财务口径必须用真实 usage，估算只配做实时护栏。
- **实战**：① 请求带上 `stream_options`，解析时把"空 choices + usage"当统计块单独处理；② 网关统一记账 `request_id + model + usage`，拿不到时标 `estimated=True`；③ 客户端中途断开时服务端往往仍按已生成 token 计费，要按最后一个 usage 或已发送内容估算；④ 对账任务比对"网关记账 vs 供应商账单"，差异 > 2% 告警；⑤ 解析器对未知字段保持宽容，供应商会加字段。

```python
"""SSE 解析：delta 拼接、空 choices 的 usage 块、[DONE] 边界。"""
import json


def parse_sse(chunks: list[str]) -> tuple[str, dict | None]:
    """返回 (拼接后的文本, usage 或 None)。"""
    text_parts: list[str] = []
    usage: dict | None = None
    for raw in chunks:
        for line in raw.splitlines():
            if not line.startswith("data: "):
                continue                      # 忽略注释行与空行
            payload = line[len("data: "):]
            if payload.strip() == "[DONE]":
                continue
            obj = json.loads(payload)
            choices = obj.get("choices") or []
            if not choices:                    # 统计块：只有 usage
                usage = obj.get("usage")
                continue
            delta = choices[0].get("delta") or {}
            piece = delta.get("content")
            if piece:
                text_parts.append(piece)
    return "".join(text_parts), usage


if __name__ == "__main__":
    # 典型流：三条 delta、一条空 choices 的 usage、最后 [DONE]
    chunks = [
        'data: {"choices":[{"delta":{"role":"assistant"}}]}',
        'data: {"choices":[{"delta":{"content":"退款"}}]}',
        'data: {"choices":[{"delta":{"content":"需 7 个工作日"}}]}',
        'data: {"choices":[],"usage":{"prompt_tokens":812,"completion_tokens":37}}',
        'data: [DONE]',
    ]
    text, usage = parse_sse(chunks)
    print("文本:", text)
    print("usage:", usage)
    cost = usage["prompt_tokens"] * 0.0000015 + usage["completion_tokens"] * 0.000006
    print(f"单次成本: {cost:.6f}")

    # 未开 include_usage：永远拿不到 usage
    no_usage = [c for c in chunks if '"usage"' not in c]
    text2, usage2 = parse_sse(no_usage)
    print("不开 include_usage:", text2, "| usage:", usage2, "-> 只能估算")

    # 粗估 vs 真实：中文按 1.6 token/字符
    est = int(len(text) * 1.6) + 40
    print(f"粗估 completion={est} 真实={usage['completion_tokens']} "
          f"偏差={(est - usage['completion_tokens']) / usage['completion_tokens']:.0%}")

    print("结论：流式计量靠 stream_options；解析器要容忍空 choices；账单以 usage 为准")
```

**追问一**：客户端中途断开，供应商会退费吗？
→ 解析：通常按**已生成**的 token 计费（服务端已经开始/完成推理），不会因为客户端断开而退。取消要及时（服务端取消信号），记账必须覆盖被取消的请求，否则报表只会记录"成功"的那部分，系统性偏低。

**追问二**：为什么最后一个 chunk 的 `choices` 是空数组？
→ 解析：usage 是整条请求的聚合信息，不属于任何单个 choice，协议用"空 choices + usage"表达统计块。解析器若假设每个 chunk 都有 `choices[0].delta.content`，会在这一块抛 IndexError/KeyError，整条流处理失败。
