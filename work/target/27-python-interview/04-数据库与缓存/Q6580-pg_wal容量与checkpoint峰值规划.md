---
title: [Q6580] pg_wal 空间容量与 checkpoint 峰值规划
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6580 · pg_wal 空间容量与 checkpoint 峰值规划

难度：P7 ｜ 标签：PostgreSQL / WAL / 容量规划

**问**：大促写入峰值日，磁盘上的 pg_wal 目录涨到平时 10 倍并把磁盘写满，数据库拒写。WAL 空间到底怎么算容量？

**答**：
- **结论**：WAL 磁盘占用 = 生成速率 × 保留时长，而"保留时长"由三个最慢的消费者决定：checkpoint 回收（`max_wal_size`）、归档（archive 落盘/上传速度）、复制槽消费（若槽滞后）。大促写入高峰时 WAL 生成速率随写入量线性放大（每行修改都要写全页或 WAL 记录），若归档线程吞吐固定，积压就是速率差 × 时间。公式：`pg_wal 容量 ≥ max_wal_size + 滞后峰值 × 峰值生成速率 × 最慢消费者容忍时长`。
- **取舍**：`max_wal_size` 调大：好处是 checkpoint 摊薄、减少全页写（full_page_writes 触发更平滑）、写入高峰更稳；代价是崩溃恢复时间变长（要回放更多 WAL）与磁盘瞬时占用上限更高。这是"恢复 RTO"与"高峰写入稳定"的直接交换。归档用压缩（archive_command 里 gzip/zstd 或 wal-g）能降一档带宽但不能解速率倒挂，最终还是要么扩带宽要么限流写入。
- **实战**：规划步骤：① 用 `pg_stat_wal`（PG 14+）和测试环境大促回放测峰值 WAL MB/s；② 归档带宽按峰值速率的 1.5-2 倍配置；③ 磁盘容量按 max_wal_size + 2 小时峰值滞留量预留；④ 监控 `pg_stat_archiver.fail_count` 与 `pg_replication_slots` 滞后字节，双告警线（60% 容量警告、80% 限流写入）。

```python
# pg_wal 容量规划计算器（纯标准库）
# 基线：Python 3.9+


def wal_disk_budget(
    peak_mbps: float,            # 峰值 WAL 生成速率 MB/s
    max_wal_size_gb: float,      # checkpoint 上限
    lag_hours: float,            # 最慢消费者允许滞留时长
) -> float:
    """返回建议磁盘容量 GB"""
    retained = peak_mbps * 3600 * lag_hours / 1024  # 滞留量 GB
    return max_wal_size_gb + retained


def archive_headroom(peak_mbps: float, archive_mbps: float) -> bool:
    """归档带宽须 >= 峰值速率的 1.5 倍"""
    return archive_mbps >= peak_mbps * 1.5


def main() -> None:
    peak = 80.0  # 大促峰值 80 MB/s
    budget = wal_disk_budget(peak, max_wal_size_gb=16, lag_hours=2)
    print(f"建议 pg_wal 磁盘 ≈ {budget:.0f} GB")
    assert budget > 550  # 80MB/s * 7200s ≈ 562GB
    ok = archive_headroom(peak, archive_mbps=150)
    print("归档带宽够?", ok)
    assert ok
    print("归档带宽 100MB/s 够?", archive_headroom(peak, 100))
    assert not archive_headroom(peak, 100)  # 不达 1.5x 需扩容


if __name__ == "__main__":
    main()
```

**追问 1**：为什么 WAL 峰值速率可能比数据目录增长快得多？
→ 一句话提示：WAL 记录的是变更物理量——大批量 UPDATE/DELETE、频繁索引维护、每个 checkpoint 后的首个修改都写全页（fpw），重复更新同一行也每次都记 WAL。

**追问 2**：磁盘快满时除了扩容还有什么应急手段？
→ 一句话提示：临时调小 max_wal_size 促 checkpoint 回收、手动 `pg_switch_wal` 推进回收、清理无用复制槽（`pg_drop_replication_slot`）——但注意调小 max_wal_size 会加剧 IO 波动。

## 背诵要点
- pg_wal 容量 = max_wal_size + 峰值速率 × 允许滞留时长；消费者最慢者决定保留时长。
- max_wal_size 是"恢复 RTO vs 高峰写入稳定"的交换；归档带宽按峰值 1.5-2 倍配。
- 监控四件：pg_stat_wal 速率、archiver.fail_count、复制槽滞后字节、双阈值（60%/80%）。

## 复盘追问
- 为什么把 WAL 和数据目录放同一块盘有风险？提示：WAL 暴涨会挤占数据页空间，双双写满后数据库完全拒写，应分盘或至少分文件系统。
- 检查点间隔和全页写（full_page_writes）什么关系？提示：checkpoint 后每页首次修改要写全页，checkpoint 越频繁全页写越多、WAL 越大。
