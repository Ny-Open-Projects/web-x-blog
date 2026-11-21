import time

class TokenBucket:
    def __init__(self, capacity: int, refill_per_sec: float):
        self.capacity = capacity
        self.rate = refill_per_sec
        self.tokens = float(capacity)
        self.last = time.monotonic()

    def allow(self, n: int = 1) -> bool:
        now = time.monotonic()
        self.tokens = min(self.capacity, self.tokens + (now - self.last) * self.rate)
        self.last = now
        if self.tokens >= n:
            self.tokens -= n
            return True
        return False

bucket = TokenBucket(capacity=5, refill_per_sec=2)
print("连发 8 个:", [bucket.allow() for _ in range(8)])
time.sleep(0.6)                                # 补充约 1.2 个令牌
print("等待后两连发:", [bucket.allow() for _ in range(2)])
