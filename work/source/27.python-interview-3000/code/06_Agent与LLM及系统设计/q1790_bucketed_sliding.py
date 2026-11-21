"""滑动日志近似:窗口切桶计数,内存从 O 事件数 降到 O 桶数,误差有界。"""


class ExactSlidingLog:
    def __init__(self, limit, window):
        self.limit, self.window = limit, window
        self.events = []

    def allow(self, ts):
        self.events = [t for t in self.events if ts - t < self.window]
        if len(self.events) >= self.limit:
            return False
        self.events.append(ts)
        return True

    def memory(self):
        return len(self.events)


class BucketedSlidingLog:
    def __init__(self, limit, window, buckets=5):
        self.limit, self.window, self.buckets = limit, window, buckets
        self.bucket_span = window / buckets
        self.counts = {}                         # 桶序号 -> 计数

    def _bucket_of(self, ts):
        return int(ts // self.bucket_span)

    def allow(self, ts):
        cur = self._bucket_of(ts)
        oldest = cur - self.buckets + 1
        used = sum(n for b, n in self.counts.items() if b >= oldest)
        if used >= self.limit:
            return False
        self.counts[cur] = self.counts.get(cur, 0) + 1
        for b in [b for b in self.counts if b < oldest]:
            del self.counts[b]                   # 老桶顺手清掉
        return True

    def memory(self):
        return len(self.counts)


if __name__ == "__main__":
    ex, bk = ExactSlidingLog(3, 10.0), BucketedSlidingLog(3, 10.0, buckets=5)
    seq = [1.0, 2.0, 3.0, 4.0, 12.0, 12.5, 13.0, 14.0]
    exact_decisions = [ex.allow(t) for t in seq]
    bucket_decisions = [bk.allow(t) for t in seq]
    assert exact_decisions == [True, True, True, False, True, True, True, False]
    assert bucket_decisions == exact_decisions, "稀疏负载下分桶与精确决策一致"
    assert bk.memory() <= 5 and ex.memory() == 3

    ex2, bk2 = ExactSlidingLog(10 ** 6, 10.0), BucketedSlidingLog(10 ** 6, 10.0, buckets=5)
    for i in range(200):
        ex2.allow(i * 0.1)
        bk2.allow(i * 0.1)
    assert bk2.memory() <= 5, "高频下分桶内存恒为桶数"
    assert ex2.memory() > bk2.memory() * 10, "精确日志内存比分桶高一个数量级"
    print("分桶近似通过:决策与精确一致,内存从事件数级降到桶数级")
