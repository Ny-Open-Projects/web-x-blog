# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130450957
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
from collections import Counter  # from collections import Counter


def hasGroupsSizeX(deck):  # 定义函数 hasGroupsSizeX（参数：deck）
    if len(deck) < 2:  # 若 长度(deck) 小于 2
        return False  # 返回 False
    count = Counter(deck)  # 把 Counter(deck) 存入 计数
    n = len(deck)  # 把 长度(deck) 存入 元素个数
    for x in range(2, n + 1):  # 让 x 从 2 到 元素个数 加 1 遍历
        if n % x == 0 and all(
            v % x == 0 for v in count.values()
        ):  # 若 元素个数 对…取模 x 等于 0 and all(值 对…取模 x 等于 0 for 值 in 计数.values(
            return True  # 返回 True
    return False  # 返回 False


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(hasGroupsSizeX([1, 1, 2, 2, 2, 2]))  # 打印输出
