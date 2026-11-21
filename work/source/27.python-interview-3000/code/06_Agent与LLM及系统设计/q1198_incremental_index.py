"""增量索引:内容指纹去重 + 变更检测 + 墓碑删除 + 版本原子切换。"""
import hashlib


def norm_hash(text):
    normalized = "".join(text.split()).lower()
    return hashlib.sha256(normalized.encode()).hexdigest()[:16]


class IncrementalIndex:
    def __init__(self):
        self.entries = {}        # doc_id -> {"hash", "chunks", "version", "active"}
        self.tombstones = set()

    def upsert(self, doc_id, text, chunks):
        h = norm_hash(text)
        old = self.entries.get(doc_id)
        if old and old["hash"] == h and old["active"]:
            return "unchanged"
        if old:
            self.tombstones.add((doc_id, old["version"]))
        self.entries[doc_id] = {"hash": h, "chunks": chunks,
                                "version": (old["version"] + 1) if old else 1,
                                "active": True}
        return "updated" if old else "created"

    def delete(self, doc_id):
        e = self.entries.get(doc_id)
        if e and e["active"]:
            self.tombstones.add((doc_id, e["version"]))
            e["active"] = False
            return "tombstoned"
        return "missing"

    def search_all(self, query, keyword):
        return [doc_id for doc_id, e in self.entries.items()
                if e["active"] and any(keyword in c for c in e["chunks"])]


if __name__ == "__main__":
    idx = IncrementalIndex()
    print(idx.upsert("d1", "退货 政策 七天 无理由", ["七天 无理由 退货"]))
    print(idx.upsert("d1", "退货 政策 七天 无理由", ["七天 无理由 退货"]), "(重复入库被指纹拦截)")
    print(idx.upsert("d1", "退货 政策 改为 十五天", ["十五天 无理由 退货"]))
    assert idx.entries["d1"]["version"] == 2
    print("搜索:", idx.search_all(None, "退货"))
    assert idx.search_all(None, "七天") == [], "旧版本不再可见"
    print(idx.upsert("d2", "发货 说明", ["48 小时 发货"]))
    print(idx.delete("d2"))
    assert idx.search_all(None, "发货") == [], "墓碑删除立即生效"
    print("增量更新闭环:去重/变更检测/墓碑/版本切换 全部生效")
