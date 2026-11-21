"""元数据过滤前置 vs 后置:前置先过滤后排序,后置浪费召回名额,利用率可量化。"""
import math

_VOCAB = {}


def embed(text, dim=64):
    """词表登记式假嵌入:token 顺序登记,小词表内零碰撞,确定性可复现。"""
    v = [0.0] * dim
    for tok in text.split():
        if tok not in _VOCAB:
            _VOCAB[tok] = len(_VOCAB)
        v[_VOCAB[tok] % dim] += 1.0
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))


CORPUS = [
    {"id": "c1", "year": 2024, "text": "2024 退货 政策 七天"},
    {"id": "c2", "year": 2024, "text": "2024 保修 条款 两年"},
    {"id": "c3", "year": 2020, "text": "2020 退货 政策 旧版"},
    {"id": "c4", "year": 2019, "text": "2019 运费 规则"},
    {"id": "c5", "year": 2021, "text": "2021 退货 政策 过期"},
]


def pre_filter_search(query, year, topk=3):
    """前置:先按元数据筛候选池,再在池内向量排序,名额全花在合格文档上。"""
    pool = [c for c in CORPUS if c["year"] == year]
    q = embed(query)
    ranked = sorted(((cosine(q, embed(c["text"])), c) for c in pool),
                    key=lambda p: -p[0])
    return [c for _, c in ranked[:topk]]


def post_filter_search(query, year, topk=3):
    """后置:先全局召回 top-k 再按元数据丢弃,名额被旧文档占掉。"""
    q = embed(query)
    ranked = sorted(((cosine(q, embed(c["text"])), c) for c in CORPUS),
                    key=lambda p: -p[0])
    hits = [c for _, c in ranked[:topk]]
    return [c for c in hits if c["year"] == year]


if __name__ == "__main__":
    pre = pre_filter_search("退货 政策", 2024)
    post = post_filter_search("退货 政策", 2024)

    assert len(post) == 1, "后置 top3 里两条旧文档浪费了名额"
    assert len(pre) == 2 and all(c["year"] == 2024 for c in pre), "前置名额全部合格"
    assert "c3" not in [c["id"] for c in pre] and "c5" not in [c["id"] for c in pre]
    assert pre[0]["id"] == "c1", "前置不改变相关性排序"

    wasted = 3 - len(post)
    assert wasted == 2, "可量化:后置浪费 2 个召回名额"
    print("过滤前置通过:同 top3 下前置命中 2 条合格,后置仅 1 条,浪费名额可见")
