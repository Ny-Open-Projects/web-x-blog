import threading
import time


class TokenBucket:
    def __init__(self, rate: float, capacity: int):
        self.rate = rate              # 每秒补充令牌数
        self.capacity = capacity      # 桶容量,决定突发上限
        self.tokens = float(capacity)
        self.last = time.monotonic()
        self.lock = threading.Lock()

    def allow(self, n: int = 1) -> bool:
        with self.lock:
            now = time.monotonic()
            self.tokens = min(self.capacity,
                              self.tokens + (now - self.last) * self.rate)
            self.last = now
            if self.tokens >= n:
                self.tokens -= n
                return True
            return False


if __name__ == "__main__":
    bucket = TokenBucket(rate=5, capacity=5)
    ok = [bucket.allow() for _ in range(10)]
    print(ok)               # 前 5 个 True,后 5 个 False
    time.sleep(0.5)
    print(bucket.allow())   # 又有令牌
