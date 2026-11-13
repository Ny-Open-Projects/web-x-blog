# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113877588
# LMP - 最长曼哈顿路径 (只能向右/向下, 求路径上权重之和最大)
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def longest_manhattan_path(grid):  # 定义函数 longest_manhattan_path（参数：网格）
    if not grid or not grid[0]:  # 若 not 网格 or not 网格[0]
        return 0  # 返回 0
    m = len(grid)  # 把 长度(网格) 存入 映射表
    n = len(grid[0])  # 把 长度(网格[0]) 存入 元素个数
    dp = [[0] * n for _ in range(m)]  # 把 [[0] 乘 元素个数 for _ in range(映射表)] 存入 DP 表
    dp[0][0] = grid[0][0]  # 把 网格[0][0] 写入 dp[0][0]
    for i in range(m):  # 让 下标 i 从 映射表 遍历
        for j in range(n):  # 让 下标 j 从 元素个数 遍历
            if i == 0 and j == 0:  # 若 下标 i 等于 0 and 下标 j 等于 0
                continue  # 跳过本轮，进入下一次
            up = dp[i - 1][j] if i > 0 else float("-inf")
            left = dp[i][j - 1] if j > 0 else float("-inf")
            dp[i][j] = grid[i][j] + max(
                up, left
            )  # 把 网格[下标 i][下标 j] 加 取较大值 up, 左边界) 写入 dp[i][j]
    return dp[m - 1][n - 1]  # 返回 DP 表[映射表 减 1][元素个数 减 1]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    grid = [
        [5, 1, 3],
        [2, 4, 2],
        [3, 2, 1],
    ]
    print(longest_manhattan_path(grid))  # 14
