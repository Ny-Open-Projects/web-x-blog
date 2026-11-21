"""多模态 RAG 概念桩:图文双塔共用向量空间,跨模态检索 + 元数据溯源。"""
import hashlib, math, re


def _tok(text):
    return re.findall(r"[a-z0-9]+|[\u4e00-\u9fff]", text.lower())


def embed_text(text, dim=32):
    v = [0.0] * dim
    for tok in _tok(text):
        v[int(hashlib.md5(tok.encode()).hexdigest(), 16) % dim] += 1.0
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


def embed_image_stub(image_id, dim=32):
    """桩:真实场景是视觉编码器;这里用图片 id 与描述哈希模拟同空间对齐。"""
    return embed_text(image_id.replace("_", " "), dim)


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))


class MultimodalIndex:
    def __init__(self):
        self.items = []       # {"type", "vec", "meta"}

    def add_text(self, text, meta):
        self.items.append({"type": "text", "vec": embed_text(text), "meta": meta})

    def add_image(self, image_id, caption_meta):
        self.items.append({"type": "image", "vec": embed_image_stub(image_id), "meta": caption_meta})

    def search(self, query, k=2):
        qv = embed_text(query)
        return sorted(self.items, key=lambda it: cosine(qv, it["vec"]), reverse=True)[:k]


if __name__ == "__main__":
    idx = MultimodalIndex()
    idx.add_text("季度 营收 增长 15%", {"doc": "q3报告", "page": 2})
    idx.add_image("fig_季度营收曲线", {"doc": "q3报告", "page": 3, "kind": "chart"})
    idx.add_text("风险 提示 汇率 波动", {"doc": "q3报告", "page": 9})

    hits = idx.search("营收 曲线 图")
    for h in hits:
        print(f"  [{h['type']}] page={h['meta']['page']} {h['meta']}")
    assert hits[0]["type"] == "image", "跨模态命中图片"
    assert hits[0]["meta"]["page"] == 3, "可溯源到页码"
    assert hits[1]["type"] == "text", "文本证据同时召回"
    print("双塔同空间检索:文本 query 直接命中相关图表与文本")
