"""表格查询路由:聚合类数值问题走结构化计算,叙述类走向量检索,数值必须精确。"""
import re

ROWS = [
    {"year": "2024", "quarter": "Q1", "revenue": 1500.0},
    {"year": "2024", "quarter": "Q2", "revenue": 1800.0},
    {"year": "2024", "quarter": "Q3", "revenue": 2100.0},
    {"year": "2023", "quarter": "Q4", "revenue": 1200.0},
]

AGG_WORDS = {"总和": "sum", "合计": "sum", "平均": "avg", "均值": "avg",
             "最高": "max", "最低": "min"}


def classify_query(query):
    """含聚合词即路由结构化,年份可选提取;否则走向量检索。"""
    for word, fn in AGG_WORDS.items():
        if word in query:
            years = re.findall(r"20\d\d", query)
            return {"route": "structured", "agg": fn,
                    "year": years[0] if years else None}
    return {"route": "vector"}


def structured_answer(plan):
    rows = [r for r in ROWS if plan["year"] is None or r["year"] == plan["year"]]
    vals = [r["revenue"] for r in rows]
    if not vals:
        return "没有该年份的数据"
    label = plan["year"] + " 年" if plan["year"] else "全部年份"
    fn = plan["agg"]
    if fn == "sum":
        return "%s营收总和 %.0f 万" % (label, sum(vals))
    if fn == "avg":
        return "%s季度均营收 %.1f 万" % (label, sum(vals) / len(vals))
    if fn == "max":
        return "%s最高季度营收 %.0f 万" % (label, max(vals))
    return "%s最低季度营收 %.0f 万" % (label, min(vals))


def vector_answer_stub(query):
    """向量检索桩:只找得到相似行,不会算术——这正是要路由走开的原因。"""
    best = max(ROWS, key=lambda r: sum(1 for w in (r["year"], r["quarter"]) if w in query))
    return "最相关行: %s %s 营收 %s 万" % (best["year"], best["quarter"], best["revenue"])


if __name__ == "__main__":
    plan = classify_query("2024 年四个季度营收总和多少")
    assert plan["route"] == "structured" and plan["agg"] == "sum" and plan["year"] == "2024"
    assert structured_answer(plan) == "2024 年营收总和 5400 万"

    plan2 = classify_query("2024 年平均季度营收")
    assert structured_answer(plan2) == "2024 年季度均营收 1800.0 万"

    plan4 = classify_query("营收最高是多少")
    assert plan4["route"] == "structured" and plan4["year"] is None
    assert structured_answer(plan4) == "全部年份最高季度营收 2100 万"

    plan3 = classify_query("介绍一下 Q3 的业务背景")
    assert plan3["route"] == "vector"
    assert "Q3" in vector_answer_stub("介绍一下 Q3 的业务背景")
    print("表格路由通过:聚合词触发结构化精确计算,叙述类交给向量检索")
