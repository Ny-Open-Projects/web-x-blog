"""多工具结果合并去重:按规范键归并实体,保留来源标记,分数字段择优。"""


def norm_url(url):
    return url.split("?")[0].rstrip("/").lower()


class ResultMerger:
    def __init__(self):
        self.by_key = {}
        self.order = []

    def add(self, source, items):
        """items: [{url, title, score}],按规范化 url 归并,同实体多来源合并。"""
        for it in items:
            key = norm_url(it["url"])
            if key not in self.by_key:
                self.by_key[key] = {"title": it["title"], "score": it["score"],
                                    "sources": [source]}
                self.order.append(key)
                continue
            merged = self.by_key[key]
            if source not in merged["sources"]:
                merged["sources"].append(source)
            if it["score"] > merged["score"]:
                merged["score"] = it["score"]
                merged["title"] = it["title"]
        return len(items)

    def merged(self):
        return [{"url": k, **self.by_key[k]} for k in self.order]


if __name__ == "__main__":
    web = [{"url": "https://a.com/doc?id=1", "title": "A 文档", "score": 0.9},
           {"url": "https://b.com/page/", "title": "B 页面", "score": 0.7}]
    kb = [{"url": "https://a.com/doc?id=1&from=kb", "title": "A 文档(知识库)", "score": 0.8},
          {"url": "https://c.com/note", "title": "C 笔记", "score": 0.6}]

    m = ResultMerger()
    m.add("web", web)
    m.add("kb", kb)
    out = m.merged()
    assert len(out) == 3, "4 条原始结果去重为 3 个实体"
    a = [x for x in out if x["url"] == "https://a.com/doc"][0]
    assert a["sources"] == ["web", "kb"], "同实体来源必须合并标记"
    assert a["title"] == "A 文档" and a["score"] == 0.9, "分数择优,标题跟最优走"
    assert "https://b.com/page" in [x["url"] for x in out], "尾部斜杠被规范化"
    print("多工具合并通过:4 条去重为 3 条,来源标记合并,分数与标题择优保留")
