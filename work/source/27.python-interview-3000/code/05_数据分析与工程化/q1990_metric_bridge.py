"""口径变更桥接:并行期双口径算校准系数,历史数据按系数换算可比"""

PARALLEL = [
    # (日期, 旧口径日活, 新口径日活)
    ("11-01", 10200, 9100), ("11-02", 10450, 9320), ("11-03", 10180, 9050),
    ("11-04", 10990, 9800), ("11-05", 11230, 10010), ("11-06", 12300, 11020),
    ("11-07", 12180, 10900),
]


def calibration_ratio(rows):
    """并行期新/旧比值的中位数做校准系数,抗单日波动"""
    ratios = sorted(new / old for _, old, new in rows)
    n = len(ratios)
    mid = ratios[n // 2] if n % 2 else (ratios[n // 2 - 1] + ratios[n // 2]) / 2
    return mid, ratios


if __name__ == "__main__":
    k, ratios = calibration_ratio(PARALLEL)
    print("并行期 新/旧 比值:", [f"{r:.4f}" for r in ratios])
    print(f"校准系数(中位数)k = {k:.4f}")
    old_last = PARALLEL[-1][1]   # 并行期最后一天的旧口径实测
    print(f"桥接校验: 同日旧口径 {old_last} x k = {old_last * k:.0f}"
          f"  ≈ 新口径实测 {PARALLEL[-1][2]}")
    drift = max(ratios) - min(ratios)
    verdict = "稳定,系数可用" if drift < 0.03 else "波动大,先查口径实现再并行"
    print(f"比值极差 {drift:.4f} -> {verdict}")
    print("要点:切换前至少两周并行;系数取中位数;换算序列必须标注口径与系数生效区间,报表读者有权知道今天和昨天用的不是一个定义")
