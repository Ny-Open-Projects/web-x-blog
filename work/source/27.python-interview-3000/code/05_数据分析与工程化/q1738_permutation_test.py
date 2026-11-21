"""置换检验:把两组标签随机重排,看观测差值在随机世界里有多罕见"""

import random

A = [12.1, 11.8, 12.4, 12.0, 11.9, 12.3, 12.2, 11.7]   # 对照
B = [12.6, 12.3, 12.9, 12.5, 12.4, 12.8, 12.7, 12.2]   # 处理


def mean(xs):
    return sum(xs) / len(xs)


def perm_test(a, b, iters=10000, seed=42):
    rng = random.Random(seed)
    pooled = a + b
    n_a = len(a)
    obs = abs(mean(b) - mean(a))
    hits = 0
    for _ in range(iters):
        rng.shuffle(pooled)
        if abs(mean(pooled[n_a:]) - mean(pooled[:n_a])) >= obs:
            hits += 1
    return hits / iters, obs


if __name__ == "__main__":
    p, obs = perm_test(A, B)
    print(f"观测差值 {obs:.3f},置换检验 p 值 ≈ {p:.4f}")
    print("结论:", "两组差异显著" if p < 0.05 else "差异不显著,可能只是波动")
    print("要点:置换检验不假设正态,只要求两组可交换;小样本比 t 检验稳;迭代 1 万起步,固定种子保证可复现")
