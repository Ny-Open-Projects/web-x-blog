# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144831173
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def longestArithSeqLength(nums):  # 定义函数 longestArithSeqLength（参数：数组）
    if len(nums) <= 2:  # 若 长度(数组) 不超过 2
        return len(nums)  # 返回 长度(数组)
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    dp = [{} for _ in range(n)]  # 把 [{} for _ in range(元素个数)] 存入 DP 表
    ans = 2  # 把 2 存入 答案
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        for j in range(i):  # 让 下标 j 从 下标 i 遍历
            d = nums[i] - nums[j]  # 把 数组[下标 i] 减 数组[下标 j] 存入 d
            prev = dp[j].get(d, 1)  # 把 DP 表[下标 j] 查找 d, 1) 存入 前一个
            cur = prev + 1  # 把 前一个 加 1 存入 当前值
            dp[i][d] = cur  # 把 当前值 写入 dp[i][d]
            if cur > ans:  # 若 当前值 超过 答案
                ans = cur  # 把 当前值 存入 答案
    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(longestArithSeqLength([9, 4, 7, 2, 10]))  # 打印输出
