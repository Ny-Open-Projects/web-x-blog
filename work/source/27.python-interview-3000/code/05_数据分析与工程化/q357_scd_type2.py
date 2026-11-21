from datetime import date

def apply_scd2(dim_rows, current, new_state, eff_date):
    """拉链表:字段有变才关旧开新。current: uid -> row"""
    uid = new_state["uid"]
    old = current.get(uid)
    if old is None:
        new_state.update(eff_from=eff_date, eff_to=None, is_current=True)
        dim_rows.append(new_state)
    elif any(new_state[k] != old[k] for k in ("city",) ):
        old["eff_to"] = eff_date            # 关旧
        old["is_current"] = False
        new_state.update(eff_from=eff_date, eff_to=None, is_current=True)
        dim_rows.append(new_state)          # 开新
    current[uid] = new_state

if __name__ == "__main__":
    rows = []
    cur = {}
    apply_scd2(rows, cur, {"uid": 1, "city": "BJ"}, date(2026, 1, 1))
    apply_scd2(rows, cur, {"uid": 1, "city": "BJ"}, date(2026, 3, 1))  # 未变,不产生新版本
    apply_scd2(rows, cur, {"uid": 1, "city": "SH"}, date(2026, 6, 1))  # 变更,拉链
    for r in rows:
        print(r)
    assert len(rows) == 2, "未变更不应新增版本"
