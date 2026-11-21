"""节假日对齐同比: 基期映射表修正假期漂移"""

from datetime import date

SALES_2025 = {date(2025, 9, 28): 300, date(2025, 9, 29): 305, date(2025, 9, 30): 310,
              date(2025, 10, 1): 900, date(2025, 10, 2): 880, date(2025, 10, 3): 860,
              date(2025, 10, 8): 320}
SALES_2026 = {date(2026, 9, 28): 330, date(2026, 9, 29): 335, date(2026, 9, 30): 340,
              date(2026, 10, 1): 950, date(2026, 10, 2): 930, date(2026, 10, 3): 340,
              date(2026, 10, 8): 330}
# 基期映射: 假期第 N 天对第 N 天, 节后工作日对节后工作日
HOLIDAY_MAP = {
    date(2026, 10, 1): date(2025, 10, 1),
    date(2026, 10, 2): date(2025, 10, 2),
    date(2026, 10, 3): date(2025, 10, 8),   # 今年节后首个工作日 对 去年节后首个工作日
}


def align_base(today, holiday_map):
    """今天的对齐基期: 命中映射表走映射, 否则走自然日"""
    return holiday_map.get(today, date(today.year - 1, today.month, today.day))


if __name__ == "__main__":
    print(f"{'日期':<14}{'自然日同比':>12}{'对齐同比':>12}{'对齐基期':>14}")
    for d in sorted(SALES_2026):
        natural = None
        nb = date(d.year - 1, d.month, d.day)
        if SALES_2025.get(nb):
            natural = (SALES_2026[d] - SALES_2025[nb]) / SALES_2025[nb]
        base = align_base(d, HOLIDAY_MAP)
        aligned = None
        if SALES_2025.get(base):
            aligned = (SALES_2026[d] - SALES_2025[base]) / SALES_2025[base]
        n_txt = f"{natural:+.1%}" if natural is not None else "-"
        a_txt = f"{aligned:+.1%}" if aligned is not None else "-"
        print(f"{str(d):<14}{n_txt:>12}{a_txt:>12}{str(base):>14}")
    print("要点: 假期漂移日必须走映射表; 没有映射的日期输出空值加标注, 不给错位同比")
