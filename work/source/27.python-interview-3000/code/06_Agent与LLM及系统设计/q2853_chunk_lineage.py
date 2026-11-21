"""Q2853 重切后的块血缘映射:旧块到新块的对齐与引用续接。

语料重切后块 id 全变,历史答案里的引用就断了。重切时按字符区间
重叠建立旧块到新块的血缘映射,老引用凭映射续接到新块,重叠不足
一半的标成孤儿单独暴露,而不是悄悄指错。
"""


def build_lineage(old_chunks, new_chunks):
    """old/new: [{id, start, end}],按重叠比率对齐。"""
    mapping = {}
    orphans = []
    for oc in old_chunks:
        best_id, best_ratio = None, 0.0
        old_len = oc["end"] - oc["start"]
        for nc in new_chunks:
            lo = max(oc["start"], nc["start"])
            hi = min(oc["end"], nc["end"])
            overlap = max(0, hi - lo)
            ratio = overlap / float(old_len)
            if ratio > best_ratio or (ratio == best_ratio and best_id is None):
                best_ratio, best_id = ratio, nc["id"]
        if best_ratio >= 0.5:
            mapping[oc["id"]] = best_id
        else:
            orphans.append(oc["id"])
    return mapping, orphans


def resolve(citation, mapping):
    return mapping.get(citation)


def main():
    # 旧版按 10 字切块,新版按 15 字切块
    old_chunks = [
        {"id": "c1", "start": 0, "end": 10},
        {"id": "c2", "start": 10, "end": 20},
        {"id": "c3", "start": 20, "end": 30},
    ]
    new_chunks = [
        {"id": "n1", "start": 0, "end": 15},
        {"id": "n2", "start": 15, "end": 30},
    ]
    mapping, orphans = build_lineage(old_chunks, new_chunks)
    assert mapping == {"c1": "n1", "c2": "n1", "c3": "n2"}, (mapping, orphans)
    assert orphans == [], orphans
    # 历史答案引用 c2:重切后仍可解析到 n1
    assert resolve("c2", mapping) == "n1"
    # 新块与旧块错位严重时必须报孤儿,不能硬指
    old3 = [{"id": "c1", "start": 0, "end": 10}]
    new3 = [{"id": "n9", "start": 6, "end": 16}]
    mapping3, orphans3 = build_lineage(old3, new3)
    assert orphans3 == ["c1"] and mapping3 == {}, (mapping3, orphans3)
    print("血缘映射:", mapping)
    print("旧引用 c2 续接到:", resolve("c2", mapping))
    print("对不上的旧块进孤儿清单:", orphans3)


if __name__ == "__main__":
    main()
