# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144829935
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def longestMonotonicSubarray(nums):  # 定义函数 longestMonotonicSubarray（参数：数组）
    if not nums:  # 若 not 数组
        return 0  # 返回 0
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    ans = 1  # 把 1 存入 答案
    i = 0  # 把 0 存入 下标 i
    while i < n:  # 循环，直到不满足「下标 i 小于 元素个数」
        j = i  # 把 下标 i 存入 下标 j
        while (
            j + 1 < n and nums[j + 1] > nums[j]
        ):  # 循环，直到不满足「下标 j 加 1 小于 元素个数 and 数组[下标 j 加 1] 超过 数组[下标 j]」
            j += 1  # 下标 j累加 1
        ans = max(ans, j - i + 1)  # 把 取较大值 答案, 下标 j 减 下标 i 加 1) 存入 答案
        j = i  # 把 下标 i 存入 下标 j
        while (
            j + 1 < n and nums[j + 1] < nums[j]
        ):  # 循环，直到不满足「下标 j 加 1 小于 元素个数 and 数组[下标 j 加 1] 小于 数组[下标 j]」
            j += 1  # 下标 j累加 1
        ans = max(ans, j - i + 1)  # 把 取较大值 答案, 下标 j 减 下标 i 加 1) 存入 答案
        i += 1  # 下标 i累加 1
    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(longestMonotonicSubarray([1, 4, 3, 3, 2]))  # 打印输出
