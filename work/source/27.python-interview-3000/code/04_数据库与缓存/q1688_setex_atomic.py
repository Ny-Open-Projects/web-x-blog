"""SETEX 原子性: SET 与 EXPIRE 两步之间的窗口会留下永不过期的孤儿键"""
import time

class FakeRedis:
    def __init__(self, crash_after_set=False):
        self.store, self.expire_at = {}, {}
        self.crash_after_set = crash_after_set

    def set(self, key, value):
        self.store[key] = value
        if self.crash_after_set:
            raise RuntimeError("进程在 SET 之后 EXPIRE 之前崩溃")

    def expire(self, key, ttl):
        self.expire_at[key] = time.time() + ttl

    def setex(self, key, value, ttl):
        self.store[key] = value              # 原子命令: 值与 TTL 同时生效
        self.expire_at[key] = time.time() + ttl

    def get(self, key):
        if key in self.expire_at and time.time() >= self.expire_at[key]:
            self.store.pop(key, None)
            self.expire_at.pop(key, None)
        return self.store.get(key)

# 两步写: 中间崩溃 -> 缓存键永不过期
r1 = FakeRedis(crash_after_set=True)
try:
    r1.set("stock:1", "999")
    r1.expire("stock:1", 60)
except RuntimeError as e:
    print("两步写失败:", e)
print("崩溃后残留:", r1.store, "-> 无 TTL 的孤儿键, 可能永远遮住新值")

# 一步写: SETEX / SET key val EX ttl, 原子生效
r2 = FakeRedis()
r2.setex("stock:1", "999", 60)
print("setex 后:", r2.get("stock:1"), "TTL 已注册, 不存在中间窗口")
print("工程规则: 任何'值加过期'的写入必须一条命令完成; SETEX 与 SET EX 等价, 后者参数更灵活")
print("同理: 分布式锁 SET NX EX 也是同一条命令, 先 SETNX 再 EXPIRE 的老写法都会留死锁键")
