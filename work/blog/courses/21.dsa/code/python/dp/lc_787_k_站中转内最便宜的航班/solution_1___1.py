# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130717572
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def findCheapestPrice(
    n, flights, src, dst, k
):  # 定义函数 findCheapestPrice（参数：元素个数, flights, src, dst, 下标 k）
    INF = float("inf")  # 把 float('inf') 存入 INF
    # dp[i][j]: 恰好经过 i 条边（i-1 次中转）到达城市 j 的最低价格
    dp = [[INF] * n for _ in range(k + 2)]  # 把 [[INF] 乘 元素个数 for _ in range(下标 k 加 2)] 存入 DP 表
    for i in range(k + 2):  # 让 下标 i 从 下标 k 加 2 遍历
        dp[i][src] = 0  # 把 0 写入 dp[i][src]
    for i in range(1, k + 2):  # 让 下标 i 从 1 到 下标 k 加 2 遍历
        for frm, to, price in flights:  # for frm, to, price in flights:
            if dp[i - 1][frm] != INF:  # 若 DP 表[下标 i 减 1][frm] 不等于 INF
                dp[i][to] = min(dp[i][to], dp[i - 1][frm] + price)
    ans = min(
        dp[i][dst] for i in range(1, k + 2)
    )  # 把 取较小值 DP 表[下标 i][dst] for 下标 i in range(1, 下标 k 加 2)) 存入 答案
    return ans if ans != INF else -1  # 返回 答案 if 答案 不等于 INF else 减 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(
        findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1)
    )  # 打印输出
