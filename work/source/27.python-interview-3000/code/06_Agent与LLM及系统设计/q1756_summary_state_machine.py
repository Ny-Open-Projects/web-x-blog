"""超长对话分段摘要状态机:分窗摘要逐块落检查点,崩溃后从断点续跑不重复。"""


class FakeLLM:
    """摘要桩:块摘要与合并都不联网;可注入故障模拟进程崩溃。"""

    def __init__(self, fail_after=None):
        self.summarize_calls = 0
        self.fail_after = fail_after

    def summarize(self, text):
        if self.fail_after is not None and self.summarize_calls >= self.fail_after:
            self.fail_after = None              # 一次性故障:崩溃重启后恢复
            raise RuntimeError("simulated crash")
        self.summarize_calls += 1               # 只计成功调用
        return "摘%d[%s]" % (self.summarize_calls, text[:6])

    def merge(self, parts):
        return "MERGE(" + "|".join(parts) + ")"


class SegmentedSummarizer:
    """状态机:idle -> chunking -> summarizing -> merging -> done,检查点贯穿始终。"""

    def __init__(self, llm, window=2, checkpoint=None):
        self.llm = llm
        self.window = window
        self.cp = checkpoint or {"state": "idle", "summaries": [], "next_chunk": 0}

    def run(self, turns):
        self.cp["state"] = "chunking"
        chunks = [",".join(turns[i:i + self.window])
                  for i in range(0, len(turns), self.window)]
        self.cp["state"] = "summarizing"
        while self.cp["next_chunk"] < len(chunks):
            i = self.cp["next_chunk"]
            summary = self.llm.summarize(chunks[i])   # 崩溃点:抛异常即中断
            self.cp["summaries"].append(summary)      # 成功即落盘,永不重算
            self.cp["next_chunk"] = i + 1
        self.cp["state"] = "merging"
        final = self.llm.merge(self.cp["summaries"])
        self.cp["state"] = "done"
        return final


if __name__ == "__main__":
    turns = ["用户问%d" % i for i in range(9)]        # 9 轮 -> 5 个窗口
    llm = FakeLLM(fail_after=2)
    sm = SegmentedSummarizer(llm, window=2)
    crashed = False
    try:
        sm.run(turns)
    except RuntimeError as e:
        crashed = str(e) == "simulated crash"
    assert crashed, "注入的崩溃必须原样抛出"
    assert sm.cp["state"] == "summarizing" and sm.cp["next_chunk"] == 2
    assert len(sm.cp["summaries"]) == 2, "已完成的 2 块已在检查点"

    final = sm.run(turns)                              # 同检查点续跑
    assert sm.cp["state"] == "done"
    assert llm.summarize_calls == 5, "总摘要调用数恰为块数,绝无重算"
    assert final.startswith("MERGE") and final.count("|") == 4

    fresh = SegmentedSummarizer(FakeLLM(), window=2).run(turns)
    assert fresh == final, "无故障路径与断点续跑结果一致"
    print("分段摘要状态机通过:崩溃停在 summarizing,续跑只补 3 块,结果一致")
