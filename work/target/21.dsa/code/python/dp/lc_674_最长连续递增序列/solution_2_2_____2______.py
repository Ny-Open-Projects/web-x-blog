# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144821546
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def findLengthOfLCIS(nums):  # 定义函数 findLengthOfLCIS（参数：数组）
    if not nums:  # 若 not 数组
        return 0  # 返回 0
    ans = 1  # 把 1 存入 答案
    cur = 1  # 把 1 存入 当前值
    for i in range(1, len(nums)):  # 让 下标 i 从 1 到 长度(数组 遍历
        if nums[i] > nums[i - 1]:  # 若 数组[下标 i] 超过 数组[下标 i 减 1]
            cur += 1  # 当前值累加 1
            ans = max(ans, cur)  # 把 取较大值 答案, 当前值) 存入 答案
        else:  # 否则
            cur = 1  # 把 1 存入 当前值
    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(findLengthOfLCIS([2, 2, 2, 2, 2]))  # 打印输出
