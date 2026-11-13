# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def bubble_sort(arr):  # 定义函数 bubble_sort（参数：数组）
    # 冒泡排序：最坏/平均时间复杂度 O(n^2)
    n = len(arr)  # 把 长度(数组) 存入 元素个数
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        for j in range(n - i - 1):  # 让 下标 j 从 元素个数 减 下标 i 减 1 遍历
            if arr[j] > arr[j + 1]:  # 若 数组[下标 j] 超过 数组[下标 j 加 1]
                arr[j], arr[j + 1] = (
                    arr[j + 1],
                    arr[j],
                )  # 把 数组[下标 j 加 1], 数组[下标 j] 写入 arr[j], arr[j + 1]
    return arr  # 返回 数组


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    arr = [3, 1, 4, 1, 5, 9, 2, 6]  # 把 [3, 1, 4, 1, 5, 9, 2, 6] 存入 数组
    print(bubble_sort(arr[:]))  # [1, 1, 2, 3, 4, 5, 6, 9]
