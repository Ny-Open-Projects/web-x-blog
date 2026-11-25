---
title: "[Q6798] HOT 更新失效的三个条件：fillfactor 什么时候救不了你"
date: 2026-11-25
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6798 · HOT 更新失效的三个条件：fillfactor 什么时候救不了你

难度：P6 ｜ 标签：PostgreSQL、HOT、fillfactor、索引膨胀、MVCC、n_tup_hot_upd

基线：PostgreSQL 12+；Python 3.12 用堆页槽位模型复现 HOT/非 HOT 更新与膨胀，全标准库实跑。

**问**：一张用户余额表每秒更新几千行，索引膨胀得很快，DBA 把 `fillfactor` 从 100 调到 70，观察两周发现**几乎没效果**，索引该涨还是涨。fillfactor 不是专门为 HOT 更新留空间的吗？HOT 到底要满足什么条件才会发生？怎么用 `pg_stat_user_tables` 判断"没走 HOT"的原因是页满还是别的？

**答**：

- **结论**：HOT（heap-only tuple）更新要**同时**满足三个条件：① **没有任何索引列被修改**——只要 update 的列出现在任一索引里，就必须为新版本在每个索引里插入新条目，HOT 直接失效；② **新版本能放进同一个堆页**——页里得有空洞或预留空间；③ 新版本不跨页（同一个 page，不是同一个文件）。`fillfactor` 只作用于条件②：建表/重建时把每页只填到 70%，留 30% 给后续更新。所以它救不了条件①——更新索引列的场景，fillfactor 调到 50 也只是让表更大、索引照涨。条件②还有一层：**只有当更新发生在"该页还有预留空间"时才有用**，如果更新是均匀随机打在整个大表上，早期页的预留空间很快被消耗完，之后全部退化成非 HOT，你付出的代价（表大 30%、顺序扫描多读页、buffer pool 命中率下降）却一直存在。
- **取舍**：fillfactor 是"用空间换索引写放大"的局部优化，适用范围很窄：**更新集中在最近插入的热尾行、且更新列不在索引里**的表（会话表、任务队列表、余额/计数表）。冷表保持 100；更新随机的超大表调低只会增加扫描成本。如果更新列确实是索引列，正解不是调 fillfactor，而是**减少索引**（把不必要索引删掉）、用**部分索引**（只索引 `status='PENDING'` 的行，状态流转出索引范围后不再产生条目）、或按状态分区让更新落到不同分区。另外 `fillfactor` 只影响**后续插入**，已有页不会自动重排，调完必须 `VACUUM FULL`/`pg_repack` 才生效——很多人"调了没效果"其实是没重建。
- **实战**：一张 4000 万行的订单表，`UPDATE ... SET status=?` 每秒 3000 次，`n_tup_hot_upd/n_tup_upd` 只有 3%。DBA 先把 fillfactor 调到 70，两周后索引还是涨——因为 `status` 在三个索引里（两个业务索引 + 一个 partial 之外的普通索引），条件①根本不满足。真正的治理是：删掉两个冗余索引、把"待处理"查询改成 partial index（`WHERE status IN ('PENDING','RUNNING')`），状态流转到终态后不再进索引；索引写放大降了 70%，表大小没变。fillfactor 最后只用在会话表上（更新 `last_seen`，不在索引里），HOT 比例从 40% 提到 96%。

下面用堆页槽位模型对比"热尾更新 / 随机更新 / 更新索引列"三种负载下 fillfactor 的实际效果。

```python
# HOT 三条件: 索引列、页内空位、同页; fillfactor 只影响第二条
import random

CAP = 40                      # 每页 40 个元组槽位


class Table:
    def __init__(self, fillfactor):
        self.max_fill = max(1, int(CAP * fillfactor / 100))
        self.used = [0]           # 每页已用槽位
        self.page_of = {}
        self.non_hot = 0
        self.total_updates = 0

    def _alloc(self):
        if self.used[-1] >= self.max_fill:
            self.used.append(0)
        self.used[-1] += 1
        return len(self.used) - 1

    def insert(self, rid):
        self.page_of[rid] = self._alloc()

    def update(self, rid, indexed_change=False):
        self.total_updates += 1
        p = self.page_of[rid]
        if not indexed_change and self.used[p] < CAP:   # 条件1 + 条件2
            self.used[p] += 1
            return True
        self.page_of[rid] = self._alloc()
        self.non_hot += 1
        return False


def workload(fillfactor, pattern, indexed_change=False, rows=2000, updates=8000, seed=3):
    t = Table(fillfactor)
    for r in range(rows):
        t.insert(r)
    rnd = random.Random(seed)
    for _ in range(updates):
        if pattern == "hot":
            rid = rnd.randrange(int(rows * 0.8), rows)   # 80% 的更新打最后 20% 行
        else:
            rid = rnd.randrange(rows)
        t.update(rid, indexed_change)
    hot = t.total_updates - t.non_hot
    return hot / t.total_updates, len(t.used)


for pattern in ("hot", "uniform"):
    print(f"[1] {pattern} 更新:")
    for ff in (100, 70, 50):
        ratio, pages = workload(ff, pattern)
        print(f"    fillfactor={ff:>3}: HOT 比例 {ratio:.0%}, 堆页数 {pages}")
hot100, _ = workload(100, "hot")
hot70, _ = workload(70, "hot")
uni100, _ = workload(100, "uniform")
uni70, _ = workload(70, "uniform")
print(f"    → 实测 热尾: ff70 把 HOT 从 {hot100:.0%} 提到 {hot70:.0%}; "
      f"随机: {uni100:.0%} → {uni70:.0%}")
assert hot70 > hot100 * 1.5, "热尾更新 fillfactor 有效"
assert uni70 > uni100, "随机更新也有收益, 但每页预留被同页所有行共享"

# 条件1: 更新索引列, fillfactor 再低也不会有 HOT
idx100, _ = workload(100, "hot", indexed_change=True)
idx50, _ = workload(50, "hot", indexed_change=True)
print(f"[2] 更新索引列: ff100 HOT {idx100:.0%}, ff50 HOT {idx50:.0%} "
      f"(条件1 不满足, 预留空间白留)")
assert idx100 == 0 and idx50 == 0

# 空间代价: 低 fillfactor 直接放大堆页数, 顺序扫描与缓存命中一起变差
_, pages100 = workload(100, "hot")
_, pages70 = workload(70, "hot")
_, pages50 = workload(50, "hot")
print(f"[3] 空间账: 堆页 ff100={pages100}, ff70={pages70}, ff50={pages50}; "
      f"ff50 比 ff100 多 {pages50 / pages100 - 1:.0%}")
assert pages50 > pages70 > pages100
print("    → 实测 fillfactor 是'用常驻空间换索引写放大', 调过头会反噬扫描与缓存")
print("    → 另注意: 参数只影响新插入, 老页要 VACUUM FULL/pg_repack 后才享受预留")
```

**追问一**：HOT 链变长会不会让查询变慢？为什么 `VACUUM` 之后才恢复？—— HOT 更新在堆页内形成一条版本链，索引只指向链头，读的时候要顺着 `ctid` 链找到对当前快照可见的版本。链短时是页内指针跳转，成本可忽略；链很长（同一行被更新几百次且没 vacuum）时，每次读都要遍历链，且链跨越的页可能已被换出。`VACUUM` 会清理死元组、把仍被引用的版本"搬"到链头附近（heap-only tuple 的 prune），链变短，读放大下降。所以高频更新表除了 fillfactor，还要保证 autovacuum 跟得上；`pg_stat_user_tables.n_dead_tup` 与 `last_autovacuum` 是必看指标。

**追问二**：`n_tup_hot_upd/n_tup_upd` 很低，怎么区分"页满"和"更新了索引列"？—— 先看**更新语句的列**与表的索引定义：任何被更新的列出现在索引里，HOT 必然为 0，这种情况调 fillfactor 无效。排除后再看页空间：`pgstattuple` 或 `pg_freespace` 看目标表的平均空闲空间；如果 `avg_leaf_density` 很高、free space 接近 0，说明是页满。还有一个容易忽略的第三种原因：**更新把行变宽了**（如 `text` 字段变长、加了列），即使索引列没变、页里有空位，新版本也可能放不下，退化为非 HOT。三种原因对应三种解法：删/改索引、调 fillfactor + 重建、控制行宽或把大字段拆表。

## 背诵要点

- HOT 三条件：更新列不在任何索引里、新版本能放进同一堆页、不跨页；缺一条就退化为非 HOT，每个索引都要插新条目。
- `fillfactor` 只作用于"页内预留空间"，且只影响后续插入；调完必须 `VACUUM FULL`/`pg_repack` 重建才生效。
- 诊断看 `n_tup_hot_upd/n_tup_upd`；低 HOT 的三种原因——索引列被更新、页满、行变宽，对应删索引/调 fillfactor/控行宽。

## 复盘追问

- 余额表调了 fillfactor 索引还是涨，你怎么用一条 SQL 证明"更新列在索引里"？（比对 `pg_index.indkey` 与 UPDATE 的 SET 列；只要交集非空，HOT 必为 0）
- 为什么随机更新的大表调低 fillfactor 往往不划算？（预留空间被同页所有行共享、老页很快耗尽，收益随时间衰减；表却永久变大，顺序扫描与缓存都变差）
