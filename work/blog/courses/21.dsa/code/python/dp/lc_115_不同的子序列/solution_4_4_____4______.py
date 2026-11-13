# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144848405
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def numDistinct(s, t):  # 定义函数 numDistinct（参数：字符串, 另一字符串）
    # 动态规划（从前往后，二维）
    sLen = len(s)  # 把 长度(字符串) 存入 sLen
    tLen = len(t)  # 把 长度(另一字符串) 存入 tLen
    dp = [
        [0] * (tLen + 1) for _ in range(sLen + 1)
    ]  # 把 [[0] 乘 (tLen 加 1) for _ in range(sLen 加 1)] 存入 DP 表
    for i in range(sLen + 1):  # 让 下标 i 从 sLen 加 1 遍历
        dp[i][0] = 1  # 把 1 写入 dp[i][0]
    for i in range(1, sLen + 1):  # 让 下标 i 从 1 到 sLen 加 1 遍历
        for j in range(1, tLen + 1):  # 让 下标 j 从 1 到 tLen 加 1 遍历
            if s[i - 1] == t[j - 1]:  # 若 字符串[下标 i 减 1] 等于 另一字符串[下标 j 减 1]
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:  # 否则
                dp[i][j] = dp[i - 1][j]  # 把 DP 表[下标 i 减 1][下标 j] 写入 dp[i][j]
    return dp[sLen][tLen]  # 返回 DP 表[sLen][tLen]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(numDistinct("rabbbit", "rabbit"))  # 打印输出
