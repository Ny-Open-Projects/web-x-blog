"""zset 滑动窗口限流: 清理 -> 统计 -> 记录 -> 过期兜底"""
import time

class SlidingWindow:
    def __init__(self, limit, window_sec):
        self.limit, self.window = limit, window_sec
        self.zsets = {}                                # key -> [(ts, member)]

    def _zremrange(self, key, now):
        self.zsets[key] = [t for t in self.zsets.get(key, [])
                           if t[0] > now - self.window]

    def allow(self, key, now=None):
        now = now if now is not None else time.monotonic()
        self._zremrange(key, now)                      # 1 清理窗口外
        n = len(self.zsets.get(key, []))               # 2 统计
        if n >= self.limit:
            return False
        member = (now, time.monotonic_ns())            # 3 记录(member 保唯一)
        self.zsets.setdefault(key, []).append(member)
        return True

if __name__ == "__main__":
    sw = SlidingWindow(limit=3, window_sec=2)
    print("连续请求:", [sw.allow("api") for _ in range(4)], "<- 第4次被限")
    time.sleep(2.05)
    print("2 秒后窗口滑出:", sw.allow("api"), "<- 旧记录过期恢复")
