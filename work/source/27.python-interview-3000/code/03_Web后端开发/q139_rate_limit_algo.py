import time

class TokenBucket:
    """令牌桶:rate 个/秒,容量 burst 允许突发"""
    def __init__(self, rate: float, burst: int):
        self.rate = rate
        self.burst = burst
        self.tokens = float(burst)
        self.last = time.monotonic()

    def allow(self, cost: int = 1) -> bool:
        now = time.monotonic()
        self.tokens = min(self.burst, self.tokens + (now - self.last) * self.rate)
        self.last = now
        if self.tokens >= cost:
            self.tokens -= cost
            return True
        return False

class FixedWindow:
    """固定窗口:实现简单但有边界突刺"""
    def __init__(self, limit: int, window: float):
        self.limit = limit
        self.window = window
        self.count = 0
        self.start = time.monotonic()

    def allow(self) -> bool:
        now = time.monotonic()
        if now - self.start >= self.window:
            self.count, self.start = 0, now
        self.count += 1
        return self.count <= self.limit

bucket = TokenBucket(rate=5, burst=10)
print(sum(bucket.allow() for _ in range(15)))   # 前 15 次约放行 10+若秒
