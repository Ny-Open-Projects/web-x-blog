"""检索宽度自适应:短窄问题用小 top_k,模糊多义问题自动加宽,预算封顶。"""
import math
from collections import Counter


def query_entropy(query_tokens):
    c = Counter(query_tokens)
    total = len(query_tokens)
    ent = 0.0
    for v in c.values():
        p = v / total
        ent -= p * math.log2(p)
    return ent


def pick_topk(query_tokens, k_min=2, k_max=8, cap=6):
    ent = query_entropy(query_tokens)
    if ent <= 1.0:
        k = k_min
    elif ent <= 1.8:
        k = k_min + 2
    else:
        k = k_max
    return min(k, cap), ent


def retrieve(index, query, k):
    return index[:k]


if __name__ == "__main__":
    index = ["d%d" % i for i in range(10)]
    k1, e1 = pick_topk(["退货", "政策"])
    k2, e2 = pick_topk(["那个", "东西", "怎么", "弄", "帮忙", "看看"])
    k3, e3 = pick_topk(["退货"])
    assert k1 == 2 and k3 == 2, "聚焦查询用最小宽度"
    assert k2 > k1, "高熵模糊查询自动加宽"
    k4, _ = pick_topk(["模糊", "查询", "很", "发散", "完全", "没有", "重点"], cap=5)
    assert k4 == 5, "宽度受预算封顶"
    assert e2 > e1 >= 0
    assert retrieve(index, "q", k2) == index[:k2]
    print("自适应宽度通过:低熵收窄 高熵加宽 预算封顶")
