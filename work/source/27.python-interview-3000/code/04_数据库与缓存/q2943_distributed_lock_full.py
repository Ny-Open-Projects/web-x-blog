"""分布式锁完整模板: 原子获取 看门狗续期 owner 校验释放"""
import threading
import time
import uuid


class FakeRedis:
    """最小 Redis 模拟: SET NX EX / expire / del-if-owner 全部原子"""

    def __init__(self):
        self._kv, self._exp = {}, {}
        self._mu = threading.Lock()

    def _alive(self, k):
        return k in self._kv and self._exp[k] > time.monotonic()

    def set_nx_ex(self, k, v, ttl):
        with self._mu:
            if self._alive(k):
                return False
            self._kv[k] = v
            self._exp[k] = time.monotonic() + ttl
            return True

    def expire_if_owner(self, k, owner, ttl):
        with self._mu:
            if self._kv.get(k) == owner:
                self._exp[k] = time.monotonic() + ttl
                return True
            return False

    def delete_if_owner(self, k, owner):
        with self._mu:
            if self._kv.get(k) == owner and self._alive(k):
                self._kv.pop(k)
                self._exp.pop(k, None)
                return True
            return False


class DistLock:
    def __init__(self, store, key, ttl=0.4, watchdog=True):
        self.s, self.key, self.ttl = store, key, ttl
        self.token = uuid.uuid4().hex
        self.watchdog = watchdog
        self._stop = threading.Event()

    def acquire(self, wait=0.0):
        deadline = time.monotonic() + wait
        while True:
            if self.s.set_nx_ex(self.key, self.token, self.ttl):
                if self.watchdog:
                    self._start_watchdog()
                return True
            if time.monotonic() >= deadline:
                return False
            time.sleep(0.02)

    def _start_watchdog(self):
        def beat():
            while not self._stop.wait(self.ttl / 3):
                self.s.expire_if_owner(self.key, self.token, self.ttl)
        threading.Thread(target=beat, daemon=True).start()

    def release(self):
        self._stop.set()
        return self.s.delete_if_owner(self.key, self.token)


r = FakeRedis()
la, lb = DistLock(r, "order:77"), DistLock(r, "order:77")
print("A 获得锁:", la.acquire(), "token =", la.token[:8])
print("B 立即抢:", lb.acquire(), "<- 互斥")
print("B 等 0.3s 再抢:", lb.acquire(wait=0.3),
      "<- 看门狗每 %.2fs 续期, 锁一直活着" % (0.4 / 3))
time.sleep(1.0)   # 长任务持锁 1.0s, 远超 TTL 0.4s
print("持锁 1.0s 后外人仍抢不进:", r.set_nx_ex("order:77", "intruder", 0.4) is False)
print("A 释放:", la.release())
print("B 现在能拿到:", lb.acquire(wait=0.5))
fake = DistLock(r, "order:77")
print("冒充他人释放被拒:", fake.release() is False)
print("B 正常释放:", lb.release())
print("B 重复释放:", lb.release(), "<- 幂等, 返回 False")
