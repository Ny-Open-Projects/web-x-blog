"""Q2854 检索结果的来源封顶:防止单一来源垄断上下文。

一个站点 SEO 做得好,同一来源能占满 top_k,生成端就只能听到一家
之言。装配上下文时按来源设上限:超额的先跳过,让位给其他来源,
最后不够再回头补,既保多样性又不浪费高相关结果。
"""


def cap_per_source(ranked, cap, top_n):
    out = []
    counts = {}
    overflow = []
    for h in ranked:
        s = h["source"]
        if counts.get(s, 0) >= cap:
            overflow.append(h)
            continue
        out.append(h)
        counts[s] = counts.get(s, 0) + 1
        if len(out) == top_n:
            return out, overflow
    # 名额没满:回头用超额结果补
    while overflow and len(out) < top_n:
        out.append(overflow.pop(0))
    return out, overflow


def main():
    ranked = [
        {"doc": "a1", "source": "wiki", "score": 0.93},
        {"doc": "a2", "source": "wiki", "score": 0.90},
        {"doc": "a3", "source": "wiki", "score": 0.88},
        {"doc": "b1", "source": "gov", "score": 0.80},
        {"doc": "b2", "source": "gov", "score": 0.78},
    ]
    out, overflow = cap_per_source(ranked, cap=2, top_n=4)
    docs = [h["doc"] for h in out]
    assert docs == ["a1", "a2", "b1", "b2"], docs   # a3 让位
    assert [h["doc"] for h in overflow] == ["a3"], overflow
    counts = {}
    for h in out:
        counts[h["source"]] = counts.get(h["source"], 0) + 1
    assert counts == {"wiki": 2, "gov": 2}, counts
    # 名额空缺时回头补位:超额的 a2 a3 按原顺序回填
    out2, _ = cap_per_source(ranked, cap=1, top_n=4)
    assert [h["doc"] for h in out2] == ["a1", "b1", "a2", "a3"], out2
    print("封顶后 top4:", docs)
    print("被让位的:", [h["doc"] for h in overflow])
    print("补位模式:", [h["doc"] for h in out2])


if __name__ == "__main__":
    main()
