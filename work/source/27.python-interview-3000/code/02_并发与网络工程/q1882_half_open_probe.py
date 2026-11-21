# -*- coding: utf-8 -*-
"""熔断器半开探测的并发实现: HALF_OPEN 只放一个探测, 其余快速失败。

- OPEN 冷却到点不直接 CLOSED, 先进 HALF_OPEN, 只发一张探测通行证;
- 并发请求在同一把锁里抢单飞的 probe 通行证, 抢不到的立刻被拒;
- 探测成功回 CLOSED 清零, 失败回 OPEN 且冷却时间翻倍, 防止反复试探。
"""
import threading
import time


class CircuitOpenError(Exception):
    pass


class CircuitBreaker:
    def __init__(self, failure_threshold=3, cooldown=0.4):
        self.failure_threshold = failure_threshold
        self.cooldown = cooldown
        self._lock = threading.Lock()
        self.state = "CLOSED"
        self.failures = 0
        self.opened_at = 0.0
        self.probe_in_flight = False
        self.probe_runs = 0
        self.rejected = 0

    def call(self, fn):
        with self._lock:
            now = time.monotonic()
            if self.state == "OPEN":
                if now - self.opened_at >= self.cooldown:
                    self.state = "HALF_OPEN"
                    self.probe_in_flight = False
                else:
                    self.rejected += 1
                    raise CircuitOpenError("熔断冷却中, 快速失败")
            if self.state == "HALF_OPEN":
                if self.probe_in_flight:
                    self.rejected += 1
                    raise CircuitOpenError("半开探测进行中, 只放一个")
                self.probe_in_flight = True       # 发出唯一一张探测通行证
                probe = True
            else:
                probe = False
        try:
            result = fn()
        except Exception:
            with self._lock:
                if probe:
                    self.state = "OPEN"
                    self.opened_at = time.monotonic()
                    self.cooldown *= 2            # 探测失败, 冷却翻倍
                    self.probe_in_flight = False
                else:
                    self.failures += 1
                    if self.failures >= self.failure_threshold:
                        self.state = "OPEN"
                        self.opened_at = time.monotonic()
            raise
        else:
            with self._lock:
                if probe:
                    self.state = "CLOSED"         # 探测成功, 闭合清零
                    self.failures = 0
                    self.probe_in_flight = False
                    self.probe_runs += 1
                else:
                    self.failures = 0
            return result


def main():
    cb = CircuitBreaker(failure_threshold=3, cooldown=0.4)

    def fail():
        raise RuntimeError("依赖挂了")

    def ok():
        time.sleep(0.15)                          # 拉长探测窗口, 让并发涌进来
        return "ok"

    # 第一阶段: 连续 3 次失败 -> OPEN
    for _ in range(3):
        try:
            cb.call(fail)
        except RuntimeError:
            pass
    print("三次失败后状态:", cb.state)
    assert cb.state == "OPEN"

    # 第二阶段: 冷却未到, 直接拒绝
    r0 = cb.rejected
    try:
        cb.call(ok)
        raise AssertionError("冷却期内不应放行")
    except CircuitOpenError as e:
        print("冷却期内拒绝:", e)

    # 第三阶段: 冷却到点进 HALF_OPEN, 10 并发只放一个探测
    time.sleep(0.45)
    outcomes = []
    out_lock = threading.Lock()
    r1 = cb.rejected
    start = threading.Event()

    def caller():
        start.wait()
        try:
            result = cb.call(ok)
            with out_lock:
                outcomes.append(("ok", result))
        except CircuitOpenError as e:
            with out_lock:
                outcomes.append(("rejected", str(e)))

    ts = [threading.Thread(target=caller) for _ in range(10)]
    for t in ts:
        t.start()
    time.sleep(0.02)
    start.set()
    for t in ts:
        t.join(timeout=3.0)

    rejected_in_halfopen = cb.rejected - r1
    oks = sum(1 for kind, _ in outcomes if kind == "ok")
    print("半开阶段: 探测执行 %d 次, 放行成功 %d, 并发拒绝 %d, 状态 %s"
          % (cb.probe_runs, oks, rejected_in_halfopen, cb.state))
    assert cb.probe_runs == 1, "半开只放一个探测"
    assert rejected_in_halfopen >= 6, "其余并发应被快速拒绝"
    assert cb.state == "CLOSED", "探测成功应闭合"

    # 第四阶段: 再次打开, 半开探测失败 -> 冷却翻倍
    cooldown_before = cb.cooldown
    for _ in range(3):
        try:
            cb.call(fail)
        except RuntimeError:
            pass
    time.sleep(0.45)
    try:
        cb.call(fail)
    except RuntimeError:
        pass
    print("探测失败后冷却翻倍: %.2fs -> %.2fs, 状态 %s"
          % (cooldown_before, cb.cooldown, cb.state))
    assert cb.cooldown == cooldown_before * 2, "探测失败冷却必须翻倍"
    assert cb.state == "OPEN"

    print("结论: 半开的灵魂是单飞探测, 通行证一张, 其余人立刻请回")


if __name__ == "__main__":
    main()
