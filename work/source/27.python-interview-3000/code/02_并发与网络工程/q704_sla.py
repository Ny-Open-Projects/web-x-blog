from datetime import timedelta


def downtime_budget(availability: float) -> dict:
    year = timedelta(days=365).total_seconds()
    month = timedelta(days=30).total_seconds()
    return {
        "availability": availability,
        "year_human": str(timedelta(seconds=year * (1 - availability))),
        "month_human": str(timedelta(seconds=month * (1 - availability))),
        "error_budget_year_s": round(year * (1 - availability)),
    }


def achieved_from_incidents(incidents: list, window_days: int = 30) -> float:
    window = timedelta(days=window_days).total_seconds()
    down = sum(s for s in incidents)
    return 1 - down / window


def series_availability(*services: float) -> float:
    """串联依赖: 可用性相乘。"""
    r = 1.0
    for s in services:
        r *= s
    return r


if __name__ == "__main__":
    print("停机预算对照表:")
    for a in (0.99, 0.999, 0.9999, 0.99999):
        b = downtime_budget(a)
        print(f"  {a * 100:6.3f}% → 年 {b['year_human']}, 月 {b['month_human']}, "
              f"错误预算 {b['error_budget_year_s']}s/年")

    print("\n串联依赖折算:")
    print("  自身 99.95% × DB 99.95% × 缓存 99.9% =",
          f"{series_availability(0.9995, 0.9995, 0.999) * 100:.3f}%")
    print("  结论: 链路上每加一环, 整体 SLA 都被拉低 → 非关键依赖要可降级")

    print("\n事故复盘口径 (30 天窗口):")
    incidents = [1800, 600, 300]  # 三次事故: 30min, 10min, 5min
    got = achieved_from_incidents(incidents)
    print(f"  事故总停机 {sum(incidents)}s → 实际可用性 {got * 100:.3f}% "
          f"({'达标 99.9%' if got >= 0.999 else '未达 99.9%'})")

    print("\n错误预算实践: 月度预算 43.2min, 已烧 40min → 冻结发布, 优先稳定性")
