"""同期群对比的显著性: 等成熟龄对齐后再做两比例检验"""
import math
from datetime import date


def normal_cdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def age_days(cohort_start, today):
    return (today - cohort_start).days


def two_prop_ztest(r1, n1, r2, n2):
    p1, p2 = r1 / n1, r2 / n2
    pooled = (r1 + r2) / (n1 + n2)
    se = (pooled * (1 - pooled) * (1 / n1 + 1 / n2)) ** 0.5
    z = (p1 - p2) / se
    p_value = 2 * (1 - normal_cdf(abs(z)))
    return p1, p2, z, p_value


TODAY = date(2026, 11, 20)
COHORTS = {
    # 同期群: 起始日, 规模, 第 7 日留存人数
    "10月群": {"start": date(2026, 10, 1), "n": 1200, "retained_d7": 540},
    "11月群": {"start": date(2026, 11, 3), "n": 1100, "retained_d7": 440},
}
MATURE_AGE = 7


def mature_enough(c):
    return age_days(c["start"], TODAY) >= MATURE_AGE


if __name__ == "__main__":
    for name, c in COHORTS.items():
        print(f"{name}: 起始 {c['start']}, 今天成熟龄 {age_days(c['start'], TODAY)} 天, "
              f"{'可比较' if mature_enough(c) else '未成熟, 不可比'}")
    assert all(mature_enough(c) for c in COHORTS.values()), "等成熟龄对齐要求两群都满 7 天"
    oct_c, nov_c = COHORTS["10月群"], COHORTS["11月群"]
    p1, p2, z, pv = two_prop_ztest(oct_c["retained_d7"], oct_c["n"],
                                   nov_c["retained_d7"], nov_c["n"])
    print(f"等成熟龄第 7 日: 10月群 {p1:.1%} vs 11月群 {p2:.1%}, 差 {p1 - p2:+.1%}")
    print(f"两比例 z 检验: z={z:.3f}, p={pv:.4f}")
    verdict = "显著下降" if pv < 0.05 and p2 < p1 else ("显著上升" if pv < 0.05 else "差异不显著")
    print(f"结论(alpha=0.05): {verdict}")
    assert pv < 0.05 and p2 < p1, "本例 4.4 个百分点的差应有统计显著性"
    print("要点: 同期群对比先对齐成熟龄, 再用两比例检验说话, '看起来跌了'和'真的跌了'隔一个 p 值")
