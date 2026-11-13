# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144853675
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def minCostClimbingStairs(cost):  # 定义函数 minCostClimbingStairs（参数：cost）
    n = len(cost)  # 把 长度(cost) 存入 元素个数
    dp = [0] * n  # 把 [0] 乘 元素个数 存入 DP 表
    dp[0] = cost[0]  # 把 cost[0] 写入 dp[0]
    dp[1] = cost[1]  # 把 cost[1] 写入 dp[1]
    for i in range(2, n):  # 让 下标 i 从 2 到 元素个数 遍历
        dp[i] = (
            min(dp[i - 1], dp[i - 2]) + cost[i]
        )  # 把 取较小值 DP 表[下标 i 减 1], DP 表[下标 i 减 2]) 加 cost[下标 i] 写入 dp[i]
    return min(dp[n - 1], dp[n - 2])  # 返回 取较小值 DP 表[元素个数 减 1], DP 表[元素个数 减 2])


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(minCostClimbingStairs([10, 15, 20]))  # 打印输出
