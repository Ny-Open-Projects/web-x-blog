import re

SCHEMA = {
    "user_id": {"type": int, "nullable": False},
    "email": {"type": str, "nullable": False, "pattern": r"^[^@\s]+@[^@\s]+\.[a-z]{2,}$"},
    "amount": {"type": float, "nullable": True, "min": 0, "max": 1_000_000},
}

def validate(row):
    errs = []
    for field, rule in SCHEMA.items():
        v = row.get(field)
        if v is None:
            if not rule["nullable"]:
                errs.append(f"{field} 不可为空")
            continue
        if not isinstance(v, rule["type"]):
            errs.append(f"{field} 类型应为 {rule['type'].__name__}")
            continue
        if "pattern" in rule and not re.match(rule["pattern"], v):
            errs.append(f"{field} 不匹配取值域")
        if ("min" in rule and v < rule["min"]) or ("max" in rule and v > rule["max"]):
            errs.append(f"{field} 超出统计边界")
    return errs

rows = [
    {"user_id": 1, "email": "a@b.com", "amount": 9.9},
    {"user_id": 2, "email": "bad-mail", "amount": -1},
    {"email": "c@d.com", "amount": None},
]
for i, r in enumerate(rows):
    print(i, validate(r) or "通过")
