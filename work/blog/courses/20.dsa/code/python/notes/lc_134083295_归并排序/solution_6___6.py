# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134083295
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def merge_sort(nums):  # 定义函数 merge_sort（参数：数组）
    def ms_fn(arr, left, right):  # 定义函数 ms_fn（参数：数组, 左边界, 右边界）
        if left >= right:  # 若 左边界 不低于 右边界
            return  # return
        mid = (left + right) // 2  # 把 (左边界 加 右边界) 除以 除以 2 存入 中点
        ms_fn(arr, left, mid)  # ms_fn(数组, 左边界, 中点)
        ms_fn(arr, mid + 1, right)  # ms_fn(数组, 中点 加 1, 右边界)
        merge(arr, left, mid, right)  # merge(数组, 左边界, 中点, 右边界)

    def merge(arr, left, mid, right):  # 定义函数 merge（参数：数组, 左边界, 中点, 右边界）
        temp = [0] * (right - left + 1)  # 把 [0] 乘 (右边界 减 左边界 加 1) 存入 临时变量
        i, j, k = left, mid + 1, 0  # 把 左边界, 中点 加 1, 0 写入 i, j, k
        while i <= mid and j <= right:  # 循环，直到不满足「下标 i 不超过 中点 and 下标 j 不超过 右边界」
            if arr[i] <= arr[j]:  # 若 数组[下标 i] 不超过 数组[下标 j]
                temp[k] = arr[i]  # 把 数组[下标 i] 写入 temp[k]
                i += 1  # 下标 i累加 1
            else:  # 否则
                temp[k] = arr[j]  # 把 数组[下标 j] 写入 temp[k]
                j += 1  # 下标 j累加 1
            k += 1  # 下标 k累加 1
        while i <= mid:  # 循环，直到不满足「下标 i 不超过 中点」
            temp[k] = arr[i]  # 把 数组[下标 i] 写入 temp[k]
            i += 1  # 下标 i累加 1
            k += 1  # 下标 k累加 1
        while j <= right:  # 循环，直到不满足「下标 j 不超过 右边界」
            temp[k] = arr[j]  # 把 数组[下标 j] 写入 temp[k]
            j += 1  # 下标 j累加 1
            k += 1  # 下标 k累加 1
        for idx in range(len(temp)):  # 让 idx 从 长度(临时变量 遍历
            arr[left + idx] = temp[idx]  # 把 临时变量[idx] 写入 arr[left + idx]

    ms_fn(nums, 0, len(nums) - 1)  # ms_fn(数组, 0, 长度(数组) 减 1)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    list_ = [5, 4, 3, 2, 1]  # 把 [5, 4, 3, 2, 1] 存入 list_
    merge_sort(list_)  # merge_sort(list_)
    print(list_)  # 输出: [1, 2, 3, 4, 5]
