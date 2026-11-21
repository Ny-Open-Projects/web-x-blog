"""令牌桶限速器,线程安全。"""
import threading
import time


class TokenBucket:
    def __init__(self, rate: float, capacity: int):
        self.rate = rate          # 每秒生成令牌数
        self.capacity = capacity  # 桶容量,允许的最大突发
        self.tokens = capacity
        self.last = time.monotonic()
        self.lock = threading.Lock()

    def acquire(self, n: int = 1) -> bool:
        with self.lock:
            now = time.monotonic()
            self.tokens = min(self.capacity, self.tokens + (now - self.last) * self.rate)
            self.last = now
            if self.tokens >= n:
                self.tokens -= n
                return True
            return False

    def wait(self, n: int = 1):
        while not self.acquire(n):
            time.sleep(1 / self.rate)  # 简单退避,可精确计算等待时间


if __name__ == "__main__":
    bucket = TokenBucket(rate=5, capacity=2)  # 平均 5 QPS,瞬时最多 2
    start = time.monotonic()
    for i in range(5):
        bucket.wait()
        print(f"第 {i} 次请求, 距开始 {time.monotonic() - start:.2f}s")
