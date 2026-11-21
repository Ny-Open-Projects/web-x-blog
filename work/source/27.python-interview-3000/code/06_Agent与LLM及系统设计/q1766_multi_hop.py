"""多跳检索编排:第一跳找桥接实体,第二跳换查询继续召回,链路即引用链。"""
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


DOCS = [
    {"id": "d1", "text": "Acme 公司 创始人 是 张三"},
    {"id": "d2", "text": "张三 的 出生地 是 杭州"},
    {"id": "d3", "text": "杭州 的 人口 约 一千万"},
    {"id": "d4", "text": "北京 的 人口 约 两千万"},
    {"id": "d5", "text": "Acme 公司 主营 机器人"},
]


class FakeLLM:
    """桥接实体抽取桩:按句式抽取下一跳实体,离线确定。"""

    @staticmethod
    def extract_entity(text):
        if "创始人" in text:
            return "张三"
        if "出生地" in text:
            return "杭州"
        return None


class MultiHopRetriever:
    def __init__(self, docs, hops=2, topk=1):
        self.vecs = [(d, embed(d["text"])) for d in docs]
        self.hops = hops
        self.topk = topk

    def search(self, query, exclude):
        q = embed(query)
        cands = [(cosine(q, v), d) for d, v in self.vecs if d["id"] not in exclude]
        cands.sort(key=lambda p: -p[0])          # 只按分数排,平分时保序不比字典
        return [d for _, d in cands[:self.topk]]

    def retrieve(self, question):
        seen, chain = set(), []
        query = question
        for hop in range(self.hops):
            hits = self.search(query, seen)
            if not hits:
                break
            seen.add(hits[0]["id"])
            entity = FakeLLM.extract_entity(hits[0]["text"])
            if not entity:
                break
            chain.append({"hop": hop + 1, "query": query,
                          "hit": hits[0]["id"], "entity": entity})
            query = entity                       # 桥接实体成为下一跳查询
        return chain, seen


if __name__ == "__main__":
    retriever = MultiHopRetriever(DOCS, hops=2)
    chain, seen = retriever.retrieve("Acme 公司 创始人 出生 城市 人口")
    assert [c["hit"] for c in chain] == ["d1", "d2"], "链路 d1 创始人 d2 出生地"
    assert chain[0]["entity"] == "张三" and chain[1]["entity"] == "杭州"
    assert seen == {"d1", "d2"}, "已见集合防止跳回旧文档"

    final = retriever.search(chain[-1]["entity"] + " 人口", seen)
    assert final[0]["id"] == "d3", "第三跳命中杭州人口而非北京"
    assert "d4" not in [d["id"] for d in final]
    print("多跳检索通过:两跳拿到桥接实体,末跳命中目标属性,链路可追溯")
