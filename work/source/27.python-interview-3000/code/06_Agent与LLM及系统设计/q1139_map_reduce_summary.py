"""长文 map-reduce 摘要:分片并行摘要 + 树形归并,支持两级 reduce 防超窗。"""


class FakeLLM:
    def summarize(self, text, max_chars=40):
        # 桩:取每段首句模拟"抽取式摘要"
        sents = [s.strip() for s in text.replace("。", "。\n").split("\n") if s.strip()]
        return "。".join(s.content if hasattr(s, "content") else s for s in sents[:2])[:max_chars]


def chunk(doc, size=200, overlap=40):
    step = size - overlap
    return [doc[i:i + size] for i in range(0, len(doc), step)]


def map_reduce(llm, doc, fan_out=3):
    parts = chunk(doc)
    summaries = [llm.summarize(p) for p in parts]           # map 阶段可并行
    while len(summaries) > 1:                                # 树形归并防 reduce 超窗
        nxt = []
        for i in range(0, len(summaries), fan_out):
            group = summaries[i:i + fan_out]
            merged = " / ".join(f"片段{i+j}:{s}" for j, s in enumerate(group))
            nxt.append(llm.summarize(merged, max_chars=60) if len(group) > 1 else group[0])
        summaries = nxt
    return summaries[0], len(parts)


if __name__ == "__main__":
    llm = FakeLLM()
    doc = "第一章介绍了系统架构。系统分为四层。第二章讲检索增强。检索质量决定答案上限。" * 30
    summary, n_parts = map_reduce(llm, doc)
    print(f"原文 {len(doc)} 字 -> {n_parts} 片")
    print("最终摘要:", summary)
    assert n_parts >= 5 and 0 < len(summary) <= 80
    print("map-reduce 完成,reduce 未超窗")
