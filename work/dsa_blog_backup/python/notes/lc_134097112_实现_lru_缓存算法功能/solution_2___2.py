# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134097112
# LRU 缓存 - 方案2: 基于 OrderedDict
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
from collections import OrderedDict  # from collections import OrderedDict


class LRUCache:  # 定义类
    def __init__(self, length):  # 构造函数：初始化成员
        self.length = length  # 把 长度 写入 长度
        self.data = OrderedDict()  # 把 OrderedDict() 写入 self.data

    def set(self, key, value):  # 定义函数 set（参数：self, key, value）
        if key in self.data:  # 若 key in self.data
            del self.data[key]  # del self.data[key]
        self.data[key] = value  # 把 value 写入 self.data[key]
        if len(self.data) > self.length:  # 若 长度(self.data) 超过 self.长度
            self.data.popitem(last=False)  # 把 False) 写入 self.data.popitem(last

    def get(self, key):  # 定义函数 get（参数：self, key）
        if key not in self.data:  # 若 key not in self.data
            return None  # 返回 None
        self.data.move_to_end(key)  # self.data.move_to_end(key)
        return self.data[key]  # 返回 self.data[key]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    lru_cache = LRUCache(2)  # 把 LRUCache(2) 存入 lru_cache
    lru_cache.set(1, 1)  # lru_cache.set(1, 1)
    lru_cache.set(2, 2)  # lru_cache.set(2, 2)
    print(lru_cache.get(1))  # 1
    lru_cache.set(3, 3)  # lru_cache.set(3, 3)
    print(lru_cache.get(2))  # None
    lru_cache.set(4, 4)  # lru_cache.set(4, 4)
    print(lru_cache.get(1))  # None
    print(lru_cache.get(3))  # 3
    print(lru_cache.get(4))  # 4
