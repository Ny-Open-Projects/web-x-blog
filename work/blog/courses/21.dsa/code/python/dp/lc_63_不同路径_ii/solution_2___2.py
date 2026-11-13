# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130713079
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def uniquePathsWithObstacles(obstacleGrid):  # 定义函数 uniquePathsWithObstacles（参数：obstacleGrid）
    m = len(obstacleGrid)  # 把 长度(obstacleGrid) 存入 映射表
    n = len(obstacleGrid[0])  # 把 长度(obstacleGrid[0]) 存入 元素个数
    f = [0] * n  # 把 [0] 乘 元素个数 存入 f
    f[0] = 1 if obstacleGrid[0][0] == 0 else 0  # 把 1 if obstacleGrid[0][0] 等于 0 else 0 写入 f[0]
    for j in range(1, n):  # 让 下标 j 从 1 到 元素个数 遍历
        f[j] = 0 if (obstacleGrid[0][j] == 1 or f[j - 1] == 0) else f[j - 1]
    for i in range(1, m):  # 让 下标 i 从 1 到 映射表 遍历
        for j in range(n):  # 让 下标 j 从 元素个数 遍历
            if obstacleGrid[i][j] == 1:  # 若 obstacleGrid[下标 i][下标 j] 等于 1
                f[j] = 0  # 把 0 写入 f[j]
            elif j > 0:  # 否则，若 下标 j 超过 0
                f[j] += f[j - 1]  # f[j]累加 f[下标 j 减 1]
    return f[n - 1]  # 返回 f[元素个数 减 1]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # 打印输出
