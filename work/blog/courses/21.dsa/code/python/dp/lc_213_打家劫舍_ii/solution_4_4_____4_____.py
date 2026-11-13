# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144850170
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def rob(nums):  # 定义函数 rob（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    if n == 0:  # 若 元素个数 等于 0
        return 0  # 返回 0
    if n == 1:  # 若 元素个数 等于 1
        return nums[0]  # 返回 数组[0]

    def helper(arr):  # 定义函数 helper（参数：数组）
        f0 = 0  # 把 0 存入 f0
        f1 = 0  # 把 0 存入 f1
        for x in arr:  # 逐个取出 数组 的元素（x）
            f0, f1 = f1, max(f1, f0 + x)  # 把 f1, 取较大值 f1, f0 加 x) 写入 f0, f1
        return f1  # 返回 f1

    return max(
        nums[0] + helper(nums[2 : n - 1]), helper(nums[1:n])
    )  # 返回 取较大值 数组[0] 加 helper(数组[2:元素个数 减 1]), helper(数组[1:元素个数]))


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(rob([2, 3, 2]))  # 打印输出
