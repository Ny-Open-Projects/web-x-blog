"""检索命中率评估器:双检索器对比 hit@k 曲线,定位回归查询。用 hash 假嵌入。"""
import hashlib
import math


def embed(text, dim=32):
    """假嵌入:按字符 3-gram 哈希累加到定长向量并归一化。"""
    vec = [0.0] * dim
    padded = " " + text + " "
    for i in range(len(padded) - 2):
        h = int(hashlib.md5(padded[i:i + 3].encode()).hexdigest(), 16)
        vec[h % dim] += 1.0
    norm = math.sqrt(sum(v * v for v in vec)) or 1.0
    return [v / norm for v in vec]


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))


def build_index(docs):
    return [(did, embed(text)) for did, text in docs.items()]


class Retriever:
    """混合检索桩:0.5 余弦向量分 + 0.5 字符召回分,top-k 输出。"""

    def __init__(self, docs, name):
        self.index = build_index(docs)
        self.raw = dict(docs)
        self.name = name

    @staticmethod
    def _lexical(query, text):
        q = set(query) - {" "}
        t = set(text) - {" "}
        return len(q & t) / max(1, len(q))

    def search(self, query, k=3):
        qv = embed(query)
        scored = []
        for did, dv in self.index:
            s = 0.5 * cosine(qv, dv) + 0.5 * self._lexical(query, self.raw[did])
            scored.append((did, s))
        scored.sort(key=lambda t: -t[1])
        return [did for did, _ in scored[:k]]


class HitRateEvaluator:
    """对比两个检索器:逐 k 命中率、MRR,并输出回退查询清单。"""

    def __init__(self, golden):
        self.golden = golden               # [(query, {relevant_ids})]

    def hit_curve(self, retriever, ks=(1, 2, 3)):
        curve = {}
        for k in ks:
            hits = sum(any(g in retriever.search(q, k) for g in rel) for q, rel in self.golden)
            curve[k] = hits / len(self.golden)
        return curve

    def mrr(self, retriever):
        total = 0.0
        for q, rel in self.golden:
            ranked = retriever.search(q, k=10)
            for i, did in enumerate(ranked, 1):
                if did in rel:
                    total += 1.0 / i
                    break
        return total / len(self.golden)

    def regressions(self, base, cand, k=3):
        """候选比基线变差的查询,即回归点。"""
        out = []
        for q, rel in self.golden:
            b, c = any(g in base.search(q, k) for g in rel), any(g in cand.search(q, k) for g in rel)
            if b and not c:
                out.append(q)
        return out


if __name__ == "__main__":
    docs = {"d1": "退款流程 需要在订单页申请 48 小时到账",
            "d2": "会员积分 每消费一元累计一分 年底清零",
            "d3": "发票申请 电子发票 开票信息 在个人中心",
            "d4": "物流查询 快递单号 在订单详情查看",
            "d5": "账户注销 二次验证 短信验证码"}
    golden = [("退款到账要多久", {"d1"}), ("怎么开发票", {"d3"}),
              ("积分什么时候过期", {"d2"}), ("快递到哪了怎么查", {"d4"})]

    v1 = Retriever(docs, "v1")
    v2 = Retriever(docs, "v2")
    # v2 模拟索引污染:d1 被错误文本覆盖
    docs_v2 = dict(docs)
    docs_v2["d1"] = "促销活动 全场满减 限时优惠"
    v2_polluted = Retriever(docs_v2, "v2-polluted")

    ev = HitRateEvaluator(golden)
    c1 = ev.hit_curve(v1)
    assert c1[1] == 1.0 and c1[3] == 1.0, "干净索引全命中"
    assert ev.mrr(v1) == 1.0

    c2 = ev.hit_curve(v2_polluted)
    assert c2[1] < c1[1], "污染后 hit@1 必须下降"
    reg = ev.regressions(v1, v2_polluted)
    assert reg == ["退款到账要多久"], "回归定位应指向退款问题"
    print("命中率评估器通过:v1 hit@1 =", c1[1], "v2 hit@1 =", c2[1], "回归查询:", reg)
