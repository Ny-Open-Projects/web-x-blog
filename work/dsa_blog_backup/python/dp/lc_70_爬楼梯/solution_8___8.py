# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660487
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def climbStairs(n):  # 定义函数 climbStairs（参数：元素个数）
    # 闭式公式（Binet）—— n 较小时精确
    import math  # 引入依赖

    sqrt5 = math.sqrt(5)  # 把 math.sqrt(5) 存入 sqrt5
    phi = (1 + sqrt5) / 2  # 把 (1 加 sqrt5) 除以 2 存入 phi
    psi = (1 - sqrt5) / 2  # 把 (1 减 sqrt5) 除以 2 存入 psi
    return round(
        (phi ** (n + 1) - psi ** (n + 1)) / sqrt5
    )  # 返回 round((phi 乘 乘 (元素个数 加 1) 减 psi 乘 乘 (元素个数 加 1)) 除以 sqrt5)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(climbStairs(5))  # 打印输出
