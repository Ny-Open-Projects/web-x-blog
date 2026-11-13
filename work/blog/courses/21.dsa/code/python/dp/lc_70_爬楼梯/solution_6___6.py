# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660487
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def climbStairs(n):  # 定义函数 climbStairs（参数：元素个数）
    # 快速倍增法求斐波那契（climbStairs(n) = fib(n+1)）
    def fib(k):  # 定义函数 fib（参数：下标 k）
        # 返回 (F(k), F(k+1))
        if k == 0:  # 若 下标 k 等于 0
            return (0, 1)  # 返回 (0, 1)
        a, b = fib(k >> 1)  # 把 fib(下标 k 超过 超过 1) 写入 a, b
        c = a * (2 * b - a)  # 把 数组 乘 (2 乘 b 减 数组) 存入 字符
        d = a * a + b * b  # 把 数组 乘 数组 加 b 乘 b 存入 d
        if k & 1:  # 若 下标 k 按位与 1
            return (d, c + d)  # 返回 (d, 字符 加 d)
        return (c, d)  # 返回 (字符, d)

    return fib(n + 1)[0]  # 返回 fib(元素个数 加 1)[0]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(climbStairs(5))  # 打印输出
