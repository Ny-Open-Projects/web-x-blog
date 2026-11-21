"""多路召回 RRF 融合:关键词路 + 向量路,按排名融合,鲁棒于量纲差异。"""
import hashlib, math


def embed(text, dim=64):
    v = [0.0] * dim
    for tok in text.split():
        v[int(hashlib.md5(tok.encode()).hexdigest(), 16) % dim] += 1.0
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


def keyword_search(docs, q, k=5):
    terms = q.split()
    scored = [(d, sum(d.count(t) for t in terms)) for d in docs]
    scored = [d for d, s in sorted(scored, key=lambda x: -x[1]) if s > 0][:k]
    return scored


def vector_search(docs, q, k=5):
    qv = embed(q)
    return sorted(docs, key=lambda d: cosine(embed(d), qv), reverse=True)[:k]


def rrf_fuse(list_a, list_b, k=60, top=3):
    scores = {}
    for lst in (list_a, list_b):
        for rank, doc in enumerate(lst):
            scores.setdefault(doc, 0.0)
            scores[doc] += 1.0 / (k + rank + 1)
    return sorted(scores.items(), key=lambda x: -x[1])[:top]


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))


if __name__ == "__main__":
    docs = [
        "错误码 E1203 表示超时",
        "订单超时未支付会自动关闭",
        "支付回调失败重试三次",
        "E1203 常见于网络抖动",
        "退货流程说明",
    ]
    q = "E1203 超时"
    kw = keyword_search(docs, q)
    vec = vector_search(docs, q)
    print("关键词路:", kw)
    print("向量路  :", vec)
    fused = rrf_fuse(kw, vec)
    print("RRF 融合:", [(d[:14], round(s, 4)) for d, s in fused])
    assert any("E1203" in d for d, _ in fused[:2]), "精确术语必须靠关键词路拉进结果"
    assert fused[0][0] in kw and fused[0][0] in vec, "两路共同认可者应排最前"
