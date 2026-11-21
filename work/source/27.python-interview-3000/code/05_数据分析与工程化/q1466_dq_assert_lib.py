"""数据质量断言库:声明式 DSL、解析器与结果对象"""

import re

TABLE = {
    "columns": ["user_id", "email", "age"],
    "rows": [
        {"user_id": 1, "email": "a@x.com", "age": 20},
        {"user_id": 1, "email": None, "age": 300},     # 重复 id + 非法年龄
        {"user_id": 3, "email": "c@x.com", "age": None},
    ],
}

RULES = [
    "row_count >= 2",
    "unique:user_id == True",
    "null_ratio:email <= 0.5",
    "in_range:age 0 120",
]


def parse_rule(rule):
    m = re.match(r"^(row_count|unique:(\w+)|null_ratio:(\w+)|in_range:(\w+))\s*(.*)$",
                 rule)
    kind, col, rest = m.group(1), m.group(2) or m.group(3) or m.group(4), m.group(5)
    return kind, col, rest.strip()


def eval_rule(table, rule):
    kind, col, rest = parse_rule(rule)
    rows = table["rows"]
    if kind == "row_count":
        op, bound = rest.split()
        actual = len(rows)
        ok = actual >= float(bound) if op == ">=" else actual == float(bound)
    elif kind.startswith("unique"):
        ids = [r[col] for r in rows if r.get(col) is not None]
        actual, ok = len(ids) == len(set(ids)), len(ids) == len(set(ids))
    elif kind.startswith("null_ratio"):
        op, bound = rest.split()
        actual = sum(1 for r in rows if r.get(col) is None) / len(rows)
        ok = actual <= float(bound)
    else:  # in_range col lo hi
        lo, hi = rest.split()
        bad = [r for r in rows if r.get(col) is not None
               and not (float(lo) <= r[col] <= float(hi))]
        actual, ok = len(bad), len(bad) == 0
    return {"rule": rule, "ok": ok, "actual": actual}


if __name__ == "__main__":
    results = [eval_rule(TABLE, r) for r in RULES]
    for r in results:
        print(("PASS" if r["ok"] else "FAIL"), r["rule"], "实际值:", r["actual"])
    print("总体:", "通过" if all(r["ok"] for r in results) else "存在质量问题,阻断下游")
