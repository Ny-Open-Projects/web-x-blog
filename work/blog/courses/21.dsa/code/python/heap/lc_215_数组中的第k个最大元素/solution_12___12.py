# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
# 数组中的第 K 个最大元素 - 方案: 排序后取第 k 个


import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def find_kth_largest(nums, k):  # 定义函数 find_kth_largest（参数：数组, 下标 k）
    return sorted(nums)[len(nums) - k]  # 返回 sorted(数组)[长度(数组) 减 下标 k]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # 5
