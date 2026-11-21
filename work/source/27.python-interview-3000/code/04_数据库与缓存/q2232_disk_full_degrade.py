"""磁盘满的降级写入: 按优先级落盘 缓冲与丢弃"""

class DegradedWriter:
    def __init__(self, free_mb):
        self.free = free_mb
        self.cost = {"log": 0.3, "metric": 0.2, "order": 1.0}
        self.prio = {"log": 0, "metric": 1, "order": 2}
        self.buffer = []
        self.dropped = {"low": 0, "mid": 0}

    def write(self, kind, payload):
        cost = self.cost[kind]
        if self.free >= cost:
            self.free -= cost
            return "落盘"
        if self.prio[kind] == 2:
            self.buffer.append((kind, payload))
            return "缓冲"
        self.dropped["low" if self.prio[kind] == 0 else "mid"] += 1
        return "丢弃"

    def release(self, mb):
        self.free += mb
        flushed = []
        while self.buffer and self.free >= self.cost[self.buffer[0][0]]:
            kind, payload = self.buffer.pop(0)
            self.free -= self.cost[kind]
            flushed.append(payload)
        return flushed

w = DegradedWriter(free_mb=1.2)
for kind, payload in [("log", "l1"), ("metric", "m1"), ("log", "l2"), ("order", "o1"),
                      ("log", "l3"), ("order", "o2"), ("metric", "m2"), ("log", "l4")]:
    print("写入 %-4s -> %s" % (payload, w.write(kind, payload)))
print("释放 2MB 后冲刷缓冲:", w.release(2.0))
print("丢弃计数:", w.dropped, " <- 低价值先丢, 核心缓冲待补, 全程不阻塞主流程")
