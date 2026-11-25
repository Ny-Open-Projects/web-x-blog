---
title: [Q6652] 主从 schema 漂移复制中断复盘
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6652 · 主从 schema 漂移复制中断复盘

难度：P6-P7 | 标签：MySQL、复制、事故复盘

**问**：DBA 只在主库手工加了一列，从库后来补加，之后复制报错 `1054 Unknown column 'new_col'` 中断。为什么会出现"漂移"，如何设计让 schema 变更永不漂移？

**答**：结论：漂移的根因是 schema 变更**绕过了与数据一致的变更通道**——主从各自手工 DDL，没有统一版本号；复制流按 binlog 里的列序/列数重放，两边列序一旦不同就错位报错。根治不是"下次小心"，而是把 schema 变更纳入版本化迁移（migration 表记录版本），只允许一条通道（CI 里的 migration job）对主库执行，从库只靠复制获得 schema；或统一用 gh-ost/pt-osc 在主库执行、由 binlog 自然带到从库。

实战要点：
1. 校验器：定时 diff 主从 `information_schema.columns`（列名+序号+类型），漂移在复制中断**之前**就被发现。
2. 复制中断的恢复顺序：先停写或定位位点，从主库重新以一致性快照重建从库，而不是在从库上"手工改到一样"——列序/默认值仍可能不同。
3. migration 工具要记录 `applied_versions` 表并在 CI 里断言"线上版本 == 仓库最新版本"。

```python
"""schema 版本账本：检测漂移并阻断未走 migration 的变更（标准库演示）"""
from dataclasses import dataclass


@dataclass
class SchemaLedger:
    applied: dict[str, str]  # db -> version

    def assert_sync(self, db: str, repo_latest: str) -> None:
        cur = self.applied.get(db)
        if cur != repo_latest:
            raise RuntimeError(
                f"schema drift: {db} at {cur}, repo at {repo_latest}")


@dataclass
class Column:
    name: str
    pos: int
    dtype: str


def diff_columns(master: list[Column], replica: list[Column]) -> list[str]:
    """列序或类型不一致都算漂移，不等复制报错才发现"""
    issues = []
    for m, r in zip(master, replica):
        if m != r:
            issues.append(f"pos {m.pos}: master {m} vs replica {r}")
    if len(master) != len(replica):
        issues.append(f"column count {len(master)} != {len(replica)}")
    return issues


ledger = SchemaLedger({"orders": "v41"})
try:
    ledger.assert_sync("orders", "v43")  # 有人绕过 migration 直接 DDL
except RuntimeError as e:
    print("gate:", e)

print(diff_columns(
    [Column("id", 1, "int"), Column("amount", 2, "bigint")],
    [Column("id", 1, "int"), Column("note", 2, "varchar(64)")],
))
```

**追问 1**：为什么"从库手工补一列看起来成功了"反而是隐患？
**提示**：手工列与主库列序/定义可能不同，binlog 重放按位置映射，迟早 1054/1132 中断，且中断点可能在大事务处造成更长的追平窗口。

**追问 2**：gh-ost/pt-osc 这类在线变更工具为什么也要在主库跑而不是从库跑？
**提示**：从库执行不会进入主库 binlog，其他从库拿不到新 schema，等于又造一次漂移。

## 背诵要点
- schema 漂移根因是绕过 migration 通道的手工 DDL，靠列序映射重放，错位必中断。
- 主从列 diff（名+序+类型）定时跑，要在复制中断前发现漂移。
- 复制中断的正解是从一致性快照重建从库，不是"手工改到一样"。

## 复盘追问
- 如果中断发生在一张核心大表，停写重建 vs 跳过事务各有什么代价？
- 如何在 CI 里强制"任何人不能对从库直接 DDL"？
