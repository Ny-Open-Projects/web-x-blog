"""Q2586 答案引用的页码级定位:块级引用归并成页码区间。

块是检索单位,页是人读单位;引用若干块时把块的页区间排序合并
相邻页,输出连续页码,再渲染成 第3-5页 这样的可读引用。
"""

CHUNKS = {
    "c1": (3, 4), "c2": (4, 5), "c3": (9, 9), "c4": (2, 2),
}


def pages_of(chunk_ids):
    spans = sorted(CHUNKS[c] for c in chunk_ids)
    merged = []
    for s, e in spans:
        if merged and s <= merged[-1][1] + 1:  # 相邻页也算连续
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])
    return [tuple(x) for x in merged]


def cite_text(chunk_ids):
    parts = []
    for s, e in pages_of(chunk_ids):
        parts.append("第" + str(s) + "页" if s == e else "第" + str(s) + "-" + str(e) + "页")
    return "、".join(parts)


def main():
    out = pages_of(["c1", "c2", "c3"])
    assert out == [(3, 5), (9, 9)], out
    assert cite_text(["c1", "c2"]) == "第3-5页", cite_text(["c1", "c2"])
    assert cite_text(["c4"]) == "第2页"
    assert cite_text(["c3", "c4"]) == "第2页、第9页"
    print("引用 [c1,c2,c3] 归并为:", cite_text(["c1", "c2", "c3"]))
    print("引用 [c3,c4] 归并为:", cite_text(["c3", "c4"]))


if __name__ == "__main__":
    main()
