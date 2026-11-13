# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134032039
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def rotate(matrix):  # 定义函数 rotate（参数：矩阵）
    n = len(matrix)  # 把 长度(矩阵) 存入 元素个数
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        for j in range(i + 1, n):  # 让 下标 j 从 下标 i 加 1 到 元素个数 遍历
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        matrix[i].reverse()  # 反转


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 把 [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 存入 矩阵
    rotate(matrix)  # rotate(矩阵)
    print(matrix)  # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
