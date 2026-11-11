# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def findKthLargest(nums, k):  # 定义函数 findKthLargest（参数：数组, 下标 k）
    nums = nums[:]  # 把 复制 数组 存入 数组
    length = len(nums) - 1  # 把 长度(数组) 减 1 存入 长度
    for i in range(length, length - k, -1):  # 让 下标 i 从 长度 到 长度 减 下标 k 到 减 1 遍历
        for j in range(i):  # 让 下标 j 从 下标 i 遍历
            if nums[j] > nums[j + 1]:  # 若 数组[下标 j] 超过 数组[下标 j 加 1]
                nums[j], nums[j + 1] = (
                    nums[j + 1],
                    nums[j],
                )  # 把 数组[下标 j 加 1], 数组[下标 j] 写入 nums[j], nums[j + 1]
    return nums[length - k + 1]  # 返回 数组[长度 减 下标 k 加 1]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(findKthLargest([1, 2, 3], 1))  # 打印输出
