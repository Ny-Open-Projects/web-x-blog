"""告警升级链: 确认超时自动升级"""

CHAIN = [("primary", 10), ("secondary", 10), ("manager", None)]
ALERTS = [
    ("err_rate_high", 2, "primary"),     # 2 分钟被 primary 确认
    ("queue_backlog", 14, "secondary"),  # primary 超时, secondary 接住
    ("db_disk_full", 25, None),          # 无人认领, 升级到底
]


def escalation(acker):
    path = []
    for role, limit in CHAIN:
        if acker == role:
            path.append(f"{role} 确认")
            return path, "闭环"
        if limit is None:
            path.append(f"{role} 电话强制介入")
            return path, "升级到底"
        path.append(f"{role} {limit} 分钟未确认 -> 升级")
    return path, "未闭环"


if __name__ == "__main__":
    for name, ack_after, acker in ALERTS:
        path, final = escalation(acker)
        print(f"告警 {name} ({ack_after} 分钟后由 {acker or '无人'} 认领):")
        for step in path:
            print(f"  {step}")
        print(f"  结果: {final}")
    print("要点: 升级是自动的时间驱动; 每级预算独立计时; 升级到底的告警当天必须复盘认领缺失原因")
