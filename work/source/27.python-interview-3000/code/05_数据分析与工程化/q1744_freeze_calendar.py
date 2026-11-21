"""冻结日历:日期区间 + 星期规则求并集判定可否发布,并给最近可发布窗口"""

from datetime import date, timedelta

FREEZE_RANGES = [
    (date(2025, 11, 1), date(2025, 11, 12), "双11大促"),
    (date(2025, 12, 28), date(2026, 1, 3), "财结封账"),
]
WEEKLY_FROZEN = {4: "周五变更窗口禁用"}  # Monday=0


def is_frozen(d):
    for start, end, reason in FREEZE_RANGES:
        if start <= d <= end:
            return True, reason
    if d.weekday() in WEEKLY_FROZEN:
        return True, WEEKLY_FROZEN[d.weekday()]
    return False, None


def next_release(d, horizon=45):
    for i in range(horizon):
        cand = d + timedelta(days=i)
        if not is_frozen(cand)[0]:
            return cand, i
    return None, horizon


if __name__ == "__main__":
    for d in (date(2025, 10, 28), date(2025, 11, 7), date(2025, 12, 30)):
        frozen, reason = is_frozen(d)
        if frozen:
            cand, wait = next_release(d)
            print(f"{d} 冻结中({reason}),最近可发布 {cand},等待 {wait} 天")
        else:
            print(f"{d} 可发布")
    print("要点:冻结规则=区间+星期+临时事件的并集,审批系统强制校验;大促冻结要覆盖放量前 3 天和收尾 2 天,临时冻结要能秒级加进去")
