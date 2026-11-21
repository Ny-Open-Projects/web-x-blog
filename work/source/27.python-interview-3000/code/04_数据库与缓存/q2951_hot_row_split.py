"""热点行拆分实测: 单行锁串行排队 vs 分片后并行 的耗时对比"""
import random
import threading
import time

LOCK_IO = 0.001   # 模拟一次行更新在库内的持锁与落盘耗时


class RowCounter:
    """单行: 所有更新在同一把行锁上排队, 这就是热点行天花板"""
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def incr(self, n):
        for _ in range(n):
            with self.lock:
                time.sleep(LOCK_IO)
                self.value += 1


class ShardedCounter:
    """拆分: 计数拆 N 片, 写随机片, 读时 SUM 聚合, 锁压力摊薄"""
    def __init__(self, shards=8):
        self.parts = [0] * shards
        self.locks = [threading.Lock() for _ in range(shards)]

    def incr(self, n):
        for _ in range(n):
            i = random.randrange(len(self.parts))
            with self.locks[i]:
                time.sleep(LOCK_IO)
                self.parts[i] += 1

    @property
    def value(self):
        return sum(self.parts)


def bench(cls, threads=8, per_thread=100):
    obj = cls()
    t0 = time.perf_counter()
    ts = [threading.Thread(target=obj.incr, args=(per_thread,))
          for _ in range(threads)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    return obj, (time.perf_counter() - t0) * 1000


single, ms1 = bench(RowCounter)
sharded, ms2 = bench(ShardedCounter)
print("单行 800 次更新: %.0f ms, 终值=%d" % (ms1, single.value))
print("8 片 800 次更新: %.0f ms, 终值=%d, 快约 %.1f 倍"
      % (ms2, sharded.value, ms1 / ms2))
assert single.value == sharded.value == 800
print("分片把单行串行队列拆成 N 条短队, 读侧一次 SUM 聚合拿全量")
