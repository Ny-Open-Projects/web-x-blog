# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134191965
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def radixSort(nums):  # 定义函数 radixSort（参数：数组）
    if not nums:  # 若 not 数组
        return nums  # 返回 数组
    max_num = max(nums)  # 把 取较大值 数组) 存入 max_num
    exp = 1  # 把 1 存入 exp
    while max_num // exp > 0:  # 循环，直到不满足「max_num 除以 除以 exp 超过 0」
        counting_sort_by_digit(nums, exp)  # counting_sort_by_digit(数组, exp)
        exp *= 10  # 把 10 写入 exp *
    return nums  # 返回 数组


def counting_sort_by_digit(nums, exp):  # 定义函数 counting_sort_by_digit（参数：数组, exp）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    output = [0] * n  # 把 [0] 乘 元素个数 存入 输出
    count = [0] * 10  # 把 [0] 乘 10 存入 计数
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        index = nums[i] // exp  # 把 数组[下标 i] 除以 除以 exp 存入 index
        count[index % 10] += 1  # 把 1 写入 count[index % 10] +
    for i in range(1, 10):  # 让 下标 i 从 1 到 10 遍历
        count[i] += count[i - 1]  # count[i]累加 计数[下标 i 减 1]
    for i in range(n - 1, -1, -1):  # 让 下标 i 从 元素个数 减 1 倒数回去（每步减 1）
        index = nums[i] // exp  # 把 数组[下标 i] 除以 除以 exp 存入 index
        output[count[index % 10] - 1] = nums[i]  # 把 数组[下标 i] 写入 output[count[index % 10] - 1]
        count[index % 10] -= 1  # 把 1 写入 count[index % 10] -
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        nums[i] = output[i]  # 把 输出[下标 i] 写入 nums[i]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(radixSort([1, 2, 3]))  # 打印输出
