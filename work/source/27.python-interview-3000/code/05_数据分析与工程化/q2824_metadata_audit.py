"""元数据完整性审计: 台账自身的缺口也要有人查"""

REGISTRY = {
    "ods_sync_user":  {"owner": "team-infra", "sla_hours": 2,
                       "downstream": ["dwd_user"]},                       # 缺 oncall
    "dwd_user":       {"oncall": "bob", "sla_hours": 4,
                       "downstream": ["dws_user_day"]},                   # 缺 owner
    "dws_user_day":   {"owner": "team-warehouse", "oncall": "bob",
                       "downstream": ["ads_funnel"]},                     # 缺 sla_hours
    "ads_funnel":     {"owner": "team-bi", "oncall": "carol", "sla_hours": 6,
                       "downstream": ["dm_unknown"]},                     # 下游是幽灵任务
    "ads_cohort":     {"owner": "team-bi", "oncall": "carol", "sla_hours": 6,
                       "downstream": []},
}

REQUIRED_FIELDS = ["owner", "oncall", "sla_hours"]


def audit(registry):
    findings = []
    for task, meta in sorted(registry.items()):
        for field in REQUIRED_FIELDS:
            if field not in meta:
                sev = "high" if field in ("owner", "sla_hours") else "medium"
                findings.append((task, f"缺少 {field}", sev))
        for down in meta.get("downstream", []):
            if down not in registry:
                findings.append((task, f"下游 {down} 未登记, 影响面查询会断链", "high"))
    return findings


if __name__ == "__main__":
    findings = audit(REGISTRY)
    print("审计发现:")
    for task, issue, sev in findings:
        print(f"  [{sev:<6}] {task}: {issue}")
    assert len(findings) == 4, "四处埋的缺口都应被发现"
    assert any("oncall" in i and t == "ods_sync_user" for t, i, _ in findings)
    assert any("dm_unknown" in i for t, i, _ in findings), "幽灵下游必须暴露"
    sevs = {s for _, _, s in findings}
    assert "high" in sevs, "缺属主或幽灵下游都应为高危"
    # 干净台账应零发现
    clean = {t: dict(m, **{k: "x" for k in REQUIRED_FIELDS if k not in m})
             for t, m in REGISTRY.items()}
    for t, m in clean.items():
        m["downstream"] = [d for d in m["downstream"] if d in clean]
    assert audit(clean) == [], "修补后台账应零发现"
    print("要点: 台账是事故时唯一敢信的地图, 自己必须被审计; 缺属主 幽灵下游都是高危, 每周自动扫一次")
