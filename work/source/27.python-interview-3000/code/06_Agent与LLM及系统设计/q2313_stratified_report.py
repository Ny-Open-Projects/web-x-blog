"""评估分层报告:用例带难度与类目标签,分桶统计通过率,短板层一目了然。"""
def stratified_report(results, gate=0.8):
    buckets = {}
    for r in results:
        key = (r["diff"], r["cat"])
        b = buckets.setdefault(key, {"n": 0, "pass": 0})
        b["n"] += 1
        b["pass"] += 1 if r["pass"] else 0
    rows = []
    for (diff, cat), b in sorted(buckets.items()):
        rate = b["pass"] / b["n"]
        rows.append({"diff": diff, "cat": cat, "n": b["n"],
                     "rate": round(rate, 2), "fail": b["n"] - b["pass"]})
    overall = sum(1 for r in results if r["pass"]) / len(results) if results else 0.0
    weak = [r for r in rows if r["rate"] < gate]
    return {"overall": round(overall, 2), "rows": rows, "weak": weak,
            "gate": gate, "verdict": "fail" if weak else "pass"}


if __name__ == "__main__":
    data = [
        {"id": "c1", "diff": "easy", "cat": "faq", "pass": True},
        {"id": "c2", "diff": "easy", "cat": "faq", "pass": True},
        {"id": "c3", "diff": "hard", "cat": "tool", "pass": False},
        {"id": "c4", "diff": "hard", "cat": "tool", "pass": False},
        {"id": "c5", "diff": "hard", "cat": "faq", "pass": True},
        {"id": "c6", "diff": "mid", "cat": "rag", "pass": True},
    ]
    rep = stratified_report(data, gate=0.8)
    assert rep["overall"] == 0.67
    assert rep["verdict"] == "fail", "hard/tool 层通过率 0 应卡门禁"
    assert rep["weak"] == [{"diff": "hard", "cat": "tool", "n": 2, "rate": 0.0, "fail": 2}]
    fixed = [dict(d, **{"pass": True}) if d["id"] in ("c3", "c4") else d for d in data]
    rep2 = stratified_report(fixed, gate=0.8)
    assert rep2["verdict"] == "pass" and rep2["weak"] == [], "短板修复后门禁放行"
    print("分层报告通过:分桶通过率 短板定位 门禁联动")
