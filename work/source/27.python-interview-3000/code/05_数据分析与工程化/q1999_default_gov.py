"""字段默认值治理:注册表单点管理,使用默认必须留审计痕迹"""

DEFAULTS = {
    # 字段: (默认值, 生效自版本, 理由)
    "channel": ("unknown", "v1.2", "老版本埋点无渠道字段"),
    "device": ("unknown", "v1.0", "服务端日志无设备信息"),
}


def fill_defaults(record):
    filled, used = dict(record), []
    for field, (value, since, _why) in DEFAULTS.items():
        if field not in filled or filled[field] in (None, ""):
            filled[field] = value
            used.append((field, value, since))
    return filled, used


def audit(filled_rows):
    """统计默认值命中率:命中率升高=上游字段劣化"""
    n = len(filled_rows)
    if not n:
        return {}
    stats = {}
    for _, used in filled_rows:
        for field, _, _since in used:
            stats[field] = stats.get(field, 0) + 1
    return {f: c / n for f, c in stats.items()}


if __name__ == "__main__":
    batch = [
        {"uid": "u1", "channel": "push"},
        {"uid": "u2"},
        {"uid": "u3", "channel": None},
        {"uid": "u4", "channel": "search", "device": "ios"},
    ]
    filled_rows = []
    for r in batch:
        filled, used = fill_defaults(r)
        filled_rows.append((filled, used))
        if used:
            print(f"uid={r['uid']} 补默认: {used}")
    rates = audit(filled_rows)
    print("默认值命中率:", {k: f"{v:.0%}" for k, v in rates.items()})
    if rates.get("channel", 0) > 0.5:
        print("告警:channel 默认值命中过半,推动上游修埋点,而不是永久兜底")
    print("要点:默认值必须注册生效版本与理由,禁止散落硬编码;命中率是上游健康度信号,兜底变常态等于掩盖故障")
