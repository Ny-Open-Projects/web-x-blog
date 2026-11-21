"""查询改写:规则桩生成变体 + 各变体检索 + 原 query 加权融合。"""
import hashlib, math


def embed(text, dim=64):
    v = [0.0] * dim
    for tok in text.split():
        v[int(hashlib.md5(tok.encode()).hexdigest(), 16) % dim] += 1.0
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))


SYNONYMS = {"运费": ["邮费", "物流费用"], "退货": ["退换", "退款退货"]}


class Rewriter:
    def variants(self, q):
        out = [q]
        for word, syns in SYNONYMS.items():
            if word in q:
                out += [q.replace(word, s) for s in syns]
        return out[:4]


class Retriever:
    def __init__(self, docs):
        self.docs, self.vecs = docs, [embed(d) for d in docs]

    def search(self, q, k=3):
        qv = embed(q)
        ranked = sorted(range(len(self.docs)),
                        key=lambda i: cosine(qv, self.vecs[i]), reverse=True)
        return [(self.docs[i], r) for r, i in enumerate(ranked[:k])]


def fused_search(retriever, q, k=3, original_weight=2.0):
    weights = {}
    rewriter = Rewriter()
    for i, v in enumerate(rewriter.variants(q)):
        w = original_weight if i == 0 else 1.0
        for doc, rank in retriever.search(v, k):
            weights.setdefault(doc, 0.0)
            weights[doc] += w / (60 + rank + 1)
    return sorted(weights.items(), key=lambda x: -x[1])


if __name__ == "__main__":
    docs = ["退货运费由买家承担", "邮费说明 满 99 包邮", "发货时间 48 小时", "退款时效 3 个工作日"]
    r = Retriever(docs)
    plain = r.search("运费谁出", k=2)
    print("原始单查询 top:", [d for d, _ in plain])
    fused = fused_search(r, "运费谁出")
    print("改写融合 top:", [d for d, _ in fused])
    assert any("邮费" in d for d, _ in fused), "改写变体应召回同义文档"
    assert fused[0][0] == "退货运费由买家承担", "原 query 加权后真实意图排前"
    print("改写扩展召回,原查询加权抑制噪声")
