"""多文档冲突标注:同一事实不同取值时按 新鲜度优先 权威次之 仲裁并标注落选方。"""

DOCS = [
    {"id": "d1", "fact": "退货期限", "value": "7 天", "date": "2023-05-01", "rank": 2},
    {"id": "d2", "fact": "退货期限", "value": "15 天", "date": "2024-01-01", "rank": 1},
    {"id": "d3", "fact": "退货期限", "value": "15 天", "date": "2024-02-01", "rank": 3},
    {"id": "d4", "fact": "保修期", "value": "1 年", "date": "2024-03-01", "rank": 1},
]


class ConflictAnnotator:
    def annotate(self, fact):
        docs = sorted([d for d in DOCS if d["fact"] == fact],
                      key=lambda d: (d["date"], d["rank"]), reverse=True)
        if not docs:
            return {"conflict": False, "note": "无来源"}
        winner = docs[0]
        values = {d["value"] for d in docs}
        suppressed = []
        for d in docs[1:]:
            if d["date"] < winner["date"]:
                suppressed.append({"id": d["id"], "reason": "旧版本", "value": d["value"]})
            elif d["date"] == winner["date"] and d["rank"] < winner["rank"]:
                suppressed.append({"id": d["id"], "reason": "同日期低权威", "value": d["value"]})
            else:
                suppressed.append({"id": d["id"], "reason": "与胜出方一致", "value": d["value"]})
        return {"conflict": len(values) > 1, "winner": winner["id"],
                "value": winner["value"], "suppressed": suppressed}


if __name__ == "__main__":
    r = ConflictAnnotator().annotate("退货期限")
    assert r["conflict"] is True, "7 天与 15 天取值不同即冲突"
    assert r["winner"] == "d3" and r["value"] == "15 天", "最新日期胜出"
    reasons = {s["id"]: s["reason"] for s in r["suppressed"]}
    assert reasons == {"d2": "旧版本", "d1": "旧版本"}, "落选方必须带压制原因"

    same = ConflictAnnotator().annotate("保修期")
    assert same["conflict"] is False and same["suppressed"] == [], "取值一致不算冲突"
    print("冲突标注通过:新旧裁决 最新胜出,落选方带原因,一致来源不误标")
