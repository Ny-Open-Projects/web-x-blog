# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
# 数组中的第 K 个最大元素 - 方案: 计数排序 (按值域)


import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def find_kth_largest(nums, k):  # 定义函数 find_kth_largest（参数：数组, 下标 k）
    lo = min(nums)  # 把 取较小值 数组) 存入 左边界
    hi = max(nums)  # 把 取较大值 数组) 存入 右边界
    count = [0] * (hi - lo + 1)  # 把 [0] 乘 (右边界 减 左边界 加 1) 存入 计数
    for x in nums:  # 逐个取出 数组 的元素（x）
        count[x - lo] += 1  # 把 1 写入 count[x - lo] +
    remaining = k  # 把 下标 k 存入 remaining
    for v in range(hi, lo - 1, -1):  # 让 值 从 右边界 到 左边界 减 1 到 减 1 遍历
        remaining -= count[v - lo]  # remaining累减 计数[值 减 左边界]
        if remaining <= 0:  # 若 remaining 不超过 0
            return v  # 返回 值
    return lo  # 返回 左边界


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # 5
