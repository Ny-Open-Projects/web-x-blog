# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144850170
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def rob(nums):  # 定义函数 rob（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    if n == 0:  # 若 元素个数 等于 0
        return 0  # 返回 0
    if n == 1:  # 若 元素个数 等于 1
        return nums[0]  # 返回 数组[0]

    # dp1 不抢最后一个房子, dp2 不抢第一个房子
    dp1 = [0] * n  # 把 [0] 乘 元素个数 存入 dp1
    dp2 = [0] * n  # 把 [0] 乘 元素个数 存入 dp2

    dp1[0] = nums[0]  # 把 数组[0] 写入 dp1[0]
    dp1[1] = max(nums[0], nums[1])  # 把 取较大值 数组[0], 数组[1]) 写入 dp1[1]
    dp2[1] = nums[1]  # 把 数组[1] 写入 dp2[1]

    for i in range(2, n):  # 让 下标 i 从 2 到 元素个数 遍历
        dp1[i] = max(
            dp1[i - 1], dp1[i - 2] + nums[i]
        )  # 把 取较大值 dp1[下标 i 减 1], dp1[下标 i 减 2] 加 数组[下标 i]) 写入 dp1[i]
    for i in range(2, n - 1):  # 让 下标 i 从 2 到 元素个数 减 1 遍历
        dp2[i] = max(
            dp2[i - 1], dp2[i - 2] + nums[i]
        )  # 把 取较大值 dp2[下标 i 减 1], dp2[下标 i 减 2] 加 数组[下标 i]) 写入 dp2[i]

    return max(dp1[n - 2], dp2[n - 1])  # 返回 取较大值 dp1[元素个数 减 2], dp2[元素个数 减 1])


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(rob([2, 3, 2]))  # 打印输出
