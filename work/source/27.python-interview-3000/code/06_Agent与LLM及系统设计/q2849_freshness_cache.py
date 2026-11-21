"""Q2849 答案缓存的新鲜度分层:分档 TTL 与语料版本双重失效。

答案缓存最大的坑是「过期方式只有一种」:价格类答案半小时就敢用了,
政策类答案可以放一天,语料一重建索引所有缓存又都不可信。给缓存条目
带分档 TTL 和语料版本号,双重校验都过才命中,失效原因也要分型上报。
"""


class FreshnessCache:
    TIER_TTL = {"hot": 60, "evergreen": 86400}

    def __init__(self):
        self.store = {}

    def put(self, q, ans, tier, now, corpus_version):
        self.store[q] = {"ans": ans, "tier": tier,
                         "ts": now, "ttl": self.TIER_TTL[tier],
                         "corpus_version": corpus_version}

    def get(self, q, now, corpus_version):
        e = self.store.get(q)
        if e is None:
            return None, "miss"
        if e["corpus_version"] != corpus_version:
            return None, "stale_corpus"
        if now - e["ts"] > e["ttl"]:
            return None, "expired"
        return e["ans"], "hit"


def main():
    cache = FreshnessCache()
    cache.put("退货多久到账", "3 个工作日", "hot", now=1000, corpus_version="v7")
    cache.put("公司成立于哪年", "2019 年", "evergreen", now=1000, corpus_version="v7")
    ans, why = cache.get("退货多久到账", now=1030, corpus_version="v7")
    assert why == "hit" and ans == "3 个工作日", (ans, why)
    # hot 档 TTL 只有 60 秒
    _, why = cache.get("退货多久到账", now=1080, corpus_version="v7")
    assert why == "expired", why
    # evergreen 档 24 小时内仍然命中
    ans, why = cache.get("公司成立于哪年", now=80000, corpus_version="v7")
    assert why == "hit", why
    # 语料重建版本变了:TTL 未到也必须失效
    _, why = cache.get("公司成立于哪年", now=80001, corpus_version="v8")
    assert why == "stale_corpus", why
    print("命中/过期/版本失效三种结局齐备:")
    print("  hot 档 60 秒过期 -> expired")
    print("  evergreen 档跨夜仍命中 -> hit")
    print("  语料 v7->v8 触发 stale_corpus,失效原因分型可统计")


if __name__ == "__main__":
    main()
