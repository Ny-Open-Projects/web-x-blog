"""写入合并: 窗口内多次写聚合为一次远端提交"""

class FakeRedis:
    def __init__(self):
        self.hash = {}
        self.ops = 0

    def hincrby(self, key, field, delta):
        self.ops += 1
        self.hash.setdefault(key, {})
        self.hash[key][field] = self.hash[key].get(field, 0) + delta

class WriteCoalescer:
    """按 key 收集增量, flush 时合并函数折叠后一次提交"""
    def __init__(self, redis, merge):
        self.r = redis
        self.buf = {}
        self.merge = merge

    def add(self, key, field, delta):
        self.buf.setdefault(key, {})
        self.buf[key][field] = self.merge(self.buf[key].get(field, 0), delta)

    def flush(self):
        n = 0
        for key, fields in self.buf.items():
            for f, v in fields.items():
                self.r.hincrby(key, f, v)
                n += 1
        self.buf = {}
        return n

r = FakeRedis()
for _ in range(1000):
    r.hincrby("stats:pv", "home", 1)
print("直写 1000 次远端命令 =", r.ops)

r2 = FakeRedis()
wc = WriteCoalescer(r2, merge=lambda a, b: a + b)
for _ in range(1000):
    wc.add("stats:pv", "home", 1)
wc.flush()
print("合并后远端命令 =", r2.ops, " 结果一致:", r.hash == r2.hash)
print("可合并的语义才可合并的写: 计数求和 覆盖取后 极值取 max, 不可丢的状态仍要直写")
