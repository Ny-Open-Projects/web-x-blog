import threading
import time
from collections import deque


class SlidingWindowLimiter:
    def __init__(self, max_requests: int, window_seconds: float):
        self.max_requests = max_requests
        self.window = window_seconds
        self.hits: deque[float] = deque()
        self.lock = threading.Lock()

    def allow(self) -> bool:
        now = time.monotonic()
        with self.lock:
            while self.hits and now - self.hits[0] > self.window:
                self.hits.popleft()  # 清理过期记录
            if len(self.hits) < self.max_requests:
                self.hits.append(now)
                return True
            return False


if __name__ == "__main__":
    limiter = SlidingWindowLimiter(max_requests=3, window_seconds=1.0)
    print([limiter.allow() for _ in range(5)])  # T T T F F
