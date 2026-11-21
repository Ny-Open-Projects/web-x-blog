---
title: [Q6536] Serverless 短任务的数据库连接爆炸与池化
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6536 · Serverless 短任务连接爆炸：500 个实例 × 连接池 5 = 事故

> 难度:★★★★ | 标签:连接池, PgBouncer, Serverless

**问**：函数计算/定时任务场景，实例并发 500、每个实例只活几秒、每实例开连接池 size=5 直连 PostgreSQL，会发生什么？为什么说 serverless 下"每实例自带连接池"是反模式？外置事务级连接池（PgBouncer transaction pooling / 云 HTTP endpoint）能解决什么、又会引入什么坑？

**答**：结论：连接需求 = 实例数 × 池大小，500×5=2500 远超 PG 的 `max_connections`（常见 100-500），报 `FATAL: too many connections`，而且 PG 每连接是一个后端进程（数 MB 内存 + 调度开销），就算连上也是灾难。解法是把"连接"从实例生命周期解耦：① 实例内池缩到 1（serverless 单实例通常无并发查询）；② 外置连接代理 PgBouncer transaction 模式，把几千客户端连接复用到几十条真连接；③ 无状态短查询走云厂 HTTP endpoint，完全绕过 TCP 长连接。

机理与实战：
- **transaction 模式的代价**：连接是"按事务"借还的，**会话级状态不再可靠**——`SET search_path`、session 级 advisory lock、命名 prepared statement、跨语句的 WITH HOLD 游标都会串话或失效。SQL 里用全限定表名替代 SET search_path；advisory lock 用事务级（`pg_advisory_xact_lock`）；prepared statement 用无名语句或客户端侧禁用。
- **实例内池参数**：serverless 场景 `pool_size=1`、`max_lifetime` 调短，避免实例冻结/销毁留下僵尸连接；定时任务用独立账号 + 并发上限，防止批处理把池打满挤掉在线业务。
- **容量账公式**：真连接数 ≈ DB 可承受并发（CPU/IO 决定），客户端连接数 ≈ 瞬时实例数 × 每实例并发事务——两者解耦正是池化代理存在的意义。

```python
# 基线:Python 3.10+;纯标准库模拟 serverless 高并发短实例下的数据库连接账
# 真实场景:应用直连 PG / PgBouncer transaction pool / 云 HTTP endpoint 三种模式
from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class ServerConn:
    """一条真实数据库连接(PG:每连接一个后端进程)。"""
    state: dict = field(default_factory=dict)    # 会话级状态:SET 的变量/临时设置
    busy_with: str | None = None                 # 当前占用它的客户端


class DirectPool:
    """每实例自带连接池:serverless 下的反模式。"""

    def __init__(self, instances: int, pool_size: int) -> None:
        self.total = instances * pool_size

    def verdict(self, max_conns: int) -> str:
        if self.total > max_conns:
            return f"需 {self.total} 连接 > max_connections={max_conns} -> too many connections!"
        return f"需 {self.total} 连接,勉强够但后端进程内存 = {self.total} 份"


class TransactionPool:
    """PgBouncer transaction 模式:客户端连接 >> 真连接,按事务复用。"""

    def __init__(self, real_conns: int) -> None:
        self.conns = [ServerConn() for _ in range(real_conns)]
        self._cursor = 0

    def _next_conn(self, client: str) -> ServerConn:
        c = self.conns[self._cursor % len(self.conns)]   # 轮转复用(简化)
        self._cursor += 1
        c.busy_with = client
        return c

    def run(self, client: str, sql: str) -> ServerConn:
        """每个事务可能落在不同真连接上。"""
        return self._next_conn(client)


def demo() -> None:
    instances, pool_size, max_conns = 500, 5, 300    # 并发实例 500,PG 上限 300

    direct = DirectPool(instances, pool_size)
    print(f"直连:{direct.verdict(max_conns)}")

    proxy = TransactionPool(real_conns=20)
    all(proxy.run(f"fn{i}", "SELECT 1") for i in range(500 * 5))
    print(f"transaction pool:2500 客户端连接复用到 {len(proxy.conns)} 条真连接 ✅")

    # 事故:session 级状态在 transaction pool 下会"串话"
    c1 = proxy.run("tenant-a", "SET search_path = tenant_a")   # 连接 #0 上 SET
    c1.state["search_path"] = "tenant_a"
    leaked = 0
    for _ in range(21):                                        # tenant-b 连续 21 个事务
        c = proxy.run("tenant-b", "SELECT * FROM orders")
        if c.state.get("search_path") == "tenant_a":
            leaked += 1
    assert leaked >= 1
    print(f"事故复现 ✅:tenant-b 的 21 个事务里 {leaked} 个落在 tenant-a "
          "SET 过的连接上 -> search_path 串话,查错 schema!")
    print("对策:transaction 模式禁用会话级 SET;用全限定表名 / advisory lock 换事务级 / "
          "prepared statement 用无名语句")


if __name__ == "__main__":
    demo()
```

**追问一**：为什么 PG 的连接比 MySQL "贵"？
答：PG 每连接 fork 一个后端进程，内存（几 MB 起）与上下文切换开销大、可承载连接数天然低；MySQL 是线程模型，单机几千连接也能扛。这决定了 PG 侧必须更激进地池化，也是 PgBouncer 在 PG 生态成为标配而在 MySQL 生态相对少见的原因。

**追问二**：定时任务半夜把在线业务的连接池挤满了，怎么隔离？
答：账号维度限流（批处理账号限制并发数）、PgBouncer 按业务分 pool/database（在线与批处理各自独立真连接配额）、DB 层 `max_connections` 预留 superuser 通道保运维入口；更进一步用 workload 隔离——批处理走独立只读副本或数据仓库。

## 背诵要点
- 连接需求 = 实例数 × 每实例池大小；serverless 高并发短实例直连必然打爆 max_connections（PG 每连接一个进程）。
- 解耦方案：实例内池 size=1 → 外置 PgBouncer transaction pool → 无状态查询走 HTTP endpoint。
- transaction 模式下会话级状态（SET/命名 prepared statement/session 锁）不可靠，必须全限定名 + 事务级锁 + 无名语句。

## 复盘追问
- 函数平台扩容风暴后出现大量 `too many connections`，除了池化还能怎么缓？（提示：连接上限前置到代理层排队 + 应用侧指数退避重试，避免重试风暴叠加）
- 如何在 CI 里防住"transaction pool 不兼容 SQL"回归？（提示：用 SET/命名语句/会话锁的静态扫描门禁 + transaction pool 模式的集成测试环境）
