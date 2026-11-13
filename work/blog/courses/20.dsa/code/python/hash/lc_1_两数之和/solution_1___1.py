# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133322239
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def twoSum(nums, target):  # 定义函数 twoSum（参数：数组, 目标值）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        for j in range(i + 1, n):  # 让 下标 j 从 下标 i 加 1 到 元素个数 遍历
            if nums[i] + nums[j] == target:  # 若 数组[下标 i] 加 数组[下标 j] 等于 目标值
                return [i, j]  # 返回 [下标 i, 下标 j]
    return []  # 返回 []


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(twoSum([2, 7, 11, 15], 9))  # 打印输出
