# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144850170
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def rob(nums):  # 定义函数 rob（参数：数组）
    length = len(nums)  # 把 长度(数组) 存入 长度
    if length == 0:  # 若 长度 等于 0
        return 0  # 返回 0
    if length == 1:  # 若 长度 等于 1
        return nums[0]  # 返回 数组[0]

    def robRange(start, end):  # 定义函数 robRange（参数：起点, 终点）
        if end == start:  # 若 终点 等于 起点
            return nums[start]  # 返回 数组[起点]
        dp = [0] * (end + 1)  # 把 [0] 乘 (终点 加 1) 存入 DP 表
        dp[start] = nums[start]  # 把 数组[起点] 写入 dp[start]
        dp[start + 1] = max(
            nums[start], nums[start + 1]
        )  # 把 取较大值 数组[起点], 数组[起点 加 1]) 写入 dp[start + 1]
        for i in range(start + 2, end + 1):  # 让 下标 i 从 起点 加 2 到 终点 加 1 遍历
            dp[i] = max(
                dp[i - 2] + nums[i], dp[i - 1]
            )  # 把 取较大值 DP 表[下标 i 减 2] 加 数组[下标 i], DP 表[下标 i 减 1]) 写入 dp[i]
        return dp[end]  # 返回 DP 表[终点]

    ret1 = robRange(0, length - 2)  # 把 robRange(0, 长度 减 2) 存入 ret1
    ret2 = robRange(1, length - 1)  # 把 robRange(1, 长度 减 1) 存入 ret2
    return max(ret1, ret2)  # 返回 取较大值 ret1, ret2)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(rob([2, 3, 2]))  # 打印输出
