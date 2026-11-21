"""上下文超限降级阶梯:裁剪工具结果、丢最旧轮次、摘要替换、硬失败,四级逐级加压。"""


def est_tokens(text):
    return max(1, len(text) // 2)          # 演示用粗估:2 字符 1 token


class FakeLLM:
    """摘要桩:不联网,把历史压成一条极短的台账式摘要。"""

    def summarize(self, text):
        return "摘要历史" + str(text.count("。")) + "句"


class LadderCompressor:
    """按代价从小到大逐级降级:先测原样,不行再逐级加工,最后一级直接硬失败。"""

    LEVELS = ["trim_tool_results", "drop_old_turns", "summarize"]

    def __init__(self, budget, llm=None):
        self.budget = budget
        self.llm = llm or FakeLLM()
        self.applied = []

    def fit(self, context):
        """context: [{role, text}],返回压缩后的副本与所用级别。"""
        work = [dict(m) for m in context]
        used = self._used(work)
        if used <= self.budget:
            return work, "none", used
        for level in self.LEVELS:
            self.applied.append(level)
            step = {"trim_tool_results": self._trim,
                    "drop_old_turns": self._drop,
                    "summarize": self._summarize}[level]
            work = step(work)
            used = self._used(work)
            if used <= self.budget:
                return work, level, used
        raise MemoryError(f"三级降级后仍超限 需要 {used} 预算 {self.budget}")

    @staticmethod
    def _used(ctx):
        return sum(est_tokens(m["text"]) for m in ctx)

    def _trim(self, ctx):
        """把超长工具结果截到 40 字并留截断标记,系统消息不动。"""
        out = []
        for m in ctx:
            if m["role"] == "tool" and est_tokens(m["text"]) > 20:
                out.append(dict(m, text=m["text"][:40] + "…[已截断]"))
            else:
                out.append(m)
        return out

    def _drop(self, ctx):
        """保留 system 与最近 2 条,其余丢弃。"""
        sys_msgs = [m for m in ctx if m["role"] == "system"]
        rest = [m for m in ctx if m["role"] != "system"]
        return sys_msgs + rest[-2:]

    def _summarize(self, ctx):
        """旧轮次整体替换为一条摘要消息。"""
        sys_msgs = [m for m in ctx if m["role"] == "system"]
        rest = [m for m in ctx if m["role"] != "system"]
        old, recent = rest[:-1], rest[-1:]
        joined = " ".join(m["text"] for m in old)
        return sys_msgs + [{"role": "summary", "text": self.llm.summarize(joined)}] + recent


if __name__ == "__main__":
    ctx = [{"role": "system", "text": "你是助手。"},
           {"role": "user", "text": "帮我查三本书。"},
           {"role": "tool", "text": "书A的介绍。" * 60},
           {"role": "tool", "text": "书B的介绍。" * 60},
           {"role": "assistant", "text": "找到了两本,还差最后一本。"},
           {"role": "user", "text": "继续。"}]

    wide, l0, u0 = LadderCompressor(budget=10 ** 6).fit(ctx)
    assert l0 == "none" and u0 == sum(est_tokens(m["text"]) for m in ctx)

    mid, l1, u1 = LadderCompressor(budget=90).fit(ctx)
    assert l1 == "trim_tool_results" and u1 <= 90
    assert all("已截断" in m["text"] for m in mid if m["role"] == "tool")

    tighter, l2, u2 = LadderCompressor(budget=20).fit(ctx)
    assert l2 == "drop_old_turns" and u2 <= 20

    tight, l3, u3 = LadderCompressor(budget=8).fit(ctx)
    assert l3 == "summarize" and u3 <= 8
    assert [m["role"] for m in tight] == ["system", "summary", "user"]

    blown = 0
    try:
        LadderCompressor(budget=4).fit(ctx)
    except MemoryError:
        blown = 1
    assert blown == 1, "预算 4 连摘要也塞不下 必须硬失败"
    print("降级阶梯通过:none→trim→drop→summarize→硬失败 各级预算", u0, u1, u2, u3)
