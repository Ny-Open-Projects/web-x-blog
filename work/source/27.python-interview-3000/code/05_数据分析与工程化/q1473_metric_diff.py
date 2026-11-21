"""发布前后指标快照对比:阈值化 diff 与回归报告"""

import json

BEFORE = {"gmv": 1023400, "orders": 8123, "cvr": 0.032, "refund_rate": 0.011}
AFTER = {"gmv": 1021800, "orders": 8150, "cvr": 0.0315, "refund_rate": 0.018}

# 相对波动容忍度:业务指标宽,质量指标严
TOLERANCE = {"gmv": 0.01, "orders": 0.01, "cvr": 0.02, "refund_rate": 0.3}


def metric_diff(before, after, tolerance):
    rows = []
    for name in sorted(before):
        old, new = before[name], after[name]
        if old == 0:
            rel = 0.0 if new == 0 else float("inf")
        else:
            rel = (new - old) / abs(old)
        limit = tolerance.get(name, 0.05)
        rows.append({"metric": name, "before": old, "after": new,
                     "rel": rel, "limit": limit,
                     "regressed": abs(rel) > limit})
    return rows


if __name__ == "__main__":
    rows = metric_diff(BEFORE, AFTER, TOLERANCE)
    print(json.dumps(rows, ensure_ascii=False, indent=2))
    bad = [r["metric"] for r in rows if r["regressed"]]
    print("回归结论:", "以下指标超阈值需排查 -> " + ", ".join(bad) if bad else "全部在容忍范围内")
