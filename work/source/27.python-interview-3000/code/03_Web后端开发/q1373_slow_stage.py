"""分层计时:把请求耗时拆到各阶段并找最慢一环(纯标准库)。"""
import time


class StageTimer:
    def __init__(self):
        self.spans = {}
        self._start = {}

    def begin(self, name):
        self._start[name] = time.perf_counter()

    def end(self, name):
        self.spans[name] = self.spans.get(name, 0.0) + time.perf_counter() - self._start.pop(name)

    def report(self):
        total = sum(self.spans.values()) or 1e-9
        return [(name, span, span / total)
                for name, span in sorted(self.spans.items(), key=lambda kv: -kv[1])]


timer = StageTimer()
timer.begin("auth")
time.sleep(0.002)
timer.end("auth")
timer.begin("db")
time.sleep(0.030)
timer.end("db")
timer.begin("downstream")
time.sleep(0.006)
timer.end("downstream")

for name, span, ratio in timer.report():
    print(f"{name:12s} {span * 1000:6.1f}ms  {ratio:.0%}")
print("结论:先攻占比最高的阶段,而不是全进程 profile")
