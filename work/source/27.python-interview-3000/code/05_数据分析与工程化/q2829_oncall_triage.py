"""oncall 工具箱: 一键分诊包, 把查数据 查日志 查指标 查属主聚成一个入口"""
from datetime import datetime

NOW = datetime(2026, 11, 4, 9, 0)
FRESHNESS = {
    "dwd_trade": {"last_success": "2026-11-04 02:30", "sla_hours": 6},
    "dwd_pay":   {"last_success": "2026-11-03 09:10", "sla_hours": 6},
    "dwd_user":  {"last_success": "2026-11-04 03:05", "sla_hours": 8},
}
RECENT_ERRORS = {"pay-api": 47, "order-api": 3, "settle-job": 2}
PAY_SUCCESS_HOURLY = [0.992, 0.991, 0.990, 0.988, 0.981, 0.962]
BASELINE = 0.99
REGISTRY = {
    "pay-api": {"owner": "team-pay", "tables": ["dwd_pay"]},
    "dwd_pay": {"owner": "team-warehouse"},
    "dwd_trade": {"owner": "team-warehouse"},
}


def staleness_hours(rec):
    last = datetime.strptime(rec["last_success"], "%Y-%m-%d %H:%M")
    return (NOW - last).total_seconds() / 3600


def triage(keyword):
    stale = []
    for table, rec in FRESHNESS.items():
        if keyword[:2] not in table and keyword not in table:
            continue
        late = staleness_hours(rec) - rec["sla_hours"]
        if late > 0:
            stale.append((table, staleness_hours(rec), rec["sla_hours"], late))
    err_top = sorted(((s, c) for s, c in RECENT_ERRORS.items()
                      if keyword[:3] in s or "pay" in s), key=lambda x: -x[1])
    last_rate = PAY_SUCCESS_HOURLY[-1]
    drop = (BASELINE - last_rate) * 100
    owners = set()
    for table, *_ in stale:
        meta = REGISTRY.get(table)
        if meta:
            owners.add(meta["owner"])
    for svc, _ in err_top:
        meta = REGISTRY.get(svc)
        if meta:
            owners.add(meta["owner"])
    verdict = "支付域异常成立: 表迟到 + 错误激增 + 成功率下滑, 三条证据互证" \
        if stale and err_top and drop > 1 else "证据不足, 继续观察"
    return {"stale_tables": stale, "error_top": err_top,
            "rate_drop_pp": round(drop, 1), "owners": sorted(owners),
            "verdict": verdict}


if __name__ == "__main__":
    bundle = triage("pay")
    print("== 一键分诊包: 支付 ==")
    for table, late_h, sla, over in bundle["stale_tables"]:
        print(f"数据: {table} 已 {late_h:.1f}h 未成功, SLA {sla}h, 超时 {over:.1f}h")
    for svc, cnt in bundle["error_top"]:
        print(f"日志: {svc} 近 1h 错误 {cnt} 条")
    print(f"指标: 支付成功率 {PAY_SUCCESS_HOURLY[-1]:.1%}, 较基线 {BASELINE:.1%} 下滑 {bundle['rate_drop_pp']}pp")
    print(f"属主: {', '.join(bundle['owners'])}")
    print(f"判定: {bundle['verdict']}")
    assert ("dwd_pay", 23.833333333333332, 6, 17.833333333333332) == bundle["stale_tables"][0] or \
        bundle["stale_tables"][0][0] == "dwd_pay"
    assert all(t[0] == "dwd_pay" for t in bundle["stale_tables"]), "只有 dwd_pay 破线"
    assert bundle["error_top"] and bundle["error_top"][0][0] == "pay-api"
    assert bundle["rate_drop_pp"] > 2.5, "成功率下滑应超过 2.5 个百分点"
    assert set(bundle["owners"]) == {"team-pay", "team-warehouse"}
    print("要点: 分诊包不替代人, 它把散在四个系统里的证据拼成一段话, 30 秒内回答'哪里坏 谁负责 多严重'")
