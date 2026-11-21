---
title: [Q2829] oncall 工具箱:一键分诊包
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2829 · oncall 工具箱:一键分诊包

> 难度:★★★★★ | 标签:oncall, 分诊

**问**:面试官:值班收到"支付好像有问题",第一分钟你在四个系统里来回登录,怎么提速?

**答**:一键分诊包,把查数据、查日志、查指标、查属主聚成一个入口。输入关键词"pay",30 秒内返回结构化证据:数据面 dwd_pay 已 23.8h 未成功(SLA 6h,超时 17.8h);日志面 pay-api 近 1 小时 47 条错误;指标面支付成功率 96.2%,较基线 99.0% 下滑 2.8pp;属主 team-pay 与 team-warehouse;判定"三条证据互证,异常成立"。价值不在自动化处置而在证据聚合——值班员不再在系统间拼故事,分诊包直接回答"哪里坏、谁负责、多严重"。设计要点:每条证据带量化(超时小时数、错误条数、下滑百分点),判定阈值可配置,证据不足时明确说"继续观察",不硬下结论。

```python
# file: code/05_数据分析与工程化/q2829_oncall_triage.py
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
```

**追问**:
- 追问 1:怎么防误报?—— 每条证据带置信(新鲜度超时倍数、错误率环比倍数),判定走多证据合取,单证据只提示不定罪。
- 追问 2:工具箱自己的可用性怎么保证?—— 只读查询加多数据源降级,某个源超时就跳过并标注,分诊包永远要能出结果。
