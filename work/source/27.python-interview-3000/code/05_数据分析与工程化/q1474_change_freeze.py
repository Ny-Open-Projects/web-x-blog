"""变更冻结期自动校验:计划发布时间与冻结窗口冲突检测"""

import datetime as dt

FREEZE_WINDOWS = [
    # 大促冻结: 周四 18:00 到 周六 24:00, 月末冻结: 每月最后一天
    (dt.datetime(2025, 6, 5, 18, 0), dt.datetime(2025, 6, 7, 23, 59), "618 大促冻结"),
    (dt.datetime(2025, 6, 30, 0, 0), dt.datetime(2025, 6, 30, 23, 59), "月末结算冻结"),
]

PLANNED_RELEASES = [
    dt.datetime(2025, 6, 6, 10, 0),
    dt.datetime(2025, 6, 12, 10, 0),
    dt.datetime(2025, 6, 30, 15, 0),
]


def check_freeze(release_time, windows):
    for start, end, reason in windows:
        if start <= release_time <= end:
            return False, f"命中冻结期 {reason}({start:%m-%d %H:%M} ~ {end:%m-%d %H:%M})"
    return True, "不在任何冻结窗口内"


if __name__ == "__main__":
    for t in PLANNED_RELEASES:
        ok, reason = check_freeze(t, FREEZE_WINDOWS)
        verdict = "允许发布" if ok else "拒绝,改期"
        print(f"{t:%Y-%m-%d %H:%M} -> {verdict}: {reason}")
    print("要点:冻结规则要么配在发布系统里硬卡,要么等于没有")
