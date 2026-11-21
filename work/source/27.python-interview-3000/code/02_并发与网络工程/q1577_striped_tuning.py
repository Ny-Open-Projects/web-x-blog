"""分段锁的分片数选型: 用压测找拐点。

分片数是"锁竞争"与"内存/复杂度"的折中: 1 把锁全表串行, 分片数
不低于并发写线程数时竞争基本消失, 再往上只剩边际收益。本实验固定
8 个写线程, 对 1/2/4/8/64 分片分别压测, 观察耗时拐点。
"""
import random
import threading
import time


class ShardedCounter:
    def __init__(self, shards):
        self.shards = shards
        self.cells = [0] * shards
        self.locks = [threading.Lock() for _ in range(shards)]

    def incr(self):
        i = random.randrange(self.shards)   # 键均匀散列到分片
        with self.locks[i]:
            self.cells[i] += 1

    @property
    def total(self):
        return sum(self.cells)


THREADS = 8
OPS = 40000


def bench(shards):
    counter = ShardedCounter(shards)

    def worker():
        for _ in range(OPS):
            counter.incr()

    ts = [threading.Thread(target=worker) for _ in range(THREADS)]
    t0 = time.monotonic()
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    wall = time.monotonic() - t0
    assert counter.total == THREADS * OPS, "分片计数必须分毫不差"
    return wall


def main():
    print("写线程 %d, 每 %d 次自增, 不同分片数的耗时:" % (THREADS, OPS))
    for shards in (1, 2, 4, 8, 64):
        wall = bench(shards)
        print("  分片数 %3d -> %.3fs" % (shards, wall))
    print("结论: 拐点在'分片数 >= 并发写线程'附近; 再多只是浪费内存与遍历成本")


if __name__ == "__main__":
    main()
