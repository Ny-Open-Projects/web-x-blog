---
title: [Q1193] 两阶段检索与 rerank 桩
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1193 · 两阶段检索与 rerank 桩

> 难度:★★★☆ | 标签:RAG, rerank

**问**:为什么召回之后还要 rerank?两阶段的成本怎么平衡?

**答**:第一阶段召回(bi-encoder/关键词)追求快与全,把候选从十万级压到百级,但 query 和文档独立编码,交互信息丢失,精度有限;第二阶段 rerank(cross-encoder 思路)把 query 与候选拼接后精细打分,精度高但每对都要计算,只能处理小候选集。配比:召回 100-200,重排取 top 5-10 进上下文。rerank 桩用"特征打分"模拟:词重叠 + 位置 + 短语匹配加权。工程要点:rerank 超时要有直通降级(直接用召回序),不能因重排挂掉整体失败。

```python
# file: code/06_Agent与LLM及系统设计/q1193_rerank_pipeline.py
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
```

**追问**:
- rerank 模型延迟高怎么兜底?答:设置独立超时与降级直通(用召回排序),并按 query 长度/候选数预估耗时,超预算直接跳过精排。
- 召回多少候选合适?答:看 rerank 吞吐——精排 P95 单条 10ms、预算 50ms 就给 5 条预算化的候选,宁少勿超时。
