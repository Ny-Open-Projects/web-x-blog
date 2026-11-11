# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355568
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def canWinNim(n):  # 定义函数 canWinNim（参数：元素个数）
    return n % 4 != 0  # 返回 元素个数 对…取模 4 不等于 0


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(canWinNim(1))  # 打印输出
