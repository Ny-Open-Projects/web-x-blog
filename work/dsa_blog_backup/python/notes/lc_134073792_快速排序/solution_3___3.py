# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134073792
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def swap(array, i, j):  # 定义函数 swap（参数：array, 下标 i, 下标 j）
    array[i], array[j] = array[j], array[i]  # 把 array[下标 j], array[下标 i] 写入 array[i], array[j]


def partition(array, low, high):  # 定义函数 partition（参数：array, low, high）
    # 三数取中法选择基准点
    mid = (low + high) // 2  # 把 (low 加 high) 除以 除以 2 存入 中点
    if array[low] > array[high]:  # 若 array[low] 超过 array[high]
        swap(array, low, high)  # 交换 array 与 low, high
    if array[mid] > array[high]:  # 若 array[中点] 超过 array[high]
        swap(array, mid, high)  # 交换 array 与 中点, high
    if array[mid] > array[low]:  # 若 array[中点] 超过 array[low]
        swap(array, mid, low)  # 交换 array 与 中点, low
    pivot = array[low]  # 把 array[low] 存入 pivot
    i = low + 1  # 把 low 加 1 存入 下标 i
    for j in range(i, high + 1):  # 让 下标 j 从 下标 i 到 high 加 1 遍历
        if array[j] <= pivot:  # 若 array[下标 j] 不超过 pivot
            swap(array, i, j)  # 交换 array 与 下标 i, 下标 j
            i += 1  # 下标 i累加 1
    swap(array, low, i - 1)  # 交换 array 与 low, 下标 i 减 1
    return i - 1  # 返回 下标 i 减 1


def quick_sort(array, low, high):  # 定义函数 quick_sort（参数：array, low, high）
    if low < high:  # 若 low 小于 high
        pi = partition(array, low, high)  # 把 partition(array, low, high) 存入 pi
        quick_sort(array, low, pi - 1)  # quick_sort(array, low, pi 减 1)
        quick_sort(array, pi + 1, high)  # quick_sort(array, pi 加 1, high)


def quick_sort_wrapper(array):  # 定义函数 quick_sort_wrapper（参数：array）
    quick_sort(array, 0, len(array) - 1)  # quick_sort(array, 0, 长度(array) 减 1)
    return array  # 返回 array


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    unsorted_array = [
        9,
        -20,
        99,
        3,
        6,
        8,
        10,
        1,
        2,
        1,
    ]  # 把 [9, 减 20, 99, 3, 6, 8, 10, 1, 2, 1] 存入 unsorted_array
    sorted_array = quick_sort_wrapper(
        unsorted_array
    )  # 把 quick_sort_wrapper(unsorted_array) 存入 sorted_array
    print("Sorted array is:", sorted_array)  # 打印输出
