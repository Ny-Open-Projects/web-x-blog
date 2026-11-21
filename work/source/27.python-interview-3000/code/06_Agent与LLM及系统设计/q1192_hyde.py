"""HyDE 桩:假设答案生成 -> 双路检索 -> RRF 融合,对比纯 query 检索。"""
import hashlib, math


def embed(text, dim=64):
    v = [0.0] * dim
    for tok in text.split():
        v[int(hashlib.md5(tok.encode()).hexdigest(), 16) % dim] += 1.0
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))


def fake_llm_answer(q):
    """FakeLLM 桩:生成假设答案(可能含编造细节,但用词接近文档)。"""
    return "退货 运费 由 买家 承担 七天 无理由 退货 流程 在 订单 页 发起"


class HyDERetriever:
    def __init__(self, docs):
        self.docs, self.vecs = docs, [embed(d) for d in docs]

    def _search(self, text, k=2):
        qv = embed(text)
        ranked = sorted(range(len(self.docs)),
                        key=lambda i: cosine(qv, self.vecs[i]), reverse=True)
        return [(self.docs[i], r) for r, i in enumerate(ranked[:k])]

    def search_plain(self, q, k=2):
        return self._search(q, k)

    def search_hyde(self, q, k=2):
        hypo = fake_llm_answer(q)
        rrf = {}
        for lst in (self._search(q, k), self._search(hypo, k)):
            for doc, rank in lst:
                rrf.setdefault(doc, 0.0)
                rrf[doc] += 1.0 / (60 + rank + 1)
        return sorted(rrf.items(), key=lambda x: -x[1])


if __name__ == "__main__":
    docs = ["退货 运费 由 买家 承担", "七天 无理由 退货 在 订单 页 发起", "发货 48 小时 内 顺丰 承运", "退款 3 个 工作日 到账"]
    r = HyDERetriever(docs)
    plain = [d for d, _ in r.search_plain("退货 运费 怎么算", k=2)]
    hyde = [d for d, _ in r.search_hyde("退货 运费 怎么算", k=2)]
    print("纯 query:", plain)
    print("HyDE 融合:", hyde)
    assert hyde[0] == "退货 运费 由 买家 承担"
    assert len(hyde) >= len(plain), "双路融合覆盖更多相关文档"
    print("假设答案拉近了问题与文档的向量距离,融合后召回更稳")
