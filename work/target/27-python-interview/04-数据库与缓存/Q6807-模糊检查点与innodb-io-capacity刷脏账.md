---
title: "[Q6807] 模糊检查点追不上：innodb_io_capacity 与刷脏速率的账"
date: 2026-11-25
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6807 · 模糊检查点追不上：innodb_io_capacity 与刷脏速率的账

难度：P7 ｜ 标签：InnoDB、checkpoint、刷脏、innodb_io_capacity、写入抖动

基线：库知识库外知识卡，用"脏页产生速率 vs 刷脏能力"的存量模型模拟 InnoDB fuzzy checkpoint 追上/追不上两种状态。

**问**：大促前 DBA 把 `innodb_io_capacity` 从 2000 调到 800，理由是"别把磁盘打满，保护在线查询"。结果压测时写入 P99 从 12ms 涨到 900ms，`Innodb_buffer_pool_pages_dirty` 贴着上限，日志里出现"flush list 超过 90%"。降低刷脏能力为什么反而让写入更慢？`innodb_io_capacity` 到底该怎么算？

**答**：

- **结论**：InnoDB 的脏页是**存量**：写入不断产生脏页，后台按 `innodb_io_capacity`（每秒可用的 IO 页数）刷脏。稳态下必须满足 `刷脏速率 ≥ 脏页产生速率 - buffer_pool_size / max_checkpoint_age`，否则脏页存量单调上涨；涨到 `max_dirty_pages_pct`（默认 90%）后，用户线程必须**同步等待刷脏**才能拿到空闲页，写入延迟从"内存操作"变成"等磁盘"。把 2000 调到 800 不是"保护磁盘"，而是把刷脏能力降到产生速率以下，主动制造了 checkpoint 追不上的死局。
- **取舍**：① `innodb_io_capacity` 应按磁盘**持续随机写 IOPS** 的 50%~70% 设，而不是按"怕打满"拍一个低值；SSD 上通常远高于默认 200；② `innodb_io_capacity_max` 是紧急上限，允许短时超发，但持续超发会挤占读 IO；③ `innodb_adaptive_flushing` 会按脏页比例动态加速，但它只能"在能力范围内加速"，不能突破物理 IOPS；④ 写入突增时，优先限流/削峰/拆分大事务，而不是砍刷脏能力。
- **实战**：① 监控 `Innodb_buffer_pool_pages_dirty / Innodb_buffer_pool_pages_total` 与 `Innodb_checkpoint_age`，长期 >70% 就是刷脏能力不足；② 压测时同时看 `iostat` 的 `w/s`、`await` 与 InnoDB 的 `OS log fsyncs`，区分"刷脏瓶颈"与"redo 瓶颈"；③ `innodb_io_capacity` 调整按 20% 步进，观察 10 分钟脏页曲线再继续；④ 大促前做写入压测，确认稳态脏页比例 <60%，别等上线后才发现。

下面用存量模型算：脏页产生速率、刷脏能力、到 90% 的时间，以及"该调多少"。

```python
# 脏页存量模型: 产生速率 vs 刷脏能力, 算 checkpoint 追赶时间
BUFFER_PAGES = 12000
MAX_AGE_S = 600
DIRTY_RATE = 800          # 页/秒
DIRTY_LIMIT = 0.9


def steady_state(dirty_rate, io_capacity, efficiency=0.5):
    flush = io_capacity * efficiency
    required = dirty_rate - BUFFER_PAGES / MAX_AGE_S   # 维持稳态所需刷脏速率
    net = dirty_rate - flush
    result = {
        "flush": flush,
        "required": required,
        "net": net,
        "time_to_limit": None,
        "sustainable": net <= 0,
    }
    if net > 0:
        result["time_to_limit"] = BUFFER_PAGES * DIRTY_LIMIT / net
    return result


low = steady_state(DIRTY_RATE, io_capacity=800)     # 被"保护磁盘"调低
high = steady_state(DIRTY_RATE, io_capacity=2000)

print(f"[1] io_capacity=800 : 刷脏={low['flush']:.0f}/s, 需要>={low['required']:.0f}/s, "
      f"净增={low['net']:.0f}/s, 到 90% 用时={low['time_to_limit']:.0f}s")
print(f"[2] io_capacity=2000: 刷脏={high['flush']:.0f}/s, 净增={high['net']:.0f}/s, "
      f"可持续={high['sustainable']}")
assert low["flush"] < low["required"]
assert low["sustainable"] is False
assert 25 <= low["time_to_limit"] <= 35
assert high["sustainable"] is True and high["time_to_limit"] is None

# 反推: 要维持稳态, io_capacity 至少多少
min_capacity = (DIRTY_RATE - BUFFER_PAGES / MAX_AGE_S) / 0.5
print(f"[3] 维持稳态的最小 io_capacity ≈ {min_capacity:.0f}")
assert min_capacity == 1560

# 脏页贴顶后的代价: 用户线程同步等刷脏
def write_latency_ms(dirty_pct, base_ms=0.2, stall_ms=900):
    if dirty_pct < DIRTY_LIMIT:
        return base_ms
    return stall_ms


print(f"[4] 脏页 60% 时写入延迟={write_latency_ms(0.6)}ms, 92% 时={write_latency_ms(0.92)}ms")
assert write_latency_ms(0.6) == 0.2 and write_latency_ms(0.92) == 900
print("    → 实测 砍刷脏能力=把内存写变成等磁盘; 应按持续 IOPS 的 50-70% 设, 不是越低越安全")
```

**追问一**：`innodb_adaptive_flushing` 开着，为什么还会贴顶？—— 自适应刷脏只能按脏页比例**提高刷脏目标**，最终受 `innodb_io_capacity`/`innodb_io_capacity_max` 与物理 IOPS 限制。如果产生速率本身就高于设备持续写能力，任何调度都只是延缓贴顶。此时唯一解是降低写入速率（限流、拆批、冷热分离）或换更高 IOPS 的盘。

**追问二**：脏页比例高一定意味着写入会慢吗？—— 不一定，关键看**是否触发用户线程同步刷脏**。脏页 80% 但刷脏能力充足、曲线平稳，写入仍然快；脏页 50% 但产生速率远高于刷脏能力，几十秒后就会贴顶。所以看"比例 + 斜率"两个量，单看瞬时比例会误判。

## 背诵要点

- 稳态条件：`刷脏速率 ≥ 脏页产生速率 - buffer_pool / max_checkpoint_age`；不满足则脏页存量单调上涨。
- 贴到 `max_dirty_pages_pct`（默认 90%）后用户线程同步等刷脏，写入 P99 从毫秒级跳到百毫秒级。
- `innodb_io_capacity` 按磁盘持续随机写 IOPS 的 50%~70% 设；调低不是保护磁盘，是制造 checkpoint 债务。

## 复盘追问

- 脏页比例和脏页斜率，哪个更能提前预警写入抖动？为什么？
- `innodb_io_capacity_max` 短时超发能救急，但持续超发的代价落在谁身上？
