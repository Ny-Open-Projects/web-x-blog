"""k-means 的多次重启: 局部最优与最优惯性选择"""
import random

# 三个互相分离的紧凑簇, 坏起点会把两簇并一簇并拆另一簇
POINTS = [(0.0, 0.0), (0.3, 0.1), (0.1, 0.3), (0.2, 0.2), (0.0, 0.4),
          (4.0, 0.0), (4.3, 0.2), (3.8, 0.1), (4.1, 0.4), (4.0, 0.3),
          (2.0, 4.0), (2.2, 4.2), (1.8, 3.9), (2.1, 3.8), (1.9, 4.1)]


def d2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def forgy_init(points, k, rng):
    """Forgy 随机初始化: 直接抽 k 个点"""
    return [tuple(p) for p in rng.sample(points, k)]


def assign(points, centers):
    return [min(range(len(centers)), key=lambda j: d2(p, centers[j])) for p in points]


def lloyd(points, k, centers, max_iter=100):
    labels = assign(points, centers)
    for it in range(1, max_iter + 1):
        for j in range(k):
            members = [p for p, l in zip(points, labels) if l == j]
            if members:
                centers[j] = (sum(p[0] for p in members) / len(members),
                              sum(p[1] for p in members) / len(members))
            else:
                far = max(range(len(points)), key=lambda i: d2(points[i], centers[labels[i]]))
                centers[j] = tuple(points[far])
                labels[far] = j
        new_labels = assign(points, centers)
        if new_labels == labels:
            break
        labels = new_labels
    sse = sum(d2(p, centers[l]) for p, l in zip(points, labels))
    return sse, labels


if __name__ == "__main__":
    k = 3
    results = []
    for seed in range(1, 9):
        rng = random.Random(seed)
        sse, labels = lloyd(POINTS, k, forgy_init(POINTS, k, rng))
        results.append((seed, sse, labels))
    results.sort(key=lambda x: x[1])
    best_seed, best_sse, best_labels = results[0]
    worst_seed, worst_sse, _ = results[-1]
    for seed, sse, _ in results[:3]:
        print(f"  seed={seed}  SSE={sse:.3f}")
    print(f"最优 seed={best_seed} SSE={best_sse:.3f}, 最差 seed={worst_seed} SSE={worst_sse:.3f}, 相差 {(worst_sse / best_sse - 1):.0%}")
    sizes = sorted(sum(1 for l in best_labels if l == j) for j in range(k))
    worst_sizes = sorted(sum(1 for l in results[-1][2] if l == j) for j in range(k))
    print(f"最优划分簇大小 {sizes}, 最差划分簇大小 {worst_sizes}")
    assert best_sse < worst_sse, "应存在被随机起点锁死的局部最优"
    assert sizes == [5, 5, 5], "最优划分应还原三个紧凑簇"
    assert worst_sizes != sizes, "坏划分应表现为合并两簇并拆散另一簇"
    print("要点: k-means 只保证局部最优, 工程实践固定跑 5-10 次重启取最小 SSE, 起点用 k-means++ 更稳")
