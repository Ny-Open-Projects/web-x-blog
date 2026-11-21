import time

class Clock:
    def now(self) -> float:
        return time.time()

class FakeClock(Clock):
    def __init__(self, fixed):
        self.fixed = fixed

    def now(self) -> float:
        return self.fixed

class RateLimiter:
    def __init__(self, clock: Clock, limit=2, window=1.0):
        self.clock = clock
        self.limit = limit
        self.window = window
        self.hits = []

    def allow(self) -> bool:
        now = self.clock.now()
        self.hits = [h for h in self.hits if now - h < self.window]
        if len(self.hits) >= self.limit:
            return False
        self.hits.append(now)
        return True

if __name__ == "__main__":
    rl = RateLimiter(Clock())
    print("real clock:", [rl.allow() for _ in range(3)])

    fake = RateLimiter(FakeClock(1000.0))
    print("fake clock:", [fake.allow() for _ in range(3)])
    fake2 = RateLimiter(FakeClock(1000.0 + 5))    # 时间前进:窗口滑过
    print("after window:", [fake2.allow() for _ in range(3)])
