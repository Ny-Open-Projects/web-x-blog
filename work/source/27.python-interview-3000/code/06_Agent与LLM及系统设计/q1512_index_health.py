"""索引健康报告:覆盖率、孤儿块、陈旧占比、碎片度四项体检,输出可执行清单。"""
from collections import defaultdict


class IndexHealth:
    """索引体检器:对照源文档集合检查块的归属与新鲜度。"""

    def __init__(self, docs, chunks, index_entries, now_version):
        self.docs = docs                   # doc_id -> version
        self.chunks = chunks               # chunk_id -> {"doc", "version"}
        self.index_entries = index_entries # 已入索引的 chunk_id 集合
        self.now = now_version

    def report(self):
        doc_ids = set(self.docs)
        orphan_chunks = [c for c, m in self.chunks.items() if m["doc"] not in doc_ids]
        missing_chunks = [c for c, m in self.chunks.items()
                          if m["doc"] in doc_ids and c not in self.index_entries]
        stale_chunks = [c for c, m in self.chunks.items()
                        if m["doc"] in doc_ids and m["version"] < self.docs[m["doc"]]]
        coverage = len(self.chunks) and (len(self.chunks) - len(orphan_chunks)) / len(self.chunks)

        # 碎片度:某文档的块数过多即切分过碎
        per_doc = defaultdict(int)
        for m in self.chunks.values():
            per_doc[m["doc"]] += 1
        fragmented = {d: n for d, n in per_doc.items() if n > 6}

        actions = []
        if orphan_chunks:
            actions.append("删除孤儿块 " + str(orphan_chunks))
        if missing_chunks:
            actions.append("补建索引 " + str(missing_chunks))
        if stale_chunks:
            actions.append("重建陈旧块 " + str(stale_chunks))
        if fragmented:
            actions.append("合并碎片文档 " + str(sorted(fragmented)))
        if not actions:
            actions.append("健康 无需动作")
        return {"chunk_total": len(self.chunks), "coverage": round(coverage, 2),
                "orphans": orphan_chunks, "missing": missing_chunks,
                "stale": stale_chunks, "fragmented": fragmented, "actions": actions}


if __name__ == "__main__":
    docs = {"d1": 3, "d2": 2, "d3": 5}                 # d1 已到 v3 d2 到 v2
    chunks = {
        "c1": {"doc": "d1", "version": 3},
        "c2": {"doc": "d1", "version": 2},             # 陈旧
        "c3": {"doc": "d2", "version": 2},
        "c4": {"doc": "d9", "version": 1},             # 源文档已删除 孤儿
        "c5": {"doc": "d3", "version": 5},
    }
    chunks.update({"c6_%d" % i: {"doc": "d3", "version": 5} for i in range(6)})  # d3 共 7 块 碎片
    indexed = {"c1", "c3", "c4", "c5", "c6_0", "c6_1", "c6_2"}         # c2 c6_3..6 缺索引

    h = IndexHealth(docs, chunks, indexed, now_version=3).report()
    assert h["chunk_total"] == 11
    assert h["orphans"] == ["c4"]
    assert sorted(h["missing"]) == ["c2", "c6_3", "c6_4", "c6_5"]
    assert h["stale"] == ["c2"]
    assert h["fragmented"] == {"d3": 7}
    assert h["coverage"] == 0.91
    assert any("孤儿" in a for a in h["actions"])
    assert any("补建" in a for a in h["actions"])
    assert any("陈旧" in a for a in h["actions"])
    assert any("碎片" in a for a in h["actions"])

    clean = IndexHealth({"d1": 1}, {"c1": {"doc": "d1", "version": 1}}, {"c1"}, 1).report()
    assert clean["actions"] == ["健康 无需动作"] and clean["coverage"] == 1.0
    print("索引体检通过:孤儿 1 缺索引 5 陈旧 1 碎片 d3 七块 四项动作齐全")
