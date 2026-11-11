# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134191965
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def radix_sort(arr):  # 定义函数 radix_sort（参数：数组）
    if len(arr) < 2:  # 若 长度(数组) 小于 2
        return arr  # 返回 数组
    max_val = max(arr)  # 把 取较大值 数组) 存入 max_val
    min_val = min(arr)  # 把 取较小值 数组) 存入 min_val
    offset = -min_val if min_val < 0 else 0  # 把 减 min_val if min_val 小于 0 else 0 存入 offset
    adjusted_arr = [num + offset for num in arr]  # 把 [num 加 offset for num in 数组] 存入 adjusted_arr
    max_val_adjusted = max(adjusted_arr)  # 把 取较大值 adjusted_arr) 存入 max_val_adjusted
    radix = 1  # 把 1 存入 radix
    tmp = [0] * len(arr)  # 把 [0] 乘 长度(数组) 存入 临时变量
    while max_val_adjusted >= radix:  # 循环，直到不满足「max_val_adjusted 不低于 radix」
        bucket = [0] * 10  # 把 [0] 乘 10 存入 bucket
        for num in adjusted_arr:  # 逐个取出 adjusted_arr 的元素（num）
            current_radix_num = (
                num // radix
            ) % 10  # 把 (num 除以 除以 radix) 对…取模 10 存入 current_radix_num
            bucket[current_radix_num] += 1  # bucket[current_radix_num]累加 1
        for i in range(1, 10):  # 让 下标 i 从 1 到 10 遍历
            bucket[i] += bucket[i - 1]  # bucket[i]累加 bucket[下标 i 减 1]
        for i in range(
            len(adjusted_arr) - 1, -1, -1
        ):  # 让 下标 i 从 长度(adjusted_arr) 减 1 倒数回去（每步减 1）
            current_radix_num = (adjusted_arr[i] // radix) % 10
            current_index = (
                bucket[current_radix_num] - 1
            )  # 把 bucket[current_radix_num] 减 1 存入 current_index
            tmp[current_index] = adjusted_arr[i]  # 把 adjusted_arr[下标 i] 写入 tmp[current_index]
            bucket[current_radix_num] -= 1  # bucket[current_radix_num]累减 1
        adjusted_arr[:] = tmp[:]  # 把 复制 临时变量 写入 adjusted_arr[:]
        radix *= 10  # 把 10 写入 radix *
    arr[:] = [num - offset for num in adjusted_arr]  # 把 [num 减 offset for num in adjusted_arr] 写入 arr[:]
    return arr  # 返回 数组


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(radix_sort([1, 2, 3]))  # 打印输出
