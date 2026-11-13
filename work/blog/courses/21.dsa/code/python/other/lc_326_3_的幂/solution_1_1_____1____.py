# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355653
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def isPowerOfThree(n):  # 定义函数 isPowerOfThree（参数：元素个数）
    while n != 0 and n % 3 == 0:  # 循环，直到不满足「元素个数 不等于 0 and 元素个数 对…取模 3 等于 0」
        n = int(n / 3)  # 把 int(元素个数 除以 3) 存入 元素个数
    return n == 1  # 返回 元素个数 等于 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(isPowerOfThree(1))  # 打印输出
