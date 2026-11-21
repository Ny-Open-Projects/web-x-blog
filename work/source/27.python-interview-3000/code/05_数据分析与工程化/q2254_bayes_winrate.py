"""转化率的贝叶斯比较: 后验采样与赢率"""

import random

random.seed(11)


def compare(k_a, n_a, k_b, n_b, size=20000):
    sa = [random.betavariate(k_a + 1, n_a - k_a + 1) for _ in range(size)]
    sb = [random.betavariate(k_b + 1, n_b - k_b + 1) for _ in range(size)]
    wins = sum(1 for x, y in zip(sa, sb) if y > x)
    loss = sum(max(x - y, 0) for x, y in zip(sa, sb)) / size
    sa.sort()
    lo, hi = sa[int(0.025 * size)], sa[int(0.975 * size)]
    return wins / size, loss, lo, hi


if __name__ == "__main__":
    print("== 大样本组 ==")
    p, loss, lo, hi = compare(45, 1000, 60, 1000)
    print(f"A 后验区间 [{lo:.2%}, {hi:.2%}], B 赢率 {p:.1%}, 选 B 的期望损失 {loss:.3%}")
    print("== 小样本组 ==")
    p2, loss2, lo2, hi2 = compare(4, 40, 6, 40)
    print(f"A 后验区间 [{lo2:.2%}, {hi2:.2%}], B 赢率 {p2:.1%}, 期望损失 {loss2:.3%}")
    print("要点: 赢率和期望损失比 p 值可读; 小样本赢率七成也敢说'倾向B但继续积累'; 先验来源必须写进报告")
