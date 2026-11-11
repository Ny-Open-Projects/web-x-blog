# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145374997
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def getSumAbsoluteDifferences(nums):  # 定义函数 getSumAbsoluteDifferences（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    left_sum = 0  # 把 0 存入 left_sum
    right_sum = sum(nums)  # 把 累计和(数组) 存入 right_sum
    result = [0] * n  # 把 [0] 乘 元素个数 存入 结果

    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        right_sum -= nums[i]  # right_sum累减 数组[下标 i]
        result[i] = i * nums[i] - left_sum + right_sum - (n - i - 1) * nums[i]
        left_sum += nums[i]  # left_sum累加 数组[下标 i]

    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(getSumAbsoluteDifferences([1, 2, 3]))  # 打印输出
