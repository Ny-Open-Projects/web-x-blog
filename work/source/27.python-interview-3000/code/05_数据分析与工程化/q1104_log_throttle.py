import collections
import time

class LogThrottle:
    def __init__(self, window=60, max_per_window=3):
        self.window = window
        self.max = max_per_window
        self.recent = collections.defaultdict(collections.deque)
        self.suppressed = collections.Counter()

    def allow(self, key):
        now = time.monotonic()
        dq = self.recent[key]
        while dq and now - dq[0] > self.window:
            dq.popleft()
        if len(dq) < self.max:
            dq.append(now)
            return True
        self.suppressed[key] += 1
        return False

if __name__ == "__main__":
    throttle = LogThrottle(window=60, max_per_window=2)
    for i in range(10):
        if throttle.allow("user42:timeout"):
            print(f"记录第 {i + 1} 条超时日志")
    print("窗口内被抑制:", dict(throttle.suppressed), "条,周期性汇总打出")
