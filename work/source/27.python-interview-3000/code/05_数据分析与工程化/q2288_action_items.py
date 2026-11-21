"""复盘行动项跟踪: 逾期升级与老化报告"""

from datetime import date, timedelta

TODAY = date(2026, 3, 15)
ITEMS = [
    # 事项, 负责人, 到期日, 最近进展日
    ("给 dwd_clean 加行数断言", "李雷", date(2026, 3, 20), date(2026, 3, 12)),
    ("修复导出接口分页", "韩梅", date(2026, 3, 12), date(2026, 3, 1)),
    ("巡检白名单季度清理", "李雷", date(2026, 3, 5), date(2026, 2, 20)),
    ("值班手册更新 Q1 版", "王五", date(2026, 3, 30), None),
]


def bucket(due, touched, today):
    overdue = (today - due).days
    idle = 999 if touched is None else (today - touched).days
    if overdue > 0 and idle > 14:
        return "STALE", f"逾期 {overdue} 天且 {idle} 天无进展, 升级到主管"
    if overdue > 0:
        return "OVERDUE", f"逾期 {overdue} 天, 本周必须闭环"
    if overdue > -4:
        return "DUE_SOON", "临近到期, 关注"
    return "ON_TRACK", "正常推进"


if __name__ == "__main__":
    stats = {}
    for title, owner, due, touched in ITEMS:
        b, note = bucket(due, touched, TODAY)
        stats[b] = stats.get(b, 0) + 1
        print(f"[{b:<8}] {title} @{owner}: {note}")
    print("老化分布:", dict(sorted(stats.items())))
    print("要点: 四要素缺一不是行动项; STALE 比 OVERDUE 危险; 老化报告周发, 闭环率看趋势")
