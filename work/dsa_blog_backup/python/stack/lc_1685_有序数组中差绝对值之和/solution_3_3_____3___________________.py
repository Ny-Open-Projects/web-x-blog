# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145374997
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def getSumAbsoluteDifferences(nums):  # 定义函数 getSumAbsoluteDifferences（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    ans = [0] * n  # 把 [0] 乘 元素个数 存入 答案
    sum_total = sum(nums)  # 把 累计和(数组) 存入 sum_total

    # Calculate for first element
    ans[0] = sum_total - nums[0] * n  # 把 sum_total 减 数组[0] 乘 元素个数 写入 ans[0]

    # Use dynamic programming
    for i in range(1, n):  # 让 下标 i 从 1 到 元素个数 遍历
        d = nums[i] - nums[i - 1]  # 把 数组[下标 i] 减 数组[下标 i 减 1] 存入 d
        ans[i] = (
            ans[i - 1] - (n - 2 * i) * d
        )  # 把 答案[下标 i 减 1] 减 (元素个数 减 2 乘 下标 i) 乘 d 写入 ans[i]

    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(getSumAbsoluteDifferences([1, 2, 3]))  # 打印输出
