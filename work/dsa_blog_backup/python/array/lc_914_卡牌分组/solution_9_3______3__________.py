# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130450957
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import math  # 引入依赖
from collections import Counter  # from collections import Counter


def hasGroupsSizeX(deck):  # 定义函数 hasGroupsSizeX（参数：deck）
    if len(deck) < 2:  # 若 长度(deck) 小于 2
        return False  # 返回 False
    g = 0  # 把 0 存入 g
    for c in Counter(deck).values():  # 逐个取出 Counter 的元素（字符）
        g = math.gcd(g, c)  # 把 math.gcd(g, 字符) 存入 g
    return g >= 2  # 返回 g 不低于 2


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))  # 打印输出
