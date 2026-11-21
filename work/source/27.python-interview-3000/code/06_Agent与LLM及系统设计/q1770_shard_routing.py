"""索引分片与路由:类目词定向单分片,无类目散射全部分片再归并全局 topk。"""
import hashlib
import math


def embed(text, dim=24):
    v = [0.0] * dim
    for tok in text.split():
        v[int(hashlib.md5(tok.encode()).hexdigest(), 16) % dim] += 1.0
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))


class Shard:
    def __init__(self, name):
        self.name = name
        self.items = []                          # (text, vec)

    def add(self, text):
        self.items.append((text, embed(text)))

    def search(self, query, topk):
        q = embed(query)
        ranked = sorted(((cosine(q, v), t) for t, v in self.items), reverse=True)
        return ranked[:topk]


class ShardedIndex:
    ROUTE_WORDS = {"售后": "shard-support", "销售": "shard-sales", "研发": "shard-eng"}

    def __init__(self):
        self.shards = {}
        self.routed, self.scattered = 0, 0

    def add_shard(self, name):
        self.shards[name] = Shard(name)

    def add_doc(self, category, text):
        assert category in self.shards, "文档必须落在已存在分片"
        self.shards[category].add(text)

    def search(self, query, topk=3):
        target = None
        for word, shard in self.ROUTE_WORDS.items():
            if word in query:
                target = shard
                break
        if target and target in self.shards:
            self.routed += 1                     # 定向:只扫一个分片
            return self.shards[target].search(query, topk)
        self.scattered += 1                      # 散射:全分片召回后归并
        merged = []
        for shard in self.shards.values():
            merged.extend(shard.search(query, topk))
        merged.sort(reverse=True)
        return merged[:topk]


if __name__ == "__main__":
    idx = ShardedIndex()
    for name in ("shard-support", "shard-sales", "shard-eng"):
        idx.add_shard(name)
    idx.add_doc("shard-support", "售后 退货 流程 说明")
    idx.add_doc("shard-support", "售后 保修 政策")
    idx.add_doc("shard-sales", "销售 报价 单 说明")
    idx.add_doc("shard-sales", "销售 渠道 政策")
    idx.add_doc("shard-eng", "研发 发布 流程")

    hits = idx.search("售后 退货 怎么 办")
    assert len(hits) == 2 and hits[0][1].startswith("售后 退货")
    assert all(t.startswith("售后") for _, t in hits), "定向查询绝不混入其他分片"
    assert idx.routed == 1 and idx.scattered == 0

    hits2 = idx.search("政策 怎么 规定")
    assert idx.scattered == 1 and len(hits2) == 3
    texts = [t for _, t in hits2]
    assert "售后 保修 政策" in texts and "销售 渠道 政策" in texts, "散射归并返回全局最优"
    print("分片路由通过:定向查只扫 1 分片,散射查归并 3 分片全局 topk")
