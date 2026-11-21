"""句子窗口检索:句子级索引,命中句扩展前后 W 句,带相似度门控。"""
import hashlib, math


def embed(text, dim=64):
    v = [0.0] * dim
    for tok in text.split():
        v[int(hashlib.md5(tok.encode()).hexdigest(), 16) % dim] += 1.0
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))


class SentenceWindowIndex:
    def __init__(self, sents):
        self.sents = [s.strip() for s in sents if s.strip()]
        self.vecs = [embed(s) for s in self.sents]

    def search(self, q, k=1, window=2, gate=0.1):
        qv = embed(q)
        scored = sorted(range(len(self.sents)),
                        key=lambda i: cosine(qv, self.vecs[i]), reverse=True)[:k]
        contexts = []
        for i in scored:
            lo, hi = max(0, i - window), min(len(self.sents), i + window + 1)
            picked = [self.sents[j] for j in range(lo, hi)
                      if j == i or cosine(qv, self.vecs[j]) >= gate]
            contexts.append({"center": self.sents[i], "window": picked})
        return contexts


if __name__ == "__main__":
    sents = [
        "退货 政策 支持 七天 无理由 退货",
        "退货运费 由 买家 承担",
        "质量 问题 商家 承担 运费",
        "发货 时间 为 48 小时 内",
        "偏远 地区 延长 至 72 小时",
    ]
    idx = SentenceWindowIndex(sents)
    ctx = idx.search("退货运费 承担", k=1, window=2, gate=0.05)
    print("中心句:", ctx[0]["center"])
    print("窗口句:")
    for s in ctx[0]["window"]:
        print("  -", s)
    assert ctx[0]["center"].startswith("退货运费"), "必须命中中心句"
    assert any("商家" in s for s in ctx[0]["window"]), "相关邻句纳入窗口"
    assert not any("偏远" in s for s in ctx[0]["window"]), "不相关邻句被门控滤掉"
    print("句子窗口 + 相似度门控生效")
