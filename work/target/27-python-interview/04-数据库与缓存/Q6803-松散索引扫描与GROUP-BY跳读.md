---
title: "[Q6803] 松散索引扫描：GROUP BY 为什么能只读 3 条索引项"
date: 2026-11-25
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6803 · 松散索引扫描：GROUP BY 为什么能只读 3 条索引项

难度：P7 ｜ 标签：MySQL、松散索引扫描、GROUP BY、覆盖索引、执行计划

基线：库知识库外知识卡，用有序索引项列表模拟 MySQL 的 tight/loose index scan 读取数量，不依赖 MySQL。

**问**：一张 8000 万行的埋点表，索引 `(tenant_id, created_at)`，`SELECT tenant_id, MAX(created_at) FROM events GROUP BY tenant_id` 平时 0.8 秒。某天报表加了一个 `COUNT(*)`，同一条 SQL 跑了 38 分钟，把从库拖到延迟 20 分钟。为什么多一个 `COUNT(*)` 就从"跳着读"退化成"全索引扫完"？松散索引扫描到底省的是什么？哪些写法会让它失效？

**答**：

- **结论**：**松散索引扫描（loose index scan）**利用索引有序性，对每个分组只做一次"定位 + 跳读"，读完该组的第一条就直接跳到下一组的起点，读取量与**分组数**成正比，而不是行数。`MAX/MIN` 只需要每组的第一条/最后一条，所以 1.2 万个租户只读约 1.2 万条索引项。**`COUNT(*)` 需要知道每组的行数**，必须逐条扫过组内所有索引项，于是退化成**紧凑索引扫描（tight index scan）**，读取量变成 8000 万。这不是优化器"变笨"，是语义决定了下界：不数完怎么知道有多少行。
- **取舍**：① 想要"每组计数"又不想全扫，维护**汇总表**（按 tenant_id + 天预聚合），用空间换读放大；② 或者接受一次全索引扫描，但放到离线/从库，限速并错峰；③ 如果只是要"有没有数据/最大时间"，坚持 `MAX/MIN` + `EXISTS`，别顺手加 `COUNT(*)`；④ 松散扫描的适用条件很窄：必须是 `GROUP BY` 的最左前缀、只能有 `MIN/MAX/COUNT(DISTINCT)`、不能有对该列的范围条件、不能 `SELECT` 非分组列（除非函数依赖）。任一不满足就退化。
- **实战**：① 报表 SQL 上线前看 `EXPLAIN` 的 `Extra` 是否含 `Using index for group-by`，没有就按行数估算耗时；② 大表 `GROUP BY` 一律加 `LIMIT`/租户过滤，避免全租户聚合；③ 把 `COUNT(*)` 类需求迁到预聚合表，源表只保留 `MAX/MIN` 的轻查询；④ 从库上跑分析查询要设 `MAX_EXECUTION_TIME`，避免一条 SQL 拖垮复制。

下面用索引项列表对比 tight 与 loose 的读取量，并演示 `COUNT(*)` 如何让 loose 失效。

```python
# 松散索引扫描: 每组只读一条索引项; COUNT(*) 必须读完整组
INDEX = [(1, "a"), (1, "b"), (1, "c"),
         (2, "a"), (2, "d"),
         (3, "a"), (3, "b"), (3, "e")]


def tight_scan(index):
    rows, groups, last = 0, [], None
    for tenant, _ts in index:
        rows += 1
        if tenant != last:
            groups.append(tenant)
            last = tenant
    return groups, rows


def loose_scan(index, need_count_star=False):
    if need_count_star:
        return tight_scan(index)          # 语义要求数完, 只能 tight
    groups, rows, i = [], 0, 0
    while i < len(index):
        tenant = index[i][0]
        groups.append(tenant)
        rows += 1                          # 一次定位, 组内其余条目跳过
        while i < len(index) and index[i][0] == tenant:
            i += 1
    return groups, rows


g1, r1 = tight_scan(INDEX)
g2, r2 = loose_scan(INDEX)
g3, r3 = loose_scan(INDEX, need_count_star=True)
print(f"[1] tight: 分组={g1}, 读取={r1} 条")
print(f"[2] loose(MAX): 分组={g2}, 读取={r2} 条")
print(f"[3] loose + COUNT(*): 分组={g3}, 读取={r3} 条 (退化)")
assert g1 == g2 == g3 == [1, 2, 3]
assert r1 == 8 and r2 == 3 and r3 == 8
print("    → 实测 3 个分组只读 3 条; 加 COUNT(*) 后退化回 8 条")

# 适用条件: 对分组列做范围过滤, 松散扫描也失效
def can_loose(has_range_on_group_col, has_count_star, selects_non_grouped):
    return not (has_range_on_group_col or has_count_star or selects_non_grouped)


cases = {
    "MAX + 纯分组": (False, False, False),
    "加 COUNT(*)": (False, True, False),
    "WHERE tenant_id > 100": (True, False, False),
    "SELECT 非分组列": (False, False, True),
}
for name, flags in cases.items():
    print(f"[4] {name}: 可用松散扫描={can_loose(*flags)}")
assert can_loose(False, False, False) is True
assert can_loose(False, True, False) is False
print("    → 实测 四个条件任一破坏都退回紧凑扫描")
```

**追问一**：松散索引扫描为什么要求 `GROUP BY` 用最左前缀？—— 因为跳读依赖"相同前缀的索引项物理相邻"。如果分组列不是最左列，索引里同组的行不连续，无法"读完一条就跳到下一组"，只能全扫后做临时表/排序。前缀顺序决定了有序性，有序性决定了能不能跳。

**追问二**：`COUNT(DISTINCT)` 为什么能松散，`COUNT(*)` 不能？—— `COUNT(DISTINCT col)` 只需知道"有哪些不同的值"，可以按索引跳读去重；`COUNT(*)` 需要每组的行数，必须逐条累加。前者是"集合大小"，后者是"多重集计数"，语义不同，读取下界也不同。

## 背诵要点

- 松散索引扫描的读取量 ∝ **分组数**，每组只定位一次；`MAX/MIN` 天然适合，`COUNT(*)` 必须数完所有行。
- 失效条件：非最左前缀、`COUNT(*)`、分组列上的范围条件、`SELECT` 非分组列；`EXPLAIN` 看 `Using index for group-by`。
- 大表分组计数走预聚合表或离线从库；源表只留 `MAX/MIN` 轻查询，并设 `MAX_EXECUTION_TIME`。

## 复盘追问

- `SELECT tenant_id, MAX(created_at) FROM t WHERE created_at > '2026-01-01' GROUP BY tenant_id` 还能松散吗？为什么？
- 如果必须在线拿"每组行数"，除了预聚合表还有哪些不扫全索引的办法？各自的误差/新鲜度代价是什么？
