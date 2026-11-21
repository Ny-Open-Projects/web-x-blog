"""INCR 限流漂移: 固定窗口在边界处的双倍突刺复现"""

class FakeRedis:
    def __init__(self):
        self.kv = {}

    def incr(self, key):
        self.kv[key] = self.kv.get(key, 0) + 1
        return self.kv[key]

LIMIT = 5
WINDOW = 1.0                                     # 秒

def fixed_window(r, key, now):
    window_id = int(now // WINDOW)               # 窗口按整秒切
    k = f"rate:{key}:{window_id}"
    n = r.incr(k)
    return n <= LIMIT, n

r = FakeRedis()
t0 = 1000.0
print("窗口 1000 末尾连续 5 次:", [fixed_window(r, "u1", t0 + 0.99)[0] for _ in range(LIMIT)])
burst = [fixed_window(r, "u1", t0 + 1.01)[0] for _ in range(LIMIT)]
print("窗口 1001 开头 1ms 内又放行 5 次:", burst)
print("两个窗口交界约 20ms 内实际放行 10 次: 突刺是固定窗口的结构性问题, 不是参数没调好")
print("修法: 滑动窗口 zset 时间戳 或 令牌桶把计数连续化;")
print("      若保留固定窗口, 把 LIMIT 乘上窗口重叠修正系数, 并接受边界突刺")
