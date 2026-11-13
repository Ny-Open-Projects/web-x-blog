# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144829935
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def longestMonotonicSubarray(nums):  # 定义函数 longestMonotonicSubarray（参数：数组）
    if not nums:  # 若 not 数组
        return 0  # 返回 0
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    ans = 1  # 把 1 存入 答案
    length = 1  # 把 1 存入 长度
    # increasing run
    for i in range(1, n):  # 让 下标 i 从 1 到 元素个数 遍历
        if nums[i] > nums[i - 1]:  # 若 数组[下标 i] 超过 数组[下标 i 减 1]
            length += 1  # 长度累加 1
            ans = max(ans, length)  # 把 取较大值 答案, 长度) 存入 答案
        else:  # 否则
            length = 1  # 把 1 存入 长度
    # decreasing run
    length = 1  # 把 1 存入 长度
    for i in range(1, n):  # 让 下标 i 从 1 到 元素个数 遍历
        if nums[i] < nums[i - 1]:  # 若 数组[下标 i] 小于 数组[下标 i 减 1]
            length += 1  # 长度累加 1
            ans = max(ans, length)  # 把 取较大值 答案, 长度) 存入 答案
        else:  # 否则
            length = 1  # 把 1 存入 长度
    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(longestMonotonicSubarray([1, 4, 3, 3, 2]))  # 打印输出
