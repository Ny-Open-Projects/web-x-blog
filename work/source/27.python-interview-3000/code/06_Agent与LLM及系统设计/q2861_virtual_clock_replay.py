"""Q2861 回放测试的虚拟时钟:等待被记账 墙钟几乎不走。

重放一次带退避的失败流程,真实 sleep 会把测试拖到几分钟。注入虚拟
时钟:睡眠只是记账加指针,事件序列与真实时序完全一致,回放瞬间
完成,断言还能精确验到「退避总共等了几秒」。
"""

import time


class VirtualClock:
    def __init__(self):
        self._now = 0.0
        self.events = []

    def sleep(self, seconds):
        self._now += seconds
        self.events.append(("sleep", seconds))

    @property
    def now(self):
        return self._now


def retry_workflow(clock, fails_before_success, backoffs=(2, 4, 8)):
    """带指数退避的重试流程:每次失败后按档位等待。"""
    for attempt, delay in enumerate(backoffs, start=1):
        clock.events.append(("attempt", attempt))
        if attempt > fails_before_success:
            return "ok", attempt
        if delay:
            clock.sleep(delay)
    return "gave_up", len(backoffs)


def main():
    clock = VirtualClock()
    t0 = time.monotonic()
    status, attempts = retry_workflow(clock, fails_before_success=2)
    wall = time.monotonic() - t0
    assert status == "ok" and attempts == 3, (status, attempts)
    assert clock.events == [
        ("attempt", 1), ("sleep", 2),
        ("attempt", 2), ("sleep", 4),
        ("attempt", 3),
    ], clock.events
    assert clock.now == 6.0, clock.now   # 虚拟时间精确记账
    assert wall < 0.5, wall              # 真实墙钟几乎没走
    # 档位用尽仍失败:明确给 up,不无限重试
    clock2 = VirtualClock()
    status2, _ = retry_workflow(clock2, fails_before_success=99)
    assert status2 == "gave_up" and clock2.now == 14.0, (status2, clock2.now)
    print("事件序列:", clock.events)
    print("虚拟耗时 %.1fs 真实耗时 %.4fs" % (clock.now, wall))
    print("重试失败场景:", status2, "虚拟等待", clock2.now, "s")


if __name__ == "__main__":
    main()
