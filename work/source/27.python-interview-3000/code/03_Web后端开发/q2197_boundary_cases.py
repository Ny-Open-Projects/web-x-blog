"""负向与边界用例的自动扩充: 按约束生成边界值矩阵(纯标准库)。"""

FIELD_RULES = {
    "name": {"type": "str", "min": 2, "max": 10},
    "qty": {"type": "int", "min": 1, "max": 999},
}


def materialize(rule, n):
    """把长度/数值边界物化成具体值。"""
    return "x" * n if rule["type"] == "str" else n


def boundary_cases(rule):
    lo, hi = rule["min"], rule["max"]
    cases = [("min", materialize(rule, lo), 200), ("max", materialize(rule, hi), 200),
             ("min-1", materialize(rule, lo - 1), 400), ("max+1", materialize(rule, hi + 1), 400),
             ("empty", "" if rule["type"] == "str" else None, 400),
             ("wrong_type", 12345 if rule["type"] == "str" else "many", 400)]
    return cases


total = 0
for field, rule in FIELD_RULES.items():
    print("##", field, rule)
    for label, value, expect in boundary_cases(rule):
        total += 1
        print("  {:9s} value={:10s} expect {}".format(label, str(value)[:10], expect))
print("共 {} 条边界用例".format(total))
assert total == 12
print("要点: 边界五点法加空值与类型错位是最划算的自动矩阵; 预期 400 却 200 的就是校验漏洞")
