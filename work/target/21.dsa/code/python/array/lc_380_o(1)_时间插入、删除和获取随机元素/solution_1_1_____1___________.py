# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145345735
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import random  # 引入依赖


class RandomizedSet:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.nums = []  # 把 [] 写入 数组
        self.indices = {}  # 把 {} 写入 self.indices

    def insert(self, val):  # 定义函数 insert（参数：self, 值）
        if val in self.indices:  # 若 值 in self.indices
            return False  # 返回 False
        index = len(self.nums)  # 把 长度(self.数组) 存入 index
        self.nums.append(val)  # 把 值 追加到列表尾部
        self.indices[val] = index  # 把 index 写入 self.indices[val]
        return True  # 返回 True

    def remove(self, val):  # 定义函数 remove（参数：self, 值）
        if val not in self.indices:  # 若 值 not in self.indices
            return False  # 返回 False
        idx = self.indices[val]  # 把 self.indices[值] 存入 idx
        last = self.nums[-1]  # 把 self.数组[ 减 1] 存入 last
        self.nums[idx] = last  # 把 last 写入 self.nums[idx]
        self.indices[last] = idx  # 把 idx 写入 self.indices[last]
        self.nums.pop()  # 弹出栈顶元素
        del self.indices[val]  # del self.indices[值]
        return True  # 返回 True

    def getRandom(self):  # 定义函数 getRandom（参数：self）
        return random.choice(self.nums)  # 返回 random.choice(self.数组)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    rs = RandomizedSet()  # 把 RandomizedSet() 存入 rs
    print(rs.insert(1))  # 打印输出
    print(rs.remove(2))  # 打印输出
    print(rs.insert(2))  # 打印输出
    print(rs.getRandom())  # 打印输出
    print(rs.remove(1))  # 打印输出
    print(rs.insert(2))  # 打印输出
    print(rs.getRandom())  # 打印输出
