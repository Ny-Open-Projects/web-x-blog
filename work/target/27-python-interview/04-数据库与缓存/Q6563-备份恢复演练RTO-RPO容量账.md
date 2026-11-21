---
title: "[Q6563] 备份恢复演练的 RTO/RPO 容量账"
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6563 · 备份恢复演练的 RTO/RPO 容量账

难度：P6 ｜ 标签：备份 / PITR / RTO / 容量规划

**问**：领导要求"数据库挂了 30 分钟内恢复、最多丢 5 分钟数据"。你手里有每日全量备份 + binlog/WAL 归档。怎么把这句话换算成可验证的容量与演练方案？

**答**：

**结论**：RTO/RPO 不是承诺是预算，必须用"恢复速度账"验证：恢复时间 = 全量恢复时间 + 增量重放时间 + 验证时间。全量恢复吞吐通常只有备份吞吐的 30%-50%（受导入索引构建、约束校验拖累），1 TB 库全量恢复 2-4 小时是常态——如果账算出来超 30 分钟，就得改架构（缩短全量周期、上从库切换而不是 PITR）而不是改口号。

**取舍**：三个档位——① 从库提升（promote replica）：RTO 分钟级，RPO 取决于复制模式（异步可能丢秒级，半同步接近 0）；② PITR（全量+归档重放）：RPO 可到秒级但 RTO 小时级，适合"误删数据回滚"而非宕机恢复；③ 双活/跨区：成本 2-3 倍。多数业务正确解是"从库切换保可用 + PITR 保误操作回滚"，两条链路分开演练。

**实战**：容量账三个输入：备份产生速率（影响备份窗口与归档盘 IO）、恢复速率（实测！`pg_restore -j` 并行度、MySQL `innodb_flush_log_at_trx_commit` 对导入速度的影响）、归档保留期（决定存储成本）。演练制度化：每季度做一次"拉真实备份到隔离环境 → 恢复 → checksum 抽验 → 计时"的完整流程，把 RTO 实测值写进 SLO 文档。Python 侧写恢复编排脚本：解析备份元数据、计算需要重放的归档区间、生成恢复命令并断言耗时预算。

```python
# 恢复时间预算账：全量恢复 + 归档重放 + 校验，与 RTO 目标对比
# 仅标准库，Python 3.9+
from __future__ import annotations


def restore_time_budget(db_gb: float, full_restore_mbps: float,
                        wal_gb_per_day: float, hours_since_full: float,
                        replay_mbps: float, verify_minutes: int = 15) -> dict:
    full_min = db_gb * 1024 / (full_restore_mbps * 60)
    wal_gb = wal_gb_per_day * hours_since_full / 24
    replay_min = wal_gb * 1024 / (replay_mbps * 60)
    return {
        "full_min": round(full_min),
        "replay_min": round(replay_min),
        "verify_min": verify_minutes,
        "rto_min": round(full_min + replay_min + verify_minutes),
        "rpo_gap_min": round(hours_since_full * 60, 0),  # 若无流复制，最大丢数据窗口
    }


def main() -> None:
    RTO_TARGET = 30
    # 1 TB 库，全量恢复实测 180 MB/s，每日 WAL 60 GB，全量是 6 小时前的
    r = restore_time_budget(1024, 180, 60, 6, 90)
    print(r)
    assert r["rto_min"] > RTO_TARGET, "应暴露出 RTO 超预算"
    print(f"结论：PITR 路径 RTO≈{r['rto_min']}min，超 {RTO_TARGET}min 预算，"
          "宕机恢复必须走从库切换，PITR 只兜误删回滚")

    # 改进：缩短全量周期到 1 小时前（增量重放窗口变小）
    r2 = restore_time_budget(1024, 180, 60, 1, 90)
    print("缩短全量周期后:", r2["rto_min"], "min")
    assert r2["rto_min"] < r["rto_min"]
    # 但仍超预算 → 最终解是从库切换（RTO 由提升耗时决定，约 1-5 分钟）
    print("最终解：从库切换 RTO≈2min；PITR 保留用于误删回滚（RPO 精确到秒）")


if __name__ == "__main__":
    main()
```

**追问链**：

- 追问 1：为什么全量恢复速率远低于备份速率？——备份是顺序读 + 压缩流，恢复要写数据页、重建索引、校验约束、刷 redo，随机 IO 与 CPU 都成为瓶颈；所以恢复速率必须实测，不能用备份速率倒推。
- 追问 1.1：从库切换丢失数据的窗口怎么压到最小？——半同步复制（至少 1 个从库 ack）或 PG 的 `synchronous_commit=remote_apply`；代价是写入延迟增加一个网络 RTT，要对写入 P99 做回归验证。
- 追问 2：演练时发现备份文件本身损坏（恢复到一半报错），说明流程缺了什么？——缺"备份可恢复性验证"：每次备份完成后应在隔离环境做最小化恢复探针（恢复表结构 + 抽样表 checksum），而不是等到真事故才发现备份不可用。

**背诵要点**：

1. RTO 预算 = 全量恢复 + 归档重放 + 校验，全量恢复速率只有备份速率的 30-50%，必须实测不能估算。
2. 从库切换（RTO 分钟级）与 PITR（RPO 秒级但 RTO 小时级）是两条链路，分别兜宕机与误删，不可互相替代。
3. 备份必须配可恢复性探针（抽样恢复 + checksum），否则备份等于没备份；演练按季度制度化。

**复盘追问**：

1. 如果当晚主库磁盘损坏且唯一从库延迟 20 分钟，你的决策树是什么（可接受丢 20 分钟吗，谁拍板）？
2. 恢复演练耗时超出预算 2 倍，你优先优化哪个环节（并行度/硬件/架构）？怎么量化收益？
