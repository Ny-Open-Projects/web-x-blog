# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355653
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def isPowerOfThree(n):  # 定义函数 isPowerOfThree（参数：元素个数）
    return n > 0 and 1162261467 % n == 0  # 返回 元素个数 超过 0 and 1162261467 对…取模 元素个数 等于 0


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(isPowerOfThree(1))  # 打印输出
