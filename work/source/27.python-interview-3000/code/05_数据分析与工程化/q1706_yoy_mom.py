"""同环比计算器:日历对齐,不完整期只比同期,避免环比虚降"""

from datetime import date, timedelta

REVENUE_2025_09 = {date(2025, 9, d): 1000 + d * 10 for d in range(1, 16)}  # 只更新到 15 日
REVENUE_2025_08 = {date(2025, 8, d): 1000 + d * 5 for d in range(1, 32)}
REVENUE_2024_09 = {date(2024, 9, d): 900 + d * 8 for d in range(1, 31)}


def period_sum(data, start, end):
    return sum(v for d, v in data.items() if start <= d <= end)


def mom_aligned(current, previous, as_of):
    """月环比:不完整期只比上月同日为止,避免"9月半月比8月全月"的假象"""
    month_start_cur = as_of.replace(day=1)
    prev_month_end = month_start_cur - timedelta(days=1)
    month_start_prev = prev_month_end.replace(day=1)
    aligned_prev_end = month_start_prev + timedelta(days=as_of.day - 1)
    cur_sum = period_sum(current, month_start_cur, as_of)
    prev_sum = period_sum(previous, month_start_prev, aligned_prev_end)
    return cur_sum, prev_sum, (cur_sum - prev_sum) / prev_sum


def yoy_aligned(current, last_year, as_of):
    """月同比:同样对齐到去年同月的同日为止,完整月后自然切换成整月口径"""
    month_start = as_of.replace(day=1)
    ly_start = date(as_of.year - 1, as_of.month, 1)
    ly_end = date(as_of.year - 1, as_of.month, as_of.day)
    cur_sum = period_sum(current, month_start, as_of)
    ly_sum = period_sum(last_year, ly_start, ly_end)
    return cur_sum, ly_sum, (cur_sum - ly_sum) / ly_sum


if __name__ == "__main__":
    as_of = date(2025, 9, 15)
    cur, prev, r = mom_aligned(REVENUE_2025_09, REVENUE_2025_08, as_of)
    print(f"月环比(截至 9/15,与 8/1-8/15 对齐): {cur} vs {prev} = {r:+.1%}")
    naive = sum(REVENUE_2025_09.values()) / sum(REVENUE_2025_08.values()) - 1
    print(f"错误口径(9月半月 vs 8月全月): {naive:+.1%} <- 虚降,不能发出去")
    cur, ly, r = yoy_aligned(REVENUE_2025_09, REVENUE_2024_09, as_of)
    print(f"月同比(9/1-9/15 vs 去年同期): {cur} vs {ly} = {r:+.1%}")
    print("要点:不完整期必须做日历对齐;月度口径天然规避大小月,日度口径要小心 28-31 号错位")
