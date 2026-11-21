"""客户端慢调用熔断: 按慢比率跳闸而非仅按失败率(纯标准库)。"""
from collections import deque


class SlowCallBreaker:
    """滑动窗口统计慢调用比率; 慢比率超阈值即熔断, 不必等到彻底失败。

    熔断后拒绝一切调用; 冷却期到只放行一张探测通行证, 探测成功才恢复。
    """

    def __init__(self, slow_threshold=0.5, min_calls=4, slow_rate=0.5):
        self.slow_threshold = slow_threshold
        self.min_calls = min_calls
        self.slow_rate = slow_rate
        self.window = deque(maxlen=8)       # (duration, is_slow)
        self.opened = False
        self.probe_used = False

    def record(self, duration):
        self.window.append((duration, duration > self.slow_threshold))
        if len(self.window) < self.min_calls:
            return
        slow_count = sum(1 for _, s in self.window if s)
        if slow_count / float(len(self.window)) >= self.slow_rate:
            self.opened = True
            self.window.clear()

    def allow(self):
        return not self.opened

    def allow_probe(self):
        """熔断期单张探测通行证: 同一时刻只放一个请求去试探上游。"""
        if self.opened and not self.probe_used:
            self.probe_used = True
            return True
        return False

    def on_probe_result(self, duration):
        """探测结果决定去留: 仍慢继续熔断, 恢复则清窗重来。"""
        self.opened = duration > self.slow_threshold
        self.probe_used = False
        if not self.opened:
            self.window.clear()
        return not self.opened


breaker = SlowCallBreaker(slow_threshold=0.5, min_calls=4, slow_rate=0.5)
durations = [0.1, 0.6, 0.1, 0.7, 0.2, 0.8]      # 一半以上是慢调用
for d in durations:
    breaker.record(d)
print("跳闸前窗口:", [(round(d, 1), s) for d, s in breaker.window])
print("熔断后 allow:", breaker.allow())
assert not breaker.allow()
p1 = breaker.allow_probe()
p2 = breaker.allow_probe()
print("探测通行证: 第一张", p1, "第二张", p2)
assert p1 and not p2
print("探测到上游恢复 0.1s:", breaker.on_probe_result(0.1))
assert breaker.allow()
breaker.record(0.8)
breaker.record(0.9)
print("恢复后记录两条慢调用(未满 min_calls):", breaker.allow())
assert breaker.allow()
print("要点: 失败率看不出缓慢劣化, 慢比率才是上游雪崩的先行指标; 熔断期只发单张探测通行证")
