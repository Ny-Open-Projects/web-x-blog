# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145374997
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def getSumAbsoluteDifferences(nums):  # 定义函数 getSumAbsoluteDifferences（参数：数组）
    prefixSums = [0]  # 把 [0] 存入 prefixSums
    for i in range(0, len(nums)):  # 让 下标 i 从 0 到 长度(数组 遍历
        prefixSums.append(prefixSums[i] + nums[i])  # 把 prefixSums[下标 i] 加 数组[下标 i] 追加到列表尾部
    ans = []  # 把 [] 存入 答案
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    for i in range(0, n):  # 让 下标 i 从 0 到 元素个数 遍历
        x = nums[i]  # 把 数组[下标 i] 存入 x
        left = i * x - prefixSums[i]  # 把 下标 i 乘 x 减 prefixSums[下标 i] 存入 左边界
        right = prefixSums[n] - prefixSums[i + 1] - x * (n - 1 - i)
        ans.append(left + right)  # 把 左边界 加 右边界 追加到列表尾部
    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(getSumAbsoluteDifferences([1, 2, 3]))  # 打印输出
