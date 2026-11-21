import random
import time


class CircuitBreaker:
    def __init__(self, failure_threshold: int = 3, cooldown: float = 0.5,
                 max_cooldown: float = 2.0) -> None:
        self.state = "CLOSED"
        self.failures = 0
        self.cooldown = cooldown
        self.base_cooldown = cooldown
        self.max_cooldown = max_cooldown
        self.open_until = 0.0
        self.failure_threshold = failure_threshold
        self.transitions: list = []

    def _to(self, new_state: str) -> None:
        if new_state != self.state:
            self.transitions.append((time.monotonic(), self.state, new_state))
            self.state = new_state

    def allow(self) -> bool:
        now = time.monotonic()
        if self.state == "OPEN":
            if now < self.open_until:
                return False
            self._to("HALF_OPEN")  # 冷却到期, 放探测请求
        return True

    def on_success(self) -> None:
        if self.state == "HALF_OPEN":
            self.failures = 0
            self.cooldown = self.base_cooldown  # 恢复后重置冷却
            self._to("CLOSED")
        self.failures = 0

    def on_failure(self) -> None:
        self.failures += 1
        if self.state == "HALF_OPEN" or self.failures >= self.failure_threshold:
            self._to("OPEN")
            self.open_until = time.monotonic() + self.cooldown
            self.cooldown = min(self.cooldown * 2, self.max_cooldown)
            print(f"[breaker] 熔断打开, 冷却 {self.cooldown:.2f}s")


def call_dependency(breaker: CircuitBreaker, healthy_after: float, t0: float) -> str:
    if not breaker.allow():
        return "CIRCUIT-OPEN 快速失败 → 走降级缓存"
    if time.monotonic() - t0 < healthy_after:
        breaker.on_failure()
        return "依赖超时"
    breaker.on_success()
    return "依赖正常响应"


if __name__ == "__main__":
    random.seed(1)
    breaker = CircuitBreaker(failure_threshold=3, cooldown=0.3)
    t0 = time.monotonic()
    healthy_after = 1.2  # 依赖 1.2s 后恢复

    for i in range(24):
        result = call_dependency(breaker, healthy_after, t0)
        print(f"t={time.monotonic() - t0:5.2f}s [{breaker.state:>9}] {result}")
        time.sleep(0.1)

    print("\n状态迁移记录:")
    for ts, old, new in breaker.transitions:
        print(f"  t={ts - t0:.2f}s  {old} → {new}")
    assert breaker.state == "CLOSED", "依赖恢复后熔断应关闭"
