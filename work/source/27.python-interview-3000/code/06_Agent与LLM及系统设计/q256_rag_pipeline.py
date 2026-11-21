"""最小 RAG 全链路:假 embedding + 假检索 + FakeLLM 生成,验证数据流转。"""


def fake_embed(text: str) -> list[int]:
    return [ord(c) % 7 for c in text[:8].ljust(8, "x")]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


class VectorStore:
    def __init__(self):
        self.vectors: list[tuple[str, list[int]]] = []

    def add(self, chunks: list[str]):
        self.vectors += [(c, fake_embed(c)) for c in chunks]

    def search(self, query: str, k: int = 2) -> list[str]:
        qv = fake_embed(query)
        ranked = sorted(self.vectors, key=lambda x: -dot(x[1], qv))
        return [c for c, _ in ranked[:k]]


class FakeGenLLM:
    def chat(self, messages):
        ctx = next(m["content"] for m in messages if m["role"] == "system")
        return f"根据检索证据回答:{ctx[:30]}..."


def rag_answer(store, llm, query: str) -> str:
    topk = store.search(query, k=2)
    context = "\n".join(f"[片段{i}] {c}" for i, c in enumerate(topk))
    messages = [{"role": "system", "content": context},
                {"role": "user", "content": query}]
    return llm.chat(messages)


if __name__ == "__main__":
    store = VectorStore()
    store.add(["RAG 通过检索外部知识增强大模型回答",
               "向量数据库支持近似最近邻搜索 ANN",
               "今天的天气是晴天,气温 12 度"])
    print(rag_answer(store, FakeGenLLM(), "什么是 RAG?"))
