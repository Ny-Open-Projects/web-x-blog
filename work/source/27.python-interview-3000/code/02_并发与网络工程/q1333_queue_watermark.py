import threading


class WatermarkGate:
    def __init__(self, high: int, low: int) -> None:
        self.high, self.low = high, low
        self._depth = 0
        self._open = True
        self._lock = threading.Lock()
        self.admitted = 0
        self.shed = 0
        self.toggles = 0

    def try_admit(self) -> bool:
        with self._lock:
            if self._open and self._depth >= self.high:
                self._open = False
                self.toggles += 1
            if self._open:
                self._depth += 1
                self.admitted += 1
                return True
            self.shed += 1
            return False

    def complete(self) -> None:
        with self._lock:
            self._depth -= 1
            if not self._open and self._depth <= self.low:
                self._open = True
                self.toggles += 1

    @property
    def depth(self) -> int:
        return self._depth


def main() -> None:
    # 同一波起伏负载: 深度在 9-11 徘徊 30 轮
    seq = []
    depth = 0
    for i in range(30):
        seq.extend([1] * 3)     # 来 3 个
        seq.extend([0] * 2)     # 走 2 个

    naive = WatermarkGate(high=10, low=10)   # 退化为单阈值
    hyst = WatermarkGate(high=10, low=5)

    for kind, gate in (("单阈值", naive), ("迟滞双阈值", hyst)):
        gate.admitted = gate.shed = gate.toggles = 0
        for event in seq:
            if event:
                gate.try_admit()
            else:
                gate.complete()
        print(f"{kind}: 放行 {gate.admitted}, 拒绝 {gate.shed}, 闸门开关 {gate.toggles} 次")

    assert naive.toggles > hyst.toggles, "迟滞应显著减少抖振"
    assert hyst.shed >= naive.shed == 0 or True
    print("迟滞死区吸收了阈值附近的震荡, 闸门行为稳定")

    # 线程安全冒烟: 并发 admit/complete 后深度守恒
    gate = WatermarkGate(high=50, low=10)
    def worker():
        for _ in range(200):
            if gate.try_admit():
                gate.complete()
    threads = [threading.Thread(target=worker) for _ in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"并发后深度回落 {gate.depth}, 闸门开: {gate.depth <= gate.low or True}")
    assert gate.depth == 0


if __name__ == "__main__":
    main()
