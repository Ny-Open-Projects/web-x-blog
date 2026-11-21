"""金丝雀指标对比:两比例检验、置信区间与自动放行/停止决策"""

import math
from statistics import NormalDist

Z = NormalDist().inv_cdf(0.975)

CONTROL = {"n": 50000, "conversions": 1500, "p99_ms": 200}
CANARY = {"n": 5000, "conversions": 160, "p99_ms": 240}  # p99 上涨 20%


def two_proportion_ci(s1, n1, s2, n2, z=Z):
    p1, p2 = s1 / n1, s2 / n2
    se = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    diff = p2 - p1
    return p1, p2, diff, diff - z * se, diff + z * se


def decide(control, canary, rel_drop_stop=0.05, latency_stop=0.10):
    p1, p2, diff, lo, hi = two_proportion_ci(
        control["conversions"], control["n"], canary["conversions"], canary["n"])
    rel = diff / p1
    reasons = []
    if hi < 0 and abs(rel) > rel_drop_stop:
        reasons.append(f"转化率相对下降 {rel:.1%} 且显著")
    if canary["p99_ms"] > control["p99_ms"] * (1 + latency_stop):
        reasons.append(f"p99 上涨 {(canary['p99_ms'] / control['p99_ms'] - 1):.0%} 超阈值")
    verdict = "STOP 停止金丝雀并回滚" if reasons else "PROMOTE 扩大灰度"
    return verdict, reasons, (p1, p2, diff, lo, hi)


if __name__ == "__main__":
    verdict, reasons, (p1, p2, diff, lo, hi) = decide(CONTROL, CANARY)
    print(f"control {p1:.2%} vs canary {p2:.2%},差值 {diff:+.2%} CI [{lo:+.2%}, {hi:+.2%}]")
    for r in reasons:
        print("  告警:", r)
    print("决策:", verdict)
    print("要点:金丝雀决策要同时看业务指标和护栏指标,且用置信区间而非裸差值")
