"""语料更新的影响面评估:文档变更推导脏块清单与向量 答案缓存 FAQ 失效名单。"""


def content_hash(text):
    import hashlib
    return hashlib.md5(text.encode("utf-8")).hexdigest()[:10]


class CorpusManager:
    def __init__(self):
        self.chunks = {}          # chunk_id -> {doc, text, hash}
        self.doc_chunks = {}      # doc -> [chunk_id]
        self.vectors = set()      # 已建向量的 chunk
        self.answer_cache = {}    # cache_key -> 引用的 chunk 列表
        self.faq = {}             # faq_id -> 引用的 chunk

    def register_doc(self, doc, chunk_texts):
        ids = []
        for t in chunk_texts:
            cid = doc + "#" + str(len(ids))
            self.chunks[cid] = {"doc": doc, "text": t, "hash": content_hash(t)}
            self.vectors.add(cid)
            ids.append(cid)
        self.doc_chunks[doc] = ids
        return ids

    def impact(self, doc, new_chunk_texts):
        """假设重切后仍按旧块边界对齐,内容哈希变化的块即受影响。"""
        old_ids = self.doc_chunks.get(doc, [])
        dirty = []
        for i, cid in enumerate(old_ids):
            new_text = new_chunk_texts[i] if i < len(new_chunk_texts) else None
            if new_text is None or content_hash(new_text) != self.chunks[cid]["hash"]:
                dirty.append(cid)
        dirty_set = set(dirty)
        reindex = sorted(self.vectors & dirty_set)
        evicted = sorted(k for k, refs in self.answer_cache.items()
                         if dirty_set & set(refs))
        faq_hit = sorted(f for f, ref in self.faq.items() if ref in dirty_set)
        return {"dirty_chunks": dirty, "reindex": reindex,
                "cache_evicted": evicted, "faq_refresh": faq_hit}

    def apply_update(self, doc, new_chunk_texts):
        report = self.impact(doc, new_chunk_texts)
        for i, cid in enumerate(self.doc_chunks[doc]):
            if i < len(new_chunk_texts):
                self.chunks[cid]["text"] = new_chunk_texts[i]
                self.chunks[cid]["hash"] = content_hash(new_chunk_texts[i])
        for cid in report["reindex"]:
            self.vectors.add(cid)         # 演示:重建后仍视为已建向量
        for k in report["cache_evicted"]:
            del self.answer_cache[k]
        return report


if __name__ == "__main__":
    m = CorpusManager()
    m.register_doc("d1", ["七日无理由退货", "包装完好可退"])
    m.register_doc("d2", ["满 99 包邮"])
    m.answer_cache["q=退货流程"] = ["d1#1", "d2#0"]
    m.answer_cache["q=发货时效"] = ["d2#0"]
    m.faq["faq-1"] = "d1#1"

    report = m.impact("d1", ["七日无理由退货", "包装完好且配件齐全可退"])
    assert report["dirty_chunks"] == ["d1#1"], "只动了第二块"
    assert report["reindex"] == ["d1#1"]
    assert report["cache_evicted"] == ["q=退货流程"], "引用脏块的答案缓存要失效"
    assert report["faq_refresh"] == ["faq-1"]
    assert "q=发货时效" in m.answer_cache, "干净块的缓存不受牵连"

    m.apply_update("d1", ["七日无理由退货", "包装完好且配件齐全可退"])
    assert "q=退货流程" not in m.answer_cache and "q=发货时效" in m.answer_cache

    same = m.impact("d2", ["满 99 包邮"])
    assert same == {"dirty_chunks": [], "reindex": [],
                    "cache_evicted": [], "faq_refresh": []}, "无变化零影响面"
    print("影响面通过:哈希比对定位脏块,向量 重建 缓存失效 FAQ 刷新名单精确")
