# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/99759428
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def two_sum(nums, target):  # 定义函数 two_sum（参数：数组, 目标值）
    mp = {}  # 把 {} 存入 mp
    for i, num in enumerate(nums):  # 同时取 下标 i 与 num 遍历
        complement = target - num  # 把 目标值 减 num 存入 complement
        if complement in mp:  # 若 complement in mp
            return [mp[complement], i]  # 返回 [mp[complement], 下标 i]
        mp[num] = i  # 把 下标 i 写入 mp[num]
    return []  # 返回 []


def max_sub_array(nums):  # 定义函数 max_sub_array（参数：数组）
    max_sum = nums[0]  # 把 数组[0] 存入 max_sum
    current_sum = nums[0]  # 把 数组[0] 存入 current_sum
    for i in range(1, len(nums)):  # 让 下标 i 从 1 到 长度(数组 遍历
        current_sum = max(
            nums[i], current_sum + nums[i]
        )  # 把 取较大值 数组[下标 i], current_sum 加 数组[下标 i]) 存入 current_sum
        max_sum = max(max_sum, current_sum)  # 把 取较大值 max_sum, current_sum) 存入 max_sum
    return max_sum  # 返回 max_sum


def rotate_array(nums, k):  # 定义函数 rotate_array（参数：数组, 下标 k）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    if n == 0:  # 若 元素个数 等于 0
        return  # return
    k %= n  # 把 元素个数 写入 k %

    def reverse(arr, left, right):  # 定义函数 reverse（参数：数组, 左边界, 右边界）
        while left < right:  # 循环，直到不满足「左边界 小于 右边界」
            arr[left], arr[right] = (
                arr[right],
                arr[left],
            )  # 把 数组[右边界], 数组[左边界] 写入 arr[left], arr[right]
            left += 1  # 左边界累加 1
            right -= 1  # 右边界累减 1

    reverse(nums, 0, n - 1)  # reverse(数组, 0, 元素个数 减 1)
    reverse(nums, 0, k - 1)  # reverse(数组, 0, 下标 k 减 1)
    reverse(nums, k, n - 1)  # reverse(数组, 下标 k, 元素个数 减 1)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(two_sum([2, 7, 11, 15], 9))  # 打印输出
    print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 打印输出
    arr = [1, 2, 3, 4, 5]  # 把 [1, 2, 3, 4, 5] 存入 数组
    rotate_array(arr, 2)  # rotate_array(数组, 2)
    print(arr)  # 打印输出
