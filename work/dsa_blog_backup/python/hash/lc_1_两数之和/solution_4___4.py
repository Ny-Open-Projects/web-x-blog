# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133322239
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def twoSum(nums, target):  # 定义函数 twoSum（参数：数组, 目标值）
    m = {}  # 把 {} 存入 映射表
    for i, current in enumerate(nums):  # 同时取 下标 i 与 current 遍历
        wanted = target - current  # 把 目标值 减 current 存入 wanted
        if wanted in m:  # 若 wanted in 映射表
            return [m[wanted], i]  # 返回 [映射表[wanted], 下标 i]
        m[current] = i  # 把 下标 i 写入 m[current]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(twoSum([2, 7, 11, 15], 9))  # 打印输出
    print(twoSum([3, 2, 4], 6))  # 打印输出
    print(twoSum([3, 3], 6))  # 打印输出
