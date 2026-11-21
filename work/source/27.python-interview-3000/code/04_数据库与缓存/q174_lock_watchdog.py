"""看门狗续期: 后台线程定期延长 TTL, 任务结束后停止"""
import threading
import time


class FakeRedis:
    """最小 SET GET PEXPIRE 语义"""

    def __init__(self):
        self.store: dict = {}
        self.expire_at: dict = {}

    def set(self, key, value, px: int) -> bool:
        self.store[key] = value
        self.expire_at[key] = time.time() + px / 1000
        return True

    def extend(self, key, value, px: int) -> bool:
        if self.store.get(key) == value:            # 只有持有者能续期
            self.expire_at[key] = time.time() + px / 1000
            return True
        return False

    def alive(self, key) -> bool:
        return key in self.store and time.time() < self.expire_at[key]


class WatchdogLock:
    def __init__(self, client: FakeRedis, key: str, ttl_ms: int = 300):
        self.client, self.key, self.ttl_ms = client, key, ttl_ms
        self.token = "owner-1"
        self._stop = threading.Event()

    def acquire(self) -> bool:
        ok = self.client.set(self.key, self.token, px=self.ttl_ms)
        if ok:
            threading.Thread(target=self._renew, daemon=True).start()
        return ok

    def _renew(self):
        while not self._stop.wait(self.ttl_ms / 3000):   # 每 TTL/3 续一次
            if not self.client.extend(self.key, self.token, self.ttl_ms):
                return                                    # 锁已易主, 停止续期

    def release(self):
        self._stop.set()
        self.client.store.pop(self.key, None)


if __name__ == "__main__":
    c = FakeRedis()
    lock = WatchdogLock(c, "job:1")
    lock.acquire()
    time.sleep(0.5)                       # 远超过 0.3s 的 TTL
    print("0.5s 后锁仍然存活(看门狗续期):", c.alive("job:1"))
    lock.release()
    print("释放后:", c.alive("job:1"))
