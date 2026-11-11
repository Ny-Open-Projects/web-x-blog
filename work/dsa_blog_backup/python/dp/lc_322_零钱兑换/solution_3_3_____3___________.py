# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144851123
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def coinChange(coins, amount):  # 定义函数 coinChange（参数：硬币面额, 目标金额）
    if amount == 0:  # 若 目标金额 等于 0
        return 0  # 返回 0
    dp = [float("inf")] * (amount + 1)  # 把 [float('inf')] 乘 (目标金额 加 1) 存入 DP 表
    dp[0] = 0  # 把 0 写入 dp[0]
    for coin in coins:  # 逐个取出 硬币面额 的元素（coin）
        for j in range(coin, amount + 1):  # 让 下标 j 从 coin 到 目标金额 加 1 遍历
            dp[j] = min(
                dp[j], dp[j - coin] + 1
            )  # 把 取较小值 DP 表[下标 j], DP 表[下标 j 减 coin] 加 1) 写入 dp[j]
    return (
        dp[amount] if dp[amount] != float("inf") else -1
    )  # 返回 DP 表[目标金额] if DP 表[目标金额] 不等于 float('inf') else 减 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(coinChange([1, 2, 5], 11))  # 打印输出
