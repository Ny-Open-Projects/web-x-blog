"""手写布隆过滤器: 双哈希映射 + 误判率观察"""
import hashlib
import math

class BloomFilter:
    def __init__(self, m_bits, k):
        self.m, self.k = m_bits, k
        self.bits = bytearray((m_bits + 7) // 8)

    def _idx(self, item, salt):
        h = hashlib.sha1(f"{salt}:{item}".encode()).digest()
        return int.from_bytes(h[:8], "big") % self.m

    def _set(self, i):
        self.bits[i // 8] |= 1 << (i % 8)

    def _get(self, i):
        return self.bits[i // 8] >> (i % 8) & 1

    def add(self, item):
        for salt in range(self.k):
            self._set(self._idx(item, salt))

    def contains(self, item):
        return all(self._get(self._idx(item, s)) for s in range(self.k))

if __name__ == "__main__":
    bf = BloomFilter(m_bits=1 << 20, k=3)     # 1M bit, 3 个哈希
    for i in range(10000):
        bf.add(f"user:{i}")

    fp = sum(1 for i in range(10000, 20000) if bf.contains(f"user:{i}"))
    print("已收录查询全部命中:", all(bf.contains(f"user:{i}") for i in range(100)))
    print(f"误判: 10000 个陌生 key 中 {fp} 个误判, 实际 {fp / 10000:.2%}")
    theory = (1 - math.exp(-3 * 10000 / (1 << 20))) ** 3
    print(f"理论误判率约 {theory:.2%}")
