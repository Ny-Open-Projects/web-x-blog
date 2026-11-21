"""检索缓存:嵌入缓存 + 结果缓存绑定索引版本 + 热点预热。"""
import hashlib, math


def embed(text, dim=32):
    v = [0.0] * dim
    for tok in text.split():
        v[int(hashlib.md5(tok.encode()).hexdigest(), 16) % dim] += 1.0
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


class Retriever:
    def __init__(self, docs):
        self.version = 1
        self.docs = docs
        self.embed_cache = {}      # text -> vec(索引无关,长 TTL)
        self.result_cache = {}     # (version, query) -> results
        self.stats = {"embed_hits": 0, "result_hits": 0, "misses": 0}

    def vec(self, text):
        if text in self.embed_cache:
            self.stats["embed_hits"] += 1
            return self.embed_cache[text]
        v = embed(text)
        self.embed_cache[text] = v
        self.stats["misses"] += 1
        return v

    def search(self, q, k=2):
        key = (self.version, q)
        if key in self.result_cache:
            self.stats["result_hits"] += 1
            return self.result_cache[key]
        qv = self.vec(q)
        ranked = sorted(self.docs, key=lambda d: self._cos(qv, d[1]), reverse=True)[:k]
        self.result_cache[key] = ranked
        return ranked

    @staticmethod
    def _cos(a, b):
        return sum(x * y for x, y in zip(a, b))

    def warmup(self, hot_queries):
        for q in hot_queries:
            self.search(q)

    def reindex(self, docs):
        self.docs, self.version = docs, self.version + 1
        self.result_cache.clear()          # 索引变更,结果缓存全失效
        self.embed_cache.clear() if False else None   # 嵌入与内容相关,可保留


if __name__ == "__main__":
    docs = [("退货运费说明", embed("退货运费 买家 承担")), ("发货说明", embed("48 小时 发货"))]
    r = Retriever(docs)
    r.warmup(["退货运费 怎么算", "多久 发货"])
    r.search("退货运费 怎么算")
    print("预热后查询:", r.stats)
    assert r.stats["result_hits"] >= 1, "预热即命中结果缓存"
    r.reindex([("新退货政策", embed("十五天 无理由"))])
    out = r.search("退货运费 怎么算")
    print("重索引后:", out, r.stats)
    assert "新退货政策" in out[0][0], "版本失效后查到新索引结果"
    print("缓存与索引版本绑定,重索引自动失效")
