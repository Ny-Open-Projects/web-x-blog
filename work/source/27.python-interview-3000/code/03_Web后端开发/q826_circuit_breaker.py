import time

class CircuitBreaker:
    def __init__(self, fail_threshold: int = 3, cool: float = 0.2):
        self.fail_threshold = fail_threshold
        self.cool = cool
        self.fails = 0
        self.opened_at = 0.0

    @property
    def state(self) -> str:
        if self.fails < self.fail_threshold:
            return "closed"
        if time.monotonic() - self.opened_at < self.cool:
            return "open"
        return "half-open"

    def call(self, func, *args):
        if self.state == "open":
            raise RuntimeError("熔断中 直接降级")
        try:
            result = func(*args)
            self.fails = 0
            return result
        except Exception:
            self.fails += 1
            if self.fails >= self.fail_threshold:
                self.opened_at = time.monotonic()
            raise

def flaky(ok: bool) -> str:
    if not ok:
        raise ConnectionError("downstream")
    return "data"

cb = CircuitBreaker()
for ok in [False, False, False, False]:
    try:
        cb.call(flaky, ok)
    except Exception as e:
        print(type(e).__name__, cb.state)
time.sleep(0.25)
print("冷却后状态:", cb.state)
