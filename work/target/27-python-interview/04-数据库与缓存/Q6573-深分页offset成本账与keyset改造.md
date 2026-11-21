---
title: [Q6573] 深分页 offset 的 CPU 成本账与 keyset 改造
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6573 · 深分页 offset 的 CPU 成本账与 keyset 改造

难度：P6 ｜ 标签：PostgreSQL / 分页 / 成本工程

**问**：运营后台的分页导出在翻到第 5000 页时越来越慢，DB CPU 随页码线性上涨。为什么 `LIMIT 20 OFFSET 100000` 的代价是线性的？怎么改？

**答**：
- **结论**：offset 分页的代价线性于偏移量——数据库必须产生并丢弃前 N 行才能拿到第 N 页，`OFFSET 100000 LIMIT 20` 实际扫描 100020 行。成本账：每页成本 ≈ offset × 单行扫描代价，总导出成本是 O(页数²)。这是典型的"用户感知每页都一样慢一点、DB 侧平方级烧 CPU"的隐性成本。
- **取舍**：keyset 分页（seek method）用 `WHERE (sort_col, id) > (:last_sort, :last_id) ORDER BY sort_col, id LIMIT 20`，代价恒定 O(limit)。代价是：① 只能连续翻页，不能跳页（后台后台 UI 若要跳页，需保留 offset 但限制最大 offset）；② 排序列必须唯一化（附加 id 作 tiebreaker），否则会丢行/重行。
- **实战**：改造守门规则——凡是"导出/滚动加载"场景一律 keyset；"跳页搜索结果"场景保留 offset 但用 count 缓存 + 最大页数限制。Python 侧用 SQLAlchemy 时把 last row 的 sort 值回传游标，注意时区列（timestamptz）序列化要无损往返（用 UTC ISO 格式）。

```python
# 对比 offset 与 keyset 的扫描行数成本账（纯标准库）
# 基线：Python 3.9+


def offset_cost(page_size: int, page_no: int) -> int:
    return page_size * page_no  # 产生并丢弃 page_no*page_size 行


def keyset_cost(page_size: int, page_no: int) -> int:
    return page_size  # 恒定，索引 seek 后只读 limit 行


def main() -> None:
    ps = 20
    pages = range(1, 5001)
    off_total = sum(offset_cost(ps, p) for p in pages)
    ks_total = sum(keyset_cost(ps, p) for p in pages)
    print(f"导出5000页: offset总扫描={off_total:,} 行, keyset总扫描={ks_total:,} 行")
    print(f"倍数={off_total / ks_total:,.0f}x")
    assert off_total == ps * 5000 * 5001 // 2  # O(n^2)
    assert ks_total == ps * 5000

    # keyset SQL 片段生成（tiebreaker 防重复/丢行）
    last = ("2026-11-19T16:00:00Z", 12345)
    cond = "(created_at, id) > (%s, %s)"
    print("WHERE", cond % last)


if __name__ == "__main__":
    main()
```

**追问 1**：排序键带 NULL 时 keyset 会有什么坑？
→ 一句话提示：PG 中 NULL 排序默认在 ASC 时排最后（`NULLS LAST`），而行比较 `(a,b) > (x,y)` 对 NULL 的行为与 ORDER BY 不一致，需显式 `NULLS LAST` 并用独立谓词替代行比较。

**追问 2**：如果要支持"跳转到任意页"，keyset 和 offset 能不能结合？
→ 一句话提示：可预物化页号→游标映射（为每页首行 id 建轻量索引表），或限制只允许跳转最近 N 页，超过则强制走导出通道。

## 背诵要点
- OFFSET 代价 = offset × 单行成本，全量导出总成本 O(页数²)；keyset 恒定 O(limit)。
- keyset 三要素：排序列唯一化（+id tiebreaker）、游标无损序列化（timestamptz 用 UTC ISO）、NULL 排序显式声明。
- 守门规则：导出/滚动 = keyset；跳页 = offset + 最大页数限制。

## 复盘追问
- 为什么监控里"平均查询耗时"没反映这个恶化？提示：均值被大量浅分页请求稀释，要看 P99 按页码分桶。
- offset 改 keyset 后产品要求"跳页"，怎么向产品解释并给出替代方案？提示：用总数+页码 UI 保留、实际数据用游标预取，或预物化页首映射表。
