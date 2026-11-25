---
title: [Q6693] binlog 占满磁盘导致写入拒绝事故复盘
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6693 · binlog 占满磁盘导致写入拒绝事故复盘

难度：P6 ｜ 标签：事故复盘、binlog、磁盘容量、log_purge

基线：MySQL 5.7/8.0（binlog_expire_logs_seconds / expire_logs_days）；从库 relay-log 同理。

**问**：周日早上业务报"写入全部失败"，登录发现数据盘 100%，元凶是 binlog 目录——一个新上线的批量补数任务把日 binlog 量从 20GB 顶到 300GB，而保留策略是 7 天。为什么清理没生效？紧急处置和长期防线的正确姿势是什么？

**答**：
- **结论**：磁盘满时 MySQL 的行为是"拒绝写入"（磁盘不满时 binlog 无限追加），这是自保护而非 bug。清理没生效常见三个原因：(1) 只配了 `expire_logs_days` 但 8.0 用的是 `binlog_expire_logs_seconds`，参数没对上；(2) 没有任何主动 PURGE 触发点，只靠重启/FLUSH；(3) 从库还依赖这些 binlog（`PURGE` 会保护到最慢的订阅者），或 GTID 通道占用。
- **取舍**：紧急处置优先级——先限流/停掉补数任务止血；对已占满的 binlog 不能 rm（会破坏索引文件），要用 `PURGE BINARY LOGS TO/DATETIME` 或 `SET sql_log_bin=0` 之外的正规通道；如果必须 rm 救急，随后必须 `RESET` 修复 index 并评估从库重建。长期靠"量预估 + 保留策略 + 磁盘水位告警（70%/85%）+ 大批量任务限速"。
- **实战**：容量公式 `保留磁盘 = 日 binlog 量 × 保留天数 × 1.2 余量`；批量任务必须走"分批 + 限速 + 错峰"，并且 binlog 量入账（每行变更都写 binlog，一次 UPDATE 1000 万行 ≈ 数十 GB）。

```python
# binlog 磁盘容量账与清理决策模拟（标准库可运行）。
from dataclasses import dataclass

@dataclass
class BinlogFile:
    name: str
    size_gb: float
    mtime_day: int      # 距今天数

def plan_purge(files: list[BinlogFile], retain_days: int,
               disk_total_gb: float, lagging_replica_oldest_day: int | None) -> dict:
    """有效保留天数 = min(配置保留, 最慢从库依赖)。PURGE 不会越过还在被从库读取的文件。"""
    effective = retain_days
    note = None
    if lagging_replica_oldest_day is not None and lagging_replica_oldest_day > retain_days:
        effective = lagging_replica_oldest_day
        note = f"有从库最早依赖 {lagging_replica_oldest_day} 天前的日志，清理被保护拦截"
    purge = [f for f in files if f.mtime_day > effective]
    freed = sum(f.size_gb for f in purge)
    used = sum(f.size_gb for f in files)
    return {
        "usage_pct": round(used / disk_total_gb * 100, 1),
        "can_free_gb": freed,
        "after_pct": round((used - freed) / disk_total_gb * 100, 1),
        "note": note,
        "purge_files": [f.name for f in purge],
    }

if __name__ == "__main__":
    files = [BinlogFile(f"binlog.{n:06d}", 25.0, d)
             for n, d in zip(range(11, 23), range(12, 0, -1))]   # 12 个文件共 300GB
    r = plan_purge(files, retain_days=7, disk_total_gb=400,
                   lagging_replica_oldest_day=9)
    print(r)
    # usage_pct=75.0，被 9 天的落后从库保护：can_free 只能清 3 个文件
```

**追问**：
- 一层：为什么直接 `rm binlog.000012` 是错的？→ 提示：`binlog.index` 与实际文件失配，PURGE/复制/备份工具都会踩坑。
- 二层：`sql_log_bin=0` 能省 binlog 吗？什么时候敢用？→ 提示：能省但不进复制/不进恢复链，仅限可丢失的临时数据，且 GTID 环境要评估一致性。
- 三层：8.0 还有什么新手段？→ 提示：`binlog_group_commit_sync_delay` 降低小事务刷盘压力；克隆插件快速重建从库替代"从备份补 binlog"。

**背诵要点**：
1. 磁盘满是 MySQL 自保护：拒绝写入而非覆盖；binlog 不能 rm，只能 PURGE，且清理被最慢从库保护。
2. 容量公式：保留磁盘 = 日 binlog 量 × 保留天数 × 1.2；一次千万行 UPDATE 就是几十 GB。
3. 防线：批量任务分批限速错峰 + 磁盘水位 70%/85% 两级告警 + 参数按版本对齐（seconds vs days）。

**复盘追问**：
1. 为什么 300GB 的任务上线前没人算 binlog 账？提示：变更评审缺"写放大"检查项。
2. 如果从库必须保留 9 天而磁盘只够 7 天，怎么破？提示：延迟从库独立存储、克隆重建、或用备份链替代长保留 binlog。
