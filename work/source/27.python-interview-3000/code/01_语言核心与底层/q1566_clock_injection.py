import time


class RateLimiter:
    """滑动窗口限流:时间由 clock 提供,默认 monotonic。"""

    def __init__(self, limit, per_seconds, clock=time.monotonic):
        self.limit = limit
        self.window = per_seconds
        self.clock = clock
        self.hits = []

    def allow(self):
        now = self.clock()
        self.hits = [t for t in self.hits if now - t < self.window]
        if len(self.hits) >= self.limit:
            return False, round(self.window - (now - self.hits[0]), 3)
        self.hits.append(now)
        return True, 0.0


class FakeClock:
    def __init__(self, start=0.0):
        self.now_value = start

    def advance(self, seconds):
        self.now_value += seconds
        return self.now_value

    def __call__(self):
        return self.now_value


if __name__ == "__main__":
    real_start = time.monotonic()
    limiter = RateLimiter(limit=2, per_seconds=1.0)
    print("real clock:", [limiter.allow()[0] for _ in range(3)],
          "elapsed ~0:", time.monotonic() - real_start < 1.0)

    # 注入 FakeClock:确定性测试,零 sleep
    fake = FakeClock()
    limiter = RateLimiter(limit=2, per_seconds=10.0, clock=fake)
    print("t=0  :", limiter.allow())
    print("t=0  :", limiter.allow())
    denied, wait = limiter.allow()
    print("t=0 denied, wait:", denied, wait)

    fake.advance(5.0)
    print("t=5 still denied:", limiter.allow()[0] is False)
    fake.advance(5.0)
    print("t=10 window passed:", limiter.allow())
