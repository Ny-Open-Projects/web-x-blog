"""语义缓存实现:embedding 相似度命中则直接返回,否则回源 LLM 并写入缓存。"""
from __future__ import annotations


def embed(text: str, dim: int = 12) -> list[int]:
    """Toy 嵌入:字符 2-gram 词袋。只反映字面相似;真实语义缓存用 embedding 模型。"""
    v = [0] * dim
    for a, b in zip(text, text[1:]):
        v[(ord(a) * 7 + ord(b)) % dim] += 1
    return v


def sim(a, b) -> float:
    na = sum(x * x for x in a) ** 0.5
    nb = sum(y * y for y in b) ** 0.5
    if not na or not nb:
        return 0.0
    return sum(x * y for x, y in zip(a, b)) / (na * nb)  # 余弦相似度


class SemanticCache:
    def __init__(self, threshold: float = 0.85):
        self.threshold = threshold
        self.store: list[tuple[str, str]] = []   # (query, answer)

    def lookup(self, query: str) -> str | None:
        qv = embed(query)
        for q, ans in self.store:
            if sim(qv, embed(q)) >= self.threshold:
                return f"[缓存命中] {ans}"
        return None

    def put(self, query: str, answer: str):
        self.store.append((query, answer))


class OriginLLM:
    def chat(self, q: str) -> str:
        return f"[回源生成] 关于「{q}」的详细回答"


def answer_with_cache(cache, llm, query: str) -> str:
    hit = cache.lookup(query)
    if hit:
        return hit
    ans = llm.chat(query)
    cache.put(query, ans)
    return ans


if __name__ == "__main__":
    cache, llm = SemanticCache(), OriginLLM()
    print(answer_with_cache(cache, llm, "退货政策是什么"))
    print(answer_with_cache(cache, llm, "退货政策是什么呢"))  # 2-gram 高度重叠,应命中
    print(answer_with_cache(cache, llm, "怎么开发票"))        # 与缓存条目无共同 2-gram,回源
