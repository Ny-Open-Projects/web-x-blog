# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144847773
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def uniquePaths(m, n):  # 定义函数 uniquePaths（参数：映射表, 元素个数）
    # 动态规划
    f = [[0] * n for _ in range(m)]  # 把 [[0] 乘 元素个数 for _ in range(映射表)] 存入 f
    for i in range(m):  # 让 下标 i 从 映射表 遍历
        f[i][0] = 1  # 把 1 写入 f[i][0]
    for j in range(n):  # 让 下标 j 从 元素个数 遍历
        f[0][j] = 1  # 把 1 写入 f[0][j]
    for i in range(1, m):  # 让 下标 i 从 1 到 映射表 遍历
        for j in range(1, n):  # 让 下标 j 从 1 到 元素个数 遍历
            f[i][j] = (
                f[i - 1][j] + f[i][j - 1]
            )  # 把 f[下标 i 减 1][下标 j] 加 f[下标 i][下标 j 减 1] 写入 f[i][j]
    return f[m - 1][n - 1]  # 返回 f[映射表 减 1][元素个数 减 1]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(uniquePaths(3, 7))  # 打印输出
