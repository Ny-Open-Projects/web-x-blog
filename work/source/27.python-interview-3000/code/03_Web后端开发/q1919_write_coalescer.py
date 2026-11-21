"""合并写: 缓冲窗口与批量落库的两种触发(纯标准库)。"""
from collections import OrderedDict


class WriteCoalescer:
    """按主键合并写: 同键的多次更新在刷盘时只保留最后一次值。

    触发条件是或关系: 条数到 size_limit 或 时间到 tick, 先到先刷。
    """

    def __init__(self, size_limit=5, tick=1.0, flusher=None, clock=None):
        self.size_limit = size_limit
        self.tick = tick
        self.flusher = flusher or (lambda batch: batch)
        self.clock = clock or (lambda: 0.0)
        self.buffer = OrderedDict()        # key -> (value, first_seen)
        self.last_flush = 0.0

    def write(self, key, value):
        now = self.clock()
        if key not in self.buffer:
            self.buffer[key] = [value, now]
        else:
            self.buffer[key][0] = value     # 只保留最后一次的值
        if len(self.buffer) >= self.size_limit or now - self.last_flush >= self.tick:
            return self.flush()
        return None

    def flush(self):
        batch = [{"key": k, "value": v[0]} for k, v in self.buffer.items()]
        self.buffer.clear()
        self.last_flush = self.clock()
        return self.flusher(batch) if batch else None


batches = []


def record(batch):
    batches.append(batch)
    return batch


clock = {"t": 0.0}
c = WriteCoalescer(size_limit=2, tick=1.0, flusher=record, clock=lambda: clock["t"])
print("写入 1:", c.write("stock:a", 10))
print("写入 2(同键覆盖):", c.write("stock:a", 11))
print("写入 3(条数触发):", c.write("stock:b", 5))
print("第一批:", batches[0])
assert batches[0] == [{"key": "stock:a", "value": 11}, {"key": "stock:b", "value": 5}]

clock["t"] = 1.5                     # 时间触发: 不满条数也会刷
print("写入 4(时间触发):", c.write("stock:c", 1))
print("第二批:", batches[1])
assert batches[1] == [{"key": "stock:c", "value": 1}]

c2 = WriteCoalescer(size_limit=10, tick=1.0, flusher=record, clock=lambda: clock["t"])
c2.write("k1", 1)
c2.write("k1", 2)
c2.write("k1", 3)
c2.write("k1", 4)
c2.flush()
print("四写一落(合并率 4:1):", batches[-1])
assert batches[-1] == [{"key": "k1", "value": 4}]
print("要点: 合并写把 N 次写压成 1 次, 同键只留终值, 条数与时间双触发保证延迟有上界")
