"""多路召回融合:两路分数量纲不同,先各自归一再加权融合,量纲直加是经典错误。"""


def minmax(scores):
    lo, hi = min(scores), max(scores)
    if hi == lo:
        return [0.5] * len(scores)
    return [(s - lo) / (hi - lo) for s in scores]


def zscore(scores):
    n = len(scores)
    mean = sum(scores) / n
    var = sum((s - mean) ** 2 for s in scores) / n
    std = var ** 0.5 or 1.0
    return [(s - mean) / std for s in scores]


def fuse(bm25, vec, w=(0.4, 0.6), method="minmax"):
    norm = minmax if method == "minmax" else zscore
    a, b = norm(bm25), norm(vec)
    return [round(w[0] * x + w[1] * y, 4) for x, y in zip(a, b)]


if __name__ == "__main__":
    ids = ["d0 双路都好", "d1 只有词面", "d2 只有语义"]
    bm25 = [18.0, 19.0, 2.0]
    vec = [0.90, 0.10, 0.95]
    naive = [round(a + b, 3) for a, b in zip(bm25, vec)]
    assert ids[max(range(3), key=lambda i: naive[i])] == "d1 只有词面", "量纲直加被词面分淹没"
    fused = fuse(bm25, vec)
    order = [ids[i] for i in sorted(range(3), key=lambda i: -fused[i])]
    assert order[0] == "d0 双路都好", "归一后融合 双好文档登顶"
    assert fused[2] > fused[1], "语义强于纯词面命中"
    fused_z = fuse(bm25, vec, method="z")
    assert [ids[i] for i in sorted(range(3), key=lambda i: -fused_z[i])][0] == "d0 双路都好"
    flat = fuse([5.0, 5.0], [0.3, 0.3])
    assert flat == [0.5, 0.5], "单一路内无区分度时归一退化为中性分"
    print("分数归一通过:量纲问题复现 min-max 与 z 分数融合 等值退化")
