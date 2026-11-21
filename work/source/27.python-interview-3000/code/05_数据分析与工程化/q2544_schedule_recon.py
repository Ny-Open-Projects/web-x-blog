"""应跑未跑对账: 调度清单与执行台账的差集"""

SCHEDULE = {"etl_orders", "etl_payments", "etl_users"}     # 每日必跑任务
LEDGER = [
    ("etl_orders", "2026-03-01"),
    ("etl_payments", "2026-03-01"),
    ("etl_users", "2026-02-28"),        # 跑了但跑错日期
    ("adhoc_backfill", "2026-03-01"),   # 计划外临时任务
]


def reconcile(schedule, ledger, day):
    executed = {t for t, d in ledger if d == day}
    missing = sorted(schedule - executed)
    orphans = sorted(executed - schedule)
    return missing, orphans


if __name__ == "__main__":
    day = "2026-03-01"
    missing, orphans = reconcile(SCHEDULE, LEDGER, day)
    print(f"{day} 对账: 漏跑 {missing or '无'}, 计划外 {orphans or '无'}")
    assert missing == ["etl_users"], "etl_users 昨天跑的不算今天数"
    assert orphans == ["adhoc_backfill"], "临时任务必须显式登记计划"
    print("处置: 漏跑任务立即补跑并回填水位; 计划外任务补登记, 否则依赖对账永远有暗账")
    missing2, _ = reconcile(SCHEDULE, LEDGER + [("etl_users", day)], day)
    assert not missing2, "补跑后应清零"
    print("要点: 台账按 逻辑日期 对账而不是按执行时间, 补跑昨天的任务救不了今天的分区")
