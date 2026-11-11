# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660487
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def climbStairs(n):  # 定义函数 climbStairs（参数：元素个数）
    # 矩阵快速幂
    def multiply(a, b):  # 定义函数 multiply（参数：数组, b）
        return [
            [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]],
        ]

    def power(mat, p):  # 定义函数 power（参数：mat, 节点）
        res = [[1, 0], [0, 1]]  # 把 [[1, 0], [0, 1]] 存入 结果
        while p:  # 循环，直到不满足「节点」
            if p & 1:  # 若 节点 按位与 1
                res = multiply(res, mat)  # 把 multiply(结果, mat) 存入 结果
            mat = multiply(mat, mat)  # 把 multiply(mat, mat) 存入 mat
            p >>= 1  # 把 1 写入 p >>
        return res  # 返回 结果

    if n <= 1:  # 若 元素个数 不超过 1
        return 1  # 返回 1
    mat = [[1, 1], [1, 0]]  # 把 [[1, 1], [1, 0]] 存入 mat
    return power(mat, n)[0][0]  # 返回 power(mat, 元素个数)[0][0]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(climbStairs(5))  # 打印输出
