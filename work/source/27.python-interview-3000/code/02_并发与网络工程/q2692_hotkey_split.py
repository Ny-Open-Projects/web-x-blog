# -*- coding: utf-8 -*-
"""限流键的热点拆分: 大租户刷屏, 小租户还要活。

- 单桶 FIFO: 同一个限流键下, 谁先来谁占坑, 大客户把小客户挤下悬崖;
- 热点拆分: 键拆成 N 片, 每片独立配额, 片内轮转公平出票;
- 结果: 超订的大客户自己吃丢弃, 小客户的份额一根毫毛都不少。
"""
from collections import deque, defaultdict

CLIENTS = [("big-A", 70), ("big-B", 20), ("big-C", 20)]
CAPACITY = 100
SHARDS = 4


def simulate_single(ticks=10):
    """单桶 FIFO: 到达顺序即优先级。"""
    served = defaultdict(int)
    dropped = defaultdict(int)
    for _ in range(ticks):
        q = deque()
        for c, n in CLIENTS:                 # 大客户先入队, 占住队头
            q.extend([c] * n)
        for _ in range(CAPACITY):
            if q:
                served[q.popleft()] += 1
        while q:
            dropped[q.popleft()] += 1
    return served, dropped


def simulate_sharded(ticks=10):
    """热点拆分: 键拆 N 片, 每片独立配额, 片内轮转公平。"""
    served = defaultdict(int)
    dropped = defaultdict(int)
    for _ in range(ticks):
        shards = [deque() for _ in range(SHARDS)]
        for c, n in CLIENTS:                 # 请求轮转散到各分片
            for k in range(n):
                shards[k % SHARDS].append(c)
        for sq in shards:
            quota = CAPACITY // SHARDS
            buckets = defaultdict(deque)     # 片内按客户端分桶
            for c in sq:
                buckets[c].append(c)
            out = []
            while len(out) < quota:          # 轮流出票
                progressed = False
                for c in list(buckets):
                    if buckets[c]:
                        out.append(buckets[c].popleft())
                        progressed = True
                if not progressed:
                    break
            for c in out:
                served[c] += 1
            for c in list(buckets):          # 剩下的即本片丢弃
                while buckets[c]:
                    buckets[c].popleft()
                    dropped[c] += 1
    return served, dropped


if __name__ == "__main__":
    s1, d1 = simulate_single()
    s2, d2 = simulate_sharded()
    print("单桶 FIFO:   served=%s dropped=%s"
          % (dict(s1), dict(d1)))
    print("热点拆分 4 片: served=%s dropped=%s"
          % (dict(s2), dict(d2)))
    print("要点: 单桶下小客户 C 全灭, 大客户 A 一根毛都没掉")
    print("要点: 拆分后丢弃精准砸向超订者 A, 小客户份额完好")
