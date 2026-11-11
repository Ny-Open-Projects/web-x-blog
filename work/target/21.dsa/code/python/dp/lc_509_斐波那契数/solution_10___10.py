# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660242
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def fib(n):  # 定义函数 fib（参数：元素个数）
    def mat_mul(a, b):  # 定义函数 mat_mul（参数：数组, b）
        return [
            [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]],
        ]

    def mat_pow(mat, p):  # 定义函数 mat_pow（参数：mat, 节点）
        res = [[1, 0], [0, 1]]  # 把 [[1, 0], [0, 1]] 存入 结果
        while p:  # 循环，直到不满足「节点」
            if p & 1:  # 若 节点 按位与 1
                res = mat_mul(res, mat)  # 把 mat_mul(结果, mat) 存入 结果
            mat = mat_mul(mat, mat)  # 把 mat_mul(mat, mat) 存入 mat
            p >>= 1  # 把 1 写入 p >>
        return res  # 返回 结果

    if n == 0:  # 若 元素个数 等于 0
        return 0  # 返回 0
    if n == 1:  # 若 元素个数 等于 1
        return 1  # 返回 1
    m = mat_pow([[1, 1], [1, 0]], n - 1)  # 把 mat_pow([[1, 1], [1, 0]], 元素个数 减 1) 存入 映射表
    return m[0][0]  # 返回 映射表[0][0]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(fib(10))  # 打印输出
