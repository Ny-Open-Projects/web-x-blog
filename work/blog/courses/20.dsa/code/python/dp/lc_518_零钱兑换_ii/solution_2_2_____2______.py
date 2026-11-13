# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144852221
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def change(amount, coins):  # 定义函数 change（参数：目标金额, 硬币面额）
    dp = [0] * (amount + 1)  # 把 [0] 乘 (目标金额 加 1) 存入 DP 表
    dp[0] = 1  # 把 1 写入 dp[0]
    for coin in coins:  # 逐个取出 硬币面额 的元素（coin）
        for c in range(coin, amount + 1):  # 让 字符 从 coin 到 目标金额 加 1 遍历
            dp[c] += dp[c - coin]  # dp[c]累加 DP 表[字符 减 coin]
    return dp[amount]  # 返回 DP 表[目标金额]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(change(5, [1, 2, 5]))  # 打印输出
