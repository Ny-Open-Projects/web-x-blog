"""查询扩展的同义词表:领域词加权扩展,按权重截断去重,原词永远保留在首位。"""

SYNONYMS = {
    "退款": [("退货", 0.9), ("返还", 0.6)],
    "邮费": [("运费", 0.9), ("快递费", 0.5)],
    "出库": [("发货", 0.85), ("寄出", 0.6)],
}
MAX_EXTRA = 3


def expand(query, table=None, max_extra=MAX_EXTRA):
    table = table or SYNONYMS
    candidates = []
    for word in sorted(table):
        if word in query:
            for variant, weight in table[word]:
                candidates.append((variant, weight))
    seen, extras = set(), []
    for variant, weight in sorted(candidates, key=lambda x: -x[1]):
        if variant in query:
            continue
        if variant not in seen:
            seen.add(variant)
            extras.append(variant)
    extras = extras[:max_extra]
    return {"original": query, "expanded": [query] + extras,
            "n_extra": len(extras)}


if __name__ == "__main__":
    r = expand("退款邮费怎么算")
    assert r["expanded"][0] == "退款邮费怎么算", "原词必须保留且在首位"
    assert r["expanded"][1] == "退货", "权重最高的变体排最前"
    assert set(["运费", "返还"]).issubset(set(r["expanded"]))
    assert r["n_extra"] == MAX_EXTRA, "超过上限的变体被截断"

    r2 = expand("出库了吗")
    assert r2["expanded"] == ["出库了吗", "发货", "寄出"]

    # 词表没覆盖的查询不扩展,原样返回,绝不瞎编同义词
    r3 = expand("今天天气怎么样")
    assert r3["expanded"] == [r3["original"]] and r3["n_extra"] == 0

    # 扩展结果与原词重复的要被去重
    table = {"苹果": [("苹果", 0.9), ("水果", 0.8)]}
    r4 = expand("苹果", table=table)
    assert r4["expanded"] == ["苹果", "水果"], "与原词相同的变体必须剔除"
    print("同义词扩展通过:加权排序 截断 去重,未覆盖查询原样放行")
