"""嵌入模型版本迁移:新版本分批重嵌入,完成前旧版兜底,未完成禁止切换。"""


def fake_embed_v1(text):
    return [text.count("货"), text.count("款"), 1.0]


def fake_embed_v2(text):
    return [text.count("货"), text.count("款"), len(text) % 5, 0.5]


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = sum(x * x for x in a) ** 0.5
    nb = sum(x * x for x in b) ** 0.5
    return dot / (na * nb) if na and nb else 0.0


class MigratingIndex:
    def __init__(self):
        self.docs = {}
        self.active = "v1"
        self.reembedded = 0

    def add(self, did, text):
        self.docs[did] = {"text": text, "emb_v1": fake_embed_v1(text),
                          "emb_v2": None, "ver": "v1"}

    def reembed_batch(self, n=2):
        for did, d in self.docs.items():
            if d["emb_v2"] is None:
                d["emb_v2"] = fake_embed_v2(d["text"])
                d["ver"] = "dual"
                self.reembedded += 1
                n -= 1
                if n == 0:
                    break

    def migration_done(self):
        return all(d["emb_v2"] is not None for d in self.docs.values())

    def switch(self):
        if not self.migration_done():
            raise RuntimeError("仍有文档未重嵌入 禁止切换查询向量")
        self.active = "v2"

    def search(self, query, k=1):
        emb_fn = fake_embed_v1 if self.active == "v1" else fake_embed_v2
        key = "emb_" + self.active
        q = emb_fn(query)
        best, bs = None, -2.0
        for did, d in self.docs.items():
            s = cosine(q, d[key])
            if s > bs:
                best, bs = did, s
        return best


if __name__ == "__main__":
    idx = MigratingIndex()
    for i, t in enumerate(["退货政策说明", "退款进度查询", "换货流程指引"]):
        idx.add("d%d" % i, t)
    assert idx.active == "v1" and idx.search("退货") == "d0"
    try:
        idx.switch()
        raise SystemExit("未完成迁移不允许切换")
    except RuntimeError:
        pass
    idx.reembed_batch(2)
    assert not idx.migration_done() and idx.reembedded == 2, "分批重嵌入"
    idx.reembed_batch(10)
    assert idx.migration_done()
    idx.switch()
    assert idx.active == "v2" and idx.search("退款") == "d1"
    print("嵌入迁移通过:分批重嵌入 未完成禁止切换 切换后走新向量")
