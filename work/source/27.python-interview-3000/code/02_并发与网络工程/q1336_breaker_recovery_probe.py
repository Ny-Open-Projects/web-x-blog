import threading
import time


class CircuitBreaker:
    CLOSED, OPEN, HALF_OPEN = "CLOSED", "OPEN", "HALF_OPEN"

    def __init__(self, fail_threshold: int = 3, cooldown: float = 0.2,
                 probes_needed: int = 2, max_cooldown: float = 1.0) -> None:
        self._lock = threading.Lock()
        self._state = self.CLOSED
        self._fails = 0
        self._open_until = 0.0
        self._cooldown = cooldown
        self._probes_ok = 0
        self._probes_needed = probes_needed
        self._max_cooldown = max_cooldown
        self.log = []

    def allow(self) -> bool:
        with self._lock:
            now = time.monotonic()
            if self._state == self.CLOSED:
                return True
            if self._state == self.OPEN and now >= self._open_until:
                self._state = self.HALF_OPEN      # 冷却结束: 进探测态
                self._probes_ok = 0
                self.log.append("OPEN -> HALF_OPEN 放行试金石")
                return True
            return False                          # OPEN 冷却期或 HALF_OPEN 探测期

    def record(self, ok: bool) -> None:
        with self._lock:
            if self._state == self.CLOSED:
                if ok:
                    self._fails = 0
                else:
                    self._fails += 1
                    if self._fails >= 3:
                        self._state = self.OPEN
                        self._open_until = time.monotonic() + self._cooldown
                        self.log.append(f"CLOSED -> OPEN 冷却 {self._cooldown:.2f}s")
            elif self._state == self.HALF_OPEN:
                if ok:
                    self._probes_ok += 1
                    if self._probes_ok >= self._probes_needed:
                        self._state = self.CLOSED
                        self._fails = 0
                        self._cooldown = 0.2       # 恢复初始冷却
                        self.log.append("HALF_OPEN -> CLOSED 探测连续成功")
                else:
                    self._cooldown = min(self._cooldown * 2, self._max_cooldown)
                    self._state = self.OPEN
                    self._open_until = time.monotonic() + self._cooldown
                    self.log.append(f"探测失败 -> 重开 OPEN 冷却翻倍为 {self._cooldown:.2f}s")

    @property
    def state(self) -> str:
        return self._state


def main() -> None:
    brk = CircuitBreaker(cooldown=0.2)

    for i in range(3):
        brk.record(False)                  # 依赖连续失败
    print("状态机:", brk.log[-1])
    assert brk.state == "OPEN"
    assert not brk.allow(), "冷却期内请求应被拒"

    time.sleep(0.25)
    assert brk.allow(), "冷却结束应放行试金石"
    brk.record(True)
    assert brk.state == "HALF_OPEN"
    assert not brk.allow(), "探测期内其余请求继续被拒"
    brk.record(True)                       # 第二块试金石成功
    print("状态机轨迹:")
    for line in brk.log:
        print(" ", line)
    assert brk.state == "CLOSED"
    print("恢复探测: 连续试金石成功 -> 闭合, 冷却复位")

    # 探测失败路径: 冷却翻倍
    brk2 = CircuitBreaker(cooldown=0.1, probes_needed=1)
    for _ in range(3):
        brk2.record(False)
    time.sleep(0.15)
    brk2.allow()
    brk2.record(False)                     # 试金石失败
    assert brk2.state == "OPEN"
    print("失败路径:", brk2.log[-1])
    assert "翻倍" in brk2.log[-1]


if __name__ == "__main__":
    main()
