---
title: "[A290] 状态压缩 DP 旅行商 Held-Karp：子集枚举、位运算技巧与排列暴力对拍"
date: 2026-11-25
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A290 · 状态压缩 DP 旅行商 Held-Karp：子集枚举、位运算技巧与排列暴力对拍

> 难度:★★★★ | 标签:状态压缩DP, 旅行商, 位运算, 子集枚举, 对拍

**问**（笔试·编程题）：n ≤ 9 的 TSP（从 0 出发、每点恰一次、回到 0、最小总距离），面试官要看的是**状态怎么压、为什么压得住**：① 状态 `f[mask][u]` 的定义与转移，为什么用「已访问集合 + 当前所在点」就够，不需要记录路径顺序；② 位运算三件套：判在位 `mask >> v & 1`、置位 `mask | 1 << v`、全集 `(1 << n) - 1`，以及子集枚举 `sub = (sub - 1) & mask` 的用法与 `3^n` 总代价；③ 边界：n = 1 返回 0、存在不可达边（INF）时返回无解、起点/终点必须闭合；④ 与 `itertools.permutations` 暴力在 30 组 n ≤ 8 随机图上对拍（含稀疏图/不可达），并断言 `n=9` 时状态数 512×9 的规模；⑤ 说清与 A014（全排列·回溯）、A251（拓扑排序·分层批次）的分工——本题只回答「**用集合压缩消除排列枚举、把 n! 降到 2^n·n²**」。

**答**：① 分工：A014 用回溯枚举全部排列，是 TSP 暴力解的原型；A251 处理 DAG 的依赖分层；本题的关键观察是「已经走过哪些点 + 现在在哪」完全决定了后续最优代价，**走过的先后顺序不再影响未来**——这就是最优子结构，也是能用 DP 替换 `n!` 排列的根本原因。② 状态与转移：`f[mask][u]` = 从 0 出发、恰好访问 `mask` 这些点、当前停在 `u` 的最小代价；转移向未访问的 `v`：`f[mask|1<<v][v] = min(..., f[mask][u] + d[u][v])`。初始化 `f[1][0] = 0`（只访问起点、停在 0），其余 INF；答案 `min over u≠0 of f[full][u] + d[u][0]`，**闭合回起点**这一步单独算，不能塞进转移里，否则会把「回到 0」误当成访问新点。③ 位运算：Python 的 `int` 是任意精度，`1 << 8` 无符号问题，`mask >> v & 1` 的括号优先级也安全（移位高于按位与）；枚举 `mask` 的子集用 `sub = (sub - 1) & mask`（从 `mask` 开始、到 0 结束），所有 mask 的子集总数是 `3^n`——本卡只把它作为位运算演示与计数断言，TSP 本体是 `2^n·n²`。④ 为什么是 `2^n·n²`：状态数 `2^n·n`，每个状态向 n 个点转移，n=9 时约 512×9×9 ≈ 4 万次，秒内完成；而 `9! = 362880` 条排列，n=12 时 4.8 亿就爆了，状态压缩的收益随 n 指数级拉大。⑤ 易错点：`mask` 必须从 1 开始且 `f[1][0]=0`，从 0 开始会让「空集停在 0」变成非法状态却代价 0；`d[u][v] == INF` 要跳过（否则 INF 加法污染 min，虽然 float inf 仍可比较，但会误把不可达当候选）；n=1 必须提前返回 0，否则 `full=1`、`range(1,1)` 为空、`min(empty)` 抛异常；无解时返回 INF 而不是 0（0 会被误认为「免费」）。

```python
# 全部标准库；Held-Karp 状压 DP（n<=9）vs itertools.permutations 暴力，含不可达边
import itertools
import random

INF = float("inf")


def tsp_dp(d):
    """目标实现：f[mask][u] 已访问 mask、停在 u 的最小代价，O(2^n * n^2)。"""
    n = len(d)
    if n <= 1:
        return 0
    full = (1 << n) - 1
    f = [[INF] * n for _ in range(1 << n)]
    f[1][0] = 0
    for mask in range(1 << n):
        for u in range(n):
            base = f[mask][u]
            if base == INF:
                continue
            for v in range(n):
                if (mask >> v) & 1:            # v 已访问
                    continue
                if d[u][v] == INF:             # 边不可达
                    continue
                nm = mask | (1 << v)
                nd = base + d[u][v]
                if nd < f[nm][v]:
                    f[nm][v] = nd
    best = INF
    for u in range(1, n):
        if f[full][u] != INF and d[u][0] != INF:
            best = min(best, f[full][u] + d[u][0])
    return best


def tsp_brute(d):
    """参考实现：枚举 1..n-1 的全排列，独立于 DP 的正确性来源。"""
    n = len(d)
    if n <= 1:
        return 0
    best = INF
    for p in itertools.permutations(range(1, n)):
        cur, cost, ok = 0, 0, True
        for v in p:
            if d[cur][v] == INF:
                ok = False
                break
            cost += d[cur][v]
            cur = v
        if ok and d[cur][0] != INF:
            best = min(best, cost + d[cur][0])
    return best


if __name__ == "__main__":
    rng = random.Random(2901)

    # 1) 30 组随机图（n=1..8，20% 概率不可达）与排列暴力对拍
    for _ in range(30):
        n = rng.randint(1, 8)
        d = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    d[i][j] = INF if rng.random() < 0.2 else rng.randint(1, 30)
        assert tsp_dp(d) == tsp_brute(d), (n, tsp_dp(d), tsp_brute(d))
    print("TSP 对拍: 30 组随机图（含不可达边）vs 全排列暴力，全等 ✅")

    # 2) 边界：单点、两点、全不可达、经典 4 点
    assert tsp_dp([[0]]) == 0 and tsp_brute([[0]]) == 0
    assert tsp_dp([[0, 7], [7, 0]]) == 14
    assert tsp_dp([[0, INF], [INF, 0]]) == INF          # 无解
    assert tsp_dp([[0, 1, 15, 6], [2, 0, 7, 3],
                   [9, 6, 0, 12], [10, 4, 8, 0]]) == 21
    assert tsp_dp([[0, 1, INF], [1, 0, 1], [INF, 1, 0]]) == INF   # 必须经过不可达点
    assert tsp_dp([[0, 1, 5], [1, 0, 2], [5, 2, 0]]) == 8         # 绕行闭合 1+2+5
    print("边界断言: 单点/两点/无解/经典4点/必须经过不可达点 全过 ✅")

    # 3) 位运算：子集枚举总数为 3^n，置位/判位自洽
    n = 9
    total = 0
    for mask in range(1 << n):
        sub = mask
        cnt = 0
        while True:
            cnt += 1
            if sub == 0:
                break
            sub = (sub - 1) & mask
        total += cnt
    assert total == 3 ** n
    m = 0
    for v in range(n):
        m |= 1 << v
        assert (m >> v) & 1 == 1
    assert m == (1 << n) - 1
    print("位运算: 子集枚举总数 3^9 = %d，置位/判位自洽 ✅" % total)

    # 4) 规模：n=9 完整图，状态 512*9，DP 远快于 8! 暴力
    n = 9
    d = [[0 if i == j else rng.randint(1, 100) for j in range(n)] for i in range(n)]
    assert tsp_dp(d) == tsp_brute(d)
    print("规模验证: n=9 状态 512x9，DP 与 8! 暴力同解 ✅")

    print("对拍通过：Held-Karp 30 组随机 + 5 条边界 + 3^9 计数全绿")
```

**追问**：1) 为什么状态里不用记「访问顺序」，只记集合？—— 因为代价只由「当前站在哪」和「还剩哪些点」决定（边权与历史无关），历史顺序对未来的唯一影响已被「当前点」吸收；这是马尔可夫性/最优子结构的直接体现。反例是带「访问次数上限」「时间窗」的变体（如 A266 的时间窗最短路），那时集合不够，必须把时间或次数压进状态，状态数会多一维。2) `f[mask][u]` 循环顺序为什么可以直接按 `mask` 升序？—— 转移只会让 `mask` 变大（`nm = mask | 1<<v > mask`），所以按整数升序处理时，所有能转移到 `mask` 的前驱都已算完；这是 DAG 上的拓扑序，不需要额外排序。若写成递归记忆化则天然按依赖求值，两者等价，但迭代版常数更小、无递归深度风险。3) 子集枚举 `sub = (sub - 1) & mask` 在 TSP 里用得上吗？—— 本题用不上，它属于「划分型」状压（如把集合分成若干组、每组代价已知，枚举子集做集合划分 DP，总代价 `3^n`）；但面试官常在同一场里连着问，所以要能当场写出模板并说清复杂度。区分口诀：**「走过/没走过」用单点转移 `2^n·n`；「这一组怎么分」用子集枚举 `3^n`**——别把两种模板混着背。
