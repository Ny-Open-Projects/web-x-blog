"""数据订正流水: 前后镜像与预期旧值守门, 订正也是被审计的数据"""

DATASET = {
    "t1": {"amount": 100.0, "city": "北京"},
    "t2": {"amount": 250.0, "city": "上海"},
    "t3": {"amount": 88.0, "city": "广州"},
}

JOURNAL = [
    {"corr_id": "C001", "key": "t1", "field": "amount",
     "old": 100.0, "new": 120.0, "reason": "退款漏计", "operator": "alice"},
    {"corr_id": "C002", "key": "t2", "field": "amount",
     "old": 260.0, "new": 250.0, "reason": "口径调整", "operator": "bob"},
    {"corr_id": "C003", "key": "t3", "field": "city",
     "old": "广州", "new": "深圳", "reason": "地址勘误", "operator": "alice"},
]


def apply_corrections(dataset, journal):
    """预期旧值必须与现值一致才允许订正; 全过程落审计台账"""
    applied, rejected = [], []
    for entry in journal:
        rec = dataset.get(entry["key"])
        if rec is None:
            rejected.append((entry["corr_id"], f"键 {entry['key']} 不存在"))
            continue
        current = rec.get(entry["field"])
        if current != entry["old"]:
            rejected.append((entry["corr_id"],
                             f"预期旧值 {entry['old']!r} 与现值 {current!r} 不符, 数据已漂移需人工复核"))
            continue
        rec[entry["field"]] = entry["new"]
        applied.append((entry["corr_id"], entry["old"], entry["new"],
                        entry["reason"], entry["operator"]))
    return applied, rejected


if __name__ == "__main__":
    applied, rejected = apply_corrections(DATASET, JOURNAL)
    print("成功订正:")
    for cid, old, new, reason, op in applied:
        print(f"  {cid}: {old!r} -> {new!r}  ({reason}, by {op})")
    print("被拒订正:")
    for cid, why in rejected:
        print(f"  {cid}: {why}")
    assert DATASET["t1"]["amount"] == 120.0 and DATASET["t3"]["city"] == "深圳"
    assert rejected == [("C002", "预期旧值 260.0 与现值 250.0 不符, 数据已漂移需人工复核")]
    assert len(applied) == 2, "两条合法订正应成功"
    print("要点: 订正单自带预期旧值, 守门失败就进人工队列; 每条订正有单号 前镜像 理由 操作人, 订正本身可被重放审计")
