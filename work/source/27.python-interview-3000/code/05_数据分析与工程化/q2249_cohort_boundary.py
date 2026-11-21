"""cohort 窗口边界: 半开区间归属与不完整期遮罩"""

from datetime import date, timedelta

COHORT_START = {"a": date(2026, 1, 5), "b": date(2026, 1, 5), "c": date(2026, 1, 12)}
ACTIVITIES = [
    ("a", date(2026, 1, 5)), ("a", date(2026, 1, 11)), ("a", date(2026, 1, 12)),
    ("b", date(2026, 1, 5)), ("b", date(2026, 1, 6)),
    ("c", date(2026, 1, 12)), ("c", date(2026, 1, 19)),
]
TODAY = date(2026, 1, 20)      # 数据观测截止日
PERIOD_DAYS = 7
MAX_PERIOD = 4                 # 想看 P0..P3


def period_index(cohort_start, active_day):
    """半开区间 [start+i*d, start+(i+1)*d) 归第 i 期, 边界日归下一期"""
    delta = (active_day - cohort_start).days
    if delta < 0:
        return None
    return delta // PERIOD_DAYS


if __name__ == "__main__":
    for user, start in sorted(COHORT_START.items()):
        cells = []
        for i in range(MAX_PERIOD):
            users = {u for u, day in ACTIVITIES
                     if u == user and period_index(start, day) == i}
            window_end = start + timedelta(days=(i + 1) * PERIOD_DAYS - 1)
            cells.append(f"{len(users)}人" if window_end <= TODAY else "未到期")
        print(f"cohort {user} 起始 {start}: " + " | ".join(
            f"P{i}={c}" for i, c in enumerate(cells)))
    assert period_index(date(2026, 1, 5), date(2026, 1, 12)) == 1, "边界日应归下一期"
    assert period_index(date(2026, 1, 5), date(2026, 1, 11)) == 0, "窗口最后一日归本期"
    print("边界自测通过: 1月11日属 P0, 1月12日属 P1, 半开区间方向唯一")
    print("遮罩规则: 窗口未走完的期只可看不可比, 报表上必须标'未到期'")
