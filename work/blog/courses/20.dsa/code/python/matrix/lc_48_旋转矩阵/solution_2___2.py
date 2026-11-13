# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134032039
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def rotate(matrix):  # 定义函数 rotate（参数：矩阵）
    n = len(matrix)  # 把 长度(矩阵) 存入 元素个数
    for i in range(n // 2):  # 让 下标 i 从 元素个数 除以 除以 2 遍历
        for j in range(n):  # 让 下标 j 从 元素个数 遍历
            matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        for j in range(i):  # 让 下标 j 从 下标 i 遍历
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 把 [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 存入 矩阵
    rotate(matrix)  # rotate(矩阵)
    print(matrix)  # 打印输出
