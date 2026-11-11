# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def heap_sort(arr):  # 定义函数 heap_sort（参数：数组）
    # 堆排序：时间复杂度 O(n log n)，原地排序
    n = len(arr)  # 把 长度(数组) 存入 元素个数

    def heapify(size, root):  # 定义函数 heapify（参数：大小, 根节点）
        largest = root  # 把 根节点 存入 largest
        left = 2 * root + 1  # 把 2 乘 根节点 加 1 存入 左边界
        right = 2 * root + 2  # 把 2 乘 根节点 加 2 存入 右边界
        if (
            left < size and arr[left] > arr[largest]
        ):  # 若 左边界 小于 大小 and 数组[左边界] 超过 数组[largest]
            largest = left  # 把 左边界 存入 largest
        if (
            right < size and arr[right] > arr[largest]
        ):  # 若 右边界 小于 大小 and 数组[右边界] 超过 数组[largest]
            largest = right  # 把 右边界 存入 largest
        if largest != root:  # 若 largest 不等于 根节点
            arr[root], arr[largest] = (
                arr[largest],
                arr[root],
            )  # 把 数组[largest], 数组[根节点] 写入 arr[root], arr[largest]
            heapify(size, largest)  # heapify(大小, largest)

    for i in range(n // 2 - 1, -1, -1):  # 让 下标 i 从 元素个数 除以 除以 2 减 1 倒数回去（每步减 1）
        heapify(n, i)  # heapify(元素个数, 下标 i)
    for i in range(n - 1, 0, -1):  # 让 下标 i 从 元素个数 减 1 倒数回去（每步减 1）
        arr[0], arr[i] = arr[i], arr[0]  # 把 数组[下标 i], 数组[0] 写入 arr[0], arr[i]
        heapify(i, 0)  # heapify(下标 i, 0)
    return arr  # 返回 数组


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    arr = [3, 1, 4, 1, 5, 9, 2, 6]  # 把 [3, 1, 4, 1, 5, 9, 2, 6] 存入 数组
    print(heap_sort(arr[:]))  # [1, 1, 2, 3, 4, 5, 6, 9]
