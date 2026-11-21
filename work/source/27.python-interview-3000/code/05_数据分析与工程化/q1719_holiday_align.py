"""大促对齐同比:按活动日位次比较,而不是按自然日硬比"""

from datetime import date, timedelta

GMV = {
    # 2024 大促 10-28 开闸
    date(2024, 10, 28): 90, date(2024, 10, 29): 110, date(2024, 10, 30): 130,
    date(2024, 10, 31): 160, date(2024, 11, 1): 210, date(2024, 11, 11): 320,
    # 2025 大促 10-24 开闸,节奏提前 4 天
    date(2025, 10, 24): 95, date(2025, 10, 25): 118, date(2025, 10, 26): 140,
    date(2025, 10, 27): 172, date(2025, 10, 28): 226, date(2025, 11, 7): 341,
}
PROMO_START = {"2024": date(2024, 10, 28), "2025": date(2025, 10, 24)}


def raw_yoy(gmv, today):
    last = date(today.year - 1, today.month, today.day)
    return gmv.get(today, 0) / gmv.get(last, 1) - 1


def aligned_yoy(gmv, today, starts):
    """按大促第 N 天对齐:今天是本届第几天,就去比上届同一位次"""
    offset = (today - starts[str(today.year)]).days
    last = starts[str(today.year - 1)] + timedelta(days=offset)
    cur, prev = gmv.get(today, 0), gmv.get(last, 0)
    return offset, last, (cur - prev) / prev if prev else 0.0


if __name__ == "__main__":
    today = date(2025, 10, 28)
    print(f"自然日同比: {raw_yoy(GMV, today):+.1%} <- 本届第5天比上届第1天,虚高不能用")
    off, last, r = aligned_yoy(GMV, today, PROMO_START)
    print(f"大促对齐同比: 今日=本届第 {off + 1} 天,对齐 {last} -> {r:+.1%}")
    print("要点:大促/春节/寒暑假等跳变日历单独建表,同比按活动位次对齐;非活动日期仍用自然日口径,两套口径并行并明确标注")
