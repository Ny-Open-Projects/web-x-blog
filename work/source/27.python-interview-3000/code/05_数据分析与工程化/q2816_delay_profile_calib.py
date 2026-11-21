"""到达延迟的分位画像: 用历史分位数标定容忍线, 而不是拍脑袋"""

SOURCES = {
    "pay_core": [3 + (i * 7) % 25 + (i * i) % 40 for i in range(1, 121)],
    "log_sink": [10 + (i * 13) % 200 + (i * i) % 180 for i in range(1, 121)],
}
FLAT_TOLERANCE = 60


def percentile(sorted_vals, q):
    """最近秩法: 取第 ceil(q*n) 个值"""
    idx = max(0, -(-len(sorted_vals) * q // 100) - 1)
    return sorted_vals[min(idx, len(sorted_vals) - 1)]


def profile(delays):
    s = sorted(delays)
    p50 = percentile(s, 50)
    p90 = percentile(s, 90)
    p99 = percentile(s, 99)
    tol = p90          # 容忍线取 p90: 九成的历史延迟都能等到
    hard = p99         # 硬顶取 p99: 千里之一才升级
    coverage = sum(1 for d in s if d <= tol) / len(s)
    return p50, p90, p99, tol, hard, coverage


if __name__ == "__main__":
    print(f"{'数据源':<10}{'p50':>5}{'p90':>5}{'p99':>5}{'容忍线':>6}{'硬顶':>6}{'覆盖率':>7}")
    for name, delays in SOURCES.items():
        p50, p90, p99, tol, hard, cov = profile(delays)
        flat_cov = sum(1 for d in delays if d <= FLAT_TOLERANCE) / len(delays)
        print(f"{name:<10}{p50:>5}{p90:>5}{p99:>5}{tol:>6}{hard:>6}{cov:>7.1%}   统一60分线覆盖率 {flat_cov:.1%}")
        assert cov >= 0.90, "容忍线应覆盖至少九成历史延迟"
        assert hard >= tol, "硬顶不得低于容忍线"
        if name == "pay_core":
            assert tol < FLAT_TOLERANCE, "核心源的标定容忍线应远小于一刀切的 60 分钟"
    print("要点: 容忍线是统计量不是行政数字, p90 当等待线, p99 当升级线, 分源标定后每年随画像复校")
