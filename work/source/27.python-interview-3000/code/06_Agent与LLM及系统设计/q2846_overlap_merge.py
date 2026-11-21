"""Q2846 重叠块的召回合并:同源重叠命中拼回连续原文。

切块时为了让边界句子不被腰斩,相邻块通常带 overlap;代价是同一段
原文会以多个高度重叠的块被同时召回,上下文里同一段话出现三遍。
召回后按同源文档做区间合并:重叠 span 拼回连续原文,分数取最高。
"""


def merge_overlaps(hits):
    """hits: [{doc, start, end, score}],按文档合并重叠区间。"""
    by_doc = {}
    for h in hits:
        by_doc.setdefault(h["doc"], []).append(h)
    merged = []
    for doc in sorted(by_doc):
        spans = sorted(by_doc[doc], key=lambda h: (h["start"], h["end"]))
        cur = None
        for h in spans:
            if cur is not None and h["start"] < cur["end"]:
                cur["end"] = max(cur["end"], h["end"])
                cur["score"] = max(cur["score"], h["score"])
                cur["chunks"] += 1
            else:
                cur = {"doc": doc, "start": h["start"], "end": h["end"],
                       "score": h["score"], "chunks": 1}
                merged.append(cur)
    return merged


def main():
    hits = [
        {"doc": "A", "start": 0, "end": 100, "score": 0.91},
        {"doc": "A", "start": 80, "end": 180, "score": 0.74},
        {"doc": "A", "start": 160, "end": 260, "score": 0.83},
        {"doc": "A", "start": 300, "end": 400, "score": 0.60},  # 不相邻
        {"doc": "B", "start": 0, "end": 50, "score": 0.66},
    ]
    out = merge_overlaps(hits)
    a_spans = [m for m in out if m["doc"] == "A"]
    assert len(a_spans) == 2, a_spans
    assert a_spans[0] == {"doc": "A", "start": 0, "end": 260,
                          "score": 0.91, "chunks": 3}, a_spans[0]
    assert a_spans[1]["start"] == 300, a_spans[1]  # 不重叠的独立保留
    b = [m for m in out if m["doc"] == "B"][0]
    assert b["chunks"] == 1 and b["score"] == 0.66, b
    before = len(hits)
    after = len(out)
    assert after == 3 and after < before, (before, after)
    print("合并前 %d 块 → 合并后 %d 段" % (before, after))
    print("A 文档拼回:", a_spans[0])
    print("分数取最高 0.91,重复内容不再重复计费")


if __name__ == "__main__":
    main()
