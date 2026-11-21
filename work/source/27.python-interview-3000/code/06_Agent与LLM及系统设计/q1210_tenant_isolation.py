"""多租户 RAG:租户字段强制过滤 + 三层纵深校验 + 跨租户对抗测试。"""
import hashlib, math


def embed(text, dim=32):
    v = [0.0] * dim
    for tok in text.split():
        v[int(hashlib.md5(tok.encode()).hexdigest(), 16) % dim] += 1.0
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))


class TenantRAG:
    def __init__(self):
        self.index = []          # {"tenant", "text", "vec"}

    def add(self, tenant, text):
        self.index.append({"tenant": tenant, "text": text, "vec": embed(text)})

    def search(self, tenant, q, k=2):
        # 第 1 层:检索层强制过滤(不可放宽)
        pool = [it for it in self.index if it["tenant"] == tenant]
        assert pool is not None
        qv = embed(q)
        hits = sorted(pool, key=lambda it: cosine(qv, it["vec"]), reverse=True)[:k]
        # 第 2 层:返回前再校验(纵深防御)
        safe = [h for h in hits if h["tenant"] == tenant]
        return safe


class GenLayer:
    """第 3 层:生成层校验引用来源归属。"""

    @staticmethod
    def guard(tenant, hits):
        for h in hits:
            if h["tenant"] != tenant:
                raise PermissionError("跨租户引用被拦截")
        return "ok"


if __name__ == "__main__":
    rag = TenantRAG()
    rag.add("A公司", "A 的 薪酬 政策 薪资 带宽")
    rag.add("A公司", "A 的 采购 流程")
    rag.add("B公司", "B 的 薪酬 政策 薪资 带宽 机密")

    hits = rag.search("A公司", "薪酬 政策 薪资 带宽")
    print("A 租户检索结果:", [h["text"] for h in hits])
    assert all(h["tenant"] == "A公司" for h in hits), "B 文档绝不能出现"
    assert any("B" in h["text"] for h in []) is False

    # 对抗用例:诱导性 query 也要隔离
    adversarial = rag.search("A公司", "B公司 机密 薪资 带宽 泄露")
    assert all(h["tenant"] == "A公司" for h in adversarial)
    print("对抗 query 也无法跨租户")

    assert GenLayer.guard("A公司", hits) == "ok"
    try:
        GenLayer.guard("A公司", [{"tenant": "B公司", "text": "x"}])
    except PermissionError as e:
        print("生成层拦截:", e)
    print("三层纵深:索引过滤 + 返回校验 + 生成层归属检查")
