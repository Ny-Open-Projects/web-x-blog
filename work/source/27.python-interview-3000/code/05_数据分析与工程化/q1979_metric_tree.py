"""指标树拆解:GMV = UV x 转化率 x 客单价,对数分解精确定位因子贡献"""

import math

BASE = {"uv": 52000, "cvr": 0.0420, "aov": 142.8}
CURR = {"uv": 48500, "cvr": 0.0451, "aov": 147.6}
FACTORS = [("uv", "流量UV"), ("cvr", "转化率"), ("aov", "客单价")]


def gmv(f):
    return f["uv"] * f["cvr"] * f["aov"]


def log_decompose(base, curr):
    """log(GMV1/GMV0) = sum log(因子比值),各因子贡献之和恒等于总变化"""
    total = math.log(gmv(curr) / gmv(base))
    parts = {k: math.log(curr[k] / base[k]) for k in base}
    return total, parts


if __name__ == "__main__":
    g0, g1 = gmv(BASE), gmv(CURR)
    print(f"GMV: {g0:,.0f} -> {g1:,.0f}  变化 {g1 / g0 - 1:+.2%}")
    total, parts = log_decompose(BASE, CURR)
    residue = total - sum(parts.values())
    print(f"总对数变化 {total:+.4f},残差 {residue:.2e}(对数分解精确无残差)")
    for k, name in FACTORS:
        delta = CURR[k] / BASE[k] - 1
        share = parts[k] / total if abs(total) > 1e-12 else 0.0
        print(f"  {name:<6} {BASE[k]:>8} -> {CURR[k]:>8} ({delta:+.1%})  贡献 {share:+.0%}")
    print("要点:乘法链指标用对数分解替代拍脑袋归因;总变化接近 0 时占比无意义只报方向;维度下钻答'谁',指标树答'为什么'")
