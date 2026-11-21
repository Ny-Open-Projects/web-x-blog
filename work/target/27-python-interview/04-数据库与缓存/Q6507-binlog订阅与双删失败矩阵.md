---
title: [Q6507] 缓存一致性:binlog 订阅 vs 延迟双删的失败矩阵
date: 2026-11-18
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6507 · 缓存一致性:binlog 订阅 vs 延迟双删的失败矩阵

> 难度:★★★ | 标签:Redis, MySQL, 缓存一致性

**问**：缓存一致性方案网上说法很多：先删缓存再更新库、延迟双删、订阅 binlog 异步删。请给一个失败矩阵——每种方案在"删缓存失败 / 更新库失败 / 并发读写交错"时各是什么结局？你怎么选？

**答**：结论：没有无解的方案，只有"失败模式可补偿"的方案。推荐序：**业务侧 Cache-Aside（先更库后删缓存）+ binlog 订阅兜底补偿**。原理是先更库后删缓存的不一致窗口最短，而"删缓存失败"这个唯一硬伤恰好可以被 binlog 订阅（canal 模式）异步重试兜住；双删解决的是另一类问题，选型要看写路径结构。

失败矩阵（行=方案，列=故障）：
| 方案 | 更新库失败 | 删缓存失败 | 并发读写交错 |
|---|---|---|---|
| 先删缓存后更库 | 缓存被白删（可接受） | 脏数据长驻（无兜底）→最差 | 读旧库值回填缓存→长不一致 |
| 先更库后删缓存 | 缓存旧值但库没变（一致） | 脏数据直到 TTL →需订阅兜底 | 概率极低（读在更库前+删后回填），可用双删压缩 |
| 延迟双删 | 同上 | 两次删都可能失败，但第二次兜住交错 | 窗口≈延迟时长，仍非零 |
| binlog 订阅删缓存 | 库没变更无操作（天然一致） | 订阅端可无限重试→可收敛到一致 | 订阅有序，接近最终一致 |

取舍与实战：
- 双删的"延迟"是拍脑袋参数（通常 0.5~1s），它压缩的是"读旧值回填"窗口，无法归零；binlog 方案的延迟是复制+队列延迟（百 ms 级），且删除可无限重试、天然幂等，所以把它作为**兜底通道**而非主通道。
- 实战组合拳：主路径 Cache-Aside（更库成功才删缓存，删失败投递重试队列）+ 订阅 binlog 按"库中最新值"覆盖性删除 + 关键读路径容忍短 TTL（如 60s）做最终防线。三层各挡一类故障。
- 事故复盘：曾用"先删缓存后更库"叠加重试，一次 DB 主从切换期间更新重试 30 秒，期间大量请求读库（旧值）回填，切换完成后缓存里全是旧值直到 TTL。修复后改为更库后删 + binlog 订阅兜底，同类事故归零。

```python
# 基线:Python 3.9+ 标准库;一致性通道的失败注入与对账模拟(可运行)
from collections import deque

class CacheConsistency:
    def __init__(self) -> None:
        self.db: dict[str, str] = {"p1": "v0"}
        self.cache: dict[str, str] = {"p1": "v0"}
        self.retry_q: deque[str] = deque()          # 删失败重试队列

    def update(self, key: str, val: str, del_cache_ok: bool = True) -> bool:
        self.db[key] = val                          # 1) 先更库(失败则整体回滚,缓存一致)
        if del_cache_ok:
            self.cache.pop(key, None)               # 2) 后删缓存
        else:
            self.retry_q.append(key)                # 3) 删失败→投递 binlog 兜底通道
        return True

    def drain_retry(self) -> None:
        """binlog 订阅端:按库中最新值做覆盖性删除,可无限重试,幂等。"""
        while self.retry_q:
            k = self.retry_q.popleft()
            self.cache.pop(k, None)                 # 幂等:删多少次等价

    def read(self, key: str) -> str:
        if key in self.cache:
            return self.cache[key]
        self.cache[key] = self.db[key]              # 回填
        return self.db[key]

if __name__ == "__main__":
    c = CacheConsistency()
    c.update("p1", "v1", del_cache_ok=False)        # 删缓存失败
    print("未兜底读取:", c.read("p1"))              # v1? 不,缓存还有旧值 v0
    c.drain_retry()
    print("兜底后读取:", c.read("p1"))              # v1,最终一致
```

**追问**：
- 一层追问：为什么"先更新缓存再更新库"没人用？——库是事实源，缓存写成功而库失败时，缓存里的新值没有事实依据且无法靠"删"快速纠正（要等 TTL），失败模式最不可控。
- 二层追问：binlog 订阅链路的延迟抖动怎么保证"接近一致"而不是"很久才一致"？——监控 canal 位点延迟与队列积压；热点 key 更新走同步删为主、订阅只兜失败，把 P99 不可一致窗口从"队列延迟"缩到"一次删 RTT"。
- 三层追问：强一致读怎么办？——缓存方案不可能强一致，只能退化：关键路径读库 + 读写锁/分布式锁串行化，或者干脆接受"该数据不走缓存"。面试要点是敢说"做不到"。
