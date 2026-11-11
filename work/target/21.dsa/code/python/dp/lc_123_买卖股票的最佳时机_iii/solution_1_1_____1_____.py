# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144849793
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def maxProfit(prices):  # 定义函数 maxProfit（参数：价格序列）
    n = len(prices)  # 把 长度(价格序列) 存入 元素个数
    dp = [0, 0, 0, 0, 0]  # 把 [0, 0, 0, 0, 0] 存入 DP 表
    dp[1] = -prices[0]  # 把 减 价格序列[0] 写入 dp[1]
    dp[3] = -prices[0]  # 把 减 价格序列[0] 写入 dp[3]
    for i in range(1, n):  # 让 下标 i 从 1 到 元素个数 遍历
        dp[1] = max(
            dp[1], dp[0] - prices[i]
        )  # 把 取较大值 DP 表[1], DP 表[0] 减 价格序列[下标 i]) 写入 dp[1]
        dp[2] = max(
            dp[2], dp[1] + prices[i]
        )  # 把 取较大值 DP 表[2], DP 表[1] 加 价格序列[下标 i]) 写入 dp[2]
        dp[3] = max(
            dp[3], dp[2] - prices[i]
        )  # 把 取较大值 DP 表[3], DP 表[2] 减 价格序列[下标 i]) 写入 dp[3]
        dp[4] = max(
            dp[4], dp[3] + prices[i]
        )  # 把 取较大值 DP 表[4], DP 表[3] 加 价格序列[下标 i]) 写入 dp[4]
    return dp[4]  # 返回 DP 表[4]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(maxProfit([1, 2, 3]))  # 打印输出
