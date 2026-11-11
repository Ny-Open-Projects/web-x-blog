# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class Matrix:  # 定义类
    """面向对象版：矩阵类，封装填充与打印（方案 3）。"""

    def __init__(self, size):  # 构造函数：初始化成员
        self.N = size  # 把 大小 写入 self.N
        self.M = [[0] * size for _ in range(size)]  # 把 [[0] 乘 大小 for _ in range(大小)] 写入 self.M

    def fill(self, num, begin, size):  # 定义函数 fill（参数：self, num, begin, 大小）
        if size == 0:  # 若 大小 等于 0
            return  # return
        if size == 1:  # 若 大小 等于 1
            self.M[begin][begin] = num  # 把 num 写入 self.M[begin][begin]
            return  # return
        for j in range(size - 1):  # 让 下标 j 从 大小 减 1 遍历
            self.M[begin + j][begin] = num  # 把 num 写入 self.M[begin + j][begin]
            num += 1  # num累加 1
        for j in range(size - 1):  # 让 下标 j 从 大小 减 1 遍历
            self.M[begin + size - 1][begin + j] = num  # 把 num 写入 self.M[begin + size - 1][begin + j]
            num += 1  # num累加 1
        for j in range(size - 1, 0, -1):  # 让 下标 j 从 大小 减 1 倒数回去（每步减 1）
            self.M[begin + j][begin + size - 1] = num  # 把 num 写入 self.M[begin + j][begin + size - 1]
            num += 1  # num累加 1
        for j in range(size - 1, 0, -1):  # 让 下标 j 从 大小 减 1 倒数回去（每步减 1）
            self.M[begin][begin + j] = num  # 把 num 写入 self.M[begin][begin + j]
            num += 1  # num累加 1
        self.fill(num, begin + 1, size - 2)  # self.fill(num, begin 加 1, 大小 减 2)

    def show(self):  # 定义函数 show（参数：self）
        for row in self.M:  # 逐个取出 self 的元素（row）
            print(" ".join(f"{x:2d}" for x in row))  # 打印输出

    def clear(self):  # 定义函数 clear（参数：self）
        self.M = [
            [0] * self.N for _ in range(self.N)
        ]  # 把 [[0] 乘 self.N for _ in range(self.N)] 写入 self.M


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    size = 6  # 把 6 存入 大小
    obj = Matrix(size)  # 把 Matrix(大小) 存入 obj
    obj.fill(1, 0, size)  # obj.fill(1, 0, 大小)
    obj.show()  # obj.show()
    obj.clear()  # obj.clear()
