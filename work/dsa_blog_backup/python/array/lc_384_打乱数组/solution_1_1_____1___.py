# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145345965
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import random  # 引入依赖


class Solution:  # 定义类
    def __init__(self, nums):  # 构造函数：初始化成员
        self.nums = list(nums)  # 把 列表(数组) 写入 数组
        self.original = list(nums)  # 把 列表(数组) 写入 self.original

    def reset(self):  # 定义函数 reset（参数：self）
        self.nums = list(self.original)  # 把 列表(self.original) 写入 数组
        return self.nums  # 返回 self.数组

    def shuffle(self):  # 定义函数 shuffle（参数：self）
        shuffled = list(self.nums)  # 把 列表(self.数组) 存入 shuffled
        for i in range(len(shuffled) - 1, 0, -1):  # 让 下标 i 从 长度(shuffled) 减 1 倒数回去（每步减 1）
            j = random.randint(0, i)  # 把 random.randint(0, 下标 i) 存入 下标 j
            shuffled[i], shuffled[j] = (
                shuffled[j],
                shuffled[i],
            )  # 把 shuffled[下标 j], shuffled[下标 i] 写入 shuffled[i], shuffled[j]
        self.nums = shuffled  # 把 shuffled 写入 数组
        return self.nums  # 返回 self.数组


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    s = Solution([1, 2, 3])  # 把 Solution([1, 2, 3]) 存入 字符串
    print("shuffle:", s.shuffle())  # 打印输出
    print("reset:", s.reset())  # 打印输出
