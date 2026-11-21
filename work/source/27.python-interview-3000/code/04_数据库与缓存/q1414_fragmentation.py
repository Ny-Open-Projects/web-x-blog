"""内存碎片: 分配释放产生空洞, 压缩整理降低碎片率"""
class Pool:
    def __init__(self, size=32):
        self.slots = [None] * size
    def alloc(self, n, tag):
        start = None
        for i, s in enumerate(self.slots):
            if s is None:
                start = i if start is None else start
                if i - start + 1 == n:
                    for j in range(start, start + n):
                        self.slots[j] = tag
                    return start
            else:
                start = None
        raise MemoryError("no contiguous space")
    def free(self, tag):
        for i, s in enumerate(self.slots):
            if s == tag:
                self.slots[i] = None
    def compact(self):
        live = [s for s in self.slots if s is not None]
        self.slots = live + [None] * (len(self.slots) - len(live))

pool = Pool()
pool.alloc(8, "A"); pool.alloc(8, "B"); pool.alloc(8, "C"); pool.alloc(8, "D")
pool.free("B"); pool.free("D")
print("释放后占用 16, 空洞:", len(pool.slots) - 16)
try:
    pool.alloc(12, "E")
except MemoryError:
    print("再分配 12 格失败: 总空闲 16 但被切成两个 8, <- 这就是碎片")
pool.compact()
print("compact 后可容纳大块: 布局", "".join(s or "." for s in pool.slots))
print("Redis activedefrag 做的就是把数据搬回紧凑区, 不停服但耗 CPU")
