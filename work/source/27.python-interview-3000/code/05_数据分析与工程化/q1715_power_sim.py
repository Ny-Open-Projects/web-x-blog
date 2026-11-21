"""AB 实验功效的模拟估算:蒙特卡洛数显著次数,反推最小样本量"""

import math
import random

P_CONTROL = 0.05
P_TREAT = 0.055   # 相对提升 10%
ALPHA = 0.05
SIMS = 800


def two_prop_z(x1, n1, x2, n2):
    p1, p2 = x1 / n1, x2 / n2
    p = (x1 + x2) / (n1 + n2)
    se = math.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    return (p2 - p1) / se if se else 0.0


def binom(rng, n, p):
    """几何间隔法采样二项分布:随机调用次数 O(成功数),比逐人掷币快百倍"""
    logq = math.log(1.0 - p)
    count, pos = 0, -1
    while True:
        u = 1.0 - rng.random()  # (0,1]
        pos += int(math.log(u) / logq) + 1
        if pos >= n:
            return count
        count += 1


def simulate_power(n, seed=42):
    rng = random.Random(seed)
    sig = 0
    for _ in range(SIMS):
        x1 = binom(rng, n, P_CONTROL)
        x2 = binom(rng, n, P_TREAT)
        if abs(two_prop_z(x1, n, x2, n)) > 1.96:
            sig += 1
    return sig / SIMS


if __name__ == "__main__":
    for n in (3000, 8000, 16000, 32000):
        power = simulate_power(n)
        flag = " 达标" if power >= 0.8 else ""
        print(f"每组 {n:>6} 样本,模拟功效 {power:.1%}{flag}")
    print("要点:功效=真实有效时判为显著的概率,0.8 起步;模拟法不依赖公式假设,配额分层、非常规口径时尤其好用")
