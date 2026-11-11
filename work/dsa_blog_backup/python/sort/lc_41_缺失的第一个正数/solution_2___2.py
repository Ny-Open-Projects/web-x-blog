# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134429994
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def firstMissingPositive(nums):  # 定义函数 firstMissingPositive（参数：数组）
    if not nums:  # 若 not 数组
        return 1  # 返回 1
    nums = [item for item in nums if item > 0]  # 把 [item for item in 数组 if item 超过 0] 存入 数组
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    if not n:  # 若 not 元素个数
        return 1  # 返回 1
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        min_val = nums[i]  # 把 数组[下标 i] 存入 min_val
        for j in range(i + 1, n):  # 让 下标 j 从 下标 i 加 1 到 元素个数 遍历
            if nums[j] < min_val:  # 若 数组[下标 j] 小于 min_val
                min_val, nums[j] = nums[j], min_val  # 把 数组[下标 j], min_val 写入 min_val, nums[j]
        nums[i] = min_val  # 把 min_val 写入 nums[i]
        if i == 0 and min_val != 1:  # 若 下标 i 等于 0 and min_val 不等于 1
            return 1  # 返回 1
        if (
            i > 0 and nums[i] - nums[i - 1] > 1
        ):  # 若 下标 i 超过 0 and 数组[下标 i] 减 数组[下标 i 减 1] 超过 1
            return nums[i - 1] + 1  # 返回 数组[下标 i 减 1] 加 1
    return nums[n - 1] + 1  # 返回 数组[元素个数 减 1] 加 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(firstMissingPositive([1, 2, 3]))  # 打印输出
