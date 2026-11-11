# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144849130
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def maxProfit(prices):  # 定义函数 maxProfit（参数：价格序列）
    dp = [[0, 0] for _ in range(len(prices))]  # 把 [[0, 0] for _ in range(长度(价格序列))] 存入 DP 表
    dp[0] = [-prices[0], 0]  # 把 [ 减 价格序列[0], 0] 写入 dp[0]
    for i in range(1, len(prices)):  # 让 下标 i 从 1 到 长度(价格序列 遍历
        dp[i] = [
            max(dp[i - 1][0], -prices[i]),
            max(dp[i - 1][1], prices[i] + dp[i - 1][0]),
        ]
    return dp[len(prices) - 1][1]  # 返回 DP 表[长度(价格序列) 减 1][1]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(maxProfit([1, 2, 3]))  # 打印输出
