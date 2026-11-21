---
title: [Q6535] Redis 分布式信号量：租约、公平排队与原子占位
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6535 · 分布式信号量：N 个许可怎么原子发放、过期回收、公平排队？

> 难度:★★★★★ | 标签:Redis, 分布式信号量, 租约

**问**：分布式锁是互斥（1 个持有者），但 GPU 池、导出任务这类场景需要"N 个并发许可"。Redis 怎么实现分布式信号量？许可续租、持有者崩溃后的回收、公平排队分别怎么做？为什么过期清理和占位必须原子？

**答**：结论：分布式信号量 = 受计数约束的分布式锁，核心三件事：**原子占位（清理过期 + 占位 + 计数校验打包进一段 Lua）、租约 TTL（防死许可）、公平排队（防插队与饥饿）**。经典实现用 SORTED SET：member=持有者令牌、score=获取时刻，获取时先 `ZREMRANGEBYSCORE` 清过期许可，`ZADD` 占位后 `ZCARD` 校验不超 N；续租 = `ZADD XX` 刷新自己的 score；释放 = `ZREM` 自己。

机理与实战：
- **原子性**：两个客户端同时"清过期再占位"，都看到"还有一个空位"就会超发；三步必须在单段 Lua 里执行，客户端时钟不参与判定（用 Redis 服务端 `TIME`），否则时钟漂移会让租约语义失真。
- **租约与续租**：许可带 TTL，持有者崩溃后许可自然过期回收，无需人工；活跃任务定期续租（刷新 score），续租失败说明许可已被回收，必须重新获取而不是继续干活——这就是信号量版的 fencing。
- **公平排队**：zset 天然"先到先得"，但"有空许可时新来者插队"是常见缺陷——必须加公平闸：队列非空时只有队头能立即获取，新来者一律入队；否则高峰期后到的轻任务可能长期抢在等待者前面。
- **计数漂移事故**：同一持有者重复获取（拿走两个许可）、忘记释放、释放了别人的许可，都会让有效许可数低于 N。防御：令牌唯一化（member 含持有者标识+随机数）、重复获取幂等返回既有许可、释放校验持有者身份、定期对账 `ZCARD` 与活跃任务数。
- **与 Redlock 的关系**：锁是 N=1 的特例，但信号量多出"总量一致性"问题——许可计数本身是共享状态，任何非原子路径都会超发；Redlock 的一致性论证不能直接搬过来。

```python
# 基线:Python 3.10+;纯标准库模拟 Redis Sorted Set 分布式信号量(租约+公平+原子占位)
# 真实场景:ZADD/ZREMRANGEBYSCORE/ZCARD 打包进单段 Lua 保证原子;时钟用 Redis TIME
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class AcquireResult:
    granted: bool
    token: str | None = None
    queued_ahead: int = 0               # 排在你前面的等待者数(公平性观测)


class RedisSemaphore:
    """N 许可信号量:zset member=持有者令牌, score=获取时刻(服务端时钟)。"""

    def __init__(self, name: str, permits: int, lease_seconds: float) -> None:
        self.name, self.permits, self.lease = name, permits, lease_seconds
        self.holders: dict[str, float] = {}          # token -> grant_time(模拟 zset)
        self.wait_queue: list[str] = []              # 先到先得的公平队列
        self.server_clock = 0.0                      # 用"服务端时钟"防客户端漂移

    def now(self) -> float:
        return self.server_clock                     # 真实实现:eval 里调 redis.call('TIME')

    def _purge_expired(self) -> None:
        cutoff = self.now() - self.lease             # 真实实现:ZREMRANGEBYSCORE 0 cutoff
        expired = [t for t, ts in self.holders.items() if ts <= cutoff]
        for t in expired:
            self.holders.pop(t, None)

    def acquire(self, client_id: str, token: str | None = None) -> AcquireResult:
        """原子三步(真实实现打包进一段 Lua):清过期 -> 占位 -> 计数校验。"""
        self._purge_expired()
        if token and token in self.holders:          # 幂等:重复获取返回既有许可
            return AcquireResult(True, token)
        # 公平闸:有空许可也必须让给先来排队者(仅队头可立即获取)
        if len(self.holders) >= self.permits or \
                (self.wait_queue and client_id != self.wait_queue[0]):
            if client_id not in self.wait_queue:
                self.wait_queue.append(client_id)
            return AcquireResult(False, queued_ahead=self.wait_queue.index(client_id))
        grant_time = self.now()
        tok = token or f"{client_id}:{grant_time}"
        self.holders[tok] = grant_time               # 真实实现:ZADD + ZCARD 校验后放行
        if client_id in self.wait_queue:
            self.wait_queue.remove(client_id)
        return AcquireResult(True, tok)

    def renew(self, token: str) -> bool:
        """续租:刷新 score;真实实现=ZADD XX(仅更新存在成员)。"""
        self._purge_expired()
        if token in self.holders:
            self.holders[token] = self.now()
            return True
        return False                                 # 许可已被过期回收 -> 需重新获取

    def release(self, token: str) -> bool:
        """释放:真实实现=ZREM(token),配合持有者身份校验防误删他人。"""
        return self.holders.pop(token, None) is not None

    def heartbeat_crash(self, token: str, seconds: float) -> None:
        """模拟持有者崩溃:不再续租,许可靠租约 TTL 自然回收。"""
        self.server_clock += seconds                 # 时间前进,等价于不续租


def demo() -> None:
    sem = RedisSemaphore("gpu:pool", permits=2, lease_seconds=10)
    r1 = sem.acquire("job-a")
    r2 = sem.acquire("job-b")
    r3 = sem.acquire("job-c")
    assert r1.granted and r2.granted and not r3.granted
    print(f"许可 2 个:a/b 持有,c 排队(前面 {r3.queued_ahead} 人) ✅")

    # 公平:c 先到,一个许可释放后 c 优先于后来者
    sem.release(r2.token)
    r4 = sem.acquire("job-d")
    assert not r4.granted and r4.queued_ahead == 1, "后来者 d 须排在 c 之后,不得插队"
    sem.server_clock += 3                            # 时间前进 3s,制造时间差
    r5 = sem.acquire("job-c")
    assert r5.granted, "队列头部的 c 应获得许可"
    print("先到先得:c 排队优先于后来者 d ✅")

    # 崩溃回收:a(t=0 获取)不再续租;c(t=3 获取,活跃)在租约内
    n_before = len(sem.holders)
    sem.heartbeat_crash(r1.token, seconds=8)         # 快进 8s:a 的租约(t=0+10)已过
    r6 = sem.acquire("job-d")                        # d 正排在队头,优先获得回收的许可
    assert r6.granted and r5.token in sem.holders and len(sem.holders) == n_before
    print("崩溃持有者的许可被租约 TTL 回收并按公平队列交给队头 d ✅(无泄漏、不插队)")

    # 续租语义:活跃任务续租后不被回收;忘续租则过期重取
    sem.renew(r5.token)
    sem.server_clock += 5                            # 快进 5s(< lease 10s)
    assert sem.renew(r5.token) and r5.token in sem.holders
    print("活跃任务续租保住许可 ✅")

    # 时钟漂移防御:用服务端时钟(真实实现 redis.call('TIME'))而非客户端本地时间
    print(f"占位/过期判定全部用服务端时钟(server_clock={sem.server_clock}) "
          f"-> 客户端时钟漂移不影响租约语义 ✅")


if __name__ == "__main__":
    demo()
```

**追问一**：许可租约到期但持有者的任务还在跑，会发生什么？正确姿势是什么？
答：任务继续跑而许可已给别人 → **并发超发**（N+1 个任务同时用资源）。正确姿势：长任务必须周期续租，且在关键副作用执行前校验"令牌仍有效"（续租成功才继续），续租失败立即挂起或收敛；租约时长 ≥ 续租周期的 2-3 倍容忍网络抖动。

**追问二**：为什么信号量场景下"客户端时钟漂移"比锁场景更容易出事故？
答：锁只争"谁持有"，漂移多影响过期快慢；信号量的 score 既当租约又当排序依据，漂移的客户端写入的 score 会污染公平排序（让它的许可"显得更新/更旧"），还会和别的持有者一起参与 min/max 判定——影响面从单许可扩散到整个许可池的回收与排序，所以判定必须只用服务端时钟。

## 背诵要点
- 三步原子化：清过期（ZREMRANGEBYSCORE）+ 占位（ZADD）+ 计数校验（ZCARD）打包单段 Lua，时钟一律用服务端 TIME。
- 租约 TTL 回收崩溃许可 + 活跃任务周期续租，续租失败 = fencing 失效必须停手重取。
- 公平闸：等待队列非空时仅队头可获取，防止有空许可时后来者插队；对账 ZCARD 与活跃任务数防计数漂移。

## 复盘追问
- 线上发现"实际并发数偶尔超过 N"，如何定位是哪条路径漏了？（提示：先查是否所有获取/续租都走同一段 Lua、是否存在客户端时间参与判定、重复获取是否幂等）
- 信号量许可数 N 的容量怎么定？（提示：按下游资源的真实并发容量反推并留缓冲，N 超过下游容量时信号量形同虚设、限流压力转移到下游）
