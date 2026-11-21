"""双检锁缓存: 快路径无锁读 + 慢路径条目级加载。

- 第一检: 不加锁读 dict(单项读原子), 命中直接返回, 绝大多数请求走这里;
- 第二检: 拿到分片锁后再查一次, 防止两个线程重复加载同一 key;
- 分片锁: 16 把锁按 hash 分摊, 互斥范围缩到同分片, 而非全表一把锁。
对照实验: 完全无锁的版本会重复加载, 双检锁版每个 key 只加载一次。
"""
import threading
import time

SHARDS = 16


class DoubleCheckCache:
    def __init__(self, loader):
        self.loader = loader
        self.data = {}
        self.locks = [threading.Lock() for _ in range(SHARDS)]
        self.loads = {}

    def _shard(self, key):
        return self.locks[hash(key) % SHARDS]

    def get(self, key):
        value = self.data.get(key)          # 第一检: 无锁快路径
        if value is not None:
            return value
        with self._shard(key):              # 慢路径: 只锁一个分片
            value = self.data.get(key)      # 第二检: 锁内复查
            if value is None:
                self.loads[key] = self.loads.get(key, 0) + 1
                value = self.loader(key)
                self.data[key] = value
        return value


class NaiveCache:
    """对照: 完全不加锁, 展示 check-then-act 竞态。"""
    def __init__(self, loader):
        self.loader = loader
        self.data = {}
        self.loads = {}

    def get(self, key):
        value = self.data.get(key)
        if value is None:                   # 只有一检, 多线程可同时进入
            time.sleep(0.01)                # 放大加载窗口
            self.loads[key] = self.loads.get(key, 0) + 1
            value = self.loader(key)
            self.data[key] = value
        return value


def loader(key):
    return "value-of-%s" % key


def hammer(cache, out, idx):
    out[idx] = [cache.get("k%d" % i) for i in range(8)]


def main():
    results = {}
    naive = NaiveCache(loader)
    threads = [threading.Thread(target=hammer, args=(naive, results, i))
               for i in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    dup = sum(v - 1 for v in naive.loads.values())
    print("无锁版各 key 加载次数:", naive.loads)
    print("无锁版重复加载次数:", dup)

    fast = DoubleCheckCache(loader)
    threads = [threading.Thread(target=hammer, args=(fast, results, i))
               for i in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("双检锁版各 key 加载次数:", fast.loads)
    assert all(v == 1 for v in fast.loads.values()), "双检锁必须保证每 key 只加载一次"
    assert dup > 0, "无锁版应出现重复加载"
    print("结论: 第一检吃掉绝大多数无锁命中, 第二检消灭重复加载")


if __name__ == "__main__":
    main()
