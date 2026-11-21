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
