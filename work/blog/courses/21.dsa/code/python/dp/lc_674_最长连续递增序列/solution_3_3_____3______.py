# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144821546
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def findLengthOfLCIS(nums):  # 定义函数 findLengthOfLCIS（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    if n <= 1:  # 若 元素个数 不超过 1
        return n  # 返回 元素个数
    count = 1  # 把 1 存入 计数
    dp = [1] * n  # 把 [1] 乘 元素个数 存入 DP 表
    for i in range(1, n):  # 让 下标 i 从 1 到 元素个数 遍历
        if nums[i - 1] < nums[i]:  # 若 数组[下标 i 减 1] 小于 数组[下标 i]
            dp[i] = dp[i - 1] + 1  # 把 DP 表[下标 i 减 1] 加 1 写入 dp[i]
        if count < dp[i]:  # 若 计数 小于 DP 表[下标 i]
            count = dp[i]  # 把 DP 表[下标 i] 存入 计数
    return count  # 返回 计数


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(findLengthOfLCIS([1, 3, 5, 4, 7]))  # 打印输出
    print(findLengthOfLCIS([2, 2, 2, 2, 2]))  # 打印输出
    print(findLengthOfLCIS([1, 2, 3]))  # 打印输出
