# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355335
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def bitSquareSum(n):  # 定义函数 bitSquareSum（参数：元素个数）
    total = 0  # 把 0 存入 总和
    while n:  # 循环，直到不满足「元素个数」
        digit = n % 10  # 把 元素个数 对…取模 10 存入 digit
        total += digit * digit  # 总和累加 digit 乘 digit
        n //= 10  # 把 10 写入 n //
    return total  # 返回 总和


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(bitSquareSum(1))  # 打印输出
