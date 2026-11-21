---
title: [Q1755] 输出长度截断策略:finish_reason 分级处置
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1755 · 输出长度截断策略:finish_reason 分级处置

> 难度:★★☆☆ | 标签:LLM, 输出截断, 降级

**问**:模型输出被 max_tokens 截断了,finish_reason 是 length,你怎么处理?

**答**:先分级:reason 是 stop 就直接用;是 length 则进入处置流程,首选带尾部上下文发续写请求,把片段拼回去,续写次数要有上限防止无限拼;续写预算花完仍是 length,就必须做安全截断——回退到最后一个句子边界,补一个明确的截断标记,而不是让句子断在半截被下游当完整答案消费。要点是"截断是可感知状态":调用方拿到 truncated 标记,可以决定重试、改问题或告知用户,而不是收到一份悄悄缺尾的答案。

```python
# file: code/06_Agent与LLM及系统设计/q1755_output_truncation.py
"""输出截断策略:finish_reason=length 时续写拼接,超续写预算后句子边界安全截断。"""


class FakeLLM:
    """续写桩:响应被拆成若干段,首段由调用方持有,可注入永远 length 的故障。"""

    def __init__(self, chunks, always_length=False):
        self.chunks = chunks
        self.calls = 0
        self.always_length = always_length

    def continue_(self, tail):
        idx = self.calls + 1                  # 段号:首段由调用方持有
        self.calls += 1
        if idx >= len(self.chunks):
            idx = len(self.chunks) - 1
        if self.always_length:
            reason = "length"
        else:
            reason = "stop" if idx == len(self.chunks) - 1 else "length"
        return {"text": self.chunks[idx], "finish_reason": reason}


class OutputPolicy:
    def __init__(self, llm, max_extra_calls=3):
        self.llm = llm
        self.max_extra_calls = max_extra_calls

    def resolve(self, first_text, first_reason):
        text, reason = first_text, first_reason
        extra = 0
        while reason == "length" and extra < self.max_extra_calls:
            nxt = self.llm.continue_(text[-20:])     # 带尾部上下文续写
            text += nxt["text"]
            reason = nxt["finish_reason"]
            extra += 1
        if reason == "length":                        # 续写预算耗尽仍不够
            return self._safe_cut(text) + "\n[输出因长度预算截断]", "truncated"
        return text, "complete"

    @staticmethod
    def _safe_cut(text):
        idx = max(text.rfind("。"), text.rfind("!"), text.rfind("\n"))
        return text[:idx + 1] if idx >= 0 else text


if __name__ == "__main__":
    llm1 = FakeLLM(["第一段。", "第二段完。"])
    out1, st1 = OutputPolicy(llm1).resolve("第一段。", "length")
    assert st1 == "complete" and out1 == "第一段。第二段完。"

    llm2 = FakeLLM(["x" * 50, "y" * 50, "z" * 50], always_length=True)
    out2, st2 = OutputPolicy(llm2, max_extra_calls=2).resolve("开头句。", "length")
    assert st2 == "truncated" and out2.endswith("[输出因长度预算截断]")
    assert out2.count("[输出因长度预算截断]") == 1
    assert out2.startswith("开头句。"), "安全截断停在句子边界"
    print("输出截断策略通过:续写拼接可完成,超预算走句子边界截断并带可感知标记")
```

**追问**:
- 为什么续写要带尾部 20 字? 答:续写请求不重发全文,只带尾部让模型衔接语气与未完成句,成本最低且足够对齐。
- 截断标记会不会污染下游? 答:标记是协议的一部分,下游解析器认识它并据此路由到重试或人工,不认识标记的旧下游也能看到不完整提示。
