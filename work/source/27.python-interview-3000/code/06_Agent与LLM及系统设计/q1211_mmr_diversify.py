"""MMR 多样性重排:相关性 - 冗余惩罚,贪心选择平衡精度与覆盖。"""
import hashlib, math


def embed(text, dim=32):
    v = [0.0] * dim
    for tok in text.split():
        v[int(hashlib.md5(tok.encode()).hexdigest(), 16) % dim] += 1.0
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))


def mmr(query, candidates, k=3, lam=0.6):
    qv = embed(query)
    vecs = {c: embed(c) for c in candidates}
    selected, rest = [], list(candidates)
    while rest and len(selected) < k:
        def score(c):
            rel = cosine(qv, vecs[c])
            red = max((cosine(vecs[c], vecs[s]) for s in selected), default=0.0)
            return lam * rel - (1 - lam) * red
        best = max(rest, key=score)
        selected.append(best)
        rest.remove(best)
    return selected


if __name__ == "__main__":
    q = "退货 政策"
    cands = [
        "退货 政策 七天 无理由",
        "退货 政策 七天 无理由 细则",      # 与前者高度冗余
        "退货 运费 承担 规则",
        "退货 流程 操作 步骤",
        "会员 积分 规则",
        "会员 积分 说明",
    ]
    pure = sorted(cands, key=lambda c: cosine(embed(q), embed(c)), reverse=True)[:3]
    div = mmr(q, cands, k=3, lam=0.6)
    print("纯相关 top3:", pure)
    print("MMR top3  :", div)
    assert div[0] == pure[0], "最相关的必须排第一"
    dup = max(cosine(embed(div[i]), embed(div[j])) for i in range(3) for j in range(i + 1, 3))
    pure_dup = max(cosine(embed(pure[i]), embed(pure[j])) for i in range(3) for j in range(i + 1, 3))
    assert dup < pure_dup, "MMR 后最大冗余应低于纯相关排序"
    print(f"冗余度从 {pure_dup:.2f} 降到 {dup:.2f},覆盖更多政策面向")
