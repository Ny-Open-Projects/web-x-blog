# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134066237
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def bubble_sort_v4(nums):  # 定义函数 bubble_sort_v4（参数：数组）
    """冒泡排序 - 跳跃版（对应 Go 版 V4 的 Python 翻译）。"""
    length = len(nums)  # 把 长度(数组) 存入 长度
    k = length - 1  # 把 长度 减 1 存入 下标 k
    last = 0  # 把 0 存入 last
    i = 0  # 把 0 存入 下标 i
    while i < length - 1:  # 循环，直到不满足「下标 i 小于 长度 减 1」
        for j in range(k):  # 让 下标 j 从 下标 k 遍历
            if nums[j] > nums[j + 1]:  # 若 数组[下标 j] 超过 数组[下标 j 加 1]
                nums[j], nums[j + 1] = (
                    nums[j + 1],
                    nums[j],
                )  # 把 数组[下标 j 加 1], 数组[下标 j] 写入 nums[j], nums[j + 1]
                last = j  # 把 下标 j 存入 last
        k = last  # 把 last 存入 下标 k
        i += 1  # 下标 i累加 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    list_ = [5, 4, 3, 2, 1]  # 把 [5, 4, 3, 2, 1] 存入 list_
    bubble_sort_v4(list_)  # bubble_sort_v4(list_)
    print(list_)  # 输出: [1, 2, 3, 4, 5]
