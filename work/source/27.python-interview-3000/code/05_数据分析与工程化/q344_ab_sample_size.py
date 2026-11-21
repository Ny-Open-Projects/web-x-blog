import math

def sample_size(p_baseline, mde, alpha=0.05, power=0.8):
    """两比例检验样本量(每组),正态近似。
    生产上用 statsmodels.stats.power 或现成计算器精确计算。"""
    p2 = p_baseline * (1 + mde)
    p_bar = (p_baseline + p2) / 2
    z_alpha = 1.96 if alpha == 0.05 else 2.58      # 双侧
    z_beta = {0.8: 0.84, 0.9: 1.28}[power]
    n = (z_alpha * math.sqrt(2 * p_bar * (1 - p_bar))
         + z_beta * math.sqrt(p_baseline * (1 - p_baseline) + p2 * (1 - p2))) ** 2
    return math.ceil(n / (p2 - p_baseline) ** 2)   # 必须除以 δ²,漏掉会低估约 2.9 万倍

if __name__ == "__main__":
    p0, mde, daily = 0.10, 0.05, 2000     # 基线 10%,相对提升 5%,日流量 2000/组
    n = sample_size(p0, mde)
    days = math.ceil(n / daily)
    print(f"每组需 {n} 样本, 约需 {days} 天")
    assert days > 0
