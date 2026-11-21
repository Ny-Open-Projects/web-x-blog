import collections
import time


class LeakyBucketPacer:
    def __init__(self, rate_per_s: float, capacity: int,
                 clock=time.monotonic, sleep=time.sleep) -> None:
        self._interval = 1.0 / rate_per_s
        self._cap = capacity
        self._queue = collections.deque()
        self._next_out = None                 # 下一滴流出的计划时刻, 首滴时锚定
        self.rejected = 0
        self._clock = clock                   # 时钟可注入: 演示用虚拟时钟做确定性验证
        self._sleep = sleep

    def submit(self, item) -> bool:
        if len(self._queue) >= self._cap:
            self.rejected += 1                # 桶满: 立刻拒绝, 不替上游扛
            return False
        self._queue.append(item)
        return True

    def drain(self):
        """按恒定间隔逐滴流出, 节奏锚定在第一滴。"""
        while self._queue:
            if self._next_out is None:
                self._next_out = self._clock()
            now = self._clock()
            if now < self._next_out:
                self._sleep(self._next_out - now)
            self._next_out = max(self._clock(), self._next_out) + self._interval
            yield self._queue.popleft()


class FakeClock:
    """虚拟时钟: sleep 不真睡而是直接推进虚拟时间, 供确定性断言使用。"""

    def __init__(self) -> None:
        self.now = 0.0

    def monotonic(self) -> float:
        return self.now

    def sleep(self, dt: float) -> None:
        self.now += dt


def main() -> None:
    clk = FakeClock()
    pacer = LeakyBucketPacer(rate_per_s=200, capacity=8,
                             clock=clk.monotonic, sleep=clk.sleep)  # 每滴 5ms
    admitted = [i for i in range(20) if pacer.submit(i)]
    print(f"瞬时涌入 20 个, 桶容量 8 -> 接纳 {len(admitted)}, 溢出拒绝 {pacer.rejected}")
    assert len(admitted) == 8 and pacer.rejected == 12

    out_times = []
    for item in pacer.drain():
        out_times.append(clk.monotonic())
    gaps = [b - a for a, b in zip(out_times, out_times[1:])]
    print(f"流出 {len(out_times)} 滴, 虚拟时钟间隔 "
          f"{[round(g * 1000, 2) for g in gaps]}ms 目标 5.0ms")
    # 断言采用确定性设计: 真实 sleep 的唤醒抖动会让间隔天然波动,
    # 改为注入虚拟时钟, 逐滴验证调度节奏恒等于 5ms, 与机器快慢无关
    assert all(abs(g - 0.005) < 1e-9 for g in gaps), "出口间隔必须恒定不塌缩"
    assert len(out_times) == 8
    print("令牌桶: 攒下的令牌允许一波 burst; 漏桶: 再大的 burst 出口也是 5ms/滴")


if __name__ == "__main__":
    main()
