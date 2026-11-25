---
title: "[Q6703] fillfactor 与 HOT 更新：从写入侧治理索引膨胀"
date: 2026-11-23
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6703 · fillfactor 与 HOT 更新：从写入侧治理索引膨胀

难度：P6 ｜ 标签：容量成本账、PostgreSQL、MVCC、索引膨胀

基线：Python 3.12；PostgreSQL 12+；纯 Python 页模型演示。

**问**：一张高频 UPDATE 的状态表，索引膨胀很快，每次 `REINDEX` 完两周又打回原形。DBA 说"调 fillfactor"，这是什么意思？为什么它能从根上缓解，而不是又一次临时止血？

**答**：
- **结论**：PostgreSQL 的 MVCC 让 UPDATE 生成新行版本。默认 `fillfactor=100` 把数据页填满，新版本放不进原页，只能落到别页，于是**每个索引都要新增指向新版本的项**——这就是索引膨胀的源头。设 `fillfactor=70~90` 预留页内空闲空间后，更新可以走 HOT（Heap Only Tuple）：新版本与原版本在同一页，索引项不变，旧索引项无需新增，膨胀大幅降低。
- **取舍**：预留空间降低了页密度，表更占磁盘、顺序扫描读的页更多；所以适合"更新密集 + 索引点查"的表，不适合"只追加 + 大范围顺序扫描"的表。它治的是**未来写入**，对已经膨胀的存量无效。
- **实战**：`ALTER TABLE t SET (fillfactor=80)` 只对后续写入生效，存量要 `VACUUM FULL` 或 `pg_repack` 重写一次；通过 `pg_stat_user_tables.n_tup_hot_upd / n_tup_upd` 监控 HOT 比例，把它当成写入健康度指标；结合 autovacuum 及时回收死元组（避免另一个维度的膨胀）。

```python
PAGE_SLOTS = 10


def simulate_hot_rate(fillfactor: int, updates: int = 100) -> float:
    """简化页模型：页内预留槽位越多，更新越可能走 HOT 而不新增索引项。"""
    reserved = int(PAGE_SLOTS * (100 - fillfactor) / 100)
    used = PAGE_SLOTS - reserved
    hot = 0
    for _ in range(updates):
        if used + 1 <= PAGE_SLOTS:
            hot += 1
            used += 1
            if used >= PAGE_SLOTS:
                used = PAGE_SLOTS - reserved
        else:
            used = PAGE_SLOTS - reserved + 1
    return hot / updates


if __name__ == "__main__":
    for ff in (100, 90, 80, 70):
        print(f"fillfactor={ff}: HOT ratio {simulate_hot_rate(ff):.0%}")
    # fillfactor 越低，预留越多，HOT 比例越高，索引膨胀越慢。
```

**追问一**：为什么 `REINDEX` 只能管一时，fillfactor 却能治本？
→ 解析：REINDEX 重建的是当前索引，不改变后续 UPDATE 产生新索引项的行为；fillfactor 改变页布局，让后续更新走 HOT、不再新增索引项，是从写入模式上治本。

**追问二**：fillfactor 设得越低越好吗？
→ 解析：不是。预留越多，页密度越低，表和索引更占空间、顺序扫描更慢。要在"更新频率"和"读取模式"之间权衡，通常 70~90 是经验区间，需实测 HOT 比例与空间成本。
