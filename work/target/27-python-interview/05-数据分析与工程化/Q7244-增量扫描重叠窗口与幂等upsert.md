---
title: "[Q7244] 增量扫描的 updated_at 水位：不重叠漏更新，重叠了靠什么去重"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7244 · 增量扫描的 updated_at 水位：不重叠漏更新，重叠了靠什么去重

难度：P6 ｜ 标签：增量同步、水位线、重叠窗口、幂等 upsert、updated_at

基线：Python 3.12；模拟扫描窗口与写入并发竞争，对比零重叠与重叠窗口的漏抓/重复率。

**问**：增量同步用 `WHERE updated_at > last_watermark` 拉取，每天偶发丢几行更新；把条件放宽成 `>=`（重叠 5 分钟）后不丢了，但下游每天收到一批"重复行"。为什么精确的水位线天然会漏？重叠窗口抓回来的重复行，下游要怎么消化才安全？

**答**：
- **结论**：`>` 水位线漏更新的根因是**扫描与写入的竞争**：某行 updated_at=10:00:05 在 10:00:04 提交、但扫描事务的快照建在它提交之前，而水位线已经推进到 10:00:00 之后的新批次——下次扫描条件 `> 10:00:00` 反而抓不到它（它的时间戳小于新水位）。更隐蔽的是**长事务**：事务开始时 updated_at 是 09:59，提交在 10:05，如果水位线已推到 10:00，这行永远漏掉。解法不是追求精确水位，而是**有意的重叠 + 幂等消化**：条件改成 `>= last_watermark - overlap`，下游按主键 upsert（Q1726 幂等合并写），重复行被自然覆盖，代价只是多拉一小段数据。
- **取舍**：① 重叠量取"上游最大事务时长 + 管道延迟"，典型 5~15 分钟；② 下游必须幂等：同主键按 updated_at 较新者保留（LWW）或直接整行覆盖，绝不能 append 去重表否则重复堆积；③ 水位线只防"前进"，防不住"时钟回拨"（Q2275），重叠窗口顺带兜住回拨；④ 如果上游没有 updated_at 或不可信，只能改 CDC 订阅 binlog，成本高但精确。
- **实战**：① 水位线与重叠量写成任务参数并记录在运行清单（Q2537），变更走评审；② 每天统计"重叠窗口重复行占比"，暴涨说明上游事务变长或管道延迟变大；③ 对账兜底：每日全量校验关键表行数与抽样 checksum（Q1409 思路），增量漏抓最终靠对账暴露。

```python
"""增量水位：零重叠漏更新 vs 重叠窗口 + LWW 幂等消化重复。"""
Record = tuple  # (id, value, updated_min)


def scan(rows: dict[int, list[Record]], watermark: int, overlap: int) -> list[Record]:
    """抓 updated_min >= watermark - overlap 的行。"""
    out = []
    for rid, versions in rows.items():
        for _rid, v, t in versions:
            if t >= watermark - overlap:
                out.append((rid, v, t))
    return out


def upsert_lww(table: dict[int, Record], batch: list[Record]) -> int:
    """下游幂等 upsert：同主键保留 updated_min 更大的版本。返回被忽略的重复数。"""
    ignored = 0
    for rid, v, t in batch:
        cur = table.get(rid)
        if cur and cur[2] >= t:
            ignored += 1
            continue
        table[rid] = (rid, v, t)
    return ignored


if __name__ == "__main__":
    # 上游行版本：r3 在水位推进后才提交旧时间戳的更新（长事务）
    rows = {
        1: [(1, "v1", 5)],
        2: [(2, "v1", 7)],
        3: [(3, "v0", 3), (3, "v2", 9)],   # v2 时间戳 9，将在下一批水位 10 之后才被发现
    }
    truth = {1: "v1", 2: "v1", 3: "v2"}

    for overlap, label in ((0, "零重叠 >"), (2, "重叠 2 分钟 >=")):
        table: dict[int, Record] = {}
        ignored = 0
        wm = 8                              # 第一批水位
        ignored += upsert_lww(table, scan(rows, wm, overlap))
        wm = 10                             # 第二批水位推进
        ignored += upsert_lww(table, scan(rows, wm, overlap))
        got = {k: v[1] for k, v in table.items()}
        missed = {k for k in truth if got.get(k) != truth[k]}
        print(f"{label:<14} 终态={got} | 漏抓={sorted(missed) or '无'}"
              f" | 被幂等忽略的重复={ignored}")
    print("\n结论：精确水位防不住长事务与扫描竞争；重叠窗口+幂等 upsert 才是工程解")
    print("      重叠量 = 上游最大事务时长 + 管道延迟，重复率是上游健康度的探针")
```

**追问一**：为什么不用 `updated_at > watermark` 换成 `commit 时间 > watermark`（按提交时间抓）？

→ 解析：提交时间（PG 的 xmin 提交序、MySQL 的 binlog 位点）确实能根治长事务问题，但普通业务表往往没有可靠的提交时间列；用 binlog 位点做水位就是 CDC 路线，精确但要求上游开启 binlog 且下游做位点管理。updated_at 方案廉价、易实现，代价是必须接受重叠+幂等——它本质是"用最终一致性换实现成本"，团队按数据精度要求选型。

**追问二**：重叠窗口抓回来的重复行，如果下游不是覆盖而是"去重后 append"会怎样？

→ 解析：重复会在下游无限堆积，因为每轮扫描都会把重叠区里的旧行重新拉一次——除非做"已见 (id, updated_at) 台账"式的去重（Q1881 的带 TTL 台账思路），否则每次全量重拉的成本都发生。而且 append 模式下同一行会有多个历史版本，统计口径（"最新值"）要靠查询时取最大 updated_at，把复杂度推给了所有下游查询。工程上默认规则就是：增量同步的下游落点只允许 upsert 型（merge on key），append 型仅用于事件流水且必须带去重台账。
