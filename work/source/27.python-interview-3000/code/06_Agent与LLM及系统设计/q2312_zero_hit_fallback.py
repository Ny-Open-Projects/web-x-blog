"""零命中兜底:改写重试一次仍零命中则给查询建议并走拒答模板,不硬编答案。"""
def fake_retrieve(index, query):
    return [d for d in index if query in d or d in query]


def rewrite(query, synonyms):
    for src, dst in synonyms.items():
        if src in query:
            return query.replace(src, dst), "synonym:" + src
    return query, None


def answer_with_fallback(query, index, synonyms, hit_threshold=1):
    hits = fake_retrieve(index, query)
    if len(hits) >= hit_threshold:
        return {"mode": "answer", "hits": hits, "path": "direct"}
    q2, how = rewrite(query, synonyms)
    if how and q2 != query:
        h2 = fake_retrieve(index, q2)
        if len(h2) >= hit_threshold:
            return {"mode": "rewritten", "hits": h2, "query": q2,
                    "path": "direct->rewrite"}
    sugg = sorted(set(index) - set(hits))[:2]
    return {"mode": "refuse", "hits": [], "suggestions": sugg,
            "template": "没有找到相关内容,你可以试试:%s" % "、".join(sugg),
            "path": "direct->rewrite->refuse"}


if __name__ == "__main__":
    index = ["退货政策", "退款流程", "发货时效"]
    syn = {"退换货": "退货", "售后": "退货"}
    r1 = answer_with_fallback("退货", index, syn)
    assert r1["mode"] == "answer" and r1["hits"] == ["退货政策"]
    r2 = answer_with_fallback("退换货", index, syn)
    assert r2["mode"] == "rewritten" and r2["hits"] == ["退货政策"] and r2["query"] == "退货"
    r3 = answer_with_fallback("元宇宙购物", index, syn)
    assert r3["mode"] == "refuse" and r3["suggestions"], "零命中给建议并拒答"
    assert "没有找到" in r3["template"]
    assert r3["suggestions"] == ["发货时效", "退款流程"]
    print("零命中兜底通过:直查 改写重试 建议与拒答不硬编")
