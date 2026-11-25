---
title: "[Q6144] 搜索接口成本账：LIKE、FTS5 与外部引擎"
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6144 · 搜索接口成本账：LIKE、FTS5 与外部引擎

难度：P6 ｜ 标签：SQLite、FTS5、全文检索、容量规划

**问**：商品搜索接口上线后 DB CPU 直线上升，SQL 是 `SELECT * FROM goods WHERE name LIKE '%keyword%'`。为什么中缀 LIKE 必然全表扫？内置 SQLite FTS5 能撑到什么量级、成本账怎么算？什么时候必须上外部搜索引擎？

**答**：
结论：`LIKE '%kw%'` 前缀通配让 B+ 树/普通索引失效（与 Q6134 前缀 LIKE 失效同源且更极端），复杂度 O(N×模式匹配)，百万行×高频调用就是 CPU 事故。SQLite FTS5 是内置倒排索引：建虚拟表时分词入库，查询复杂度与命中数相关而非表大小，百万行内延迟毫秒级，**零额外运维**——Python 服务单机/中小规模首选。成本账：FTS5 需要额外索引存储（约原文 1~3 倍）与写入放大（每次 INSERT 维护倒排），中文场景需 `tokenize='unicode61'` 外的中文分词（内置不支持，需 jieba 预分词或 trigram `tokenize='trigram'`）。规模超过单机（千万行、多字段加权、聚合分面）再上 OpenSearch/Meilisearch——运维成本（集群、副本、调优）是数量级跳变。

取舍：分词质量决定召回率——中文不预分词时 unicode61 把整句当一个 token，几乎搜不到；trigram 方案免分词器但索引更大、支持子串匹配。数据同步方式：同事务写 FTS5 虚拟表（强一致、简单）vs 外部引擎双写（最终一致、需对账）。

实战：容量决策树——<100 万行 + 单字段 → FTS5；需要排序加权/高亮/分面 → 外部引擎；先给现有接口做 `EXPLAIN QUERY PLAN` 确认 SCAN→ 索引化改造，并把搜索 QPS 与 DB CPU 关联打点。

```python
import sqlite3
import time
import random

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("CREATE TABLE goods (id INTEGER PRIMARY KEY, name TEXT)")

# 造 10 万行模拟数据
words = ["apple", "banana", "cherry", "phone", "laptop", "desk"]
rows = [(i, " ".join(random.choices(words, k=5)) + f" sku{i}")
        for i in range(100_000)]
cur.executemany("INSERT INTO goods VALUES (?, ?)", rows)
conn.commit()

# 1) 中缀 LIKE：全表扫，量出成本
t0 = time.perf_counter()
n = cur.execute("SELECT count(*) FROM goods WHERE name LIKE '%laptop%'").fetchone()[0]
t_like = (time.perf_counter() - t0) * 1000
print(f"LIKE 100k rows: {t_like:.1f}ms, hits={n}")

# 2) FTS5 倒排：建索引成本 + 查询成本
t0 = time.perf_counter()
cur.execute("CREATE VIRTUAL TABLE goods_fts USING fts5(name, content='goods', content_rowid='id')")
cur.execute("INSERT INTO goods_fts(rowid, name) SELECT id, name FROM goods")
conn.commit()
t_build = (time.perf_counter() - t0) * 1000
print(f"FTS5 index build: {t_build:.0f}ms (one-time cost)")

t0 = time.perf_counter()
n = cur.execute("SELECT count(*) FROM goods_fts WHERE goods_fts MATCH 'laptop'").fetchone()[0]
t_fts = (time.perf_counter() - t0) * 1000
print(f"FTS5 MATCH     : {t_fts:.2f}ms, hits={n}")
print(f"speedup: {t_like / max(t_fts, 0.01):.0f}x")

# 3) 排名与片段（BM25 内置）
for r in cur.execute(
    "SELECT rowid, bm25(goods_fts), snippet(goods_fts, 0, '<b>', '</b>', '…', 8) "
    "FROM goods_fts WHERE goods_fts MATCH 'phone laptop' LIMIT 2"):
    print("rank:", round(r[1], 2), "|", r[2])

# 4) EXPLAIN QUERY PLAN 对比：SCAN vs 倒排
print("LIKE plan  :", cur.execute(
    "EXPLAIN QUERY PLAN SELECT * FROM goods WHERE name LIKE '%laptop%'").fetchall()[0])
print("FTS5 plan  :", cur.execute(
    "EXPLAIN QUERY PLAN SELECT * FROM goods_fts WHERE goods_fts MATCH 'laptop'").fetchall()[0])
```

**追问一**：中文搜索在 FTS5 上怎么落地？——两条路：写入前 jieba 分词、查询时同样分词后 MATCH（应用层一致性契约）；或 `tokenize='trigram'`（SQLite 3.34+）免分词支持子串，代价索引约 2~3 倍。讨论召回率与存储的权衡。

**追问二**：FTS5 的 external content 表（content= 选项）省了什么、丢什么？——省一份原文存储（索引引用 content 表），但删除/更新 content 行必须手动同步 FTS5（触发器或命令同步），不同步则出现"幽灵行"；完整自维护用普通虚拟表。

**追问三**：外部引擎的数据同步延迟如何写进产品承诺？——同事务 FTS5 是强一致；双写引擎是秒级最终一致，需要"搜索可见性延迟"的 SLO 与对账任务；讨论新品上架即搜即得的真实需求频率（多数业务 1 分钟内可接受）。

## 背诵要点
- `LIKE '%kw%'` 无索引可走，O(N) 全表扫；FTS5 倒排把查询成本从表大小解耦，10 万行毫秒级。
- FTS5 成本账：索引 1~3 倍存储 + 写入放大；中文需预分词或 trigram；external content 省存储但需手动同步。
- 量级跳变点：多字段加权/分面/千万行 → 外部引擎，运维成本数量级上升，双写改最终一致。

## 复盘追问
- DB CPU 事故发生后，如何快速止血而不等搜索引擎上线？（FTS5 应急索引 + 限流搜索接口 + 慢查询降级缓存，讨论 1 天内落地路径）
- 搜索排序需要业务权重（销量、价格），FTS5 的 bm25 如何扩展？（ORDER BY bm25() + 业务字段 join 排序，讨论权重融合在 SQL 层 vs 引擎层）
