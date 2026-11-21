"""混合检索:BM25 模拟 + 向量检索并行召回,RRF 融合排序。"""


def bm25_scores(query: str, docs: list[str]) -> dict[int, float]:
    """极简词频打分,模拟 BM25 的关键词倾向。"""
    terms = query.split()
    return {i: sum(d.count(t) for t in terms) for i, d in enumerate(docs)}


def vector_scores(query: str, docs: list[str]) -> dict[int, float]:
    def emb(t):
        return [ord(c) % 7 for c in t[:6].ljust(6, "x")]
    qv = emb(query)
    return {i: sum(a * b for a, b in zip(qv, emb(d))) for i, d in enumerate(docs)}


def rrf_fuse(rankings: list[list[int]], k: int = 60) -> list[int]:
    scores: dict[int, float] = {}
    for ranking in rankings:
        for rank, doc_id in enumerate(ranking, start=1):
            scores[doc_id] = scores.get(doc_id, 0) + 1.0 / (k + rank)
    return sorted(scores, key=lambda d: -scores[d])


def hybrid_search(query: str, docs: list[str], top_k: int = 3) -> list[int]:
    bm25_rank = [i for i, _ in sorted(bm25_scores(query, docs).items(), key=lambda x: -x[1])]
    vec_rank = [i for i, _ in sorted(vector_scores(query, docs).items(), key=lambda x: -x[1])]
    return rrf_fuse([bm25_rank, vec_rank])[:top_k]


if __name__ == "__main__":
    docs = ["错误码 ERR_5002 表示网关超时",
            "网关服务出现超时问题如何排查",
            "团队介绍与招聘信息"]
    print("BM25 路径:", sorted(bm25_scores("ERR_5002 超时", docs).items(), key=lambda x: -x[1]))
    print("RRF 融合结果:", hybrid_search("ERR_5002 超时", docs))
