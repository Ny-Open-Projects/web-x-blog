"""迷你 HyperLogLog: 桶分摊 + 前导零 + 调和平均"""
import hashlib
import math

class MiniHLL:
    def __init__(self, m=1024):
        self.m = m
        self.reg = [0] * m

    def _hash(self, item):
        h = hashlib.sha1(str(item).encode()).digest()
        v = int.from_bytes(h[:8], "big")
        idx = v & (self.m - 1)                    # 低 10 位选桶
        rest = v >> 10
        rho = (rest.bit_length() and (64 - rest.bit_length()) + 1) or 64
        return idx, rho

    def add(self, item):
        idx, rho = self._hash(item)
        self.reg[idx] = max(self.reg[idx], rho)

    def count(self):
        alpha = 0.7213 / (1 + 1.079 / self.m)
        raw = alpha * self.m ** 2 / sum(2.0 ** -r for r in self.reg)
        zeros = self.reg.count(0)
        if raw <= 2.5 * self.m and zeros:          # 小基数线性计数校正
            raw = self.m * math.log(self.m / zeros)
        return int(raw)

if __name__ == "__main__":
    hll = MiniHLL()
    for i in range(50000):                          # 含大量重复
        hll.add(f"user{i % 30000}")
    print(f"估计基数: {hll.count()}, 真实: 30000, "
          f"误差: {abs(hll.count() - 30000) / 30000:.1%}")
    print("Redis: 16384 桶 12KB, 误差约 0.81%, 内存与基数无关")
