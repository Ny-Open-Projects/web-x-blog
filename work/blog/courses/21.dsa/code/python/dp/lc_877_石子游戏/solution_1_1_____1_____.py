# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355902
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def stoneGame(piles):  # 定义函数 stoneGame（参数：piles）
    n = len(piles)  # 把 长度(piles) 存入 元素个数
    dp = [[0] * n for _ in range(n)]  # 把 [[0] 乘 元素个数 for _ in range(元素个数)] 存入 DP 表
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        dp[i][i] = piles[i]  # 把 piles[下标 i] 写入 dp[i][i]
    for length in range(2, n + 1):  # 让 长度 从 2 到 元素个数 加 1 遍历
        for i in range(n - length + 1):  # 让 下标 i 从 元素个数 减 长度 加 1 遍历
            j = i + length - 1  # 把 下标 i 加 长度 减 1 存入 下标 j
            dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
    return dp[0][n - 1] > 0  # 返回 DP 表[0][元素个数 减 1] 超过 0


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(stoneGame([5, 3, 4, 5]))  # 打印输出
