# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def spiral_fill(n):  # 定义函数 spiral_fill（参数：元素个数）
    """逆时针旋转填充 n*n 数字方阵：从 (0,0) 开始按 左列向下 -> 底行向右 -> 右列向上 -> 顶行向左 螺旋填充 1..n^2。"""
    m = [[0] * n for _ in range(n)]  # 把 [[0] 乘 元素个数 for _ in range(元素个数)] 存入 映射表

    def fill(num, begin, size):  # 定义函数 fill（参数：num, begin, 大小）
        if size == 0:  # 若 大小 等于 0
            return  # return
        if size == 1:  # 若 大小 等于 1
            m[begin][begin] = num  # 把 num 写入 m[begin][begin]
            return  # return
        for j in range(size - 1):  # 让 下标 j 从 大小 减 1 遍历
            m[begin + j][begin] = num
            num += 1  # 把 num; num 累加 1 写入 m[begin + j][begin]
        for j in range(size - 1):  # 让 下标 j 从 大小 减 1 遍历
            m[begin + size - 1][begin + j] = num
            num += 1  # 把 num; num 累加 1 写入 m[begin + size - 1][begin + j]
        for j in range(size - 1, 0, -1):  # 让 下标 j 从 大小 减 1 倒数回去（每步减 1）
            m[begin + j][begin + size - 1] = num
            num += 1  # 把 num; num 累加 1 写入 m[begin + j][begin + size - 1]
        for j in range(size - 1, 0, -1):  # 让 下标 j 从 大小 减 1 倒数回去（每步减 1）
            m[begin][begin + j] = num
            num += 1  # 把 num; num 累加 1 写入 m[begin][begin + j]
        fill(num, begin + 1, size - 2)  # fill(num, begin 加 1, 大小 减 2)

    fill(1, 0, n)  # fill(1, 0, 元素个数)
    return m  # 返回 映射表


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    for row in spiral_fill(6):  # 逐个取出 spiral_fill 的元素（row）
        print(" ".join("%2d" % v for v in row))  # 打印输出
