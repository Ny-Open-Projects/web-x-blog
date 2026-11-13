# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import heapq  # 引入依赖


def findKthLargest(nums, k):  # 定义函数 findKthLargest（参数：数组, 下标 k）
    return heapq.nlargest(k, nums)[-1]  # 返回 heapq.nlargest(下标 k, 数组)[ 减 1]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(findKthLargest([1, 2, 3], 1))  # 打印输出
