# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def selection_sort(arr):  # 定义函数 selection_sort（参数：数组）
    # 选择排序：时间复杂度 O(n^2)
    n = len(arr)  # 把 长度(数组) 存入 元素个数
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        min_idx = i  # 把 下标 i 存入 min_idx
        for j in range(i + 1, n):  # 让 下标 j 从 下标 i 加 1 到 元素个数 遍历
            if arr[j] < arr[min_idx]:  # 若 数组[下标 j] 小于 数组[min_idx]
                min_idx = j  # 把 下标 j 存入 min_idx
        arr[i], arr[min_idx] = (
            arr[min_idx],
            arr[i],
        )  # 把 数组[min_idx], 数组[下标 i] 写入 arr[i], arr[min_idx]
    return arr  # 返回 数组


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    arr = [3, 1, 4, 1, 5, 9, 2, 6]  # 把 [3, 1, 4, 1, 5, 9, 2, 6] 存入 数组
    print(selection_sort(arr[:]))  # [1, 1, 2, 3, 4, 5, 6, 9]
