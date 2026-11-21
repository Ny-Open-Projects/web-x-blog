---
title: [Q6542] 大批量 DELETE 磁盘不释放事故复盘：空间去哪了与表重建
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6542 · 大批量 DELETE 磁盘不释放事故复盘：删了 2 亿行，为什么磁盘一点没少？

> 难度:★★★ | 标签:事故复盘, 空间回收, 表重建

**问**：为了给日志库腾空间，跑了一条 `DELETE FROM access_log WHERE created_at < '2025-01-01'`，删掉 2 亿行、跑了 4 小时，结束后磁盘占用纹丝不动，查询还变慢了。空间去哪了？怎么做才是正确的腾空间姿势？

**答**：结论：DELETE 是**标记删除**——InnoDB/PG 都只是把行标记为 dead（PG 是 dead tuple，InnoDB 是 free 链表），空间留在表文件里供复用而不归还文件系统；同时大事务产生了 undo/redo 与膨胀，索引里还留了空洞。要归还操作系统必须**重建表**：MySQL 用 `OPTIMIZE TABLE`/gh-ost 重建，PG 用 `VACUUM FULL`/pg_repack（前者锁表，后者在线）。海量删除的正确姿势本来就该是分批删或 TRUNCATE/分区 DROP。

机理与实战：
- **为什么查询还变慢**：几十 GB 的表空洞让 B+ 树页稀疏、统计信息过时，优化器估算偏差，扫描页数变多；PG 里还叠加 autovacuum 顶不住的 dead tuple 扫描开销。
- **复用 vs 归还**：表内空洞后续 INSERT 可以复用（写放大降低），所以"不释放"不等于白删；但如果目标是把磁盘还给 OS 或这张表后续写入量小，就必须重建。
- **重建的代价**：OPTIMIZE/VACUUM FULL 都需要约等于表大小的额外磁盘（temp 副本），在"磁盘快满"的场景下要先扩盘再重建，否则重建自己就把库打满了——这是本类事故最常见的二次事故。
- **正确姿势分层**：时序/日志类表按月分区，过期直接 `DROP PARTITION`（秒级、零碎片）；普通大表清理用 1000-5000 行/批 + sleep 的分批 DELETE；一次性的大 DELETE 是反模式。

```python
# 基线:Python 3.10+;纯标准库,模拟分批删除限速器与表膨胀/重建决策
from __future__ import annotations
import time
from dataclasses import dataclass


@dataclass
class TableStats:
    rows_live: int      # 活元组
    rows_dead: int      # 死元组(标记删除未回收)
    file_gb: float      # 表文件大小
    data_gb: float      # 实际数据量

    @property
    def bloat_ratio(self) -> float:
        total = self.rows_live + self.rows_dead
        return self.rows_dead / total if total else 0.0


def decide_rebuild(s: TableStats, free_gb: float, lock_ok: bool) -> str:
    """根据膨胀率与磁盘余量给出回收方案。"""
    need = s.file_gb * 1.1  # 重建约需 1.1 倍表大小的临时空间
    if s.bloat_ratio < 0.2:
        return "膨胀<20%:无需重建,调整分批删除策略即可"
    if free_gb < need:
        return f"磁盘余量不足(需{need:.0f}GB,余{free_gb:.0f}GB):先扩盘再重建,勿直接 VACUUM FULL"
    if lock_ok:
        return f"低峰执行 VACUUM FULL/OPTIMIZE(需{need:.0f}GB 临时空间,锁表)"
    return f"用 pg_repack/gh-ost 在线重建(需{need:.0f}GB,业务无感)"


def batch_delete(total: int, batch: int = 5000, pause: float = 0.0) -> int:
    """分批删除骨架:小批次+间隔,避免长事务/主从延迟/undo 暴涨。"""
    done = 0
    while done < total:
        n = min(batch, total - done)
        # 真实实现: DELETE ... WHERE pk BETWEEN ... LIMIT n, 每批独立提交
        done += n
        if pause:
            time.sleep(pause)  # 生产给 50-200ms,让复制/日志追平
    return done


def demo() -> None:
    # 事故现场:2 亿 dead tuple,文件 500GB
    s = TableStats(rows_live=800_000_000, rows_dead=200_000_000,
                   file_gb=500, data_gb=380)
    print(f"膨胀率 {s.bloat_ratio:.0%}")
    print(decide_rebuild(s, free_gb=200, lock_ok=False))  # 扩盘提醒
    print(decide_rebuild(s, free_gb=600, lock_ok=False))  # 在线重建
    assert batch_delete(12000, batch=5000) == 12000
    print("标记删除→分批删+按需重建,腾空间正确姿势 ✅")


if __name__ == "__main__":
    demo()
```

**追问一**：PG 的 autovacuum 明明存在，为什么还会有 2 亿 dead tuple 堆着？
答：大 DELETE 是单个长事务，autovacuum 不能回收"比最老活动事务还新"的死元组（xmin 还被引用）；DELETE 结束后 autovacuum 才开始追，但 2 亿行的清理速度赶不上删的速度，且 autovacuum 只把空间放入 FSM 供复用、不收缩文件。所以长事务 + 大删除是组合拳事故。

**追问二**：为什么说分区表 DROP PARTITION 是这类场景的根治方案？
答：删除语义变成"整个文件不再需要"，DROP 是元数据操作（秒级），空间立即归还文件系统，没有标记删除、没有膨胀、没有 autovacuum 压力；代价是查询要带分区键裁剪、分区数量管理有运维成本——所以它适合时间边界清晰、写入模式稳定的时序类表。

## 背诵要点
- DELETE = 标记删除：空间留表内复用不归还 OS；查询变慢源于页稀疏+统计过时，PG 还有 dead tuple 扫描。
- 归还空间必须重建：OPTIMIZE/VACUUM FULL（锁表）或 gh-ost/pg_repack（在线）；重建需约 1.1 倍表大小临时空间，磁盘不足先扩盘。
- 根治：时序表按月分区 DROP PARTITION；普通大表 1000-5000 行/批+间隔分批删；一次性大 DELETE 是反模式。

## 复盘追问
- 重建期间业务写入持续，怎么保证 gh-ost 重建的数据一致性？（提示：影子表+binlog 回放+cut-over 原子换表；追问回放延迟阈值与切换时机选择）
- 那次事故里为什么 4 小时 DELETE 没人发现主从延迟在恶化？（提示：删除期间 binlog 量翻倍、从库单线程回放是瓶颈；应有主从延迟阈值联动限流的自动熔断）
