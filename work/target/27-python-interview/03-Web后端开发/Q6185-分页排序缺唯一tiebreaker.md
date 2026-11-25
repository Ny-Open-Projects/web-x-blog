---
title: "[Q6185] 分页排序缺唯一 tiebreaker：翻页重复与漏数据"
date: 2026-11-23
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6185 · 分页排序缺唯一 tiebreaker：翻页重复与漏数据

难度：P6 ｜ 标签：分页、ORDER BY、LIMIT OFFSET、tiebreaker、keyset

**问**：列表接口 `ORDER BY created_at DESC LIMIT ? OFFSET ?`，用户反馈"第 2 页出现了第 1 页的记录，还有几条永远刷不到"。库里 `created_at` 大量重复（批量导入、秒级精度）。SQL 没错、索引也命中，为什么结果会错？加个唯一列就能根治吗？

**答**：
结论：`ORDER BY` 只在排序键上定义"偏序"。当排序键有并列值时，并列行之间的相对顺序**不由 SQL 保证**，由执行计划决定——并行扫描、索引切换、VACUUM/页重组之后都可能变。`LIMIT/OFFSET` 是按"第几个到第几个"切的，两次查询的并列顺序一变，窗口就错位：第 1 页看到 A、B、C，第 2 页可能又出现 B、C（重复），而 D、E、F 永远落在两次窗口的缝隙里（漏）。加上唯一列（`created_at DESC, id DESC`）让排序变成全序，任意两次查询结果一致，问题消失。

取舍：补 tiebreaker 是最小改动、兼容现有前端（页码不变）；根治是 keyset/游标分页（`WHERE (created_at, id) < (?, ?) ORDER BY created_at DESC, id DESC LIMIT ?`），顺带消掉深 OFFSET 的扫描成本，代价是不支持随机跳页、要求排序键可比且唯一。两者可以并存：默认走 keyset，前端要页码时退回"带 tiebreaker 的 OFFSET"。

实战：事故形态是"导出/翻页偶发重复，客服说'第 2 页有第 1 页的人'，开发复现不了（库里数据顺序恰好稳定）"。另一个版本是"翻页期间有人插入新数据，第 2 页整体后移，用户看到重复"。下面用"并列行顺序不保证"的模拟器复现重复与漏行，再演示加唯一键后的不重不漏。

```python
import itertools

# 7 条记录，created_at 全部相同（同一秒批量导入）
DATA = [{"id": i, "created_at": "2026-11-23T10:00:00"} for i in range(1, 8)]

# 模拟真实数据库：并列行的相对顺序不保证稳定（并行扫描/索引切换/VACUUM 后都可能变）
_orders = itertools.cycle([DATA, DATA[::-1], DATA[2:] + DATA[:2]])


def fetch(offset, limit, tiebreak=False):
    rows = next(_orders)
    if tiebreak:
        rows = sorted(rows, key=lambda r: r["id"], reverse=True)
    return [r["id"] for r in rows[offset: offset + limit]]


p1 = fetch(0, 3)
p2 = fetch(3, 3)
p3 = fetch(6, 3)
seen = p1 + p2 + p3
print("[1] 无 tiebreaker 三页:", p1, p2, p3)
print("[2] 重复:", sorted({x for x in seen if seen.count(x) > 1}),
      "| 漏掉:", sorted(set(range(1, 8)) - set(seen)))

_orders = itertools.cycle([DATA, DATA[::-1], DATA[2:] + DATA[:2]])
q1, q2, q3 = fetch(0, 3, True), fetch(3, 3, True), fetch(6, 3, True)
allq = q1 + q2 + q3
print("[3] 加 (created_at, id) 复合排序:", q1, q2, q3)
print("[4] 不重不漏:", len(allq) == len(set(allq)) == 7, "| 分页稳定:", allq == [7, 6, 5, 4, 3, 2, 1])
```

**追问一**：为什么加了唯一列就"稳"了？—— 全序意味着对同一份数据，任何执行计划下的排序结果都唯一确定，`OFFSET` 切的窗口才对得上。注意唯一列必须是**真正唯一**的（主键、或唯一约束列）；`(created_at, status)` 这种组合仍可能并列，只是概率低。还有一个前提：两次查询之间数据没变，否则 OFFSET 依然会位移（这也是 keyset 的另一个优势）。

**追问二**：keyset 分页为什么能同时解决"性能"和"一致性"？—— 它把"第 N 页"换成"排在上一页最后一行之后"，不依赖行号，插入/删除不会让窗口整体位移；`WHERE (created_at, id) < (?, ?)` 能直接用复合索引做范围扫描，深翻页不再扫掉前 N 页。代价是只能"下一页/上一页"，要做"跳到第 100 页"就得额外维护序号或退回 OFFSET。

## 背诵要点
- `ORDER BY` 对并列值不保证顺序；`LIMIT/OFFSET` 按行号切 → 重复与漏行（实测重复 [2,3]、漏 [5,6,7]）。
- 补唯一列构成全序（`created_at DESC, id DESC`）即可稳定；翻页期间数据变化仍会位移。
- keyset/游标分页同时解决深 OFFSET 成本与一致性，代价是不能随机跳页。

## 复盘追问
- 用户反馈第 2 页出现第 1 页数据，如何用"偏序 + 执行计划"解释并修复？（tiebreaker、全序）
- keyset 分页为什么更稳更快？什么场景不能用？（范围扫描、无随机跳页、排序键需可比唯一）
