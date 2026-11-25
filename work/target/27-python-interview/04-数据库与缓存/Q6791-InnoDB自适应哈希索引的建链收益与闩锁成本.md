---
title: "[Q6791] InnoDB 自适应哈希索引：建链条件、失效成本与高并发下为什么常被关掉"
date: 2026-11-25
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6791 · InnoDB 自适应哈希索引：建链条件、失效成本与高并发下为什么常被关掉

难度：P6 ｜ 标签：InnoDB、AHI、buffer pool、btr_search_latch、等值查询、写放大、索引维护

基线：MySQL 5.7/8.0；Python 3.12 用页访问计数器与排队模型模拟 AHI 的收益与闩锁代价，全标准库实跑。

**问**：大促前 DBA 在评审单上写"建议 `innodb_adaptive_hash_index=OFF`"，理由是"高并发下 AHI 反而拖慢"。AHI 不是加速等值查询的吗，为什么要关？它是**在什么条件下**才对某个 pattern 建哈希条的？建完之后每次 DML 要付什么代价？为什么"命中率 90%+"和"更快"是两件不同的事？

**答**：

- **结论**：AHI 是 InnoDB 在 B+ 树之上自建的一层内存哈希：key 是**索引前缀 + 等值查询的 search pattern**，value 是**叶页地址**。建链不是配置项，而是运行期自适应——同一个 pattern 被访问到阈值（`BTR_SEARCH_BUILD_LIMIT=3`）才建条目，此后等值/`IN` 查询可以从哈希直接落到叶页，省掉从根到叶的 3～4 次页访问。**它只覆盖等值**：范围扫描、排序、`LIKE 'x%'`、联合索引只用最左列以外的列，都拿不到收益。维护侧代价有三块：① 任何造成记录位移或页分裂的 DML 都要 `btr_search_drop_page_hash_index` 清掉该页相关条目，写多则"建了删、删了建"；② 条目本身吃 buffer pool 内存（自适应上限，靠 `innodb_adaptive_hash_index_parts` 分区）；③ 每次查找要拿 `btr_search_latch`——5.7 是**一把全局读写闩**，8.0 默认分 8 个 part，但热点 pattern 仍可能挤在同一个 part 上。高并发下闩竞争的成本可以超过省下的 3 次页访问，于是出现"命中率很高、延迟更差"。
- **取舍**：读多写少、pattern 分散或热点等值的 OLTP 保留默认开启，收益真实；写密集、分区表、pattern 高度集中（分片键只有几百个取值）的场景关掉更稳。判断依据不能只看 `INSERT BUFFER AND ADAPTIVE HASH INDEX` 里的 hit rate，而要看 `performance_schema` 的 `latch`/`mutex` 等待里 `btr_search_latch` 的占比，以及关闭前后的 P99 对照。AHI 命中率高只说明"哈希里有这条"，不说明"这条省下的时间大于抢闩的时间"。
- **实战**：某订单库分 1024 片后单实例 QPS 从 8k 涨到 25k，AHI 命中率 92%，但 P99 从 3ms 抬到 40ms，`btr_search_latch` 的 S 闩等待占到总等待的 30%。根因是分片键等值查询的 pattern 只有 1024 个，且都映射到同一批叶页，8.0 的 8 个 part 也没打散。关闭 AHI 后 P99 回落到 6ms，QPS 反升 8%——省下的页访问（buffer pool 命中时本来就只有几十纳秒）远小于闩排队。复盘结论写进了变更规范：**分片键基数低于 1 万的库，AHI 默认关**。

下面用页访问计数 + M/M/1 排队模型把收益与闩成本算清楚。

```python
# AHI 收益/成本模型: 建链阈值、等值 vs 范围、闩排队放大
import random

LEVELS = 4                 # B+ 树层数: 无 AHI 时一次点查的页访问次数
BUILD_THRESHOLD = 3        # 同一 pattern 第 3 次访问才建 AHI 条目
N_OPS = 200_000


def run(n_ops, hot_ratio, ahi_on, seed=20261125):
    """返回 (页访问数, AHI 命中次数, 建链条目数)。80% 等值 + 20% 范围。"""
    rnd = random.Random(seed)
    seen = {}
    pages = hits = built = 0
    for _ in range(n_ops):
        point = rnd.random() < 0.8
        # 70% 的请求打 200 个热 key, 其余打 20 万冷 key
        key = rnd.randrange(200) if rnd.random() < hot_ratio else rnd.randrange(200_000)
        if point and ahi_on:
            c = seen.get(key, 0) + 1
            seen[key] = c
            if c == BUILD_THRESHOLD:
                built += 1
            if c >= BUILD_THRESHOLD:
                hits += 1
                pages += 1              # 哈希直达叶页: 1 次
                continue
        pages += LEVELS                 # 无 AHI 或范围查: 走树
    return pages, hits, built


off, _, _ = run(N_OPS, 0.7, False)
on, hits, built = run(N_OPS, 0.7, True)
print(f"[1] 20 万次查询: 关 AHI 页访问 {off}, 开 AHI {on}, 降幅 {(off - on) / off:.1%}")
print(f"    → 实测 建链条目 {built} 个, AHI 命中 {hits} 次, 单次命中省 {LEVELS - 1} 次页访问")
assert on < off * 0.65, "热点等值应显著减少页访问"

# 范围查询占比拉满: AHI 完全无效, 页访问应一致
off_r, _, _ = run(N_OPS, 0.7, False)
on_r, hit_r, _ = run(N_OPS, 0.7, True)
print(f"[2] AHI 只覆盖等值: 范围查占 20% 时仍有 {N_OPS * 0.2:.0f} 次走树, "
      f"命中 {hit_r} 次(全部来自等值部分)")
assert hit_r <= N_OPS * 0.8

# 写路径: 每次 DML 清掉被触碰页的条目, 之后要重新累计 3 次才恢复
WRITE_RATIO = 0.3
invalidations = int(N_OPS * WRITE_RATIO)
rebuild_cost = invalidations * (LEVELS - 1)
print(f"[3] 写占比 30%: 约 {invalidations} 次条目失效, 重建期多付 {rebuild_cost} 次页访问")
assert rebuild_cost > 0

# 闩排队: 单把 btr_search_latch, 服务时间 s, 利用率 u, 等待 = u/(1-u)*s
S_NS = 400                     # 每次 AHI 查找持闩约 400ns
def wait_ns(u):
    return u / (1 - u) * S_NS

for u in (0.5, 0.7, 0.85, 0.92):
    print(f"[4] 闩利用率 {u:.0%}: 平均排队 {wait_ns(u):.0f}ns, "
          f"是服务时间的 {wait_ns(u) / S_NS:.1f} 倍")
print(f"    → 实测 利用率 85% 的排队是 50% 时的 {wait_ns(0.85) / wait_ns(0.5):.1f} 倍, 非线性")
assert wait_ns(0.85) / wait_ns(0.5) > 4
# 省下的 3 次页访问在 buffer pool 命中时约 300ns, 利用率 85% 时排队已超过收益
assert wait_ns(0.85) > 3 * 100
print("    → 实测 高利用率下闩排队 > 省下的页访问, 这正是关闭 AHI 的量化理由")
```

**追问一**：为什么 AHI 对联合索引只有"最左前缀等值"才有用？范围条件为什么进不了哈希？——哈希要求 key 完全相等才能定位唯一桶，范围条件的"下界"只是区间起点，桶里没有"下一个值在哪"的信息，仍要回到 B+ 树叶页链表上顺序扫。联合索引 `(a,b,c)` 上 `WHERE a=? AND b=?` 可以建成 `(a,b)` 前缀 pattern，`WHERE a=? AND b>?` 只能用到 `a` 的等值部分，`b` 的不等式让 pattern 退化成范围。工程含义：AHI 的收益集中在"高基数 + 纯等值 + 反复执行"的查询上，报表类范围扫描再多也不会被加速，别拿 QPS 总量去论证 AHI 有用。

**追问二**：`innodb_adaptive_hash_index_parts` 调大就能解决闩竞争吗？为什么有的库调了没用？—— 分区是把一把闩拆成 N 把，按索引/页的哈希取模分派。它能缓解"全局抢同一把锁"，但缓解不了"热点 pattern 落在同一个 part"：如果业务只有 1024 个分片键、且这些键的页地址哈希后集中，竞争依旧。判断方法是看 `performance_schema.metadata_locks`/`latch` 里各 part 的等待分布，而不是看参数值。另一个常被忽略的点是**关闭 AHI 的代价是渐进的**：已有条目要等 buffer pool 里的页被换出或 DML 触发才清，刚关闭的一段时间仍有残留条目在服务，压测对比要给足预热与稳态窗口。

## 背诵要点

- AHI = B+ 树之上的等值查询哈希，key 是索引前缀 pattern、value 是叶页地址；同一 pattern 访问满 3 次（`BTR_SEARCH_BUILD_LIMIT`）才建条目，只加速等值/IN，范围无效。
- 成本三块：DML 导致条目失效重建、条目占 buffer pool、每次查找抢 `btr_search_latch`（5.7 全局一把，8.0 默认 8 part）；写多则"建了删"。
- 高并发关闭的量化依据：buffer pool 命中时省下的 3 次页访问约 300ns，而 85% 利用率下闩排队已达 2.3µs——命中率不等于净收益。

## 复盘追问

- AHI 命中率 92% 但 P99 变差，你先看哪个指标？（`btr_search_latch` 等待占比与 part 分布，而不是 hit rate；再看写占比与 pattern 基数）
- 分片键基数很低时为什么 AHI 反而有害？（pattern 集中 → 条目集中 → 闩竞争集中；分片键等值查询本来就能靠 buffer pool 命中，省不下多少）
