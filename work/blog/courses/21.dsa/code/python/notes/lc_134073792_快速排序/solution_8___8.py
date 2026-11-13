# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134073792
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def partition(arr, left, right):  # 定义函数 partition（参数：数组, 左边界, 右边界）
    pivot = arr[left]  # 把 数组[左边界] 存入 pivot
    i = left + 1  # 把 左边界 加 1 存入 下标 i
    j = right  # 把 右边界 存入 下标 j
    while i <= j:  # 循环，直到不满足「下标 i 不超过 下标 j」
        while (
            i <= j and arr[j] >= pivot
        ):  # 循环，直到不满足「下标 i 不超过 下标 j and 数组[下标 j] 不低于 pivot」
            j -= 1  # 下标 j累减 1
        while (
            i <= j and arr[i] <= pivot
        ):  # 循环，直到不满足「下标 i 不超过 下标 j and 数组[下标 i] 不超过 pivot」
            i += 1  # 下标 i累加 1
        if i <= j:  # 若 下标 i 不超过 下标 j
            arr[i], arr[j] = arr[j], arr[i]  # 把 数组[下标 j], 数组[下标 i] 写入 arr[i], arr[j]
    arr[left], arr[j] = arr[j], arr[left]  # 把 数组[下标 j], 数组[左边界] 写入 arr[left], arr[j]
    return j  # 返回 下标 j


def quick_sort_fn(arr, left, right):  # 定义函数 quick_sort_fn（参数：数组, 左边界, 右边界）
    if left < right:  # 若 左边界 小于 右边界
        pivot_index = partition(arr, left, right)  # 把 partition(数组, 左边界, 右边界) 存入 pivot_index
        quick_sort_fn(arr, left, pivot_index - 1)  # quick_sort_fn(数组, 左边界, pivot_index 减 1)
        quick_sort_fn(arr, pivot_index + 1, right)  # quick_sort_fn(数组, pivot_index 加 1, 右边界)


def quick_sort_v2(arr):  # 定义函数 quick_sort_v2（参数：数组）
    quick_sort_fn(arr, 0, len(arr) - 1)  # quick_sort_fn(数组, 0, 长度(数组) 减 1)
    return arr  # 返回 数组


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    arr = [-2, 1, 0, -9, 1, 3, 9, 99, 9, -30, -100, 100, 88, 88, 20, 1, 0, 3, 4, 5, -20]
    quick_sort_v2(arr)  # quick_sort_v2(数组)
    print(arr)  # 打印输出
