"""任务元数据台账: 属主与影响面速查, oncall 的第一张地图"""

TASKS = {
    "ods_sync_orders": {"owner": "team-infra", "oncall": "alice",
                        "sla_hours": 2, "downstream": ["dwd_trade"]},
    "dwd_trade":       {"owner": "team-warehouse", "oncall": "bob",
                        "sla_hours": 4, "downstream": ["dws_shop_day", "dws_category_day"]},
    "dws_shop_day":    {"owner": "team-warehouse", "oncall": "bob",
                        "sla_hours": 5, "downstream": ["ads_report"]},
    "dws_category_day": {"owner": "team-warehouse", "oncall": "carol",
                         "sla_hours": 5, "downstream": ["ads_report"]},
    "ads_report":      {"owner": "team-bi", "oncall": "dave",
                        "sla_hours": 6, "downstream": []},
}


def owner_of(task):
    return TASKS[task]["owner"]


def impact_closure(task):
    """下游影响闭包: 不含自身"""
    seen, stack = set(), [task]
    while stack:
        cur = stack.pop()
        for nxt in TASKS[cur]["downstream"]:
            if nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    return seen


def escalation_path(task):
    meta = TASKS[task]
    return [meta["oncall"], meta["owner"]]


def latest_sla_on_path(task):
    """影响面里最紧的 SLA, 决定处置节奏"""
    impacted = impact_closure(task) | {task}
    return min(TASKS[t]["sla_hours"] for t in impacted)


if __name__ == "__main__":
    print("谁坏了找谁:")
    print(f"  ods_sync_orders 属主 {owner_of('ods_sync_orders')}, 升级链 {escalation_path('ods_sync_orders')}")
    print("ods_sync_orders 挂了会影响:")
    for t in sorted(impact_closure("ods_sync_orders")):
        print(f"  - {t} (属主 {owner_of(t)}, SLA {TASKS[t]['sla_hours']}h)")
    tight = latest_sla_on_path("ods_sync_orders")
    print(f"影响面内最紧 SLA {tight} 小时 -> 处置窗口以此为准")
    assert impact_closure("ods_sync_orders") == {
        "dwd_trade", "dws_shop_day", "dws_category_day", "ads_report"}
    assert impact_closure("ads_report") == set(), "末端任务影响面为空"
    assert tight == 2, "最紧 SLA 应是上游同步任务的 2 小时"
    assert owner_of("ads_report") == "team-bi"
    print("要点: 出事先查台账再动手, 影响闭包决定通知谁, 最紧 SLA 决定多急, 这三问必须在 30 秒内有答案")
