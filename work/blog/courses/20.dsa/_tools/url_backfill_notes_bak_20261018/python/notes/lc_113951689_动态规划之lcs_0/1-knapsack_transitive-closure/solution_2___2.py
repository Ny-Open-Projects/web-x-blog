def knapsack(weights, values, capacity):
    """0/1 背包动态规划：返回最大价值与所选物品下标。"""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        w, v = weights[i - 1], values[i - 1]
        for c in range(capacity + 1):
            dp[i][c] = dp[i - 1][c]
            if c >= w:
                dp[i][c] = max(dp[i][c], dp[i - 1][c - w] + v)
    # 回溯所选物品
    c = capacity
    chosen = []
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i - 1][c]:
            chosen.append(i - 1)
            c -= weights[i - 1]
    chosen.reverse()
    return dp[n][capacity], chosen


if __name__ == '__main__':
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7
    max_value, chosen = knapsack(weights, values, capacity)
    print("最大价值:", max_value, "所选物品:", chosen)  # 9 [1, 3]
