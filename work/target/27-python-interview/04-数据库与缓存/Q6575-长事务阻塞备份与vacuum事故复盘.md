---
title: [Q6575] 长事务阻塞备份与 vacuum 的事故复盘
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6575 · 长事务阻塞备份与 vacuum 的事故复盘

难度：P6/P7 ｜ 标签：PostgreSQL / 事务 / 事故复盘

**问**：凌晨逻辑备份开始后，全库写入变慢、磁盘暴涨，天亮时复制槽告警 WAL 堆积。一条没提交的 Python 事务如何连锁引发这一切？

**答**：
- **结论**：根因是应用侧一个挂起的长事务（比如 psycopg2 里 `conn.autocommit=False` 后批量 SELECT 处理耗时、异常后忘了 rollback/commit）。长事务持有旧快照会三连击：① `pg_dump` 的 `--snapshot` 或一致性导出等待它（`pg_backup_start`/snapshot 等待）；② vacuum 无法回收它之后产生的死元组，表膨胀、磁盘暴涨；③ 若事务来自带复制槽的下游（逻辑订阅、CDC），槽的 `restart_lsn` 被钉住，WAL 无限堆积。三个症状一个根因。
- **取舍**：防御取舍在"自动杀 vs 告警人工"：`idle_in_transaction_session_timeout`（默认 0）设为 60s 能止血但可能误杀合法批处理——折中是分级：OLTP 连接池设 60s，批处理用独立用户/独立 pool 资源标签设 30min。Python 侧的结构性防御是"事务边界收窄"：把"查询-计算-写回"改为"查询（短事务）-计算-写回（短事务）+ 版本号乐观校验"。
- **实战**：事故复盘清单：① 事发时 `pg_stat_activity` 找 `xact_start` 最老的会话与 `pg_stat_progress_vacuum`；② 杀事务前确认它是否被逻辑槽依赖（`pg_replication_slots` 的 active_pid）；③ 应用侧上线事务监控（连接池钩子里统计事务持有时长 P99）；④ 给备份窗口加 `pg_dump` 前置检查：无 `xact_start < now()-interval '5 min'` 才开始。

```python
# 连接池钩子监控事务持有时长 + 备份前置检查（纯标准库模拟）
# 基线：Python 3.9+

from collections import deque
from datetime import datetime, timedelta


class TxGuard:
    """模拟 psycopg2 连接池的事务时长监控"""

    def __init__(self, idle_tx_timeout: timedelta = timedelta(seconds=60)):
        self.open_tx: dict[str, datetime] = {}
        self.timeout = idle_tx_timeout
        self.history: deque[tuple[str, float]] = deque(maxlen=1000)

    def begin(self, conn_id: str) -> None:
        self.open_tx[conn_id] = datetime.now()

    def end(self, conn_id: str) -> None:
        started = self.open_tx.pop(conn_id)
        self.history.append((conn_id, (datetime.now() - started).total_seconds()))

    def offenders(self, now: datetime) -> list[str]:
        return [c for c, t in self.open_tx.items()
                if now - t > self.timeout]


def backup_precheck(guard: TxGuard, now: datetime) -> bool:
    return not guard.offenders(now)  # 有长事务则禁止开始备份


def main() -> None:
    guard = TxGuard()
    guard.begin("conn-7")
    now = datetime.now() + timedelta(seconds=300)  # 模拟事务挂了 5 分钟
    bad = guard.offenders(now)
    print("长事务:", bad, "备份放行:", backup_precheck(guard, now))
    assert bad == ["conn-7"] and not backup_precheck(guard, now)
    guard.end("conn-7")
    assert guard.history[-1][1] >= 300  # 事务持有时长被记录


if __name__ == "__main__":
    main()
```

**追问 1**：`idle_in_transaction_session_timeout` 和 `statement_timeout` 该分别设在哪里？
→ 一句话提示：statement_timeout 管"单条 SQL 太慢"（OLTP 设 5-15s），idle_in_transaction 管"事务开着不干活"（60s 级），批处理用户单独放行——两者都要按用户/角色粒度设，不设全局一刀切。

**追问 2**：为什么死元组是"这个事务之后"的才能回收？
→ 一句话提示：MVCC 快照可见性——老事务的快照可能还需要看到旧版本行，vacuum 不能移除任何可能仍被某快照引用的元组，所以 global xmin 之前的死元组全部保留。

## 背诵要点
- 长事务三连击：阻塞备份快照 → vacuum 停摆表膨胀 → 复制槽 restart_lsn 钉住 WAL 堆积。
- 超时分级：OLTP `idle_in_transaction_session_timeout`≈60s，批处理独立角色放行，不做全局一刀切。
- 备份前置检查：`pg_stat_activity` 无超龄事务才允许 pg_backup_start。

## 复盘追问
- 为什么 Python 脚本特别容易踩长事务坑？提示：psycopg2 默认 autocommit=False，SELECT 也会开事务；ORM 的 session 长驻进一步放大。
- 如果这个长事务是"必须存在的批处理"，如何消除膨胀副作用？提示：分批提交 + `pg_stat_activity` 语义上的短事务化，或改到逻辑副本/只读实例上跑。
