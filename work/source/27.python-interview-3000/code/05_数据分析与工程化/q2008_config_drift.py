"""配置漂移检测:各实例配置对基准逐键 diff,敏感键单独分级"""

BASELINE = {
    "log_level": "INFO", "timeout": 30, "max_conn": 100,
    "feature_dark_mode": "on", "db_host": "db.internal",
}
SENSITIVE = {"db_host", "auth_url"}   # 这些键漂移必须立即告警
INSTANCES = {
    "node-1": {"log_level": "INFO", "timeout": 30, "max_conn": 100,
               "feature_dark_mode": "on", "db_host": "db.internal"},
    "node-2": {"log_level": "DEBUG", "timeout": 30, "max_conn": 80,
               "feature_dark_mode": "on", "db_host": "db-staging.internal",
               "legacy_flag": "on"},
    "node-3": {"log_level": "INFO", "timeout": 60, "max_conn": 100,
               "feature_dark_mode": "off", "db_host": "db.internal"},
}


def diff(baseline, actual):
    keys = set(baseline) | set(actual)
    out = {}
    for k in sorted(keys):
        if k not in actual:
            out[k] = ("缺失", baseline[k])
        elif k not in baseline:
            out[k] = ("多余", actual[k])
        elif baseline[k] != actual[k]:
            out[k] = ("不同", f"{baseline[k]} -> {actual[k]}")
    return out


if __name__ == "__main__":
    for node, cfg in INSTANCES.items():
        d = diff(BASELINE, cfg)
        if not d:
            print(f"{node}: 一致")
            continue
        critical = [k for k in d if k in SENSITIVE]
        suffix = f"  <敏感键漂移 {critical},立即处理>" if critical else ""
        print(f"{node}: 漂移 {len(d)} 项 {d}{suffix}")
    print("要点:基准配置入库版本化,实例配置定时拉回 diff;缺失/多余/不同三类分开报;漂移修复是回归基准,而不是把漂移固化成新基准")
