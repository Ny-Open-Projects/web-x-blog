# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def insertion_sort(arr):  # 定义函数 insertion_sort（参数：数组）
    # 插入排序：最坏时间复杂度 O(n^2)，最好 O(n)
    for i in range(1, len(arr)):  # 让 下标 i 从 1 到 长度(数组 遍历
        key = arr[i]  # 把 数组[下标 i] 存入 key
        j = i - 1  # 把 下标 i 减 1 存入 下标 j
        while j >= 0 and arr[j] > key:  # 循环，直到不满足「下标 j 不低于 0 and 数组[下标 j] 超过 key」
            arr[j + 1] = arr[j]  # 把 数组[下标 j] 写入 arr[j + 1]
            j -= 1  # 下标 j累减 1
        arr[j + 1] = key  # 把 key 写入 arr[j + 1]
    return arr  # 返回 数组


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    arr = [3, 1, 4, 1, 5, 9, 2, 6]  # 把 [3, 1, 4, 1, 5, 9, 2, 6] 存入 数组
    print(insertion_sort(arr[:]))  # [1, 1, 2, 3, 4, 5, 6, 9]
