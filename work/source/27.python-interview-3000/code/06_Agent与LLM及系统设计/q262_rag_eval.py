"""实现 Recall@k、MRR 与忠实度检查(答案句子是否被证据支撑)。"""


def recall_at_k(retrieved: list[str], relevant: set[str], k: int) -> float:
    hit = sum(1 for d in retrieved[:k] if d in relevant)
    return hit / len(relevant) if relevant else 0.0


def mrr(retrieved: list[str], relevant: set[str]) -> float:
    for rank, d in enumerate(retrieved, start=1):
        if d in relevant:
            return 1.0 / rank
    return 0.0


def faithfulness(answer: str, evidence: list[str]) -> float:
    """伪忠实度:答案中每句是否能被某条证据的字面重叠支撑。"""
    sents = [s for s in answer.split("。") if s]
    supported = 0
    for s in sents:
        words = set(s)
        ok = any(len(words & set(ev)) / max(1, len(words)) > 0.3 for ev in evidence)
        supported += ok
    return supported / len(sents) if sents else 1.0


if __name__ == "__main__":
    retrieved = ["文档A", "文档B", "文档C"]
    relevant = {"文档A", "文档C"}
    print(f"Recall@2={recall_at_k(retrieved, relevant, 2):.2f} "
          f"Recall@3={recall_at_k(retrieved, relevant, 3):.2f} "
          f"MRR={mrr(retrieved, relevant):.2f}")
    ans = "RAG 检索文档后生成答案。 completely hallucinated sentence"
    ev = ["RAG 检索相关文档"]
    print(f"忠实度={faithfulness(ans, ev):.2f}")
