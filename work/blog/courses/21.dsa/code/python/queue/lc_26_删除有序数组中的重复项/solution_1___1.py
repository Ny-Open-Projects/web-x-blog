# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114454
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def removeDuplicates(nums):  # 定义函数 removeDuplicates（参数：数组）
    # 双指针：慢指针 k 指向去重后下一个待填位置，快指针遍历
    if not nums:  # 若 not 数组
        return 0  # 返回 0
    k = 1  # 把 1 存入 下标 k
    for i in range(1, len(nums)):  # 让 下标 i 从 1 到 长度(数组 遍历
        if nums[i] != nums[i - 1]:  # 若 数组[下标 i] 不等于 数组[下标 i 减 1]
            nums[k] = nums[i]  # 把 数组[下标 i] 写入 nums[k]
            k += 1  # 下标 k累加 1
    return k  # 返回 下标 k


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    nums = [1, 1, 2]  # 把 [1, 1, 2] 存入 数组
    k = removeDuplicates(nums)  # 把 removeDuplicates(数组) 存入 下标 k
    print(k, nums[:k])  # 打印输出
