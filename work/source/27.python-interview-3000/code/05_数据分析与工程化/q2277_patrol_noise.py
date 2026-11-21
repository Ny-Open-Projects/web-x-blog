"""巡检脚本的降噪聚合: 发现项折叠与白名单豁免"""

from datetime import date

FINDINGS = [
    ("disk_high", "node-1", "WARN"), ("disk_high", "node-1", "WARN"),
    ("disk_high", "node-1", "WARN"),
    ("disk_high", "node-2", "WARN"),
    ("stale_table", "dws_user", "FAIL"), ("stale_table", "dws_user", "FAIL"),
    ("slow_task", "ads_report", "WARN"),
    ("cert_expiry", "gateway", "WARN"),
]
ALLOWLIST = {   # 规则, 资源 -> 豁免到期日, 理由
    ("slow_task", "ads_report"): (date(2026, 4, 1), "已排期 3 月底优化, 免打扰"),
    ("cert_expiry", "gateway"): (date(2026, 1, 1), "旧豁免已过期, 应恢复告警"),
}
TODAY = date(2026, 3, 15)

if __name__ == "__main__":
    groups, suppressed, expired = {}, 0, []
    for rule, res, level in FINDINGS:
        allow = ALLOWLIST.get((rule, res))
        if allow and allow[0] >= TODAY:
            suppressed += 1
            continue
        if allow and allow[0] < TODAY:
            expired.append((rule, res))
        key = (rule, res)
        g = groups.setdefault(key, {"level": level, "count": 0})
        g["count"] += 1
    print("聚合后发现项:")
    for (rule, res), g in groups.items():
        print(f"  [{g['level']}] {rule} @ {res} x{g['count']}")
    print(f"白名单抑制 {suppressed} 条; 过期豁免需清理: {expired}")
    print("要点: 同指纹折叠计数; 豁免必带到期日, 过期自动恢复; FAIL 排最上, 值班只看一屏")
