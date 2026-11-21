"""管道成本核算: 单次运行费用与成本漂移"""

RUNS = [
    # 任务, 用时分钟, 扫描 GB, 写出行数
    ("dwd_orders", 42, 380, 5_200_000),
    ("dws_user", 18, 95, 1_100_000),
    ("ads_report", 6, 12, 40_000),
]
RATE_PER_MIN = 0.9
RATE_PER_GB = 0.05
BASELINE_MIN = {"dwd_orders": 30, "dws_user": 15, "ads_report": 6}


def cost(minutes, gb):
    return minutes * RATE_PER_MIN + gb * RATE_PER_GB


if __name__ == "__main__":
    total = 0.0
    print(f"{'任务':<12}{'计算费':>7}{'扫描费':>7}{'合计':>7}{'每百万行':>9}{'耗时漂移':>9}")
    for name, m, gb, rows in RUNS:
        c = cost(m, gb)
        drift = f"{m / BASELINE_MIN[name] - 1:+.0%}".rjust(9)
        print(f"{name:<12}{m * RATE_PER_MIN:>7.1f}{gb * RATE_PER_GB:>7.1f}{c:>7.1f}"
              f"{c / (rows / 1_000_000):>9.1f}{drift}")
        total += c
    print(f"日总成本 {total:.1f} 元, 月度约 {total * 30:.0f} 元")
    print("要点: 单位成本比总额更能暴露小表重任务; 耗时漂移超 40% 先查倾斜膨胀, 再谈降配")
