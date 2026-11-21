import time
from collections import deque


class SlidingWindowQuota:
    def __init__(self, limit: int, window: float = 1.0) -> None:
        self.limit = limit
        self.window = window
        self._hits: dict = {}

    def take(self, tenant: str) -> tuple:
        now = time.monotonic()
        dq = self._hits.setdefault(tenant, deque())
        while dq and dq[0] <= now - self.window:  # 淘汰出窗时间戳
            dq.popleft()
        if len(dq) < self.limit:
            dq.append(now)
            remaining = self.limit - len(dq)
            return True, {"remaining": remaining, "reset_in": 0.0}
        reset_in = self.window - (now - dq[0])  # 最早一条出窗即恢复
        return False, {"remaining": 0, "reset_in": round(reset_in, 2)}


if __name__ == "__main__":
    quotas = {"free": SlidingWindowQuota(limit=3, window=1.0),
              "pro": SlidingWindowQuota(limit=10, window=1.0)}

    print("free 租户连发 5 个请求 (配额 3/min):")
    for i in range(5):
        ok, meta = quotas["free"].take("free")
        status = "200" if ok else "429"
        extra = "" if ok else f" reset_in={meta['reset_in']}s"
        print(f"  req{i}: {status} remaining={meta['remaining']}{extra}")

    print("\npro 租户连发 5 个请求 (配额 10/min):")
    for i in range(5):
        ok, meta = quotas["pro"].take("pro")
        print(f"  req{i}: {'200' if ok else '429'} remaining={meta['remaining']}")

    print("\n等待窗口滑过...")
    time.sleep(1.05)
    ok, meta = quotas["free"].take("free")
    print("free 恢复后:", "200" if ok else "429", "remaining =", meta["remaining"])
    assert ok
    print("要点: 时间戳队列实现真滑动窗口, reset_in 让客户端可预期")
