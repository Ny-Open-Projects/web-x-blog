# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145094527
class LRUCache:  # 定义类
    def __init__(self, capacity: int):  # 构造函数：初始化成员
        self.capacity = capacity  # 把 capacity 写入 self.capacity
        self.cache = {}  # 把 {} 写入 self.cache

    def get(self, key: int) -> int:  # 定义函数 get（参数：self, key: int）
        if key not in self.cache:  # 若 key not in self.cache
            return -1  # 返回 减 1
        # Move to end (most recently used)
        val = self.cache.pop(key)  # 把 self.cache 弹出 key) 存入 值
        self.cache[key] = val  # 把 值 写入 self.cache[key]
        return val  # 返回 值

    def put(self, key: int, value: int) -> None:  # 定义函数 put（参数：self, key: int, value: int）
        if key in self.cache:  # 若 key in self.cache
            self.cache.pop(key)  # self.cache 弹出 key)
        elif len(self.cache) >= self.capacity:  # 否则，若 长度(self.cache) 不低于 self.capacity
            # Remove oldest (first item)
            oldest = next(iter(self.cache))  # 把 下一个(iter(self.cache)) 存入 oldest
            del self.cache[oldest]  # del self.cache[oldest]
        self.cache[key] = value  # 把 value 写入 self.cache[key]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    cache = LRUCache(2)  # 把 LRUCache(2) 存入 cache
    cache.put(1, 1)  # cache.put(1, 1)
    cache.put(2, 2)  # cache.put(2, 2)
    print(cache.get(1))  # 打印输出
    cache.put(3, 3)  # cache.put(3, 3)
    print(cache.get(2))  # 打印输出
    cache.put(4, 4)  # cache.put(4, 4)
    print(cache.get(1))  # 打印输出
    print(cache.get(3))  # 打印输出
    print(cache.get(4))  # 打印输出
