# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134379497
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def maximumGap(nums):  # 定义函数 maximumGap（参数：数组）
    if len(nums) < 2:  # 若 长度(数组) 小于 2
        return 0  # 返回 0

    def radix_sort(lst):  # 定义函数 radix_sort（参数：lst）
        max_val = max(lst)  # 把 取较大值 lst) 存入 max_val
        radix = 1  # 把 1 存入 radix
        while max_val >= radix:  # 循环，直到不满足「max_val 不低于 radix」
            bucket = [0] * 10  # 把 [0] 乘 10 存入 bucket
            for num in lst:  # 逐个取出 lst 的元素（num）
                bucket[(num // radix) % 10] += 1  # 把 1 写入 bucket[(num // radix) % 10] +
            for i in range(1, 10):  # 让 下标 i 从 1 到 10 遍历
                bucket[i] += bucket[i - 1]  # bucket[i]累加 bucket[下标 i 减 1]
            tmp = [0] * len(lst)  # 把 [0] 乘 长度(lst) 存入 临时变量
            for i in range(len(lst) - 1, -1, -1):  # 让 下标 i 从 长度(lst) 减 1 倒数回去（每步减 1）
                idx = (lst[i] // radix) % 10  # 把 (lst[下标 i] 除以 除以 radix) 对…取模 10 存入 idx
                tmp[bucket[idx] - 1] = lst[i]  # 把 lst[下标 i] 写入 tmp[bucket[idx] - 1]
                bucket[idx] -= 1  # bucket[idx]累减 1
            lst[:] = tmp[:]  # 把 复制 临时变量 写入 lst[:]
            radix *= 10  # 把 10 写入 radix *

    radix_sort(nums)  # radix_sort(数组)
    max_gap = 0  # 把 0 存入 max_gap
    for i in range(1, len(nums)):  # 让 下标 i 从 1 到 长度(数组 遍历
        max_gap = max(
            max_gap, nums[i] - nums[i - 1]
        )  # 把 取较大值 max_gap, 数组[下标 i] 减 数组[下标 i 减 1]) 存入 max_gap
    return max_gap  # 返回 max_gap


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(maximumGap([1, 2, 3]))  # 打印输出
