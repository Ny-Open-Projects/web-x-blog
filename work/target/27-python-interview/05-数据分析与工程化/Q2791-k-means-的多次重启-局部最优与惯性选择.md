---
title: [Q2791] k-means 的多次重启:局部最优与惯性选择
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2791 · k-means 的多次重启:局部最优与惯性选择

> 难度:★★★☆ | 标签:聚类, 随机重启

**问**:面试官:k-means 跑出来的结果每次都一样吗?怎么向业务保证这个聚类是"对的"?

**答**:不一样,k-means 只保证局部最优,起点不同终点可以天差地别。对三个互相分离的紧凑簇跑 8 个随机种子:最好的 seed SSE 0.600,正确还原 5-5-5 的划分;最差的 seed SSE 45.417,把两个簇并成一簇、把另一簇拆成两半,簇大小变成 2-3-10,相差 7470%。这说明单次运行带运气成分,工程实践是固定跑 5-10 次重启取最小 SSE,并用 k-means++ 压低坏起点概率;向业务汇报时把 SSE 一并给出,才能回答"这是全局最优还是又一次局部最优"。确定性要求高的场景固定种子,让结果可复现可回放。

```python
# file: code/05_数据分析与工程化/q2791_kmeans_restarts.py
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
```

**追问**:
- 追问 1:怎么判断 k 该不该加大?—— 画 SSE 随 k 的下降曲线找肘部,再叠加业务可解释性,两个条件都要满足。
- 追问 2:重启次数越多越好吗?—— 收益边际递减,5-10 次后最优 SSE 基本稳定,更多次数只浪费算力。
