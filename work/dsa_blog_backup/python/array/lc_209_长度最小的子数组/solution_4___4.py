# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116019
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def minSubArrayLen(target, nums):  # 定义函数 minSubArrayLen（参数：目标值, 数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    slow = fast = 0  # 把 快指针 赋值为 0 存入 慢指针
    total = 0  # 把 0 存入 总和
    result = n + 1  # 把 元素个数 加 1 存入 结果
    while fast < n:  # 循环，直到不满足「快指针 小于 元素个数」
        total += nums[fast]  # 总和累加 数组[快指针]
        while total >= target:  # 循环，直到不满足「总和 不低于 目标值」
            result = min(result, fast - slow + 1)  # 把 取较小值 结果, 快指针 减 慢指针 加 1) 存入 结果
            total -= nums[slow]  # 总和累减 数组[慢指针]
            slow += 1  # 慢指针累加 1
        fast += 1  # 快指针累加 1
    return result if result <= n else 0  # 返回 结果 if 结果 不超过 元素个数 else 0


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(minSubArrayLen(1, [1, 2, 3]))  # 打印输出
