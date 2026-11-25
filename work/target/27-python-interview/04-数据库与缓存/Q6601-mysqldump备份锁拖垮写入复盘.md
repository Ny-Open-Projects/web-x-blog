---
title: [Q6601] mysqldump 单事务备份拖垮写入事故复盘
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6601 · mysqldump 单事务备份拖垮写入事故复盘

难度：P7 ｜ 标签：MySQL / 备份 / 事故复盘

**问**：业务低峰期运维跑了一次 `mysqldump --single-transaction` 全库备份，半小时后写入 QPS 归零、大量连接堆积在锁等待。备份不是"一致性快照不锁表"吗？为什么会拖垮写入？

**答**：
- **结论**：`--single-transaction` 只保证 InnoDB 表通过一致性快照导出，但 mysqldump 默认仍会在开始时执行 `FLUSH TABLES WITH READ LOCK`（配合 `--master-data` 记录 binlog 位点），这个全局读锁要等所有"已打开的表"关闭才拿得到——只要有一个长查询或未提交事务在跑，FTWRL 就排队，后面**所有写入全部被它挡住**，形成一次全库写停。事故放大器：mysqldump 默认把整库导成单条巨型 SQL 流、单事务持续几十分钟，read view 长期持有，undo 无法清理，版本链变长，期间所有查询的回表成本都在涨。
- **取舍**：方案对比：① 保留 `--single-transaction` 并升级到 8.0 的 `LOCK INSTANCE FOR BACKUP`（备份锁，粒度轻于 FTWRL）——8.0 默认已是备份锁，但仍挡 DDL；② 直接切到物理备份（XtraBackup / 云快照），快照不占 SQL 层锁，代价是恢复要整实例回放；③ 用 binlog 订阅做异步备份管道，RPO 秒级但链路要自己维护。Python 服务侧的正确姿势：备窗口前检查长事务（`information_schema.innodb_trx`），备份任务与业务写入做错峰+并发上限。
- **实战**：事故剧本：① 先从 `show processlist` 确认堵点是 FTWRL 而不是备份本身；② `kill` 备份连接解除写停（mysqldump 可重跑，业务优先）；③ 改用 XtraBackup 或云快照；④ 复盘项：备份任务纳入变更管理，跑前 `SELECT * FROM information_schema.innodb_trx WHERE TIME > 10` 作为门禁；Python 定时巡检脚本把长事务数作为备份窗口的健康探测。

```python
# 备份窗口健康探测 + 长事务门禁（模拟，标准库演示判定逻辑）
# 基线：Python 3.9+；真实实现用 mysql.connector / SQLAlchemy + information_schema

from dataclasses import dataclass


@dataclass
class Trx:
    trx_id: int
    seconds: int
    state: str
    rows_modified: int


def backup_gate(trxes: list[Trx], max_age: int = 10, max_rows: int = 100_000) -> tuple[bool, list[str]]:
    """备份前置门禁：存在长事务则拒绝开备份，避免 FTWRL 排队拖垮写入"""
    blockers = [
        f"trx {t.trx_id}: running {t.seconds}s, rows_modified={t.rows_modified}"
        for t in trxes
        if t.seconds > max_age or t.rows_modified > max_rows
    ]
    return (len(blockers) == 0, blockers)


def main() -> None:
    ok, blockers = backup_gate([
        Trx(101, 3, "RUNNING", 500),
        Trx(102, 8, "RUNNING", 20_000),
    ])
    assert ok and blockers == [], "健康窗口应放行"

    blocked, blockers = backup_gate([
        Trx(201, 900, "RUNNING", 5),          # 长事务：FTWRL 拿不到锁
        Trx(202, 5, "RUNNING", 2_000_000),    # 大写入：read view 会被拉长
    ])
    assert not blocked
    for b in blockers:
        print("拒绝备份:", b)
    print("OK: 长事务门禁拦截备份窗口")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么 `FLUSH TABLES WITH READ LOCK` 会被一个"只读 SELECT"卡住？
→ 一句话提示：FTWRL 需要等所有已打开的表全部关闭，任何未结束的查询/未提交事务都持有表引用；MySQL 8.0 用 `LOCK INSTANCE FOR BACKUP`（实例级备份锁）专门解决这点，只挡 DDL 不挡 DML。

**追问 2**：`--single-transaction` 导出期间另一个会话提交了修改，导出文件里是什么状态？
→ 一句话提示：是备份开始那一刻的一致性快照（可重复读 read view），后续修改不进导出；但长 read view 会让 purge 停滞、undo 膨胀——所以导出时长本身就是风险。

## 背诵要点
- `--single-transaction` 只免 InnoDB 表锁，FTWRL/master-data 位点锁仍会被任意长查询卡住，堵点在备份连接前的锁队列，写入全停。
- 备份窗口门禁：`innodb_trx` 里长事务（>10s）和大写入先清场；8.0 用 `LOCK INSTANCE FOR BACKUP` 替代 FTWRL。
- 长快照的次生灾害是 purge 停滞、undo 膨胀拖慢全库查询；生产备份优先物理备份/快照，mysqldump 只用于小库与单表逻辑导出。

## 复盘追问
- 为什么不建议在主库直接跑 mysqldump？提示：锁队列 + 长事务 + IO 带宽三重冲击，规范是从延迟副本或快照导出，副本上还要考虑复制位点对齐。
- Python 服务怎么把"备份健康度"做成可观测信号？提示：巡检 innodb_trx 时长分布、锁等待数，导出 prometheus 指标并在备份窗口前做 readiness 探测，不健康就自动顺延。
