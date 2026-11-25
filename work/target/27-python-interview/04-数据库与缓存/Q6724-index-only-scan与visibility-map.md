---
title: "[Q6724] index-only scan 为什么会偷偷回表：visibility map 的账"
date: 2026-11-23
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6724 · index-only scan 为什么会偷偷回表：visibility map 的账

难度：P7 ｜ 标签：PostgreSQL、index-only scan、visibility map、vacuum

基线：Python 3.12；PostgreSQL 11+ `EXPLAIN (ANALYZE, BUFFERS)`；纯 Python 模拟 VM 与 heap fetch。

**问**：给 `(user_id, created_at)` 建了联合索引，查询只取这两列，`EXPLAIN` 显示 `Index Only Scan`，但 `Heap Fetches: 980000`、`Buffers: shared read` 很高，实际并不比普通索引扫快。既然是 index-only，为什么还在读堆表？

**答**：
- **结论**：PG 的 MVCC 可见性信息不在索引里（索引项不存 `xmin/xmax` 的完整可见性判断所需状态）。`Index Only Scan` 只有在**visibility map（VM）把该页标记为 all-visible** 时才能确信"索引里的元组对当前快照可见"，从而跳过堆表；否则必须回表取元组头判断可见性，这就是 `Heap Fetches`。VM 由 `VACUUM` 设置，大量更新/插入后新页未 vacuum，VM 位是 0，index-only 就退化成"索引扫 + 逐行回表"。
- **取舍**：想真正吃到 index-only 的红利，必须让 **autovacuum 跟得上**，并接受 vacuum 的 IO 与锁开销；对于更新频繁的表，VM 位会被不断清除，index-only 收益不稳定。另一个前提是索引必须覆盖查询的全部列（含 `WHERE`、`SELECT`、`ORDER BY`），否则 planner 根本不会选 index-only。用宽索引换 heap fetch，会增加索引体积与写放大。
- **实战**：① 看 `EXPLAIN (ANALYZE, BUFFERS)` 的 `Heap Fetches`，它接近扫描行数就说明 VM 没帮上忙；② 查 `pg_stat_user_tables.n_dead_tup` 与 `last_autovacuum`，死元组多、vacuum 久未跑是典型信号；③ 调低 `autovacuum_vacuum_scale_factor`（大表默认 20% 太迟钝）或按表设置；④ 只读报表库可以跑 `VACUUM (ANALYZE)` 后再做基准，别在交易库高峰手动 full vacuum。

```python
"""index-only scan 的堆回表次数 = 未被 VM 标记 all-visible 的元组数。"""
from dataclasses import dataclass


@dataclass
class Page:
    page_id: int
    tuples: int
    all_visible: bool


def index_only_scan(pages: list[Page]) -> tuple[int, int, float]:
    index_entries = sum(p.tuples for p in pages)
    heap_fetches = sum(p.tuples for p in pages if not p.all_visible)
    visible_ratio = 1 - heap_fetches / index_entries
    return index_entries, heap_fetches, visible_ratio


def simulate(pages: int = 1000, tuples_per_page: int = 100,
             vm_ratio: float = 0.2) -> tuple[int, int, float]:
    visible_pages = int(pages * vm_ratio)
    data = [Page(i, tuples_per_page, i < visible_pages) for i in range(pages)]
    return index_only_scan(data)


if __name__ == "__main__":
    for ratio in (0.0, 0.2, 0.8, 1.0):
        entries, fetches, vis = simulate(vm_ratio=ratio)
        print(f"VM all-visible={ratio:>4.0%}  索引项={entries:>7}  "
              f"Heap Fetches={fetches:>7}  实际可见比例={vis:.0%}")
    print("结论：VM 未置位的页，index-only 仍要回表；vacuum 跟不上就白建覆盖索引")
```

**追问一**：为什么 `VACUUM` 之后 `Heap Fetches` 还是很高？
→ 解析：可能① 表在 vacuum 后又大量插入/更新，新页没有 VM 位；② 长事务持有旧快照，阻止 vacuum 推进 `xmin`，页无法标记 all-visible；③ 查询的快照比 VM 新，部分元组仍需回表确认；④ 索引本身不包含所有列，planner 虽然显示 Index Only Scan，但表达式或系统列触发了 heap 访问。

**追问二**：能不能干脆把可见性信息放进索引，彻底消灭回表？
→ 解析：理论上可以（某些索引组织表/覆盖索引引擎这么做），但 PG 的索引项要与 heap 的 `xmin/xmax` 保持同步，更新时要改所有索引项，写放大极大；而且索引项变宽会降低扇出、增加缓存压力。VM 是"页级粗粒度 + 后台批量维护"的折中，牺牲实时性换写入成本。
