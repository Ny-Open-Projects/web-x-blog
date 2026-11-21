"""负样本存档:检索靠前但不该命中的块记为 hard negative,评估时验证不再上榜。"""


class NegativeArchive:
    def __init__(self):
        self.items = []

    def record(self, query, doc, rank, reason="ranked_high_but_irrelevant"):
        self.items.append({"query": query, "doc": doc, "rank": rank, "reason": reason})

    def penalty_view(self):
        pen = {}
        for it in self.items:
            pen.setdefault(it["query"], {})[it["doc"]] = -0.3
        return pen


def rerank_with_archive(ranked, query, archive):
    pen = archive.penalty_view().get(query, {})
    adj = [(d, round(s + pen.get(d, 0.0), 4)) for d, s in ranked]
    adj.sort(key=lambda t: t[1], reverse=True)
    return adj


if __name__ == "__main__":
    arch = NegativeArchive()
    arch.record("苹果 价格", "iphone 发布会", 1)
    ranked = [("iphone 发布会", 0.9), ("水果 促销", 0.8)]
    before = [d for d, _ in ranked]
    after = rerank_with_archive(ranked, "苹果 价格", arch)
    assert before[0] == "iphone 发布会", "负样本原本高居榜首"
    assert after[0][0] == "水果 促销", "惩罚后正例登顶"
    assert after[1][1] == 0.6, "hard negative 被降权"
    arch.record("苹果 价格", "iphone 发布会", 1)
    assert len(arch.penalty_view()["苹果 价格"]) == 1, "重复记录去重 不叠加惩罚"
    other = rerank_with_archive(ranked, "苹果 手机", arch)
    assert other[0][0] == "iphone 发布会", "惩罚只对同查询生效"
    print("负样本存档通过:记录 hard negative 查询级降权 隔离生效范围")
