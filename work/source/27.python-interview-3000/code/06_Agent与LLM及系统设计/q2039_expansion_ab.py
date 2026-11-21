"""扩展开关对拍:同一批 golden 查询分别用原词与扩展词检索,逐条对比命中率。"""
import math

VOCAB = ["退货", "退款", "包邮", "运费", "发货", "出库", "物流", "签收"]
SYNONYMS = {
    "退款": [("退货", 0.9)],
    "邮费": [("运费", 0.9)],
    "出库": [("发货", 0.85)],
}
DOCS = ["商品签收后 7 天内可无理由退货",
        "普通订单满 99 元包邮 偏远地区另收运费",
        "订单发货后可查物流单号"]
GOLDEN = [
    {"query": "退款流程", "expect": 0},
    {"query": "邮费谁出", "expect": 1},
    {"query": "啥时候出库", "expect": 2},
]


def extract_words(text):
    return [w for w in VOCAB if w in text]


def embed(text):
    """词表 one-hot:出现该词记 1,余弦即词交集规模。"""
    words = set(extract_words(text))
    return [1.0 if w in words else 0.0 for w in VOCAB]


def cosine(a, b):
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    if na == 0 or nb == 0:
        return 0.0
    return sum(x * y for x, y in zip(a, b)) / (na * nb)


def expand_query(query):
    extras = []
    for key in sorted(SYNONYMS):
        if key in query:
            extras.extend(v for v, _ in SYNONYMS[key])
    return query + " " + " ".join(extras) if extras else query


def retrieve(query, use_expansion):
    q = expand_query(query) if use_expansion else query
    qv = embed(q)
    best, best_score = None, 0.0
    for i, doc in enumerate(DOCS):
        s = cosine(qv, embed(doc))
        if s > best_score:
            best, best_score = i, s
    return best


def ab_test(golden):
    per_query, hits = [], {"off": 0, "on": 0}
    for g in golden:
        top_off = retrieve(g["query"], use_expansion=False)
        top_on = retrieve(g["query"], use_expansion=True)
        ok_off = top_off == g["expect"]
        ok_on = top_on == g["expect"]
        hits["off"] += int(ok_off)
        hits["on"] += int(ok_on)
        per_query.append({"query": g["query"], "hit_off": ok_off,
                          "hit_on": ok_on,
                          "effect": "improved" if ok_on and not ok_off
                          else "regressed" if ok_off and not ok_on else "same"})
    n = len(golden)
    return {"hit_rate_off": hits["off"] / float(n),
            "hit_rate_on": hits["on"] / float(n),
            "per_query": per_query}


if __name__ == "__main__":
    report = ab_test(GOLDEN)
    assert report["hit_rate_off"] == 0.0, "不开扩展三条全靠不上词表"
    assert report["hit_rate_on"] == 1.0, "开扩展后三条全命中"
    improved = [q for q in report["per_query"] if q["effect"] == "improved"]
    assert len(improved) == 3
    assert report["hit_rate_on"] >= report["hit_rate_off"], "上线闸门:不得劣化"
    print("扩展对拍通过:命中率 0%% → 100%%,3 条查询全部 improved,闸门放行")
