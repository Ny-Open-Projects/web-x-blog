"""渠道响应曲线: 幂律拟合与边际 CPA, 回答下一块钱投谁"""

import math

# 渠道 -> 历史不同预算档位下的 花费, 安装数
DATA = {
    "应用商店": [(5000, 760), (10000, 1450), (20000, 2800), (40000, 5400), (80000, 10500)],
    "搜索": [(5000, 800), (10000, 1350), (20000, 2150), (40000, 3300), (80000, 4800)],
    "信息流": [(5000, 600), (10000, 1000), (20000, 1600), (40000, 2500), (80000, 3800)],
}
CURRENT = {"应用商店": 20000, "搜索": 20000, "信息流": 20000}


def fit_power(pairs):
    """安装 = k * 花费^b, 对数线性最小二乘"""
    xs = [math.log(s) for s, _ in pairs]
    ys = [math.log(i) for _, i in pairs]
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    var = sum((x - mx) ** 2 for x in xs)
    b = cov / var
    k = math.exp(my - b * mx)
    return k, b


if __name__ == "__main__":
    print(f"{'渠道':<8}{'弹性b':>7}{'当前边际CPA':>12}")
    ranked = []
    for ch, pairs in DATA.items():
        k, b = fit_power(pairs)
        s0 = CURRENT[ch]
        marginal = k * b * s0 ** (b - 1)          # 边际安装数 每 元
        mcpa = 1.0 / marginal                      # 边际每安装成本
        ranked.append((mcpa, ch, b))
        print(f"{ch:<8}{b:>7.2f}{mcpa:>10.1f}元")
    ranked.sort()
    print(f"追加预算排序: {' > '.join(ch for _, ch, _ in ranked)}")
    print("要点: 弹性接近 1 的渠道优先吃增量; 平均 CPA 会排错序, 边际才是加钱依据; 外推一倍以上预算不可信")
