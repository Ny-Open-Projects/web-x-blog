---
title: "[Q6806] Bitmap Heap Scan 的 lossy 位图：为什么会多出 10 倍 recheck"
date: 2026-11-25
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6806 · Bitmap Heap Scan 的 lossy 位图：为什么会多出 10 倍 recheck

难度：P7 ｜ 标签：PostgreSQL、bitmap scan、lossy、work_mem、Recheck Cond

基线：库知识库外知识卡，用"页级位图 vs 元组级位图"模拟 PG 的 Bitmap Heap Scan 与 `Recheck Cond`，不依赖 PG 实例。

**问**：一张 2 亿行的日志表，查"某类错误 + 最近一小时"，`EXPLAIN ANALYZE` 显示 `Bitmap Heap Scan`、`Rows Removed by Index Recheck: 1.8 亿`，CPU 打满、查询 6 分钟。索引明明只命中 60 万行，为什么 recheck 了 1.8 亿？`work_mem` 调大为什么立刻降到 8 秒？lossy 位图到底丢了什么？

**答**：

- **结论**：PG 的 bitmap index scan 先在内存里构造"哪些**页**/哪些**元组**可能命中"的位图。当 `work_mem` 不足以容纳精确到元组的位图时，PG 会**降级为 lossy 位图**：每页只保留 1 bit，表示"这页可能有命中"，丢掉页内偏移。回表时只能把该页**所有元组**都读出来，再对每行重新执行 `Recheck Cond` 过滤——于是 recheck 行数从"索引命中数"膨胀到"命中页数 × 每页元组数"。1.8 亿不是索引命中了 1.8 亿，而是位图丢精度后被迫重查了 1.8 亿。
- **取舍**：① 调大 `work_mem`：位图能精确到元组，recheck 降到命中行数，代价是每个排序/哈希/bitmap 节点都能用到这么多内存，并发一高就 OOM——它是**每节点每查询**的上限，不是全局；② 减少扫描页数：加更 selective 的索引/分区裁剪，让位图本身变小；③ 用普通 Index Scan 代替 Bitmap：随机 IO 多但 recheck 少，SSD 上常常更稳；④ 接受 lossy：如果命中页本来就稀疏，recheck 的代价可接受，别盲目调大内存。
- **实战**：① 看到 `Rows Removed by Index Recheck` 远大于 `actual rows`，第一反应是 `work_mem` 不足导致 lossy；② 用 `EXPLAIN (ANALYZE, BUFFERS)` 看 `Heap Blocks: exact/lossy`，lossy 比例高就是信号；③ `work_mem` 按"并发数 × 单查询节点数 × 设定值"估算总内存，宁可会话级 `SET LOCAL` 也不要全局调大；④ 高频查询优先做覆盖索引/分区裁剪，把位图规模降下来，比调内存更可持续。

下面模拟精确位图与 lossy 位图：同样的谓词，lossy 必须重查整页。

```python
# lossy bitmap: 每页 1 bit, 回表时整页元组都要 Recheck
PAGES, TUPLES_PER_PAGE = 10, 100
MATCH_OFFSETS = {7}          # 每页只有第 7 个元组真正命中


def exact_bitmap():
    candidates = {(p, o) for p in range(PAGES) for o in MATCH_OFFSETS}
    checked = len(candidates)          # 只回表候选元组
    recheck = 0                        # 精确位图无需页内重查
    return len(candidates), checked, recheck


def lossy_bitmap():
    pages = {p for p in range(PAGES)}  # 每页都有命中 -> 10 个页 bit
    checked = len(pages) * TUPLES_PER_PAGE
    matched = len(pages) * len(MATCH_OFFSETS)
    recheck = checked - matched        # 页内非候选元组全部重查
    return matched, checked, recheck


exact_rows, exact_checked, exact_recheck = exact_bitmap()
lossy_rows, lossy_checked, lossy_recheck = lossy_bitmap()
print(f"[1] 精确位图: 结果={exact_rows}, 回表={exact_checked}, recheck={exact_recheck}")
print(f"[2] lossy 位图: 结果={lossy_rows}, 回表={lossy_checked}, recheck={lossy_recheck}")
assert exact_rows == lossy_rows == 10
assert lossy_checked == (TUPLES_PER_PAGE // len(MATCH_OFFSETS)) * exact_checked
assert lossy_recheck == 990
print("    → 实测 结果一样, 但 lossy 多读了 100 倍元组、多做 990 次谓词求值")

# 稀疏命中页时, lossy 的放大倍数 = 每页元组数 / 每页命中数
def amplification(tuples_per_page, hits_per_page):
    return tuples_per_page / hits_per_page


for hits in (1, 5, 50):
    amp = amplification(TUPLES_PER_PAGE, hits)
    print(f"[3] 每页命中 {hits} 行: 读放大 {amp:.0f}x")
assert amplification(100, 1) == 100
assert amplification(100, 50) == 2
print("    → 实测 命中越稀疏, lossy 的 recheck 放大越狠; 调 work_mem 或减页数是正解")
```

**追问一**：`work_mem` 调大后，为什么有时反而更慢？—— 位图精确了，但内存分配、位图构造和并发下降都可能增加；更常见的是 `work_mem` 是**每个节点**的上限，一条复杂查询有多个排序/哈希节点，实际占用是倍数关系，系统开始 swap 后整体变慢。正确做法是会话级 `SET LOCAL work_mem` 只给这条查询，并监控 `pg_stat_statements` 的 `temp_blks_written` 确认没有落盘。

**追问二**：为什么 Bitmap Heap Scan 要先做位图，不直接按索引顺序回表？—— 位图把"按索引顺序的随机回表"变成"按页号顺序的批量回表"，同一页只读一次，减少随机 IO；同时能对多个索引的位图做 AND/OR 合并。代价就是位图内存与 lossy 降级。它是 IO 与内存的交换，不是无条件更优。

## 背诵要点

- `work_mem` 不足 → 位图从元组级降级为**页级 lossy**，回表要重查整页，`Rows Removed by Index Recheck` 暴涨。
- 放大倍数 ≈ 每页元组数 / 每页命中数；命中越稀疏越严重。
- 处理顺序：`EXPLAIN (ANALYZE, BUFFERS)` 看 `Heap Blocks: lossy` → 会话级调 `work_mem` → 更根本的是分区裁剪/覆盖索引减少扫描页。

## 复盘追问

- 为什么 `work_mem` 是"每节点"而不是"每查询"？一条有 3 个排序节点的查询实际可能占多少？
- lossy 位图下，`Recheck Cond` 重查的是索引条件还是所有过滤条件？这会影响哪些索引设计？
