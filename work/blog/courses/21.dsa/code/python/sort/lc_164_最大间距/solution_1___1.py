# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134379497
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def maximumGap(nums):  # 定义函数 maximumGap（参数：数组）
    if len(nums) < 2:  # 若 长度(数组) 小于 2
        return 0  # 返回 0
    nums.sort()  # 排序
    max_gap = 0  # 把 0 存入 max_gap
    for i in range(1, len(nums)):  # 让 下标 i 从 1 到 长度(数组 遍历
        max_gap = max(
            max_gap, nums[i] - nums[i - 1]
        )  # 把 取较大值 max_gap, 数组[下标 i] 减 数组[下标 i 减 1]) 存入 max_gap
    return max_gap  # 返回 max_gap


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(maximumGap([1, 2, 3]))  # 打印输出
