# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144851123
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def coinChange(coins, amount):  # 定义函数 coinChange（参数：硬币面额, 目标金额）
    max_n = amount + 1  # 把 目标金额 加 1 存入 max_n
    dp = [max_n] * (amount + 1)  # 把 [max_n] 乘 (目标金额 加 1) 存入 DP 表
    dp[0] = 0  # 把 0 写入 dp[0]
    for i in range(1, amount + 1):  # 让 下标 i 从 1 到 目标金额 加 1 遍历
        for c in coins:  # 逐个取出 硬币面额 的元素（字符）
            if i - c >= 0:  # 若 下标 i 减 字符 不低于 0
                dp[i] = min(
                    dp[i], dp[i - c] + 1
                )  # 把 取较小值 DP 表[下标 i], DP 表[下标 i 减 字符] 加 1) 写入 dp[i]
    return (
        dp[amount] if dp[amount] != max_n else -1
    )  # 返回 DP 表[目标金额] if DP 表[目标金额] 不等于 max_n else 减 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(coinChange([1, 2, 5], 11))  # 打印输出
