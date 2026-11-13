# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144829143
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def findNumberOfLIS(nums):  # 定义函数 findNumberOfLIS（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    if n == 0:  # 若 元素个数 等于 0
        return 0  # 返回 0
    maxLen = 0  # 把 0 存入 maxLen
    ans = 0  # 把 0 存入 答案
    dp = [1] * n  # 把 [1] 乘 元素个数 存入 DP 表
    cnt = [1] * n  # 把 [1] 乘 元素个数 存入 计数
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        for j in range(i):  # 让 下标 j 从 下标 i 遍历
            if nums[j] < nums[i]:  # 若 数组[下标 j] 小于 数组[下标 i]
                if dp[j] + 1 > dp[i]:  # 若 DP 表[下标 j] 加 1 超过 DP 表[下标 i]
                    dp[i] = dp[j] + 1  # 把 DP 表[下标 j] 加 1 写入 dp[i]
                    cnt[i] = cnt[j]  # 重置计数
                elif dp[j] + 1 == dp[i]:  # 否则，若 DP 表[下标 j] 加 1 等于 DP 表[下标 i]
                    cnt[i] += cnt[j]  # cnt[i]累加 计数[下标 j]
        if dp[i] > maxLen:  # 若 DP 表[下标 i] 超过 maxLen
            maxLen = dp[i]  # 把 DP 表[下标 i] 存入 maxLen
            ans = cnt[i]  # 重置计数
        elif dp[i] == maxLen:  # 否则，若 DP 表[下标 i] 等于 maxLen
            ans += cnt[i]  # 答案累加 计数[下标 i]
    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(findNumberOfLIS([1, 3, 5, 4, 7]))  # 打印输出
