"""内存淘汰实测思路: maxmemory 触发后 LRU 淘汰的观测与复现"""
from collections import OrderedDict

class FakeRedisLRU:
    def __init__(self, maxmemory):
        self.data = OrderedDict()
        self.maxmemory = maxmemory
        self.evicted = 0

    def set(self, key, val, size=10):
        self.data[key] = val
        self.data.move_to_end(key)                # 最近访问移到尾部
        while self._mem() > self.maxmemory:       # 超限后从头部淘汰最久未用
            self.data.popitem(last=False)
            self.evicted += 1

    def _mem(self):
        return len(self.data) * 10                # 每键按 10 单位估

r = FakeRedisLRU(maxmemory=1000)                  # 容量约 100 键
for i in range(1200):
    r.set(f"k:{i}", "v")
print(f"写入 1200 键后: 存活 {len(r.data)}, 淘汰 {r.evicted}")

# 观测手法一: 统计计数
print("真实 redis 看 info stats 的 evicted_keys 持续增长即淘汰在发生")
# 观测手法二: 前后对比探测
probe = ["k:%d" % i for i in range(0, 1200, 100)]
alive = [k for k in probe if k in r.data]
print("抽样探测存活:", alive, "-> 早期 key 已被 LRU 淘汰, 后期 key 保留")

print("实测流程: 灌入已知 key 集 -> 压到 maxmemory -> 观测 evicted_keys 与命中率 ->")
print("  抽样确认哪类 key 被淘汰 -> 对比 allkeys-lru 与 volatile-lru 的行为差异")
print("注意: 真实 redis 是近似 LRU 随机采样, 不是精确 LRU; volatile 策略下无可淘汰键时会直接拒绝写")
