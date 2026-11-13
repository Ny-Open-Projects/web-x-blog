# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134097112
# LRU 缓存 - 方案1: 基于 dict (Python3.7+ 保留插入顺序)
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class LRUCache:  # 定义类
    def __init__(self, length):  # 构造函数：初始化成员
        self.length = length  # 把 长度 写入 长度
        self.data = {}  # 把 {} 写入 self.data

    def set(self, key, value):  # 定义函数 set（参数：self, key, value）
        data = self.data  # 把 self.data 存入 data
        if key in data:  # 若 key in data
            del data[key]  # del data[key]
        data[key] = value  # 把 value 写入 data[key]
        if len(data) > self.length:  # 若 长度(data) 超过 self.长度
            del_key = next(iter(data))  # 把 下一个(iter(data)) 存入 del_key
            del data[del_key]  # del data[del_key]

    def get(self, key):  # 定义函数 get（参数：self, key）
        data = self.data  # 把 self.data 存入 data
        if key not in data:  # 若 key not in data
            return None  # 返回 None
        value = data[key]  # 把 data[key] 存入 value
        del data[key]  # del data[key]
        data[key] = value  # 保持最新
        return value  # 返回 value


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
