---
title: [Q6581] GTID 复制中断事故复盘
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6581 · GTID 复制中断事故复盘

难度：P7 ｜ 标签：MySQL / GTID / 复制 / 事故复盘

**问**：凌晨告警从库 SQL 线程停了，`Last_SQL_Error: could not find GTID ... server has purged required GTIDs`。业务写入还在继续，主从延迟持续拉大。这类 GTID 复制中断怎么定位与恢复？为什么不能直接跳过事务？

**答**：
- **结论**：GTID 中断的本质是"从库需要的事务在主库已被 purge 掉"（或主从 GTID 集合出现分叉）。恢复路径只有两条安全线：① 主库还留着所需 binlog → 从库 `STOP SLAVE; CHANGE MASTER ... SOURCE_AUTO_POSITION=1` 重新拉取，或直接补齐 `retired_gtid` 区间；② binlog 已 purge → 必须从备份重建从库（新备份的 GTID 起点覆盖缺口），或用主库全量+binlog 位点做并行重放。`sql_slave_skip_counter` 在 GTID 模式下根本不可用（必须 `SET GTID_NEXT` 注入空事务），而且逐个跳事务会造成主从数据永久分叉——这是"快速止血"换"数据不一致"的坏交易。
- **取舍**：预防优于恢复：`expire_logs_days`/`binlog_expire_logs_seconds` 要大于"从库最大可容忍中断时长 × 安全系数"；加了延迟从库（延迟 1 小时）就要保证主库至少留 2-3 小时 binlog。重建从库虽慢但确定性高，跳事务虽快但留下的是隐性数据漂移，未来某天对账才发现。
- **实战**：事故剧本：① 先 `SELECT @@GLOBAL.gtid_executed` 对比主从差集，确认缺口区间；② 查主库 `SHOW BINARY LOGS` 确认最老 binlog 是否覆盖缺口起点；③ 覆盖 → 从库重置 replication 重拉；不覆盖 → 走备份重建（xtrabackup + GTID 自动定位），期间把读流量切到其他从库或降级；④ 复盘项：把"主库 binlog 保留时长 ≥ 最慢从库恢复时长 × 2"写进容量账，并加"从库 IO/SQL 线程停止超过 5 分钟"的分级告警。

```python
# GTID 复制中断恢复决策器（纯标准库）
# 基线：Python 3.9+


def parse_gtid_set(s: str) -> set[int]:
    """解析 'uuid:1-5:8' 形式的 GTID 集合为整数集合"""
    out: set[int] = set()
    for part in s.split(","):
        part = part.strip()
        if not part:
            continue
        parts = part.split(":")
        uuid, ranges = parts[0], parts[1:]
        for r in ranges:
            if "-" in r:
                a, b = r.split("-")
                out.update(range(int(a), int(b) + 1))
            else:
                out.add(int(r))
    return out


def decide(master_set: str, slave_set: str, oldest_binlog_start: int) -> str:
    """返回恢复决策：重拉 / 重建备份 / 分叉需对账"""
    m = parse_gtid_set(master_set)
    s = parse_gtid_set(slave_set)
    missing = m - s
    if not missing:
        return "NO_GAP: 主从一致，检查复制线程状态即可"
    extra = s - m
    if extra:
        return "DIVERGED: 从库有主库没有的事务，存在分叉，需对账后重建"
    if min(missing) >= oldest_binlog_start:
        return "REPULL: 缺口仍在主库 binlog 内，重置 auto_position 重拉"
    return "REBUILD: 缺口事务已被 purge，必须从备份重建从库"


def main() -> None:
    uuid = "3E11FA47-71CA-11E1-9E33-C80AA9429562"
    master = f"{uuid}:1-10000"
    slave = f"{uuid}:1-9500"
    print(decide(master, slave, oldest_binlog_start=9000))
    # 缺口 9501-10000，最老 binlog 从 9000 开始 → 可重拉
    assert "REPULL" in decide(master, slave, 9000)
    assert "REBUILD" in decide(master, slave, 9600)
    # 从库多了主库没有的事务 → 分叉
    diverged = f"{uuid}:1-9500:20001"
    assert "DIVERGED" in decide(master, diverged, 9000)
    print("OK")


if __name__ == "__main__":
    main()
```

**追问 1**：GTID 模式下为什么 `sql_slave_skip_counter` 被禁用，正确做法是什么？
→ 一句话提示：GTID 用集合定位事务、位点计数器无意义；要跳过一个事务必须 `SET GTID_NEXT='uuid:n'; BEGIN; COMMIT; SET GTID_NEXT=AUTOMATIC` 注入空事务占位，让集合能对齐——但这是最后的下策。

**追问 2**：多从库架构里，哪类从库最容易触发 purge 事故？
→ 一句话提示：长期延迟的从库（报表库/延迟备份库）和暂停复制做维护的从库；要按"最慢消费者"原则定 binlog 保留期，并给延迟从库单独的保留策略或让它们走独立备份。

## 背诵要点
- GTID 中断两条安全路：缺口仍在 binlog → 重拉（auto_position）；已 purge → 备份重建；跳事务必然造成集合分叉。
- `gtid_executed` 差集是诊断起点；分叉（从库有主库没有的事务）必须对账，不能只补缺口。
- binlog 保留时长 ≥ 最慢从库恢复时长 × 2；延迟从库是 purge 事故的高发户。

## 复盘追问
- 为什么重建从库比逐事务跳过更"贵但正确"？提示：重建是确定性全量一致，跳事务留下的是不可见的行级漂移，等对账发现时代价更大。
- 半同步复制能不能避免这类事故？提示：不能——半同步只保证主库提交时有至少一个从库收到 binlog，不保证从库已回放、也不阻止 purge；它防的是丢提交，不是防回放落后。
