"""可重入锁: hash 计数 + owner 校验 + TTL, 纯标准库模拟"""
import time
import uuid

class FakeRedis:
    def __init__(self):
        self.h = {}
        self.ttl = {}

    def lock_lua(self, key, owner, ttl):
        rec = self.h.get(key)
        if rec is None or rec["owner"] == owner:
            cnt = rec["count"] + 1 if rec else 1
            self.h[key] = {"owner": owner, "count": cnt}
            self.ttl[key] = time.monotonic() + ttl
            return 1
        return 0

    def unlock_lua(self, key, owner):
        rec = self.h.get(key)
        if rec and rec["owner"] == owner:
            rec["count"] -= 1
            if rec["count"] == 0:
                del self.h[key], self.ttl[key]
            return 1
        return 0

    def expired(self, key):
        return key in self.ttl and time.monotonic() > self.ttl[key]

class ReentrantLock:
    def __init__(self, r, key, ttl=2.0):
        self.r, self.key, self.ttl = r, key, ttl
        self.owner = uuid.uuid4().hex

    def acquire(self):
        return self.r.lock_lua(self.key, self.owner, self.ttl) == 1

    def release(self):
        return self.r.unlock_lua(self.key, self.owner) == 1

if __name__ == "__main__":
    r = FakeRedis()
    lock = ReentrantLock(r, "order:1")
    print("第一次加锁:", lock.acquire())
    print("同 owner 重入:", lock.acquire(), "<- count=2")
    other = ReentrantLock(r, "order:1")
    print("他人加锁被拒:", other.acquire() == 0)
    print("释放一层:", lock.release(), "仍持有:", lock.r.h.get("order:1"))
    print("再释放:", lock.release(), "锁已删除:", "order:1" not in r.h)
