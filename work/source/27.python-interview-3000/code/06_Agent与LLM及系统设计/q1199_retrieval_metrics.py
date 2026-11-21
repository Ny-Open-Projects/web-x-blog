"""检索评估:hit@k 与 MRR 实现,按问题类型分层报告。"""


def hit_at_k(ranked_ids, golden_ids, k):
    return int(any(g in ranked_ids[:k] for g in golden_ids))


def reciprocal_rank(ranked_ids, golden_ids):
    for i, d in enumerate(ranked_ids, 1):
        if d in golden_ids:
            return 1.0 / i
    return 0.0


def evaluate(evalset, retriever_fn, k=3):
    by_type = {}
    for case in evalset:
        ranked = retriever_fn(case["q"])
        rec = {"hit": hit_at_k(ranked, case["golden"], k),
               "rr": reciprocal_rank(ranked, case["golden"]),
               "type": case["type"]}
        by_type.setdefault(case["type"], []).append(rec)
    report = {}
    for t, rows in by_type.items():
        report[t] = {"hit@k": sum(r["hit"] for r in rows) / len(rows),
                     "mrr": sum(r["rr"] for r in rows) / len(rows)}
    overall = {"hit@k": sum(r["hit"] for rows in by_type.values() for r in rows) /
               sum(len(r) for r in by_type.values()),
               "mrr": sum(r["rr"] for rows in by_type.values() for r in rows) /
               sum(len(r) for r in by_type.values())}
    return report, overall


if __name__ == "__main__":
    evalset = [
        {"q": "退货运费", "golden": ["d1"], "type": "政策"},
        {"q": "退货期限", "golden": ["d2"], "type": "政策"},
        {"q": "发货时效", "golden": ["d3"], "type": "物流"},
        {"q": "偏远地区", "golden": ["d3"], "type": "物流"},
    ]

    def weak_retriever(q):
        # 桩:能召回但排序差 -> 高 hit 低 MRR 的典型形态
        order = {"退货运费": ["d9", "d8", "d1"], "退货期限": ["d2"],
                 "发货时效": ["d3"], "偏远地区": ["d3"]}
        return order.get(q, [])

    report, overall = evaluate(evalset, weak_retriever)
    for t, m in report.items():
        print(f"  [{t}] hit@3={m['hit@k']:.0%} mrr={m['mrr']:.2f}")
    print("总体:", {k: round(v, 3) for k, v in overall.items()})
    assert overall["hit@k"] == 1.0 and overall["mrr"] < 1.0, "排序差时 hit 高 MRR 低"
    print("诊断: 召回没问题,排序拖后腿 -> 上 rerank 而不是改 chunk")
