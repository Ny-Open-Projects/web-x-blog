# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133322239
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def twoSum(nums, target):  # 定义函数 twoSum（参数：数组, 目标值）
    mp = {}  # 把 {} 存入 mp
    for i in range(len(nums)):  # 让 下标 i 从 长度(数组 遍历
        current = nums[i]  # 把 数组[下标 i] 存入 current
        wanted = target - current  # 把 目标值 减 current 存入 wanted
        if wanted in mp:  # 若 wanted in mp
            return [mp[wanted], i]  # 返回 [mp[wanted], 下标 i]
        mp[current] = i  # 把 下标 i 写入 mp[current]
    return []  # 返回 []


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(twoSum([2, 7, 11, 15], 9))  # 打印输出
