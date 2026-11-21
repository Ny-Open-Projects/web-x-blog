import time


class CircuitBreaker:
    def __init__(self, fail_threshold: int = 3, cooldown: float = 1.0):
        self.fail_threshold = fail_threshold
        self.cooldown = cooldown
        self.state = "CLOSED"
        self.failures = 0
        self.opened_at = 0.0

    def allow(self) -> bool:
        if self.state == "OPEN":
            if time.monotonic() - self.opened_at >= self.cooldown:
                self.state = "HALF_OPEN"  # 冷却结束,放探测请求
                return True
            return False
        return True

    def record_success(self) -> None:
        self.failures = 0
        self.state = "CLOSED"

    def record_failure(self) -> None:
        if self.state == "HALF_OPEN":
            self.state = "OPEN"      # 探测失败,再次熔断
            self.opened_at = time.monotonic()
            return
        self.failures += 1
        if self.failures >= self.fail_threshold:
            self.state = "OPEN"
            self.opened_at = time.monotonic()


def call_with_breaker(breaker: CircuitBreaker, fn, *args):
    if not breaker.allow():
        return "degraded"  # 降级响应
    try:
        res = fn(*args)
        breaker.record_success()
        return res
    except Exception:
        breaker.record_failure()
        return "degraded"


def bad_downstream():
    raise ConnectionError("downstream down")


if __name__ == "__main__":
    br = CircuitBreaker(fail_threshold=2, cooldown=0.2)
    for _ in range(3):
        print(call_with_breaker(br, bad_downstream))
    print(br.state)  # OPEN
    time.sleep(0.3)
    print(call_with_breaker(br, lambda: "ok"))  # HALF_OPEN 探测成功
    print(br.state)  # CLOSED
