"""Q2847 检索深度收益曲线实测:top_k 扫描 找拐点。

top_k 不是拍脑袋定的:k 太小漏证据,k 太大灌噪音烧 token。拿评估集
扫一遍 k,画召回率随 k 的收益曲线,找「再加深几乎不再提升」的拐点,
用数据定检索深度,还能顺带算出每加一档要付多少上下文成本。
"""

VOCAB = ["退款", "发票", "物流", "合同", "条款", "库存"]
DOCS = {
    "d1": "退款 政策 退款 时限",
    "d2": "退款 流程 审核",
    "d3": "退款 发票 冲红",
    "d4": "发票 开具 抬头",
    "d5": "物流 发货 签收",
    "d6": "合同 条款 签署",
    "d7": "库存 盘点 补货",
    "d8": "退款 物流 运费",
}
EVAL = [
    ("退款", {"d1", "d2", "d3", "d8"}),
    ("发票", {"d3", "d4"}),
    ("物流", {"d5", "d8"}),
]


def embed(text):
    return [text.split(" ").count(w) for w in VOCAB]


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = sum(x * x for x in a) ** 0.5
    nb = sum(x * x for x in b) ** 0.5
    return dot / (na * nb) if na and nb else 0.0


def search(q, k):
    qv = embed(q)
    scored = [(cosine(qv, embed(t)), d) for d, t in DOCS.items()]
    scored.sort(key=lambda x: (-x[0], x[1]))
    return [d for _, d in scored[:k]]


def main():
    doc_chars = sum(len(t) for t in DOCS.values()) / float(len(DOCS))
    ks = [1, 2, 4, 6, 8]
    curve = []
    for k in ks:
        recalls = []
        for q, rel in EVAL:
            top = search(q, k)
            recalls.append(len(set(top) & rel) / float(len(rel)))
        curve.append((k, sum(recalls) / len(recalls), k * doc_chars))
    for k, r, cost in curve:
        print("k=%d recall=%.3f 上下文字符=%.0f" % (k, r, cost))
    recalls_only = [r for _, r, _ in curve]
    assert recalls_only == sorted(recalls_only), curve  # 召回单调不减
    peak = max(recalls_only)
    knee = next(k for k, r, _ in curve if r >= 0.9 * peak)
    assert knee <= 4, knee  # 拐点之前已拿到绝大部分收益
    print("拐点:k=%d,此后召回几乎不再提升,多灌的只有噪音" % knee)


if __name__ == "__main__":
    main()
