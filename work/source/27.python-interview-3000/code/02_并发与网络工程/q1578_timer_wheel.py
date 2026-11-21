"""时间轮: 海量定时器的 O(1) 增删与触发。

堆定时器插入/取消是 O(log n), 时间轮把定时器放进环形槽数组:
- 添加: 按 delay 算出落在哪个槽, O(1);
- 推进: 每 tick 只检查当前槽, 没到期的留着等下一圈(圈数思想)。
适合连接空闲检测、海量短期定时器; 超长延迟靠圈数或层级轮。
"""
import threading
import time


class TimerWheel:
    def __init__(self, slots=8, tick=0.05):
        self.slots = slots
        self.tick = tick
        self.wheel = [[] for _ in range(slots)]   # 每槽: [到期时刻, fn, tag]
        self.current = 0
        self.start = None
        self.lock = threading.Lock()
        self.fired = []

    def add(self, delay, fn, tag):
        with self.lock:
            fire_at = time.monotonic() + delay
            offset = max(1, int(delay / self.tick) + 1)
            slot = (self.current + offset) % self.slots
            self.wheel[slot].append((fire_at, fn, tag))

    def run(self, seconds):
        self.start = time.monotonic()
        end = self.start + seconds
        tick_no = 0
        while True:
            tick_no += 1
            # 绝对时刻推进: sleep 的固定步进会累积漂移, 时间轮必须锚住节拍
            delta = self.start + tick_no * self.tick - time.monotonic()
            if delta > 0:
                time.sleep(delta)
            self.current = (self.current + 1) % self.slots
            now = time.monotonic()
            with self.lock:
                bucket = self.wheel[self.current]
                due = [x for x in bucket if x[0] <= now]
                self.wheel[self.current] = [x for x in bucket if x[0] > now]
            for fire_at, fn, tag in due:
                fn(tag)
                self.fired.append((tag, now - self.start))
            if time.monotonic() >= end:
                break


def main():
    wheel = TimerWheel(slots=8, tick=0.05)
    plan = [("a", 0.05), ("b", 0.10), ("c", 0.15), ("d", 0.30), ("e", 0.45)]
    for tag, delay in plan:
        wheel.add(delay, lambda tag=tag: None, tag)
    wheel.run(seconds=1.0)

    for tag, elapsed in wheel.fired:
        print("触发 %-2s 于 %.3fs" % (tag, elapsed))
    order = [tag for tag, _ in wheel.fired]
    expect = [tag for tag, _ in sorted(plan, key=lambda p: p[1])]
    assert order == expect, "触发顺序应按到期时刻排列"
    for tag, elapsed in wheel.fired:
        target = dict(plan)[tag]
        assert abs(elapsed - target) < 0.15, "触发误差应在一个 tick 量级内"
    print("结论: 时间轮用'槽 + 圈'换来了 O(1) 的增删, 精度受 tick 限制")


if __name__ == "__main__":
    main()
