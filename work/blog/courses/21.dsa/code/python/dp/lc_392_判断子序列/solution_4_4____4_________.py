# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144852792
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def isSubsequence(s, t):  # 定义函数 isSubsequence（参数：字符串, 另一字符串）
    # 动态规划优化版
    m = len(s)  # 把 长度(字符串) 存入 映射表
    n = len(t)  # 把 长度(另一字符串) 存入 元素个数
    dp = [
        [0] * (n + 1) for _ in range(m + 1)
    ]  # 把 [[0] 乘 (元素个数 加 1) for _ in range(映射表 加 1)] 存入 DP 表
    for i in range(1, m + 1):  # 让 下标 i 从 1 到 映射表 加 1 遍历
        for j in range(1, n + 1):  # 让 下标 j 从 1 到 元素个数 加 1 遍历
            if s[i - 1] == t[j - 1]:  # 若 字符串[下标 i 减 1] 等于 另一字符串[下标 j 减 1]
                dp[i][j] = dp[i - 1][j - 1] + 1  # 把 DP 表[下标 i 减 1][下标 j 减 1] 加 1 写入 dp[i][j]
            else:  # 否则
                dp[i][j] = dp[i][j - 1]  # 把 DP 表[下标 i][下标 j 减 1] 写入 dp[i][j]
    return dp[m][n] == m  # 返回 DP 表[映射表][元素个数] 等于 映射表


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(isSubsequence("abc", "ahbgdc"))  # 打印输出
