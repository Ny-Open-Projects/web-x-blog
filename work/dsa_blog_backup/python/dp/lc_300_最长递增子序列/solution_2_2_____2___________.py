# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144823912
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import bisect  # 引入依赖


def lengthOfLIS(nums):  # 定义函数 lengthOfLIS（参数：数组）
    # 动态规划 + 二分查找（O(n log n)）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    if n == 0:  # 若 元素个数 等于 0
        return 0  # 返回 0
    dp = []  # 把 [] 存入 DP 表
    for num in nums:  # 逐个取出 数组 的元素（num）
        i = bisect.bisect_left(dp, num)  # 把 bisect.bisect_left(DP 表, num) 存入 下标 i
        if i == len(dp):  # 若 下标 i 等于 长度(DP 表
            dp.append(num)  # 把 num 追加到列表尾部
        else:  # 否则
            dp[i] = num  # 把 num 写入 dp[i]
    return len(dp)  # 返回 长度(DP 表)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 打印输出
