"""两阶段检索:粗召回 top-N -> rerank 桩精排 -> top-k 进上下文,带超时降级。"""
import hashlib, math, time


def embed(text, dim=64):
    v = [0.0] * dim
    for tok in text.split():
        v[int(hashlib.md5(tok.encode()).hexdigest(), 16) % dim] += 1.0
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))


def recall(docs, vecs, q, n=8):
    qv = embed(q)
    return sorted(docs, key=lambda d: cosine(embed(d), qv), reverse=True)[:n]


class Reranker:
    def score(self, q, doc):
        q_terms, d_terms = set(q.split()), set(doc.split())
        overlap = len(q_terms & d_terms) / (len(q_terms) or 1)
        phrase = 0.5 if " ".join(q.split()) in doc else 0.0
        return 0.6 * overlap + 0.4 * phrase

    def rerank(self, q, docs, k=3, timeout=0.01):
        t0 = time.monotonic()
        try:
            scored = sorted(docs, key=lambda d: self.score(q, d), reverse=True)[:k]
            if time.monotonic() - t0 > timeout:
                raise TimeoutError
            return scored, "reranked"
        except TimeoutError:
            return docs[:k], "fallback_recall_order"


if __name__ == "__main__":
    docs = [
        "退货运费 由 买家 承担 特殊 情况 除外",
        "七天 无理由 退货 流程",
        "退货 时 请 保持 商品 完好",
        "发货 时间 48 小时",
        "运费 险 说明 满 99 元 赠送",
        "质量问题 退货运费 商家 承担",
        "退款 时效 3 个 工作日",
        "会员 退货运费 险 规则",
        "其他 无关 文档 内容 展示",
    ]
    q = "退货运费 谁 承担"
    candidates = recall(docs, None, q, n=8)
    print("粗召回:", [d[:12] for d in candidates])
    rr = Reranker()
    final, mode = rr.rerank(q, candidates, k=3)
    print(f"精排模式={mode}:", final)
    assert mode == "reranked"
    assert final[0] in ("退货运费 由 买家 承担 特殊 情况 除外", "质量问题 退货运费 商家 承担"), "高重叠文档排前"
    assert "发货 时间 48 小时" not in final, "低相关候选被重排挤掉"
    print("两阶段: 粗召回保全,精排提质")
