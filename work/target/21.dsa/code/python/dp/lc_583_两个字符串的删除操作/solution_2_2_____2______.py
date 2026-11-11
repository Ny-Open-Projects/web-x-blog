# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144853278
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def minDistance(word1, word2):  # 定义函数 minDistance（参数：word1, word2）
    m = len(word1)  # 把 长度(word1) 存入 映射表
    n = len(word2)  # 把 长度(word2) 存入 元素个数
    dp = [
        [0] * (n + 1) for _ in range(m + 1)
    ]  # 把 [[0] 乘 (元素个数 加 1) for _ in range(映射表 加 1)] 存入 DP 表
    for i in range(1, m + 1):  # 让 下标 i 从 1 到 映射表 加 1 遍历
        dp[i][0] = i  # 把 下标 i 写入 dp[i][0]
    for j in range(1, n + 1):  # 让 下标 j 从 1 到 元素个数 加 1 遍历
        dp[0][j] = j  # 把 下标 j 写入 dp[0][j]
    for i in range(1, m + 1):  # 让 下标 i 从 1 到 映射表 加 1 遍历
        c1 = word1[i - 1]  # 把 word1[下标 i 减 1] 存入 c1
        for j in range(1, n + 1):  # 让 下标 j 从 1 到 元素个数 加 1 遍历
            c2 = word2[j - 1]  # 把 word2[下标 j 减 1] 存入 c2
            if c1 == c2:  # 若 c1 等于 c2
                dp[i][j] = dp[i - 1][j - 1]  # 把 DP 表[下标 i 减 1][下标 j 减 1] 写入 dp[i][j]
            else:  # 否则
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
    return dp[m][n]  # 返回 DP 表[映射表][元素个数]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(minDistance("sea", "eat"))  # 打印输出
