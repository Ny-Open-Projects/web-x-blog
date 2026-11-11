# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130670245
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def rob(nums):  # 定义函数 rob（参数：数组）
    prev = 0  # 把 0 存入 前一个
    cur = 0  # 把 0 存入 当前值
    for x in nums:  # 逐个取出 数组 的元素（x）
        prev, cur = cur, max(cur, prev + x)  # 把 当前值, 取较大值 当前值, 前一个 加 x) 写入 prev, cur
    return cur  # 返回 当前值


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(rob([2, 7, 9, 3, 1]))  # 打印输出
