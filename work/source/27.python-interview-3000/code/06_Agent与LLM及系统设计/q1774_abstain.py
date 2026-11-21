"""检索不足的拒答决策:分数门限加候选不足双门槛,拒答带原因与建议改写。"""
import math

_VOCAB = {}


def embed(text, dim=32):
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


KNOWLEDGE = ["退货 政策 七天 无 理由", "发票 开具 流程"]


def top_scores(query, corpus, k=3):
    q = embed(query)
    scored = sorted((cosine(q, embed(t)) for t in corpus), reverse=True)
    return scored[:k]


class AbstainPolicy:
    def __init__(self, score_gate=0.35, min_docs=1):
        self.score_gate = score_gate
        self.min_docs = min_docs

    def decide(self, query, scores):
        best = max(scores, default=0.0)
        if len(scores) < self.min_docs or best < self.score_gate:
            return {"action": "abstain",
                    "reason": "候选不足或最高分 %.2f 低于门限 %.2f" % (best, self.score_gate),
                    "fallback": "这个问题我还没掌握可靠资料,先不猜;可换个说法或补充背景再问",
                    "suggest": "试试只问单一事实,例如: " + query[:6] + " 的官方规则是什么"}
        return {"action": "answer", "confidence": round(best, 3)}


if __name__ == "__main__":
    policy = AbstainPolicy()
    good = policy.decide("退货 政策 是 什么", top_scores("退货 政策 是 什么", KNOWLEDGE))
    assert good["action"] == "answer" and good["confidence"] >= 0.35

    bad = policy.decide("团建 报销 额度", top_scores("团建 报销 额度", KNOWLEDGE))
    assert bad["action"] == "abstain" and "低于门限" in bad["reason"]
    assert "换个说法" in bad["fallback"] and "官方规则" in bad["suggest"]

    empty = policy.decide("任意", [])
    assert empty["action"] == "abstain", "候选为零直接拒答"
    print("拒答决策通过:门限与候选数双门槛,拒答带原因 兜底话术 建议改写")
