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
