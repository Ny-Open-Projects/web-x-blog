# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130713079
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def uniquePathsWithObstacles(obstacleGrid):  # 定义函数 uniquePathsWithObstacles（参数：obstacleGrid）
    m = len(obstacleGrid)  # 把 长度(obstacleGrid) 存入 映射表
    n = len(obstacleGrid[0])  # 把 长度(obstacleGrid[0]) 存入 元素个数
    dp = [[0] * n for _ in range(m)]  # 把 [[0] 乘 元素个数 for _ in range(映射表)] 存入 DP 表
    for i in range(m):  # 让 下标 i 从 映射表 遍历
        if obstacleGrid[i][0] == 0:  # 若 obstacleGrid[下标 i][0] 等于 0
            dp[i][0] = 1  # 把 1 写入 dp[i][0]
        else:  # 否则
            break  # 跳出循环
    for j in range(n):  # 让 下标 j 从 元素个数 遍历
        if obstacleGrid[0][j] == 0:  # 若 obstacleGrid[0][下标 j] 等于 0
            dp[0][j] = 1  # 把 1 写入 dp[0][j]
        else:  # 否则
            break  # 跳出循环
    for i in range(1, m):  # 让 下标 i 从 1 到 映射表 遍历
        for j in range(1, n):  # 让 下标 j 从 1 到 元素个数 遍历
            if obstacleGrid[i][j] == 1:  # 若 obstacleGrid[下标 i][下标 j] 等于 1
                continue  # 跳过本轮，进入下一次
            dp[i][j] = (
                dp[i - 1][j] + dp[i][j - 1]
            )  # 把 DP 表[下标 i 减 1][下标 j] 加 DP 表[下标 i][下标 j 减 1] 写入 dp[i][j]
    return dp[m - 1][n - 1]  # 返回 DP 表[映射表 减 1][元素个数 减 1]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # 打印输出
