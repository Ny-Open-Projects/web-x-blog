# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144829625
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def longestCommonSubsequence(text1, text2):  # 定义函数 longestCommonSubsequence（参数：text1, text2）
    m = len(text1)  # 把 长度(text1) 存入 映射表
    n = len(text2)  # 把 长度(text2) 存入 元素个数
    dp = [
        [0] * (n + 1) for _ in range(m + 1)
    ]  # 把 [[0] 乘 (元素个数 加 1) for _ in range(映射表 加 1)] 存入 DP 表
    for i in range(1, m + 1):  # 让 下标 i 从 1 到 映射表 加 1 遍历
        c1 = text1[i - 1]  # 把 text1[下标 i 减 1] 存入 c1
        for j in range(1, n + 1):  # 让 下标 j 从 1 到 元素个数 加 1 遍历
            c2 = text2[j - 1]  # 把 text2[下标 j 减 1] 存入 c2
            if c1 == c2:  # 若 c1 等于 c2
                dp[i][j] = dp[i - 1][j - 1] + 1  # 把 DP 表[下标 i 减 1][下标 j 减 1] 加 1 写入 dp[i][j]
            else:  # 否则
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]  # 返回 DP 表[映射表][元素个数]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(longestCommonSubsequence("abcde", "ace"))  # 打印输出
