# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
class Matrix:  # 定义类
    """矩阵类：用 __call__ 支持多下标访问 m(r, c)，并支持打印（方案 6）。"""

    def __init__(self, r, c):  # 构造函数：初始化成员
        self.row = r  # 把 右指针 写入 self.row
        self.col = c  # 把 字符 写入 self.col
        self.buf = [[0] * c for _ in range(r)]  # 把 [[0] 乘 字符 for _ in range(右指针)] 写入 self.buf

    def __call__(self, r, c):  # 定义函数 __call__（参数：self, 右指针, 字符）
        return self.buf[r][c]  # 返回 self.buf[右指针][字符]

    def __str__(self):  # 定义函数 __str__（参数：self）
        return "\n".join(" ".join(f"{x:2d}" for x in row) for row in self.buf)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    m = Matrix(4, 5)  # 把 Matrix(4, 5) 存入 映射表
    for i in range(4):  # 让 下标 i 从 4 遍历
        for j in range(5):  # 让 下标 j 从 5 遍历
            m.buf[i][j] = i * j  # 把 下标 i 乘 下标 j 写入 m.buf[i][j]
    print("Matrix 4X5:")  # 打印输出
    print(m)  # 打印输出
    print("m(2, 3) =", m(2, 3))  # 打印输出
