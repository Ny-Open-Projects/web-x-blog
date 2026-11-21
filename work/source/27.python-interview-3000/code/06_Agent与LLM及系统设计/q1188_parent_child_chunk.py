"""父子块检索:child 建索引召回,回溯 parent 提供完整上下文。"""
import hashlib, math


def embed(text, dim=64):
    v = [0.0] * dim
    for tok in text.split():
        v[int(hashlib.md5(tok.encode()).hexdigest(), 16) % dim] += 1.0
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))


class ParentChildIndex:
    def __init__(self, documents):
        self.parents = {}
        self.children = []                    # (child_text, vec, parent_id)
        for pid, text in documents.items():
            self.parents[pid] = text
            for sent in text.split("。"):
                sent = sent.strip()
                if sent:
                    self.children.append((sent, embed(sent), pid))

    def search(self, q, k=2):
        qv = embed(q)
        top = sorted(self.children, key=lambda c: cosine(qv, c[1]), reverse=True)[:k]
        parent_ids = []
        for _, _, pid in top:
            if pid not in parent_ids:
                parent_ids.append(pid)
        return top, [self.parents[p] for p in parent_ids]


if __name__ == "__main__":
    docs = {
        "policy-return": "退货政策 支持七天无理由退货。退货运费由买家承担。质量问题商家承担运费。",
        "policy-ship": "发货政策 下单后 48 小时内发货。偏远地区延长至 72 小时。支持顺丰加急。",
    }
    idx = ParentChildIndex(docs)
    hits, parents = idx.search("退货谁出运费", k=3)
    print("命中的 child 句:")
    for h, _, p in hits:
        print(f"  [{p}] {h}")
    print("回溯的 parent 全文:", parents[0][:30], "(截断展示)")
    assert any("运费" in h for h, _, _ in hits), "小块必须精准命中运费句"
    assert len(parents[0]) > len(hits[0][0]), "送入生成的是完整父块"
    assert "发货政策" not in parents[0], "父块不得跨文档"
