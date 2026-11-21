"""上游 schema 变更防护:新增列放行、删列与类型变更阻断"""

EXPECTED = {
    "order_id": "str",
    "user_id": "int",
    "amount": "decimal",
    "created_at": "datetime",
}

ACTUAL_V2 = {
    "order_id": "str",
    "user_id": "str",       # 类型变更 -> BLOCK
    "amount": "decimal",
    "created_at": "datetime",
    "channel": "str",       # 新增列 -> WARN
}


def schema_diff(expected, actual):
    blockers, warnings = [], []
    for col, typ in expected.items():
        if col not in actual:
            blockers.append(f"列被删除: {col}")
        elif actual[col] != typ:
            blockers.append(f"类型变更: {col} {typ} -> {actual[col]}")
    for col in actual:
        if col not in expected:
            warnings.append(f"新增列: {col} {actual[col]}")
    return blockers, warnings


def gate(expected, actual):
    blockers, warnings = schema_diff(expected, actual)
    decision = "BLOCK" if blockers else "PASS"
    return decision, blockers, warnings


if __name__ == "__main__":
    decision, blockers, warnings = gate(EXPECTED, ACTUAL_V2)
    print("决策:", decision)
    for b in blockers:
        print("  [阻断]", b)
    for w in warnings:
        print("  [警告]", w)
    print("原则:阻断性变更让下游任务直接失败并通知上游,而不是静默吞掉脏数据")
