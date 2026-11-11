# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def two_sum_brute(nums, target):  # 定义函数 two_sum_brute（参数：数组, 目标值）
    # 暴力解法：时间复杂度 O(n^2)
    for i in range(len(nums)):  # 让 下标 i 从 长度(数组 遍历
        for j in range(i + 1, len(nums)):  # 让 下标 j 从 下标 i 加 1 到 长度(数组 遍历
            if nums[i] + nums[j] == target:  # 若 数组[下标 i] 加 数组[下标 j] 等于 目标值
                return [i, j]  # 返回 [下标 i, 下标 j]
    return []  # 返回 []


def two_sum_hash(nums, target):  # 定义函数 two_sum_hash（参数：数组, 目标值）
    # 哈希表解法：时间复杂度 O(n)
    seen = {}  # 把 {} 存入 已见集合
    for i, num in enumerate(nums):  # 同时取 下标 i 与 num 遍历
        if target - num in seen:  # 若 目标值 减 num in 已见集合
            return [seen[target - num], i]  # 返回 [已见集合[目标值 减 num], 下标 i]
        seen[num] = i  # 把 下标 i 写入 seen[num]
    return []  # 返回 []


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    nums = [2, 7, 11, 15]  # 把 [2, 7, 11, 15] 存入 数组
    target = 9  # 把 9 存入 目标值
    print(two_sum_brute(nums, target))  # [0, 1]
    print(two_sum_hash(nums, target))  # [0, 1]
