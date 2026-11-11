# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145344649
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import bisect  # 引入依赖


class MedianFinder:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.nums = []  # 把 [] 写入 数组

    def addNum(self, num):  # 定义函数 addNum（参数：self, num）
        bisect.insort(self.nums, num)  # bisect.insort(self.数组, num)

    def findMedian(self):  # 定义函数 findMedian（参数：self）
        n = len(self.nums)  # 把 长度(self.数组) 存入 元素个数
        if n == 0:  # 若 元素个数 等于 0
            return None  # 返回 None
        if n % 2 == 1:  # 若 元素个数 对…取模 2 等于 1
            return self.nums[n // 2]  # 返回 self.数组[元素个数 除以 除以 2]
        return (
            self.nums[n // 2 - 1] + self.nums[n // 2]
        ) / 2  # 返回 (self.数组[元素个数 除以 除以 2 减 1] 加 self.数组[元素个数 除以 除以 2]) 除以 2


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    mf = MedianFinder()  # 把 MedianFinder() 存入 mf
    for x in [1, 2, 3, 4, 5]:  # for x in [1, 2, 3, 4, 5]:
        mf.addNum(x)  # mf.addNum(x)
    print(mf.findMedian())  # 打印输出
