---
title: [Q6651] 读写分离写从库READONLY复盘
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6651 · 读写分离写从库 READONLY 复盘

难度：P6-P7 | 标签：MySQL、读写分离、事故复盘

**问**：一次故障切换后，应用持续报 `1290 The MySQL server is running with the --read-only option`。为什么读写分离路由会把写流量打到从库？如何从应用侧根治？

**答**：结论：根因是"角色漂移"——路由层（或业务里的主从双池）按**地址**定角色，而故障切换后地址与角色错位：旧主被降级为只读从库，路由表/配置里的"写池"还指着旧地址；或 DNS 切换后写池和读池最终指向了同一台只读实例。取舍：正确做法不是"报错重试到别的库"，而是让应用**按角色发现、按错误熔断**：路由以 topology（`SHOW REPLICA STATUS`/集群 API）为准，收到 1290 立即把该端点标记为不可写并触发路由刷新。

实战要点：
1. 写池只允许指向"当前主"的稳定标识（VIP、集群 writer 端点、或代理如 ProxyDB/MaxScale 的 writer 分口），禁止业务代码拿裸从库地址拼写池。
2. 1290 是**可立刻转移**的错误（非幂等风险类），应从通用重试里剥出来走"路由刷新+换端点"，避免把同一写请求打到多个从库造成部分成功。
3. 上线前的演练：手工把从库切主、观察应用 P99 与错误率，验证路由刷新时长 < 故障窗口。

```python
"""读写分离路由：按错误类别熔断端点并刷新角色（标准库演示，可运行）"""
import time
from dataclasses import dataclass, field


class ReadOnlyError(Exception):
    """模拟 MySQL 1290"""


@dataclass
class Endpoint:
    name: str
    writable: bool = True
    cooldown_until: float = 0.0


class Router:
    def __init__(self, endpoints: list[Endpoint]) -> None:
        self.endpoints = endpoints
        self.cooldown = 30.0

    def pick(self, write: bool) -> Endpoint:
        now = time.monotonic()
        cands = [e for e in self.endpoints
                 if e.writable and now >= e.cooldown_until]
        if write and not cands:
            raise RuntimeError("no writable endpoint, fail fast")
        if not cands:
            raise RuntimeError("no available endpoint")
        return cands[0]

    def report(self, ep: Endpoint, err: Exception) -> None:
        if isinstance(err, ReadOnlyError):
            # 角色漂移：立即熔断该端点的"可写"资格，不重试它
            ep.writable = False
            ep.cooldown_until = time.monotonic() + self.cooldown
            self.refresh_topology()

    def refresh_topology(self) -> None:
        # 生产中：查集群 writer 端点 / SHOW REPLICA STATUS，重建端点角色
        print("refresh topology: re-discover writer...")


router = Router([Endpoint("old-master(now-replica)")])
ep = router.pick(write=True)
try:
    raise ReadOnlyError("1290 read-only")
except ReadOnlyError as e:
    router.report(ep, e)
try:
    router.pick(write=True)
except RuntimeError as e:
    print("fail-fast:", e)
```

**追问 1**：为什么 1290 不能进普通的"可重试错误"列表？
**提示**：普通重试会在同一端点上打转；且写请求重试必须先确认未产生部分写入，1290 属于"端点错误"而非"请求错误"。

**追问 2**：如果写请求在切换瞬间已经发到旧主并被拒绝，业务如何保证不丢写？
**提示**：写路径前置事务发件箱/幂等键，客户端拿明确错误后重投到新 writer，而不是静默吞掉。

**追问 3**：读池指向"旧主降级成的从库"有什么数据风险？
**提示**：它可能还没追平新主，会读到旧数据；读路由要带最小复制延迟门槛。

## 背诵要点
- 1290 是端点角色错误：立即熔断该端点可写资格并刷新拓扑，不进通用重试。
- 写池必须指向稳定 writer 标识（VIP/代理 writer 分口），禁止裸地址拼池。
- 上线前必须做"从库切主"演练：路由刷新时长要小于故障窗口。

## 复盘追问
- 如果当时 1290 被归入通用重试并无限重试，监控上最先报警的指标会是什么？
- 如何用混沌演练证明"路由刷新时长 < 故障窗口"这条 SLO？
