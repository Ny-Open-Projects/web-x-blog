---
title: [Q6587] MySQL binlog 保留与磁盘成本账
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6587 · MySQL binlog 保留时长与磁盘成本账

难度：P6 ｜ 标签：MySQL / binlog / 成本工程 / 容量规划

**问**：DBA 把 `binlog_expire_logs_seconds` 从 3 天改到 30 天来"提高安全性"，两个月后磁盘告警、每次 purge 都造成延迟毛刺。binlog 保留时长应该怎么定？这笔磁盘账怎么算？

**答**：
- **结论**：binlog 保留时长由"最慢消费者"决定，不是越大越安全。消费者三类：① 从库/GTID 缺口恢复（需保留 ≥ 从库最大中断时长 × 2）；② 增量备份链（PITR 恢复到任意时间点需要全量备份起点到现在的全部 binlog）；③ 数据订阅/ canal 类 binlog 客户端（挂了恢复后要能从旧位点重放）。磁盘账：`binlog 空间 ≈ 日均写入 WAL 量 × 保留天数`，写放大大的业务（频繁 UPDATE、多索引）日均 binlog 可达数据变更量的 2-5 倍。30 天保留在写密集库上就是 TB 级成本，还带来 purge 尖峰（MySQL 删 binlog 是逐文件 unlink，量大时 IO 抖动）。
- **取舍**：保留在本地磁盘 vs 归档到对象存储：本地只留"最短可用窗口"（如 3-7 天），更早的压缩归档到对象存储（zstd 可压 3-10 倍），PITR 时先拉归档再回放——用恢复时长换磁盘成本。purge 尖峰治理：靠 `binlog_expire_logs_seconds` 自动到期时把删除摊到每天（每天删的量 = 日均 binlog 量，可控），事故是把保留突然从 3 天调到 30 天，到期那天会一次性删掉几十个旧文件。
- **实战**：步骤：① 用 `SHOW BINARY LOGS` 统计近 7 天日均 binlog GB/天；② 按最慢消费者定最短保留（通常从库恢复 2-7 天 + PITR 起点依赖）；③ 磁盘预留 = 日均 × 保留天数 × 1.5 峰值系数，且 binlog 与数据分盘；④ 变更保留期前先算账并灰度（先调到 7 天观察 purge 抖动，再定终值）。

```python
# binlog 磁盘成本账计算器（纯标准库）
# 基线：Python 3.9+

def binlog_disk_budget(
    daily_binlog_gb: float,
    retention_days: int,
    peak_factor: float = 1.5,
) -> dict:
    """本地磁盘预留与每日 purge 量"""
    need = daily_binlog_gb * retention_days * peak_factor
    daily_purge = daily_binlog_gb  # 稳态下每天到期删除量 ≈ 日增量
    return {"disk_gb": round(need, 1), "daily_purge_gb": daily_purge}


def cost_compare(daily_gb: float, local_price_per_gb: float = 0.35,
                 archive_price_per_gb: float = 0.02,
                 local_days: int = 7, archive_days: int = 30) -> dict:
    """本地短保留 + 归档长保留 vs 全本地长保留 的月成本"""
    local = daily_gb * local_days
    archive = daily_gb * archive_days
    all_local = daily_gb * archive_days
    plan_mix = local * local_price_per_gb + archive * archive_price_per_gb
    plan_all = all_local * local_price_per_gb
    return {"mix_month": round(plan_mix * 30, 2),
            "all_local_month": round(plan_all * 30, 2),
            "saving_pct": round((1 - plan_mix / plan_all) * 100, 1)}


def main() -> None:
    # 日均 60GB binlog 的写密集库
    b = binlog_disk_budget(60, retention_days=7)
    print(b)
    assert b["disk_gb"] == 630.0   # 60*7*1.5
    c = cost_compare(60)
    print(c)
    # 全本地 30 天: 60*30*0.35*30 = 18900/月
    # 混合: 7 天本地 + 30 天归档: (60*7*0.35 + 60*30*0.02)*30 = 5490/月
    assert c["all_local_month"] == 18900.0
    assert c["mix_month"] == 5490.0
    assert c["saving_pct"] > 60.0  # 归档单价低两个数量级 → 省 70% 左右
    print("OK")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么 binlog 的日均量可能远大于数据变更量本身？
→ 一句话提示：binlog 记录的是行变更的物理量（ROW 格式含整行前后镜像选项、UPDATE 记录前后两份），加上索引维护与放大、每行一条，重复更新同一行也每次全记——写放大 2-5 倍很常见。

**追问 2**：PITR（基于时间点恢复）的恢复时长怎么估，怎么缩短？
→ 一句话提示：恢复时长 ≈ 全量备份恢复时间 + 起点到现在全部 binlog 回放时间；缩短靠缩短全量备份周期（更频繁的小全量）与并行回放工具，用备份成本换 RTO。

## 背诵要点
- 保留时长 = 最慢消费者（从库恢复 ×2 / PITR 链 / binlog 订阅客户端）中的最大值，不是越大越安全。
- 磁盘账 = 日均 binlog GB × 保留天数 × 1.5 峰值；写密集库 binlog 是变更量的 2-5 倍。
- 成本最优解：本地 3-7 天 + 对象存储归档（zstd 压 3-10 倍），用恢复时长换磁盘成本。

## 复盘追问
- 突然把保留期从 3 天调到 30 天，除了磁盘还有什么次生风险？提示：到期 purge 的文件堆积、以及写满 binlog 分盘后实例 hang 的风险——任何保留期变更都要先算磁盘账并分盘隔离。
- ROW 和 STATEMENT 格式对 binlog 体积账影响多大？提示：STATEMENT 记 SQL 体积小但有不安全函数/非确定性问题，ROW 体积大但确定；绝大多数生产用 ROW，意味着体积账必须按行变更物理量算而不是按 SQL 条数算。
