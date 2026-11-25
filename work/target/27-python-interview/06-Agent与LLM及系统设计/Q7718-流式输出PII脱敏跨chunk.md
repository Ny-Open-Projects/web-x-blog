---
title: "[Q7718] 流式输出的 PII 脱敏：敏感信息被切成两半"
date: 2026-11-23
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7718 · 流式输出的 PII 脱敏：敏感信息被切成两半

难度：P6 ｜ 标签：流式、PII、脱敏、跨 chunk 边界

基线：Python 3.12；正则 + 滑动缓冲；SSE/token 流为对照。

**问**：客服 Agent 流式输出，前端逐 token 渲染。安全团队要求对手机号、身份证做脱敏，开发在每收到一个 chunk 时跑一次正则替换。上线后用户仍然看到了完整的手机号——号码被切成 `138`、`0000`、`0000` 三段，每段都不匹配 11 位正则。流式脱敏为什么这么容易漏？怎么修？

**答**：
- **结论**：PII 模式通常有**最小长度和固定结构**（手机号 11 位、身份证 18 位），而流式 chunk 按 token/字节切，敏感串很容易跨 chunk。逐 chunk 独立匹配时，每段都不构成完整模式，正则必然漏检；等拼起来再脱敏，内容已经发给前端，无法撤回。这是"流式低延迟"与"脱敏需要完整上下文"的结构性冲突。
- **取舍**：解法是**滑动缓冲 + 延迟输出**：保留末尾"最长敏感模式长度 − 1"个字符不发出，只在确认前缀中不存在跨边界的未完成模式时才输出；流结束时 flush。代价是引入少量延迟（通常几十毫秒）和缓冲内存。另一种是**生成侧约束**（不让模型输出原始 PII、用占位符）或**非流式后置审核**，牺牲流式体验换安全。
- **实战**：① 按敏感类型维护最大模式长度，缓冲区至少覆盖最长模式；② 对已确认的完整匹配替换为占位符（保留类型与后四位便于业务）；③ 流结束时必须 flush 残留，避免最后一段漏检；④ 监控"输出中出现 PII 模式"的告警，作为脱敏器的兜底；⑤ 高敏场景不要让原始值进入模型上下文。

```python
import re

PHONE = re.compile(r"1[3-9]\d{9}")
KEEP = 10          # 最长模式 11 位，保留 10 个字符等待跨界


def naive_redact(chunks: list[str]) -> str:
    return "".join(PHONE.sub("[PHONE]", c) for c in chunks)


def stream_redact(chunks: list[str]) -> str:
    buf, out = "", []
    for chunk in chunks:
        buf += chunk
        if len(buf) > KEEP:
            cut = len(buf) - KEEP
            # 若安全前缀末尾是一段数字，它可能延续成手机号：整体回退到数字串起点
            m = re.search(r"\d+$", buf[:cut])
            if m:
                cut = m.start()
            out.append(PHONE.sub("[PHONE]", buf[:cut]))
            buf = buf[cut:]
    out.append(PHONE.sub("[PHONE]", buf))       # flush 残留
    return "".join(out)


if __name__ == "__main__":
    chunks = ["您的手机号是 138", "0000", "0000，请确认。"]
    print("逐块脱敏:", naive_redact(chunks))
    print("缓冲脱敏:", stream_redact(chunks))
    print("结论：跨 chunk 的 PII 必须用滑动缓冲，逐块正则必然漏")
```

**追问一**：缓冲区越大越安全吗？
→ 解析：缓冲只需覆盖"最长敏感模式长度 − 1"，更大不会提升正确性，反而增加首字延迟和内存。关键是按 PII 类型算出最大长度，并保证 flush 时不丢最后一段。

**追问二**：为什么"先流式输出，再异步审核删除"不可行？
→ 解析：内容一旦到达客户端就无法收回，截图、缓存、前端日志都可能保留；删除只能改服务端存储，不能消除已泄露的事实。高敏内容必须在**发出前**完成脱敏，或者根本不流式输出。
