# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144848405
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def numDistinct(s, t):  # 定义函数 numDistinct（参数：字符串, 另一字符串）
    # 动态规划（从后往前）
    m = len(s)  # 把 长度(字符串) 存入 映射表
    n = len(t)  # 把 长度(另一字符串) 存入 元素个数
    dp = [
        [0] * (n + 1) for _ in range(m + 1)
    ]  # 把 [[0] 乘 (元素个数 加 1) for _ in range(映射表 加 1)] 存入 DP 表
    for i in range(m + 1):  # 让 下标 i 从 映射表 加 1 遍历
        dp[i][n] = 1  # 把 1 写入 dp[i][n]
    for i in range(m - 1, -1, -1):  # 让 下标 i 从 映射表 减 1 倒数回去（每步减 1）
        for j in range(n - 1, -1, -1):  # 让 下标 j 从 元素个数 减 1 倒数回去（每步减 1）
            if s[i] == t[j]:  # 若 字符串[下标 i] 等于 另一字符串[下标 j]
                dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
            else:  # 否则
                dp[i][j] = dp[i + 1][j]  # 把 DP 表[下标 i 加 1][下标 j] 写入 dp[i][j]
    return dp[0][0]  # 返回 DP 表[0][0]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(numDistinct("rabbbit", "rabbit"))  # 打印输出
