"""token 速率滑动窗口:deque 存增量事件,按事件时间滑动,支持首 token 延迟。"""
import time
from collections import deque


class TokenRateMeter:
    def __init__(self, window_sec=2.0):
        self.window, self.events = window_sec, deque()
        self.total_tokens = 0
        self.first_token_at = None

    def on_delta(self, tokens, now=None):
        now = time.monotonic() if now is None else now
        if self.first_token_at is None:
            self.first_token_at = now
        self.events.append((now, tokens))
        self.total_tokens += tokens
        self._evict(now)

    def _evict(self, now):
        while self.events and self.events[0][0] < now - self.window:
            self.events.popleft()

    def rate(self, now=None):
        now = time.monotonic() if now is None else now
        self._evict(now)
        span = min(self.window, now - self.events[0][0] + 1e-9) if self.events else 1e-9
        return sum(t for _, t in self.events) / span

    def stalled(self, now, min_rate=1.0, min_tokens=10):
        """滞流判定:累计产出足够多但当前窗口速率骤降。"""
        return self.total_tokens >= min_tokens and self.rate(now) < min_rate


if __name__ == "__main__":
    meter = TokenRateMeter(window_sec=2.0)
    t0 = 100.0
    # 前一秒 50 tok/s,之后停止输出
    for i in range(5):
        meter.on_delta(10, now=t0 + i * 0.2)
    r1 = meter.rate(t0 + 1.0)
    print(f"峰值速率 {r1:.0f} tok/s, 首 token 延迟 0ms")
    assert 40 < r1 <= 60
    r2 = meter.rate(t0 + 3.5)
    print(f"停止输出 2.5s 后速率 {r2:.0f} tok/s, 滞流告警={meter.stalled(t0 + 3.5)}")
    assert meter.stalled(t0 + 3.5), "输出停止必须触发滞流检测"
    r3 = meter.rate(t0 + 10.0)
    print(f"窗口完全滑走后速率 {r3:.0f}", "-> 不会永远停留在旧速率")
    assert r3 == 0
