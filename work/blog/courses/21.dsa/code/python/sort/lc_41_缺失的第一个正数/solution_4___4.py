# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134429994
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def firstMissingPositive(nums):  # 定义函数 firstMissingPositive（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        if nums[i] <= 0:  # 若 数组[下标 i] 不超过 0
            nums[i] = n + 1  # 把 元素个数 加 1 写入 nums[i]
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        num = abs(nums[i])  # 把 取绝对值 数组[下标 i]) 存入 num
        if num <= n:  # 若 num 不超过 元素个数
            nums[num - 1] = -abs(nums[num - 1])  # 把 减 取绝对值 数组[num 减 1]) 写入 nums[num - 1]
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        if nums[i] > 0:  # 若 数组[下标 i] 超过 0
            return i + 1  # 返回 下标 i 加 1
    return n + 1  # 返回 元素个数 加 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(firstMissingPositive([1, 2, 3]))  # 打印输出
