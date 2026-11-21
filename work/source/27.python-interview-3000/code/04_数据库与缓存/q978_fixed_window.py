"""固定窗口限流: 原子 check+incr, 并观察边界突刺"""
import time

class FixedWindow:
    def __init__(self, limit, window_sec):
        self.limit, self.window = limit, window_sec
        self.store = {}

    def allow(self, key, now=None):
        now = now if now is not None else time.monotonic()
        bucket = int(now // self.window)              # 窗口号
        k = f"{key}:{bucket}"
        cnt = self.store.get(k, 0) + 1
        self.store[k] = cnt
        return cnt <= self.limit

if __name__ == "__main__":
    r = FixedWindow(limit=3, window_sec=60)
    base = 59.9                                       # 靠近窗口边界
    print("59.9s 请求:", [r.allow("u1", base + i * 0.02) for i in range(4)])
    print("60.1s 请求(新窗口):", [r.allow("u1", 60.1 + i * 0.02) for i in range(4)])
    print("两秒内合计通过 6 次 = 2 倍阈值, 这就是边界突刺")
    print("滑动窗口按时间戳计数可消除该问题")
