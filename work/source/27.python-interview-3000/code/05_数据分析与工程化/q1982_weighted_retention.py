"""加权留存:按基期流量加权,小流量日不再拉偏整体留存"""

try:
    import pandas as pd
except ImportError:
    pd = None

COHORTS = [
    # (基期日, 基期 DAU, 次日留存)
    ("周一", 12000, 0.44), ("周二", 11500, 0.43), ("周三", 11800, 0.45),
    ("周四", 11200, 0.42), ("周五", 13400, 0.38), ("周六", 15800, 0.31),
    ("周日", 15200, 0.33),
]


def simple_avg(rows):
    return sum(r for _, _, r in rows) / len(rows)


def weighted_avg(rows):
    total_w = sum(n for _, n, _ in rows)
    return sum(n * r for _, n, r in rows) / total_w


if __name__ == "__main__":
    s, w = simple_avg(COHORTS), weighted_avg(COHORTS)
    for day, n, r in COHORTS:
        print(f"  {day} DAU={n:>6} 次留 {r:.0%}")
    print(f"简单平均留存 {s:.1%}  流量加权留存 {w:.1%}  差 {w - s:+.1%}")
    print("要点:周末流量大但留存低,简单平均被高留存的工作日抬高;整体留存要么按流量加权,要么直接看 cohort 矩阵,别用日留存求均值")
    if pd is not None:
        df = pd.DataFrame(COHORTS, columns=["dow", "dau", "ret"])
        print("pandas 视角: 简单 =", round(df["ret"].mean(), 4),
              "加权 =", round(float((df["dau"] * df["ret"]).sum() / df["dau"].sum()), 4))
