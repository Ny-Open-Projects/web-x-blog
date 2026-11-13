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
        temp = []  # 把 [] 存入 临时变量
        i, j = left, mid + 1  # 把 左边界, 中点 加 1 写入 i, j
        while i <= mid and j <= right:  # 循环，直到不满足「下标 i 不超过 中点 and 下标 j 不超过 右边界」
            if arr[i] <= arr[j]:  # 若 数组[下标 i] 不超过 数组[下标 j]
                temp.append(arr[i])  # 把 数组[下标 i] 追加到列表尾部
                i += 1  # 下标 i累加 1
            else:  # 否则
                temp.append(arr[j])  # 把 数组[下标 j] 追加到列表尾部
                j += 1  # 下标 j累加 1
        temp.extend(arr[i : mid + 1])  # 临时变量.extend(数组[下标 i:中点 加 1])
        temp.extend(arr[j : right + 1])  # 临时变量.extend(数组[下标 j:右边界 加 1])
        for k in range(len(temp)):  # 让 下标 k 从 长度(临时变量 遍历
            arr[left + k] = temp[k]  # 把 临时变量[下标 k] 写入 arr[left + k]

    ms_fn(nums, 0, len(nums) - 1)  # ms_fn(数组, 0, 长度(数组) 减 1)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(merge_sort([1, 2, 3]))  # 打印输出
