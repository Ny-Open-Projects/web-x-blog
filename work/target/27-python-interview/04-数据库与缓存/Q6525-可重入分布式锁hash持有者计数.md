---
title: [Q6525] 可重入分布式锁的实现
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6525 · 可重入分布式锁：同一个调用链里二次加锁为什么死锁？怎么用 hash 实现？

> 难度:★★★★ | 标签:Redis, 分布式锁, 并发

**问**：Python 里 `threading.RLock` 可以重入，为什么 `SET NX EX` 实现的分布式锁不能重入？递归调用链上第二次加锁就卡死，怎么改造？

**答**：结论：`SET key value NX` 语义是"存在即失败"，同一持有者第二次加锁会被自己的锁挡住。可重入的实现把锁从 string 换成 hash：`field=持有者标识（实例ID+线程ID）`、`value=重入计数`，加锁时 hash 不存在则原子建锁，存在且 field 匹配则 HINCRBY +1 并刷新 TTL；解锁时 -1，减到 0 才真正 DEL。整个判断+修改必须放进 Lua 脚本保证原子，否则"检查 field 与自增"之间会有竞态。

取舍与实战：
- 持有者标识必须**全局唯一且线程感知**：用 `uuid 实例 + threading.get_ident()`，纯 uuid 会让同实例两个线程互相重入；纯线程 id 跨实例会碰撞。
- TTL 刷新策略：重入时顺带 PEXPIRE 续期，但续期基准是"整段持锁时间"还是"单次调用"要定清楚；长链路重入层数深时建议配合看门狗续期，防止深层调用耗时把 TTL 耗光。
- 代价：hash + Lua 比 `SET NX` 复杂，脚本多一次网络往返；不是所有场景值得——**重入通常是设计坏味道**（锁粒度含糊），能重构出"外层持锁、内层只传数据"的调用链就别用可重入锁。RLock 语义在分布式下还有个坑：A 释放到 0 的瞬间锁被 B 抢走，A 的旧 TTL 清理逻辑不能误删 B 的锁——Lua 里必须先比 field 再删。

```python
# 基线:Python 3.9+ / redis-py 4.x / Redis 2.6+(Lua) ;缺库降级:dict 模拟
import threading
import uuid

try:
    import redis
    HAS_REDIS = True
except ImportError:
    HAS_REDIS = False

LOCK_LUA = """
local v = redis.call('HGET', KEYS[1], ARGV[1])
if v then
    redis.call('HINCRBY', KEYS[1], ARGV[1], 1)
    redis.call('PEXPIRE', KEYS[1], ARGV[2])
    return tonumber(v) + 1
elseif redis.call('EXISTS', KEYS[1]) == 0 then
    redis.call('HSET', KEYS[1], ARGV[1], 1)
    redis.call('PEXPIRE', KEYS[1], ARGV[2])
    return 1
end
return 0
"""

UNLOCK_LUA = """
local v = redis.call('HGET', KEYS[1], ARGV[1])
if not v then return 0 end
if tonumber(v) - 1 <= 0 then
    redis.call('HDEL', KEYS[1], ARGV[1])
    return 1
end
redis.call('HINCRBY', KEYS[1], ARGV[1], -1)
return tonumber(v) - 1
"""


class ReentrantRedisLock:
    def __init__(self, client, name: str, ttl_ms: int = 30000) -> None:
        self.client = client
        self.name = name
        self.ttl_ms = ttl_ms
        self.owner = f"{uuid.uuid4().hex}:{threading.get_ident()}"  # 实例+线程唯一

    def acquire(self) -> bool:
        depth = self.client.eval(LOCK_LUA, 1, self.name, self.owner, self.ttl_ms)
        return depth > 0

    def release(self) -> None:
        self.client.eval(UNLOCK_LUA, 1, self.name, self.owner)


class MemRedis:  # 缺库降级:同语义模拟
    def __init__(self) -> None:
        self.h: dict[str, dict[str, int]] = {}
        self._lock = threading.Lock()
    def eval(self, script_no: int, nkeys: int, key: str, field: str, ttl: int) -> int:
        with self._lock:
            h = self.h.setdefault(key, {})
            if field in h:
                h[field] += 1
                return h[field]
            if not h:
                h[field] = 1
                return 1
            return 0
    def eval_unlock(self, key: str, field: str) -> int:
        with self._lock:
            h = self.h.setdefault(key, {})
            if field not in h:
                return 0
            if h[field] - 1 <= 0:
                del h[field]
                return 1
            h[field] -= 1
            return h[field]


def run(client_factory) -> None:
    lock = client_factory()
    assert lock.acquire(), "首次加锁"
    assert lock.acquire(), "同一线程重入成功"
    assert lock.acquire(), "三层重入成功"
    lock.release(); lock.release()
    assert lock.acquire(), "未减到 0 前仍持有,可继续重入"
    lock.release()
    other = client_factory()
    assert not other.acquire(), "别人拿不到持有中的锁"


def real_client():
    """redis-py 可用且本机有 Redis 才返回真客户端,否则 None 走模拟。"""
    if not HAS_REDIS:
        return None
    try:
        r = redis.Redis(socket_connect_timeout=1)
        r.ping()
        return r
    except Exception:
        return None


r = real_client()
if r is not None:
    run(lambda: ReentrantRedisLock(r, "re:demo"))
    print("Redis 真锁验证通过")
else:
    mem = MemRedis()

    class MemLock:
        def __init__(self) -> None:
            self.owner = f"{uuid.uuid4().hex}:{threading.get_ident()}"
        def acquire(self):
            return mem.eval(0, 1, "re:demo", self.owner, 30000) > 0
        def release(self):
            mem.eval_unlock("re:demo", self.owner)

    run(MemLock)
    print("可重入锁语义验证通过(模拟)")
```

**追问一**：解锁 Lua 里为什么必须先 HGET 比较 field，而不能直接 HDEL？
答：重入计数减到 0 与锁到期/被抢之间存在竞态；直接删可能把新持有者的锁删掉。先确认 field 属于自己再操作，这是"fencing 思想"的最小实现。

**追问二**：可重入锁与 Redlock 的关系？
答：正交。重入解决"同一持有者多次加锁"的语义，Redlock 解决"单点 Redis 不可信"的仲裁；两者可叠加，但生产里更常见的是重入锁 + 单实例 + 容忍极小概率锁失效（业务幂等兜底），Redlock 的时钟跳变争议使收益常常不划算。

**背诵要点**：
- 可重入锁 = hash(field=实例+线程标识, value=重入计数) + Lua 原子 HINCRBY/HDEL。
- 持有者标识必须实例 uuid + 线程 id，缺一不可。
- 解锁先验证 field 再删，防误删新持有者；重入本身常是锁粒度设计坏味道。

**复盘追问**：
- 看门狗续期与重入续期叠加时，TTL 基准如何计算才不会出现"锁提前失效"？
- 如果递归调用跨越线程（异步任务），持有者标识该怎么设计？

## 背诵要点
- SET NX 不可重入；hash 计数 + Lua 实现重入与同持有者判断。
- owner = 实例 uuid + 线程 ident；解锁 Lua 先比 field 再删。
- 重入是语义补丁，优先重构锁粒度而不是引入可重入锁。

## 复盘追问
- A 释放瞬间 B 抢到锁，如何保证 A 的清理不误删 B？
- 深层重入 + 慢调用场景，续期策略如何设计？
