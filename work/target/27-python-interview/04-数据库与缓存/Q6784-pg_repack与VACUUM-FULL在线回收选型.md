---
title: "[Q6784] VACUUM FULL 锁了四小时：PG 空间回收的在线重组选型"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6784 · VACUUM FULL 锁了四小时：PG 空间回收的在线重组选型

难度：P6 ｜ 标签：pg_repack、VACUUM FULL、表膨胀、独占锁、在线重组

基线：Python 3.12；模拟三种空间回收路径的锁行为与磁盘峰值（VACUUM FULL 独占锁、pg_repack 换库双写、普通 VACUUM 不还盘），输出选型矩阵，全标准库实跑。

**问**：一张 300GB 的日志表 DELETE 了一半数据，磁盘却没变小（Q6542 的账），DBA 说"跑个 VACUUM FULL 就行"——结果业务锁了几个小时。VACUUM FULL 为什么锁全表？pg_repack 是怎么做到在线的？三种回收手段各自的锁、空间、风险账怎么算？

**答**：
- **结论**：普通 VACUUM 只把死元组占的空间标记为"可复用"（Q6542），**不归还操作系统**；要物理缩文件只有两条路：**VACUUM FULL**——把表按主键重写成新文件再换名，重写期间持 **ACCESS EXCLUSIVE 锁**，全表读写都堵死，300GB 表等于一次全量停写，且新旧两份文件同时存在，磁盘峰值 2 倍；**pg_repack**——在线方案：先建一张带触发器的新表，全量 COPY 旧数据，然后用触发器把 COPY 期间的增量同步过去，最后在**一个短暂的 ACCESS EXCLUSIVE 窗口内**（通常秒级）原子换名——把"4 小时锁"压缩成"几秒锁 + 4 小时双写开销"。选型矩阵：能用普通 VACUUM 解决的（膨胀<30%、空间压力不急）不折腾；必须物理回收但可停写的小表用 VACUUM FULL；大表、高可用要求高用 pg_repack；都不行就靠分区表（Q6765 分区交换）把回收粒度降到分区级。
- **取舍**：① pg_repack 的代价清单：需要的磁盘空间与新表等量（2 倍峰值）、双写触发器的写入放大（COPY 期间每行变更走触发器）、外键/某些 DDL 场景受限、失控的 repack 残留一堆半成品表要手工清理；② VACUUM FULL 并非一无是处：逻辑简单、结果干净（还顺带重建所有索引）、窗口可控的小表上是首选；③ 根因治理优先于回收动作：膨胀的真凶通常是长事务挡 vacuum（Q6575）、autovacuum 跟不上（Q6503）、批量 DELETE 设计——先止血再缩表，否则缩完接着涨；④ 回收是危险操作，任何形态都要有"失败回退"：pg_repack 中断不破坏原表（原表只是多了触发器），VACUUM FULL 中断文件已重写不可逆。
- **实战**：① 预检三件事：磁盘余量 ≥ 表大小、副本延迟容量、长事务清零（`pg_stat_activity` 里最老事务）；② 低峰执行 + 事务保护：repack 期间业务侧降低写入速率，监控触发器积压；③ 换名窗口前的观察：repack 的 swap 阶段要求排他锁瞬时获得，若有长查询占着锁会一直等（甚至死锁风险），执行前 kill 长查询；④ 治本三板斧：fillfactor 调低给 HOT 更新留空间（Q6703）、批量 DELETE 改成分区 DROP、长事务治理（Q6575）——缩表动作是一次性的，膨胀机理是持续性的。

```python
"""Q6784 空间回收三路径: VACUUM(不还盘) / VACUUM FULL(独占锁) / pg_repack(秒级换名)."""
from dataclasses import dataclass


@dataclass
class Outcome:
    path: str
    lock_window_s: float        # 排他锁窗口
    disk_peak_gb: float         # 磁盘峰值
    write_amp: float            # 期间写入放大
    usable: bool                # 业务可写时间占比


def vacuum_plain(size_gb: float, bloat: float) -> Outcome:
    """普通 VACUUM: 清死元组可复用, 不归还 OS, 锁窗口≈0."""
    return Outcome("VACUUM", 0.0, size_gb, 1.0, bloat < 0.3)


def vacuum_full(size_gb: float) -> Outcome:
    """VACUUM FULL: 全表重写, 全程 ACCESS EXCLUSIVE, 磁盘峰值 2x."""
    rewrite_s = size_gb * 48     # 演示: ~48s/GB 的重写耗时即锁窗口
    return Outcome("VACUUM FULL", rewrite_s, size_gb * 2, 0.0, True)


def pg_repack(size_gb: float) -> Outcome:
    """pg_repack: COPY+触发器双写在线, 仅换名瞬间持排他锁."""
    return Outcome("pg_repack", 3.0, size_gb * 2, 1.4, True)


if __name__ == "__main__":
    GB = 300
    for o in (vacuum_plain(GB, 0.5), vacuum_full(GB), pg_repack(GB)):
        print(f"{o.path:<12} 排他锁 {o.lock_window_s:>7.0f}s | 磁盘峰值 "
              f"{o.disk_peak_gb:>4.0f}GB | 写放大 {o.write_amp} | "
              f"{'可用' if o.usable else '膨胀可容忍但空间不还'}")
    vf, rp = vacuum_full(GB), pg_repack(GB)
    ok = (vf.lock_window_s > 10000 and rp.lock_window_s < 10
          and vf.disk_peak_gb == 600 and rp.disk_peak_gb == 600)
    print(f"校验: 300GB 表 FULL 锁 ~4h vs repack 秒级换名 -> {'通过' if ok else '异常'}")
    print("结论：VACUUM 不还盘, FULL 换空间换锁, repack 换在线换复杂度;")
    print("      大表在线回收选 pg_repack, 治本靠分区 DROP 与长事务治理")
```

**追问一**：pg_repack 换名那"几秒"为什么也不是零风险？窗口内到底发生了什么、什么情况下卡死？

→ 解析：换名窗口做的事：短暂持有 ACCESS EXCLUSIVE → 排空触发器积压的增量 → 原表与新表**原子交换物理文件标识** → 重建索引元数据关联。风险点：① **锁排队链**：ACCESS EXCLUSIVE 是最高级锁，请求它要等所有已持锁者释放，同时**阻塞所有新请求进入队列**——如果 COPY 结束时恰好有一个长查询（或未关闭的 idle in transaction）持着 ACCESS SHARE，换名就一直等，而队列里的普通查询也全被堵住，等于变相停服（Q884 MDL 排队链的 PG 版）；所以 repack 前要 `SET lock_timeout`（等不到就放弃重来而不是死等），并事先清理长事务；② **增量积压量**：窗口时长与触发器积压成正比，写入高峰期启动 repack 会让 swap 窗口拖长——选低峰 + 控制源表写入速率；③ **索引重建的锁**：repack 建新索引用 CREATE INDEX（非 CONCURRENTLY）是因为写在新表上无业务流量，但换名后索引统计信息要跑 ANALYZE，否则换名瞬间计划可能翻车。一句话：在线工具把"锁"换成了"时序协调"，窗口虽短但前置条件苛刻——**在线 ≠ 无风险，是把风险从时长换成了复杂度。**

**追问二**：如果既不能用 VACUUM FULL 也不能用 pg_repack（磁盘不够 2 倍峰值），还有哪些出路？

→ 解析：磁盘预算不足时的四条出路：① **分区化再滚动**：把大表改造成按时间分区（PG 大版本里 pg_repack 也能 repack 到分区母表，或用逻辑迁移重建），之后过期数据靠 DROP PARTITION 秒级回收（Q6780/Q6765），一次改造永久止损——磁盘峰值压力转移到"逐分区迁移"（每次只迁移一个分区，峰值≈一个分区 × 2）；② **逻辑导出-裁剪-重建**：`COPY (SELECT ...)` 导出保留数据 → TRUNCATE → COPY 回去，用外部存储顶住中间态，窗口比 VACUUM FULL 更可控且能顺便裁列/清洗，但要自己处理增量（双写或停写窗口）；③ **复制拓扑里的滚动重建**：新库/新表重建好（磁盘在另一台机器上），逻辑复制增量同步，最后切流量、旧库退役——磁盘峰值落在"另一台机器"，是云上最常用的形态（Q6624 初始同步容量账）；④ **接受膨胀 + 控制水位**：空间压力大但真挤不出峰值时，靠 fillfactor、归档冷数据、延长 autovacuum 覆盖维持可用水位，把物理回收排进下一次扩容窗口。决策顺序永远是：**先算清"这次回收要多少峰值空间、多少停写窗口"两个硬约束，再看四条路哪条满足——约束决定方案，工具只是手段。**
