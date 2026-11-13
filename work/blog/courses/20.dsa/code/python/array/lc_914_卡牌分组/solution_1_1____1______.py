# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130450957
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def hasGroupsSizeX(deck):  # 定义函数 hasGroupsSizeX（参数：deck）
    from collections import Counter  # from collections import Counter

    count = Counter(deck)  # 把 Counter(deck) 存入 计数
    N = len(deck)  # 把 长度(deck) 存入 N
    for X in range(2, N + 1):  # 让 X 从 2 到 N 加 1 遍历
        if N % X == 0:  # 若 N 对…取模 X 等于 0
            if all(v % X == 0 for v in count.values()):  # 若 all(值 对…取模 X 等于 0 for 值 in 计数.values(
                return True  # 返回 True
    return False  # 返回 False


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3]))  # 打印输出
    print(hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))  # 打印输出
