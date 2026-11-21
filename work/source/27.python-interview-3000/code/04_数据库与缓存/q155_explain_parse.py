"""解析 EXPLAIN 结果行, 自动标记可疑计划(以常见字段为例)"""
from typing import Any

BAD_TYPES = {"ALL", "index"}           # 全表/全索引扫描
BAD_EXTRA = ("Using filesort", "Using temporary")
GOOD_EXTRA = "Using index"


def review_plan(rows: list[dict[str, Any]]) -> list:
    findings = []
    for row in rows:
        table = row.get("table", "?")
        if row.get("type") in BAD_TYPES:
            findings.append(f"{table}: 全表扫描 type={row['type']}")
        if row.get("rows", 0) and int(row["rows"]) > 100_000:
            findings.append(f"{table}: 预估扫描 {row['rows']} 行 过大")
        extra = row.get("Extra", "")
        for bad in BAD_EXTRA:
            if bad in extra:
                findings.append(f"{table}: {bad} 需要优化排序或分组")
        if GOOD_EXTRA in extra:
            findings.append(f"{table}: 覆盖索引生效 Using index")
    return findings


if __name__ == "__main__":
    plan = [
        {"table": "orders", "type": "ALL", "rows": 500000, "Extra": "Using where; Using filesort"},
        {"table": "users", "type": "eq_ref", "rows": 1, "Extra": "Using index"},
    ]
    for msg in review_plan(plan):
        print(msg)
