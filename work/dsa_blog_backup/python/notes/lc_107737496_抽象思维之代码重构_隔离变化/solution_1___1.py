# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def fill(matrix, num, begin, size):  # 定义函数 fill（参数：矩阵, num, begin, 大小）
    """将 num 开头的数，从 (begin, begin) 开始逆时针旋转填充 size*size 的子矩阵。"""
    if size == 0:  # 若 大小 等于 0
        return  # return
    if size == 1:  # 若 大小 等于 1
        matrix[begin][begin] = num  # 把 num 写入 matrix[begin][begin]
        return  # return
    # 左列向下
    for j in range(size - 1):  # 让 下标 j 从 大小 减 1 遍历
        matrix[begin + j][begin] = num  # 把 num 写入 matrix[begin + j][begin]
        num += 1  # num累加 1
    # 底行向右
    for j in range(size - 1):  # 让 下标 j 从 大小 减 1 遍历
        matrix[begin + size - 1][begin + j] = num  # 把 num 写入 matrix[begin + size - 1][begin + j]
        num += 1  # num累加 1
    # 右列向上
    for j in range(size - 1, 0, -1):  # 让 下标 j 从 大小 减 1 倒数回去（每步减 1）
        matrix[begin + j][begin + size - 1] = num  # 把 num 写入 matrix[begin + j][begin + size - 1]
        num += 1  # num累加 1
    # 顶行向左
    for j in range(size - 1, 0, -1):  # 让 下标 j 从 大小 减 1 倒数回去（每步减 1）
        matrix[begin][begin + j] = num  # 把 num 写入 matrix[begin][begin + j]
        num += 1  # num累加 1
    fill(matrix, num, begin + 1, size - 2)  # fill(矩阵, num, begin 加 1, 大小 减 2)


def generate_square_matrix(n):  # 定义函数 generate_square_matrix（参数：元素个数）
    m = [[0] * n for _ in range(n)]  # 把 [[0] 乘 元素个数 for _ in range(元素个数)] 存入 映射表
    fill(m, 1, 0, n)  # fill(映射表, 1, 0, 元素个数)
    return m  # 返回 映射表


def print_matrix(m):  # 定义函数 print_matrix（参数：映射表）
    for row in m:  # 逐个取出 映射表 的元素（row）
        print(" ".join(f"{x:2d}" for x in row))  # 打印输出


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print_matrix(generate_square_matrix(6))  # print_matrix(generate_square_matrix(6))
