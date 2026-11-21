---
title: [Q6053] offset 深分页与 cursor 游标分页的容量账
date: 2026-11-20
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6053 · offset 深分页与 cursor 游标分页的容量账

> 难度:★★★★ | 标签:分页, offset, cursor, LIMIT, 容量规划

**问**：订单列表翻到第 5 万页时接口 P99 从 20ms 涨到 8 秒。`LIMIT 20 OFFSET 9999980` 慢在哪？cursor 分页（`WHERE id > last LIMIT 20`）为什么快？两种方案的 API 契约和迁移代价分别是什么？

**答**：offset 的成本是**跳过也是扫描**：数据库必须读出并丢弃前 OFFSET 行（有 WHERE 时逐行判断），OFFSET 越大翻得越慢，P99 随页深线性恶化——这就是"深分页税"。实测（Python 模拟同构模型）：跳 50 万行 O(n) vs 索引定位 O(log n)，模型里差两个数量级；SQL 上 `WHERE id > last_id ORDER BY id LIMIT 20` 走主键/二级索引直接定位，成本恒定。cursor 方案三件套：a) 排序键必须**单调且唯一**（id，或 created_at+id 复合键防同秒并列）；b) 返回 `next_cursor`（最后一行的键值，可 base64 编码带校验防篡改），请求带 `after=cursor`；c) 排序方向改变时要整体换协议。代价与取舍：cursor **不能跳页、不能数总页数**（COUNT 同样是全扫，产品要"共 X 条"就得另做估算或缓存计数），前端"页码跳转"交互要么放弃要么降级为只支持相邻翻页——这是 API 契约变更，迁移要灰度并保留旧 offset 接口一个版本周期。混合方案：浅页（前几页，offset 索引扫描还便宜）用 offset 兼容老客户端，深页强制 cursor，同时给 offset 接口加最大页深硬限制（超限 400）兜底。

```python
# file: code/03_Web后端开发/q6053_pagination.py
import bisect, time

rows = list(range(1_000_000))            # 按 id 有序, 模拟索引

def offset_page(page, size):
    return rows[page * size:(page + 1) * size]      # SQL: LIMIT size OFFSET page*size -> O(n) 跳行

def cursor_page(after, size):
    i = bisect.bisect_right(rows, after)            # SQL: WHERE id > after LIMIT size -> O(log n)
    return rows[i:i + size], rows[i + size - 1] if i + size <= len(rows) else None

t0 = time.perf_counter(); offset_page(499_999, 20); t1 = time.perf_counter() - t0
t0 = time.perf_counter(); page, last = cursor_page(9_999_979, 20); t2 = time.perf_counter() - t0
print(f"offset 第 50 万页 O(n) 跳行: {t1*1e3:.1f}ms | cursor O(log n): {t2*1e3:.3f}ms")
print("cursor 返回 next_cursor:", last, "(下一页: WHERE id >", last, ")")

# 复合排序键防并列: ORDER BY created_at DESC, id DESC, cursor=(created_at,id) 二元组
print("并列防护: 单调唯一键, 或 (created_at, id) 复合; 只比 id 会在同毫秒批量插入时漏/重行")
print("契约代价: cursor 不能跳页/不能 COUNT 总数; 深页强制 cursor + offset 加最大页深 400 兜底")
```

**追问**：1) `ORDER BY created_at LIMIT 20` 为什么还是会慢？——created_at 有并列值且二级索引要回表；正确形态是复合索引 (created_at, id) 且 cursor 带二元组，比较用元组语义（`(t,id) > (t0,id0)`）。2) `COUNT(*)` 为什么和分页一样是深水雷？——全扫/全索引扫，大表上秒级；用估算（EXPLAIN row estimate/统计表）、精确数改缓存计数、或产品上砍掉总页数。3) keyset 分页遇到"中间插入新行"会重或漏吗？——升序 cursor 会漏新插入的旧区间行（数据只增时是可接受语义），实时性要求高时用"快照事务"或按 (ts, id) 严格单调语义明说；这是面试常追问的语义坑。

## 背诵要点
- `LIMIT/OFFSET` 跳过也是扫描，成本随页深 O(n) 涨；`WHERE id > last ORDER BY id LIMIT n` 走索引 O(log n) 恒定。
- cursor 三件套：单调唯一排序键（或 (created_at,id) 复合防并列）、next_cursor 可校验编码、方向变更换协议。
- 代价：不能跳页、COUNT 同雷；迁移策略——浅页 offset 兼容 + 深页强制 cursor + 最大页深 400 兜底。

## 复盘追问
- 你们列表接口最深被翻到过多少页？有 offset 页深限制吗？（提示：从网关日志按 offset 分布统计，超阈值样本看耗时曲线）
- 迁 cursor 分页时前端"总条数/跳页"交互怎么谈？（提示：拿深页耗时数据推动交互降级；COUNT 改估算或缓存，写进方案评审）
