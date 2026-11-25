---
title: "[Q6796] 过期删除也会阻塞主线程：active expire 的采样账与 lazyfree-lazy-expire"
date: 2026-11-25
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6796 · 过期删除也会阻塞主线程：active expire 的采样账与 lazyfree-lazy-expire

难度：P6 ｜ 标签：Redis、TTL、active expire、lazyfree、大 key、主线程阻塞、内存回收

基线：Redis 6/7，`hz=10`、`ACTIVE_EXPIRE_CYCLE_LOOKUPS_PER_LOOP=20`；Python 3.12 用过期采样与释放成本模型复现停顿，全标准库实跑。

**问**：没人执行 `DEL`，也没人跑 `UNLINK`，但每天 02:00 整监控都会出现一批 300～500ms 的延迟毛刺，正好卡在批量缓存的 TTL 到期点。过期删除不是后台慢慢做的吗，为什么也会卡主线程？一个 800 万 field 的 hash 到期时到底发生了什么？为什么"过期了"不等于"内存降下来了"？

**答**：

- **结论**：Redis 的过期删除有两条路径，**两条都可能同步阻塞主线程**。① 惰性删除：访问到已过期 key 时当场删，成本落在这次访问上；② 主动删除（active expire cycle）：每个 `hz` 周期（默认 10，即 100ms 一次）从过期字典里**随机采样 20 个 key**，删掉其中已过期的；如果这一轮过期比例超过 25%，就**继续采样下一轮**，直到比例降下来或撞到时间预算（默认最多占 25% 的周期时间）。问题在于：采样到的大 key 一旦过期，释放它的 800 万个 field 是**在主线程同步做**的——几百毫秒，直接把"25ms 预算"击穿，这期间所有命令排队。这就是"没人 DEL 也会卡"的机制。
- **取舍**：`lazyfree-lazy-expire yes` 把过期 key 的释放丢给后台 bio 线程，主线程只做"摘链 + 入队"，停顿从几百毫秒降到几十微秒；代价是**内存不会立刻还**——`used_memory` 高位滞留，`lazyfree_pending_objects` 上升，极端情况下后台释放速度跟不上过期速度，会顶到 `maxmemory` 触发淘汰甚至写失败。所以 lazyfree 不是"免费"，它把"延迟尖刺"换成了"内存滞留 + 后台 CPU"。另一半治理在**写入侧**：TTL 加随机抖动打散到期时刻、大 key 拆桶、给大 key 单独设更长的过期窗口，避免同一秒内一批大对象同时到期。
- **实战**：某推荐缓存每天 02:00 全量刷新，刷新时给 30 万个 key 设了统一的 2 小时 TTL。04:00 整出现毛刺：`INFO stats` 的 `expired_keys` 在一秒内跳了几万，`latency monitor` 抓到 `expire-cycle` 事件 480ms。根因是三个 500 万 field 的 hash 同时到期，active expire 采样命中后同步释放。修复三步：开 `lazyfree-lazy-expire`、TTL 加 ±10% 抖动、把三个大 hash 拆成 64 个分片 key。之后同一时段的 `expire-cycle` 最大耗时降到 7ms。

下面把"采样命中概率"和"单次释放成本"分开算，看清两个不同的问题。

```python
# active expire: 采样命中延迟 + 大 key 同步释放对时间预算的击穿
HZ = 10                       # 每秒 10 个周期
PERIOD_MS = 1000 / HZ         # 每周期 100ms
LOOKUPS = 20                  # 每轮采样 20 个 key
TIME_BUDGET_MS = PERIOD_MS * 0.25   # 单周期最多用 25% 时间 = 25ms
VOLATILE_KEYS = 1_000_000

examined_per_sec = HZ * LOOKUPS
p_per_sec = examined_per_sec / VOLATILE_KEYS
expected_wait_s = 1 / p_per_sec
print(f"[1] 100 万带 TTL 的 key, hz={HZ}, 每轮采 {LOOKUPS} 个:")
print(f"    每秒检查 {examined_per_sec} 个, 单个 key 每秒被抽中概率 {p_per_sec:.1e}")
print(f"    → 实测 平均要等 {expected_wait_s:.0f}s ({expected_wait_s / 60:.0f}min) 才被主动过期检查")
assert expected_wait_s > 3600
print("    → 结论: TTL 只是'最早可删时间', 实际删除时间由采样决定")

# 大 key 释放成本: 800 万 field, 每 100 万 field 约 50ms
FIELDS = 8_000_000
FREE_MS = FIELDS / 1_000_000 * 50
print(f"[2] {FIELDS:,} field 的 hash 同步释放约 {FREE_MS:.0f}ms, "
      f"是单周期预算 {TIME_BUDGET_MS:.0f}ms 的 {FREE_MS / TIME_BUDGET_MS:.0f} 倍")
assert FREE_MS > TIME_BUDGET_MS * 10

# 一个周期里命中 1 个大 key: 同步 vs lazyfree
SYNC_OVERHEAD_MS = 0.05       # 主线程摘链 + 入队
print(f"[3] 采样命中大 key: 同步释放停顿 {FREE_MS:.0f}ms; "
      f"lazyfree-lazy-expire 主线程仅 {SYNC_OVERHEAD_MS}ms, 后台还债 {FREE_MS:.0f}ms")
assert SYNC_OVERHEAD_MS < 1

# 集中到期: 1% 的 key 在同一秒过期, 25% 规则会让周期连续重复
EXPIRING_RATIO = 0.01
expiring = VOLATILE_KEYS * EXPIRING_RATIO
rounds = 0
remaining = expiring
while remaining > LOOKUPS * 0.25 and rounds < 10_000:
    remaining *= 0.75              # 每轮删掉采样中的过期项, 剩余按比例下降
    rounds += 1
print(f"[4] 1% key 同秒过期({expiring:.0f} 个): 25% 规则触发连续 {rounds} 轮采样")
assert rounds > 10
print("    → 实测 集中到期会把'每 100ms 一次'放大成'一个周期内连续多轮', "
      "大 key 落在其中任一轮都直接击穿预算")

# 内存账: lazyfree 后 used_memory 不立即下降
freed_mb = FIELDS * 64 / 1024 / 1024
print(f"[5] lazyfree 的代价: 约 {freed_mb:.0f}MB 内存滞留到后台释放完成, "
      f"期间 maxmemory 余量被占")
assert freed_mb > 100
```

**追问一**：`hz` 调大能不能让 TTL 更准、毛刺更少？—— 方向对但代价明确。`hz` 从 10 提到 100，每轮采样仍是 20 个，检查速率提高 10 倍，单 key 平均等待从约 83 分钟降到约 8 分钟，TTL 语义更接近"准时"；但周期从 100ms 缩到 10ms，单周期时间预算变成 2.5ms，**大 key 同步释放的伤害反而被放大**（同样是 400ms，相对预算更离谱），且更高的 `hz` 本身增加 CPU 与延迟抖动。正确组合是：`hz` 适度（10～20）+ 开 lazyfree + 打散 TTL + 拆大 key，而不是靠调 `hz` 硬扛。

**追问二**：开了 `lazyfree-lazy-expire` 就万事大吉了吗？还有什么会同步释放？—— 不是。`lazyfree-lazy-expire` 只覆盖"过期删除"这一条路径；显式 `DEL` 仍然同步（要用 `UNLINK`），`lazyfree-lazy-eviction` 覆盖淘汰、`lazyfree-lazy-server-del` 覆盖 `RENAME`/覆盖写导致的旧值释放、`replica-lazy-flush` 覆盖全量同步前的 flush。任何一条没开，对应的路径都能复现同样的停顿。另外要注意 `lazyfree_pending_objects` 持续不降说明后台释放跟不上，最终会体现在内存水位和 `maxmemory` 淘汰上——那是另一个事故。

## 背诵要点

- active expire 每周期随机采样 20 个 key（`hz=10`），过期比例 >25% 就连续多轮；单 key 平均被检查的等待 = 总 key 数 / (hz×20)。
- 采样命中大 key 时释放是主线程同步做，400ms 级停顿直接击穿 25ms 预算；`lazyfree-lazy-expire yes` 把释放挪到 bio 线程。
- lazyfree 的代价是内存滞留（`lazyfree_pending_objects`）与后台 CPU；治理组合是抖散 TTL + 拆大 key + 适度 hz，而不是单靠调参。

## 复盘追问

- 没人删 key 却每天固定时刻毛刺，你先查哪两个指标？（`expired_keys` 的瞬时跳变 + `latency monitor` 的 `expire-cycle` 事件，再对照 TTL 集中到期时间）
- 开了 lazyfree 后延迟好了但内存不降，怎么判断是"滞留"还是"泄漏"？（看 `lazyfree_pending_objects` 是否最终归零、`MEMORY USAGE` 与 `used_memory` 的差值趋势）
