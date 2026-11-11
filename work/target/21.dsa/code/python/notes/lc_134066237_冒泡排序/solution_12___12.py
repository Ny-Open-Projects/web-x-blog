# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134066237
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def bubble_sort_v2(nums):  # 定义函数 bubble_sort_v2（参数：数组）
    """冒泡排序 - 交换优化版（对应 Go 版 V2 的 Python 翻译）。"""
    length = len(nums)  # 把 长度(数组) 存入 长度
    for i in range(length):  # 让 下标 i 从 长度 遍历
        for j in range(length - 1 - i):  # 让 下标 j 从 长度 减 1 减 下标 i 遍历
            if nums[j] > nums[j + 1]:  # 若 数组[下标 j] 超过 数组[下标 j 加 1]
                nums[j], nums[j + 1] = (
                    nums[j + 1],
                    nums[j],
                )  # 把 数组[下标 j 加 1], 数组[下标 j] 写入 nums[j], nums[j + 1]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    list_ = [5, 4, 3, 2, 1]  # 把 [5, 4, 3, 2, 1] 存入 list_
    bubble_sort_v2(list_)  # bubble_sort_v2(list_)
    print(list_)  # 输出: [1, 2, 3, 4, 5]
