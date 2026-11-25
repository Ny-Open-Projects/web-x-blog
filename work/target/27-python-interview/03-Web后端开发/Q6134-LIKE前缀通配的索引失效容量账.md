---
title: [Q6134] LIKE 前缀通配查询的索引失效容量账
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6134 · LIKE 前缀通配查询的索引失效容量账

难度：P6 | 标签：LIKE、B-tree、全表扫描、容量规划

**问**：商品搜索接口用了 `WHERE name LIKE '%手机%'`，表涨到 800 万行后接口 P99 从 80ms 恶化到 4s，DB CPU 飙高拖垮同实例其他业务。为什么 `%xx%` 用不上 B-tree 索引？容量账怎么算？演进路径（前缀索引/全文检索/外部搜索引擎）各自适合什么规模？

**答**：

**结论**：B-tree 按"最左前缀"有序组织：`LIKE '手机%'` 可以范围扫描索引（等价于 `>= '手机' AND < '手要'` 的区间），而 `LIKE '%手机%'` 前缀未知，只能在全部索引项上逐个 match，优化器放弃索引走全表扫描——扫描成本 = 表页数 × IO 成本，随行数线性增长，800 万行 × 每行字符串匹配在几秒量级，且缓存命中差时是物理 IO。容量账：全表扫描的代价 ≈ 表大小/内存缓冲比 × 随机 IO 延迟；并发 Q 个这类查询就把 DB 的 IOPS/CPU 打满，这就是"一个慢查询拖垮共享实例"的机制。演进阶梯：a) 业务能改成前缀匹配（补全/搜索建议）→ 零改造成本；b) 倒排能力——PostgreSQL `pg_trgm` GIN 索引支持 `%xx%`，MySQL FULLTEXT ngram 分词；c) 千万级以上或需要分词/相关性排序 → 外部搜索引擎（Elasticsearch/OpenSearch），引入同步链路成本。

**取舍**：trgm/GIN 的代价是索引体积（可达表 2-3 倍）与写放大（每次写入更新 n-gram 条目），写多读少场景要权衡；FULLTEXT 对中文依赖分词器质量；外部引擎引入最终一致性窗口（同步延迟秒级），"刚发布的商品搜不到"要有产品解释。

**实战**：验证索引是否真的失效：`EXPLAIN` 看 type=ALL/rows≈全表；慢查询日志 + `pg_stat_statements`/`performance_schema` 排 Top 查询。示例用 sqlite 演示前缀 LIKE 走索引 vs 中缀 LIKE 全扫的执行计划差异。

```python
import sqlite3, time

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE goods (id INTEGER PRIMARY KEY, name TEXT)")
conn.execute("CREATE INDEX idx_name ON goods(name)")
conn.executemany("INSERT INTO goods(name) VALUES(?)",
                 [(f"商品{i}号蓝牙耳机{i%97}",) for i in range(200_000)])

# 前缀 LIKE：可以用到 B-tree 区间扫描
plan = conn.execute(
    "EXPLAIN QUERY PLAN SELECT * FROM goods WHERE name LIKE '商品1000%'"
).fetchall()
print("前缀 LIKE 计划 ->", plan)

# 中缀 LIKE：全表扫描
plan = conn.execute(
    "EXPLAIN QUERY PLAN SELECT * FROM goods WHERE name LIKE '%蓝牙%'"
).fetchall()
print("中缀 LIKE 计划 ->", plan)

# 计时对比
for label, sql in [("前缀", "SELECT count(*) FROM goods WHERE name LIKE '商品1000%'"),
                   ("中缀", "SELECT count(*) FROM goods WHERE name LIKE '%蓝牙%'")]:
    t = time.perf_counter()
    conn.execute(sql).fetchone()
    print(f"{label} LIKE 耗时 {(time.perf_counter()-t)*1000:6.1f} ms")
```

**追问 1**：为什么 `LIKE 'abc%'` 在 collation 不匹配时也走不了索引？
答：B-tree 按列的 collation 排序，LIKE 前缀范围推导要求相同序关系；大小写不敏感 collation（ci）或 NOCASE 列上，优化器无法把 LIKE 的字典序映射到索引序，退化为扫描——建索引与查询要用一致 collation。

**追问 2**：pg_trgm 的 GIN 索引为什么能支持 `%xx%`？
答：trgm 把字符串切成三元组集合，`%xx%` 的模式可拆成三元组序列，GIN 倒排先按三元组取候选集再逐个 recheck；查询质量取决于模式的最短 n-gram 区分度，短模式（1-2 字）候选集过大效果差。

**追问 3**：把搜索迁到 ES 后，DB 还需要保留 LIKE 吗？
答：保留一个兜底（降级路径）但要有超时与行数上限，防止 ES 故障时 LIKE 兜底流量又打挂 DB——降级链路也要做容量压测。

## 背诵要点

- B-tree 只支持最左前缀：`LIKE 'x%'` 走区间扫描，`'%x%'` 全表扫描，成本随表线性增长并打满共享实例。
- 演进阶梯：前缀化改造 → pg_trgm/FULLTEXT 倒排 → 外部搜索引擎；倒排索引体积 2-3 倍、写放大要评估。
- 判定靠 EXPLAIN（type=ALL）与慢查询日志；ES 降级路径的 LIKE 兜底同样要限流。

## 复盘追问

- 如何给"搜索类查询"建立 DB 保护阈值？(提示：超时 hint + max_rows + 慢查询熔断)
- 中文场景 FULLTEXT 与 ES 的分词差异如何影响召回验收？(提示：用标注查询集对比召回率)
