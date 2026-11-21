"""限流测试方法: 突发探测桶容、恢复验证与限流头断言(纯标准库)。"""
import time


class TokenBucket:
    def __init__(self, capacity, rate):
        self.capacity = capacity
        self.rate = rate
        self.tokens = float(capacity)
        self.last = time.monotonic()

    def allow(self):
        now = time.monotonic()
        self.tokens = min(self.capacity, self.tokens + (now - self.last) * self.rate)
        self.last = now
        if self.tokens >= 1:
            self.tokens -= 1
            return True, 0.0
        return False, (1 - self.tokens) / self.rate     # Retry-After 秒数


bucket = TokenBucket(capacity=5, rate=2)                # 桶容 5, 速率 2/s
burst = [bucket.allow() for _ in range(10)]
allowed = sum(1 for ok, _ in burst if ok)
retry_after = max(r for ok, r in burst if not ok)
print("瞬时 10 发: 放行 {} 拒绝 {} (桶容 5), Retry-After≈{:.2f}s".format(
    allowed, 10 - allowed, retry_after))
assert allowed == 5 and retry_after > 0
time.sleep(retry_after + 0.05)
print("按 Retry-After 恢复后再打:", bucket.allow()[0])
print("要点: 限流测试三件事——突发探桶容、按 Retry-After 验恢复、断言限流头; 测试用独立 key 防污染")
