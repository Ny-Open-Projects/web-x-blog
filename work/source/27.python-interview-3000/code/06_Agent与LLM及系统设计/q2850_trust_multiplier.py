"""Q2850 检索排序的来源可信度乘数:分级表 未知降权与封顶。

相关性分数不能代表可信度:论坛帖也能和官方文档算出一样高的相似度。
在重排阶段给每个来源乘一个可信度系数:官方域 1.0,百科 0.8,论坛
0.5,没登记过的来源按最低档对待,高分低信的来源再也无法霸占榜首。
"""

TRUST = {
    "help.example.com": 1.0,
    "wikipedia.org": 0.8,
    "forum.example.com": 0.5,
}
UNKNOWN_FACTOR = 0.3


def rerank(hits):
    out = []
    for h in hits:
        factor = TRUST.get(h["source"], UNKNOWN_FACTOR)
        final = min(h["score"] * factor, 1.0)   # 封顶防单一来源溢出
        out.append(dict(h, final=round(final, 4)))
    out.sort(key=lambda h: (-h["final"], h["source"]))
    return out


def main():
    hits = [
        {"doc": "x1", "source": "unknown-blog.io", "score": 0.99},
        {"doc": "f1", "source": "forum.example.com", "score": 0.95},
        {"doc": "g1", "source": "help.example.com", "score": 0.82},
        {"doc": "w1", "source": "wikipedia.org", "score": 0.80},
    ]
    out = rerank(hits)
    order = [h["doc"] for h in out]
    assert order == ["g1", "w1", "f1", "x1"], order  # 官方反超论坛
    assert out[0]["final"] == 0.82, out[0]  # 1.0 乘数不加分
    f1 = [h for h in out if h["doc"] == "f1"][0]
    assert abs(f1["final"] - 0.475) < 1e-6, f1  # 0.95 x 0.5,从第2掉到第3
    x1 = [h for h in out if h["doc"] == "x1"][0]
    assert x1["final"] == round(0.99 * 0.3, 4), x1  # 未知来源最低档垫底
    print("重排后:", [(h["doc"], h["final"]) for h in out])
    print("0.95 的论坛帖被压到 0.475,让位给 0.82 的官方文档")


if __name__ == "__main__":
    main()
