# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def partition(arr, left, right):  # 定义函数 partition（参数：数组, 左边界, 右边界）
    pivot = arr[right]  # 把 数组[右边界] 存入 pivot
    i = left  # 把 左边界 存入 下标 i
    for j in range(left, right):  # 让 下标 j 从 左边界 到 右边界 遍历
        if arr[j] < pivot:  # 若 数组[下标 j] 小于 pivot
            arr[i], arr[j] = arr[j], arr[i]  # 把 数组[下标 j], 数组[下标 i] 写入 arr[i], arr[j]
            i += 1  # 下标 i累加 1
    arr[i], arr[right] = arr[right], arr[i]  # 把 数组[右边界], 数组[下标 i] 写入 arr[i], arr[right]
    return i  # 返回 下标 i


def quick_sort(
    arr, left=0, right=None
):  # 定义函数 quick_sort（参数：数组, 左边界 赋值为 0, 右边界 赋值为 None）
    # 快速排序：平均时间复杂度 O(n log n)
    if right is None:  # 若 右边界 is None
        right = len(arr) - 1  # 把 长度(数组) 减 1 存入 右边界
    if left < right:  # 若 左边界 小于 右边界
        pivot_index = partition(arr, left, right)  # 把 partition(数组, 左边界, 右边界) 存入 pivot_index
        quick_sort(arr, left, pivot_index - 1)  # quick_sort(数组, 左边界, pivot_index 减 1)
        quick_sort(arr, pivot_index + 1, right)  # quick_sort(数组, pivot_index 加 1, 右边界)
    return arr  # 返回 数组


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    arr = [3, 1, 4, 1, 5, 9, 2, 6]  # 把 [3, 1, 4, 1, 5, 9, 2, 6] 存入 数组
    print(quick_sort(arr[:]))  # [1, 1, 2, 3, 4, 5, 6, 9]
