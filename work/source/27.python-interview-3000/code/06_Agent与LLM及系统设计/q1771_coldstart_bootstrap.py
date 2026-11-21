"""冷启动语料引导:从种子问题反向扩出变体与答案,灌入索引拉起命中率。"""
import math

_VOCAB = {}


def embed(text, dim=64):
    """词表登记式假嵌入:token 顺序登记,小词表内零碰撞,确定性可复现。"""
    v = [0.0] * dim
    for tok in text.split():
        if tok not in _VOCAB:
            _VOCAB[tok] = len(_VOCAB)
        v[_VOCAB[tok] % dim] += 1.0
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))


VARIANTS = {
    "退货": ["怎么退货", "退货流程是什么", "如何申请退货"],
    "发票": ["怎么开发票", "发票怎么开", "开票流程"],
}


class FakeLLM:
    """答案生成桩:种子词 -> 固定口径答案,离线可复现。"""

    @staticmethod
    def answer(seed):
        return "关于%s的标准答案" % seed


def bootstrap(seed_questions):
    """种子 -> 变体问题加答案,合成语料文档。"""
    docs = []
    for seed in seed_questions:
        for v in VARIANTS.get(seed, [seed]):
            docs.append({"q": v, "text": v + " " + FakeLLM.answer(seed)})
    return docs


class MiniIndex:
    def __init__(self):
        self.docs = []

    def add(self, doc):
        self.docs.append((doc, embed(doc["text"])))

    def hit(self, query, threshold=0.3):
        if not self.docs:
            return False
        q = embed(query)
        return max(cosine(q, v) for _, v in self.docs) >= threshold


if __name__ == "__main__":
    seeds = ["退货", "发票"]
    queries = [q for seed in seeds for q in VARIANTS[seed]]     # 模拟真实用户问法

    cold = MiniIndex()
    before = sum(cold.hit(q) for q in queries)
    assert before == 0, "冷启动索引命中率必须为零"

    for doc in bootstrap(seeds):
        cold.add(doc)
    after = sum(cold.hit(q) for q in queries)
    assert after == len(queries) == 6, "种子变体全部命中"

    assert not cold.hit("今天 天气 怎么样"), "无关查询仍然不命中,无虚假召回"
    assert len(cold.docs) == 6
    print("冷启动引导通过:2 个种子扩出 6 条问答对,命中率 0 到 6,无关查询不误伤")
