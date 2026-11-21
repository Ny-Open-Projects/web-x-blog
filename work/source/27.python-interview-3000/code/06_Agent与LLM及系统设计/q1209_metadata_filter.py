"""元数据过滤检索:query 解析出 filter -> 先过滤后相似 -> 空结果降级策略。"""
import hashlib, math, re


def embed(text, dim=32):
    v = [0.0] * dim
    for tok in text.split():
        v[int(hashlib.md5(tok.encode()).hexdigest(), 16) % dim] += 1.0
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))


class FilteredIndex:
    def __init__(self):
        self.items = []

    def add(self, text, meta, vec=None):
        self.items.append({"text": text, "meta": meta, "vec": vec or embed(text)})

    def parse_filter(self, q):
        f = {}
        m = re.search(r"(20\d\d)年", q)
        if m:
            f["year"] = m.group(1)
        if "国际" in q:
            f["region"] = "intl"
        return f

    def search(self, q, filt, k=2, relax=True):
        def ok(meta, f):
            return all(meta.get(k2) == v for k2, v in f.items())
        cands = [it for it in self.items if ok(it["meta"], filt)]
        if not cands and relax and filt:
            relaxed = {k2: v for k2, v in filt.items() if k2 != "year"}
            cands = [it for it in self.items if ok(it["meta"], relaxed)]
            if cands:
                filt = relaxed
        qv = embed(q)
        ranked = sorted(cands, key=lambda it: cosine(qv, it["vec"]), reverse=True)[:k]
        return ranked, filt


if __name__ == "__main__":
    idx = FilteredIndex()
    idx.add("退货 政策 七天 无理由", {"year": "2020", "region": "cn"})
    idx.add("退货 政策 十五天 无理由", {"year": "2024", "region": "cn"})
    idx.add("国际 订单 退货 30 天", {"year": "2024", "region": "intl"})
    q = "2024年退货政策"
    filt = idx.parse_filter(q)
    print("解析 filter:", filt)
    hits, used = idx.search(q, filt)
    print("命中:", [(h["text"], h["meta"]) for h in hits])
    assert all(h["meta"]["year"] == "2024" for h in hits), "旧政策绝不能出现"

    hits2, used2 = idx.search("2024年国际退货政策", {"year": "2024", "region": "intl"})
    assert "国际" in hits2[0]["text"]
    print("无匹配场景:只用 美区 查询 2025 政策")
    hits3, used3 = idx.search("2025年政策", {"year": "2025"})
    print("降级后 filter:", used3, "命中:", [h["text"] for h in hits3])
    assert used3 == {} and hits3, "放宽后仍有结果,需告知降级"
