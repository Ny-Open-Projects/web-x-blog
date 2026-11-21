"""滑动日志限流持久化:事件时间戳快照落盘,重启恢复并按新窗口对齐裁剪。"""
import json


class SlidingLogLimiter:
    def __init__(self, limit, window, now=0.0):
        self.limit = limit
        self.window = window
        self.events = []
        self.now = now

    def allow(self, ts):
        self.now = ts
        self.events = [t for t in self.events if ts - t < self.window]
        if len(self.events) >= self.limit:
            return False
        self.events.append(ts)
        return True

    def snapshot(self):
        return json.dumps({"events": self.events})

    @classmethod
    def restore(cls, blob, limit, window, now):
        state = json.loads(blob)
        lim = cls(limit, window, now=now)
        lim.events = [t for t in state["events"] if now - t < window]   # 窗口对齐
        return lim


if __name__ == "__main__":
    lim = SlidingLogLimiter(limit=3, window=10.0)
    assert [lim.allow(t) for t in (1.0, 2.0, 3.0)] == [True, True, True]
    assert lim.allow(4.0) is False, "窗口内第 4 次拒绝"
    blob = lim.snapshot()

    rebooted = SlidingLogLimiter.restore(blob, limit=3, window=10.0, now=100.0)
    assert rebooted.events == [], "远超窗口的旧事件恢复时被裁掉"
    assert [rebooted.allow(t) for t in (100.0, 101.0, 102.0)] == [True, True, True]

    mid = SlidingLogLimiter.restore(lim.snapshot(), limit=3, window=10.0, now=9.0)
    assert mid.events == [1.0, 2.0, 3.0], "窗口内的历史事件完整恢复"
    assert mid.allow(9.0) is False, "恢复后限流语义连续,仍然拒绝"
    assert mid.allow(11.5) is True, "1.0 滑出窗口后放行"
    print("滑动日志持久化通过:快照恢复 窗口对齐裁剪,重启前后限流语义连续")
