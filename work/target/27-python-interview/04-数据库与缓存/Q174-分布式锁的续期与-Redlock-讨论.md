---
title: [Q174] 分布式锁的续期与 Redlock 讨论
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q174 · 分布式锁的续期与 Redlock 讨论

> 难度:★★★★ | 标签:Redis, 分布式锁

**问**:持锁任务执行时间不可控怎么办?了解 Redlock 吗,有什么争议?

**答**:用看门狗:后台线程定期(如 TTL/3)用 Lua 检查 value 后延长 PX,任务结束停止续期。Redlock 是向 N 个独立 Redis 实例依次加锁、多数成功且耗时小于 TTL 才算获得,旨在应对单实例故障时的锁安全性;争议在于 Martin Kleppmann 指出依赖时钟与进程暂停不可靠,关键业务建议用 fencing token(递增令牌)或改用 ZooKeeper/etcd 这类共识系统。

```python
# file: code/04_数据库与缓存/q174_lock_watchdog.py
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
```

**追问**:
- fencing token 怎么工作?——锁服务发放单调递增令牌,存储端拒绝旧令牌写入,即使锁失效旧持有者也无法破坏数据。
- 看门狗线程挂了会怎样?——锁到期自动释放,业务侧必须有幂等与重试兜底,锁只做效率优化时才可接受。

---
