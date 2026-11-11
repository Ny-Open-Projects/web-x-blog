# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134191965
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def radix_sort(arr):  # 定义函数 radix_sort（参数：数组）
    # 基数排序（LSD，基于计数排序思想），支持负数，时间复杂度 O(kn)
    if len(arr) < 2:  # 若 长度(数组) 小于 2
        return arr  # 返回 数组
    max_val = max(arr)  # 把 取较大值 数组) 存入 max_val
    min_val = min(arr)  # 把 取较小值 数组) 存入 min_val
    # 若有负数，整体平移为非负
    offset = -min_val if min_val < 0 else 0  # 把 减 min_val if min_val 小于 0 else 0 存入 offset
    adjusted = [num + offset for num in arr]  # 把 [num 加 offset for num in 数组] 存入 adjusted
    max_adjusted = max(adjusted)  # 把 取较大值 adjusted) 存入 max_adjusted
    radix = 1  # 把 1 存入 radix
    tmp = [0] * len(arr)  # 把 [0] 乘 长度(数组) 存入 临时变量
    while max_adjusted >= radix:  # 循环，直到不满足「max_adjusted 不低于 radix」
        bucket = [0] * 10  # 把 [0] 乘 10 存入 bucket
        for num in adjusted:  # 逐个取出 adjusted 的元素（num）
            bucket[(num // radix) % 10] += 1  # 把 1 写入 bucket[(num // radix) % 10] +
        for i in range(1, 10):  # 让 下标 i 从 1 到 10 遍历
            bucket[i] += bucket[i - 1]  # bucket[i]累加 bucket[下标 i 减 1]
        for i in range(len(adjusted) - 1, -1, -1):  # 让 下标 i 从 长度(adjusted) 减 1 倒数回去（每步减 1）
            d = (adjusted[i] // radix) % 10  # 把 (adjusted[下标 i] 除以 除以 radix) 对…取模 10 存入 d
            tmp[bucket[d] - 1] = adjusted[i]  # 把 adjusted[下标 i] 写入 tmp[bucket[d] - 1]
            bucket[d] -= 1  # bucket[d]累减 1
        adjusted[:] = tmp[:]  # 把 复制 临时变量 写入 adjusted[:]
        radix *= 10  # 把 10 写入 radix *
    arr[:] = [num - offset for num in adjusted]  # 把 [num 减 offset for num in adjusted] 写入 arr[:]
    return arr  # 返回 数组


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    test_cases = [
        [100, 34, 1002, 1234, 66, 137, 49, 102, 9, 108, 102, 101, 104, 109, 102],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
        [],
        [1],
        [-2, 1, 0, -9, 1, 3, 9, 99, 9, -30, -100, 100, 88, 88, 20, 1, 0, 3, 4, 5, -20],
    ]
    for case in test_cases:  # 逐个取出 test_cases 的元素（case）
        print(radix_sort(case[:]))  # 打印输出
