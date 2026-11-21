---
title: [Q1004] HyperLogLog: 0.81% 误差数千万 UV
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1004 · HyperLogLog: 0.81% 误差数千万 UV

> 难度:★★★★ | 标签:HyperLogLog, 基数统计

**问**:PFADD/PFCOUNT 为什么能用 12KB 估计上亿基数?误差怎么来的?

**答**:HLL 思想:对每个元素哈希,记录哈希值的"前导零个数"——基数越大,出现"很多前导零"的概率越大。Redis 用 16384 个寄存器(桶)分摊,每桶 6 bit,按哈希低 14 位选桶、剩余位算前导零,取每桶最大值,经调和平均与偏置校正估计基数。固定内存约 12KB(16384×6bit),标准误差 1.04/sqrt(16384) ≈ 0.81%。适合 UV、独立 IP 这类"要数量不要明细"的统计;不能取明细、不能精确去重,需要精确就用 set/bitmap。PFCOUNT 读多会缓存,PFCOUNT 多键合并是实时计算,合并大 HLL 有成本。

```python
# file: code/04_数据库与缓存/q1004_hyperloglog.py
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
```

**追问**:
- HLL 能合并吗?——能,PFMERGE 逐桶取 max 合并,是线性可合并(sketch)结构,适合分天统计再合并月 UV。
- 为什么前导零能代表基数?——哈希均匀时出现 r 个前导零的概率约 2^-r,观察到"前导零最多为 r"意味着基数大概率在 2^r 量级,多桶调和平均降低方差。

---
