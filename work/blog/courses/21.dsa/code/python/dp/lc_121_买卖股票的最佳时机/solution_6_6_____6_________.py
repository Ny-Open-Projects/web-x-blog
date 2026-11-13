# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144849130
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def maxProfit(prices):  # 定义函数 maxProfit（参数：价格序列）
    if len(prices) == 0:
        return 0  # 若 长度(价格序列) 等于 0: return 0
    maxProfit = 0  # 把 0 存入 maxProfit
    dp = [0] * len(prices)  # 把 [0] 乘 长度(价格序列) 存入 DP 表
    dp[0] = prices[0]  # 把 价格序列[0] 写入 dp[0]
    for i in range(1, len(prices)):  # 让 下标 i 从 1 到 长度(价格序列 遍历
        dp[i] = min(dp[i - 1], prices[i])  # 把 取较小值 DP 表[下标 i 减 1], 价格序列[下标 i]) 写入 dp[i]
        maxProfit = max(
            prices[i] - dp[i], maxProfit
        )  # 把 取较大值 价格序列[下标 i] 减 DP 表[下标 i], maxProfit) 存入 maxProfit
    return maxProfit  # 返回 maxProfit


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(maxProfit([1, 2, 3]))  # 打印输出
