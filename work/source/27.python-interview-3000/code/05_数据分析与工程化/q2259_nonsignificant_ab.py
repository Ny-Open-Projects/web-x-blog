"""实验不显著的正确解读: 差值区间与回溯功效"""

import math

NA = NB = 9800
XA, XB = 210, 232


def two_prop_ci(xa, na, xb, nb, z=1.96):
    pa, pb = xa / na, xb / nb
    diff = pb - pa
    pooled = (xa + xb) / (na + nb)
    se = math.sqrt(pooled * (1 - pooled) * (1 / na + 1 / nb))
    return diff, diff - z * se, diff + z * se


def required_n_per_arm(p, mde):
    """两比例检验 80% 功效所需每组样本量"""
    z_alpha, z_beta = 1.96, 0.84
    return 2 * p * (1 - p) * (z_alpha + z_beta) ** 2 / mde ** 2


if __name__ == "__main__":
    diff, lo, hi = two_prop_ci(XA, NA, XB, NB)
    print(f"A 率 {XA / NA:.3%}, B 率 {XB / NB:.3%}, 差 {diff:+.3%}")
    print(f"差值 95% 区间 [{lo:+.3%}, {hi:+.3%}], 跨 0 -> 不显著, 但不是'无差异'")
    p_pool = (XA + XB) / (NA + NB)
    need = required_n_per_arm(p_pool, abs(diff))
    print(f"按当前差异为 MDE, 每组需 {need:.0f} 样本, 是现有 {NA} 的 {need / NA:.1f} 倍")
    print("决策: 上界收益不够覆盖成本就放弃, 下界都够赚就上, 中间地带才延长实验")
