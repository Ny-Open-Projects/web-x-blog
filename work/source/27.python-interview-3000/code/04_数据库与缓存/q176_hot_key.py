"""热 key 治理: 本地 LRU 缓存 + 热 key 打散副本"""
from collections import OrderedDict
import random


class LocalLRU:
    def __init__(self, capacity: int = 2):
        self.data: OrderedDict = OrderedDict()
        self.capacity = capacity
        self.hits = 0

    def get(self, key):
        if key in self.data:
            self.data.move_to_end(key)
            self.hits += 1
            return self.data[key]
        return None

    def put(self, key, value):
        self.data[key] = value
        self.data.move_to_end(key)
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)


REPLICAS = 4       # 热 key 打散成 4 个副本


def shard_key(key: str) -> str:
    return f"{key}:{random.randrange(REPLICAS)}"


class TieredCache:
    def __init__(self):
        self.local = LocalLRU()
        self.remote: dict = {}
        self.remote_reads = 0

    def load_remote(self, key: str, value: str):
        for i in range(REPLICAS):          # 写: 更新全部副本
            self.remote[f"{key}:{i}"] = value

    def get(self, key: str):
        hit = self.local.get(key)
        if hit is not None:
            return hit, "local"
        self.remote_reads += 1
        value = self.remote.get(shard_key(key))   # 读: 随机副本分流
        if value is not None:
            self.local.put(key, value)            # 回填本地
        return value, "remote"


if __name__ == "__main__":
    cache = TieredCache()
    cache.load_remote("hot:news", "头条内容")
    for _ in range(100):
        cache.get("hot:news")
    print(f"本地命中 {cache.local.hits} 次, 远端读取 {cache.remote_reads} 次")
    # 本地缓存把绝大部分读挡在进程内, 剩余读也被副本分散到多个分片
