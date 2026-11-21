"""同店同比:剔除开业不满 N 月的门店,避免门店集合漂移虚增同比"""

from datetime import date

STORES = {
    "s1": {"open": date(2023, 6, 1), "cur": 520.0, "ly": 480.0},
    "s2": {"open": date(2022, 3, 1), "cur": 300.0, "ly": 310.0},
    "s3": {"open": date(2022, 11, 1), "cur": 410.0, "ly": 395.0},
    "s4": {"open": date(2025, 8, 1), "cur": 180.0, "ly": 0.0},   # 新店,去年无营收
    "s5": {"open": date(2025, 10, 1), "cur": 60.0, "ly": 0.0},   # 新店
}
AS_OF = date(2026, 6, 30)
MIN_AGE_MONTHS = 12


def month_age(opened, as_of):
    return (as_of.year - opened.year) * 12 + (as_of.month - opened.month)


if __name__ == "__main__":
    cur_all = sum(s["cur"] for s in STORES.values())
    ly_all = sum(s["ly"] for s in STORES.values())
    mature = {k: s for k, s in STORES.items()
              if month_age(s["open"], AS_OF) >= MIN_AGE_MONTHS}
    cur_same = sum(s["cur"] for s in mature.values())
    ly_same = sum(s["ly"] for s in mature.values())
    print(f"全店口径: {cur_all:.0f} vs {ly_all:.0f}  同比 {cur_all / ly_all - 1:+.1%}(被新店抬高)")
    print(f"同店口径(开业≥{MIN_AGE_MONTHS}月,共 {len(mature)} 家): "
          f"{cur_same:.0f} vs {ly_same:.0f}  同比 {cur_same / ly_same - 1:+.1%}")
    new_contrib = cur_all - cur_same
    if cur_all > ly_all:
        print(f"新店贡献 {new_contrib:.0f},占全部增量 {new_contrib / (cur_all - ly_all):.0%}")
    print("要点:门店/品类集合随时间漂移,同比必须固定可比集合;同店定义(剔除几个月)要写进报表标题,换定义等于换指标")
