# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def matrix_multiply(a, b):  # 定义函数 matrix_multiply（参数：数组, b）
    # 朴素矩阵乘法：时间复杂度 O(n^3)
    n = len(a)  # 把 长度(数组) 存入 元素个数
    c = [[0] * n for _ in range(n)]  # 把 [[0] 乘 元素个数 for _ in range(元素个数)] 存入 字符
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        for j in range(n):  # 让 下标 j 从 元素个数 遍历
            for k in range(n):  # 让 下标 k 从 元素个数 遍历
                c[i][j] += a[i][k] * b[k][j]  # c[i][j]累加 数组[下标 i][下标 k] 乘 b[下标 k][下标 j]
    return c  # 返回 字符


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    a = [[1, 2], [3, 4]]  # 把 [[1, 2], [3, 4]] 存入 数组
    b = [[5, 6], [7, 8]]  # 把 [[5, 6], [7, 8]] 存入 b
    print(matrix_multiply(a, b))  # [[19, 22], [43, 50]]
