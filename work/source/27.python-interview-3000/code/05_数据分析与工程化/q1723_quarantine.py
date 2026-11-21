"""脏数据隔离区:不合格行进 quarantine 带原因码与原始载荷,好数据继续走"""

GOOD_ROWS = []
QUARANTINE = []


def validate(row):
    """返回 None 表示通过,否则返回 (原因码, 详情)"""
    uid, amount, city = row
    if not isinstance(uid, str) or not uid:
        return ("missing_key", "user_id 为空")
    if not isinstance(amount, (int, float)) or not 0 <= amount <= 100000:
        return ("bad_amount", f"金额越界 {amount!r}")
    if city not in {"华东", "华南", "华北"}:
        return ("bad_enum", f"非法城市 {city!r}")
    return None


def ingest(rows):
    stats = {"pass": 0, "quarantined": 0}
    for row in rows:
        reason = validate(row)
        if reason is None:
            GOOD_ROWS.append(row)
            stats["pass"] += 1
        else:
            QUARANTINE.append({"row": row, "reason": reason[0], "detail": reason[1]})
            stats["quarantined"] += 1
    return stats


if __name__ == "__main__":
    batch = [
        ("u1", 120, "华东"),
        ("u2", -5, "华南"),
        ("", 80, "华北"),
        ("u4", 250000, "华东"),
        ("u5", 66, "海外"),
        ("u6", 99, "华北"),
    ]
    stats = ingest(batch)
    print(f"通过 {stats['pass']} 条,隔离 {stats['quarantined']} 条")
    for q in QUARANTINE:
        print(f"  原因={q['reason']} 明细={q['detail']} 原始行={q['row']}")
    print("要点:隔离区带原因码与原始载荷,修复后回放而不是丢弃;同一原因码批量出现要报警——可能是上游改口径而不是脏数据")
