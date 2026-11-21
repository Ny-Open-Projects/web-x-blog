"""语义缓存:hash 假嵌入 + 余弦最近邻 + 阈值门控 + 高风险白名单直连。"""
import hashlib, math, re


def embed(text, dim=64):
    v = [0.0] * dim
    for tok in re.findall(r"[\u4e00-\u9fff]|[a-z0-9]+", text.lower()):
        v[int(hashlib.md5(tok.encode()).hexdigest(), 16) % dim] += 1.0
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))


class SemanticCache:
    def __init__(self, threshold=0.5):
        self.entries, self.threshold = [], threshold

    def lookup(self, q):
        if not self.entries:
            return None
        qv = embed(q)
        best = max(self.entries, key=lambda e: cosine(qv, e["vec"]))
        sim = cosine(qv, best["vec"])
        return (best["answer"], sim) if sim >= self.threshold else None

    def put(self, q, answer):
        self.entries.append({"q": q, "vec": embed(q), "answer": answer})


class Service:
    RISKY = ["退款", "投诉", "法律"]

    def __init__(self, threshold=0.5):
        self.cache = SemanticCache(threshold)
        self.calls = 0

    def _llm(self, q):
        self.calls += 1
        return f"LLM 回答:{q}"

    def ask(self, q):
        if any(k in q for k in self.RISKY):
            return self._llm(q) + " [高风险直连]"
        hit = self.cache.lookup(q)
        if hit:
            return f"{hit[0]} [缓存命中 sim={hit[1]:.2f}]"
        ans = self._llm(q)
        self.cache.put(q, ans)
        return ans


if __name__ == "__main__":
    s = Service()
    print(s.ask("怎么查物流"))                       # miss,入库
    print(s.ask("帮我查一下物流信息"))               # 语义近似,hit
    print(s.ask("退货退款流程"))                     # 高风险直连
    print(s.ask("今天天气怎么样"))                   # 不相关,miss
    assert s.calls == 3, "一次命中 + 高风险直连 + 一次不相关 miss = 3 次 LLM"
    print(f"LLM 调用 {s.calls} 次(4 次请求),相似命中与白名单直连生效,不相关问题未命中")
