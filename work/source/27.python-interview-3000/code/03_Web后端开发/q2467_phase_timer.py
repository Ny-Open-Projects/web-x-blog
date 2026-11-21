"""请求耗时的分段计时器: 阶段占比与慢点定位(纯标准库)。"""
import time
from contextlib import contextmanager


class PhaseTimer:
    """记录命名阶段耗时, 支持嵌套, 报告按耗时降序并给出占比。"""

    def __init__(self):
        self.spans = []                          # (名称, 秒, 层级)

    @contextmanager
    def phase(self, name):
        level = len(getattr(self, "_stack", []))
        if not hasattr(self, "_stack"):
            self._stack = []
        self._stack.append(name)
        t0 = time.perf_counter()
        try:
            yield self
        finally:
            dt = time.perf_counter() - t0
            self._stack.pop()
            self.spans.append((name, dt, level))

    def report(self):
        if not self.spans:
            return [], 0.0
        top_total = sum(d for _, d, lv in self.spans if lv == 0) or 1.0
        rows = sorted(self.spans, key=lambda s: -s[1])
        return [(name, dt, dt / top_total * 100, lv)
                for name, dt, lv in rows], top_total


timer = PhaseTimer()
with timer.phase("total"):
    with timer.phase("auth"):
        time.sleep(0.002)
    with timer.phase("db.query"):
        time.sleep(0.030)
        with timer.phase("db.n+1-loop"):
            time.sleep(0.020)
    with timer.phase("render"):
        time.sleep(0.003)

rows, total = timer.report()
print("总耗时 {:.1f} ms, 各阶段按耗时排序:".format(total * 1000))
for name, dt, pct, level in rows:
    print("  {}{:<14} {:7.1f} ms {:5.1f}%".format("  " * level, name,
                                                  dt * 1000, pct))

assert rows[0][0] == "total" and rows[0][3] == 0, "外层 total 必然最慢"
leaf_rows = [r for r in rows if r[3] == 1]          # total 的直接子阶段
assert leaf_rows[0][0] == "db.query", "total 之外最慢的顶层阶段是 db.query"
assert abs(sum(d for n, d, _, lv in rows if lv == 0) - total) < 1e-6
nested = [r for r in rows if r[3] == 2]
assert nested and nested[0][0] == "db.n+1-loop"
print("要点: 分段计时把一个总耗时拆成 可归因的阶段, "
      "嵌套层级让 db.query 与其内部循环同时可见, 排序后第一名就是优化靶心")
