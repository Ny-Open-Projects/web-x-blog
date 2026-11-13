# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144823912
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def lengthOfLIS(nums):  # 定义函数 lengthOfLIS（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    if n == 0:  # 若 元素个数 等于 0
        return 0  # 返回 0
    # 初始化 dp 数组，每个元素设为 1
    dp = [1] * n  # 把 [1] 乘 元素个数 存入 DP 表
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        for j in range(i):  # 让 下标 j 从 下标 i 遍历
            if nums[j] < nums[i]:  # 若 数组[下标 j] 小于 数组[下标 i]
                dp[i] = max(dp[i], dp[j] + 1)  # 把 取较大值 DP 表[下标 i], DP 表[下标 j] 加 1) 写入 dp[i]
    return max(dp)  # 返回 取较大值 DP 表)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 打印输出
