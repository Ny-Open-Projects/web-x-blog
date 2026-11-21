---
title: [Q1003] bitmap 签到与活跃统计
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1003 · bitmap 签到与活跃统计

> 难度:★★★☆ | 标签:bitmap, 统计

**问**:连续签到天数、月度活跃用户数,用 bitmap 怎么算?内存账怎么算?

**答**:SETBIT key offset 1 把"第 N 天/第 N 用户"位标记为 1,BITCOUNT 统计总数,BITOP AND/OR 对多个 bitmap 按位运算得到"连续/交集"。连续签到:对月内 bitmap 做"本周 AND 上一周"或按天逐位检查 offset;月活跃:每天一个 bitmap(当天活跃用户 id 为位),BITOP OR 合并月内即活跃用户数。内存账:1 亿用户一个 bitmap 是 1 亿 bit ≈ 12MB,32 天活跃数据 32 张约 384MB——紧凑但位偏移要收敛(用"用户短 id"而非 uuid,或分片)。避免稀疏大位:用户 id 跨度极大时改 RoaringBitmap 或 HyperLogLog(只要基数不要明细)。

```python
# file: code/04_数据库与缓存/q1003_bitmap_signin.py
"""bitmap 签到: SETBIT/BITCOUNT/BITOP 语义模拟"""
class Bitmap:
    def __init__(self):
        self.bits = bytearray()

    def setbit(self, offset, val=1):
        byte, bit = offset // 8, offset % 8
        self.bits.extend(b"\x00" * (byte + 1 - len(self.bits)))
        if val:
            self.bits[byte] |= 1 << bit
        else:
            self.bits[byte] &= ~(1 << bit)

    def getbit(self, offset):
        byte, bit = offset // 8, offset % 8
        if byte >= len(self.bits):
            return 0
        return self.bits[byte] >> bit & 1

    def bitcount(self):
        return sum(bin(b).count("1") for b in self.bits)

    def bitop_and(self, other):
        out = Bitmap()
        n = max(len(self.bits), len(other.bits))
        out.bits = bytearray((self.bits[i] & other.bits[i]) if i < min(len(self.bits), len(other.bits)) else 0
                             for i in range(n))
        return out

if __name__ == "__main__":
    sign = Bitmap()
    for day in (1, 2, 3, 5, 6, 7):               # 11 月签到日-1 为 offset
        sign.setbit(day)
    print("本月签到天数:", sign.bitcount())
    print("第 4 天签了吗:", sign.getbit(4))
    week1 = Bitmap(); [week1.setbit(d) for d in (1, 2, 3)]
    week2 = Bitmap(); [week2.setbit(d) for d in (5, 6)]
    print("与运算(演示交集语义):", week1.bitop_and(week2).bitcount())
    print("1 亿用户活跃统计约 12MB/天, BITOP 注意目标键内存瞬时翻倍")
```

**追问**:
- BITOP 的内存风险?——结果 bitmap 与源同尺寸,OR 32 天数据瞬时再多一份,错峰执行与限制参与运算的 bitmap 数量。
- 怎么算"连续签到最长天数"?——遍历位找最长 1 串 O(月天数),或客户端把 BITFIELD 段取回本地算,数据量大用分段。

---
