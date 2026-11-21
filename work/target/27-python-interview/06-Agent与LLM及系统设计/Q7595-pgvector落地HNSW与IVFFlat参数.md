---
title: [Q7595] pgvector 落地：HNSW 与 IVFFlat 的参数与过滤性能
date: 2026-11-20
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7595 · pgvector 落地：HNSW/IVFFlat 索引怎么选？带过滤条件检索为什么变慢？

> 难度:★★★★ | 标签:pgvector, RAG, 向量检索

**问**：RAG 知识库选 pgvector（百万级块，768 维）。建 IVFFlat 还是 HNSW？业务还要求"只检索某部门的文档"——加了 WHERE 条件后召回率和延迟都崩了，为什么？

**答**：结论：索引选型上，百万级、写入频繁、查询要求高召回优先 **HNSW**（`m=16, ef_construction=64` 建，查询 `hnsw.ef_search` 调召回）；数据更新极少、内存受限可选 IVFFlat（`lists ≈ rows/1000`，查询 `probes` 要 ≥ lists 的 5-10%）。带 WHERE 过滤后性能崩的根因是：**索引先找近邻再过滤，若过滤条件命中比例很低，"最近邻"大多被 WHERE 淘汰，图/簇遍历耗光 ef_search 也凑不满 limit**——pgvector 的 HNSW 是"过滤后回填"不是"过滤前置"。对策：`iterative index scan`（0.8+：`hnsw.iterative_scan` 让它边走边筛凑满 limit）、或查询侧放宽 limit、或把高选择性过滤字段拆到独立的元数据库先定集合再向量检索。

机理与实战：
- 参数直觉：IVFFlat 的 lists 过大导致每簇太小、probes 要扫更多簇；过小召回塌陷。HNSW 的 ef_search 是召回/延迟的直接旋钮（默认 40，压 P99 到 50ms 内一般 60-100），ef 必须 ≥ limit。
- 距离算子与索引必须匹配：`<->`（L2）、`<=>`（cosine）、`<#>`（内积）各自需要对应索引（`vector_cosine_ops`），算子和索引错配时优化器直接弃用索引全表扫——"加了索引反而更慢"排查第一站。
- 落地纪律：embedding 列用半精度（`vector(768)` 默认 float4 存储已是压缩态）；表 vacuum/analyze 维护；监控用 `EXPLAIN (ANALYZE, BUFFERS)` 确认走的是 `Index Scan using ... hnsw` 而不是 Seq Scan。

```python
# 基线:Python 3.9+ / psycopg2 / pgvector 0.7+ ;缺库降级:纯标准库模拟 ef_search 语义
import math

try:
    import psycopg2
    HAS_PG = True
except ImportError:
    HAS_PG = False

DDL = """
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE chunks (
  id bigserial PRIMARY KEY,
  dept text NOT NULL,
  emb vector(768)
);
CREATE INDEX ON chunks USING hnsw (emb vector_cosine_ops) WITH (m=16, ef_construction=64);
"""

QUERY = """
SET hnsw.ef_search = 80;
SET hnsw.iterative_scan = strict_order;   -- 0.8+:过滤下仍凑满 limit
SELECT id, dept, emb <=> %(q)s AS dist
FROM chunks
WHERE dept = %(dept)s
ORDER BY emb <=> %(q)s
LIMIT 10;
"""


def filtered_search(dsn: str, qvec: list[float], dept: str) -> list[tuple]:
    conn = psycopg2.connect(dsn)
    c = conn.cursor()
    c.execute(QUERY, {"q": qvec, "dept": dept})
    return c.fetchall()


def demo_stdlib() -> None:
    """降级演示:ef_search 不足时,低选择性过滤把召回掏空。"""
    import random
    random.seed(42)
    # 1000 个候选,其中 990 个属于 deptA(高比例过滤不伤),10 个 deptB
    corpus = [{"id": i, "dept": "B" if i < 10 else "A",
               "v": [random.random() for _ in range(8)]} for i in range(1000)]
    q = [random.random() for _ in range(8)]

    def dist(a, b):
        return 1 - sum(x * y for x, y in zip(a, b)) / (
            math.sqrt(sum(x * x for x in a)) * math.sqrt(sum(y * y for y in b)))

    # 模拟 ef_search=15 的近邻探索:先取全域最近邻再过滤
    ranked = sorted(corpus, key=lambda c: dist(q, c["v"]))[:15]
    after_filter = [c for c in ranked if c["dept"] == "B"]
    print(f"ef_search=15 探索后过滤剩余 {len(after_filter)} 条,凑不满 limit=10")
    # iterative 思路:继续向下扫描直到凑满
    pool, need, i = [], 10, 0
    ranked_all = sorted(corpus, key=lambda c: dist(q, c["v"]))
    while len([c for c in pool if c["dept"] == "B"]) < need and i < len(ranked_all):
        pool.append(ranked_all[i]); i += 1
    print(f"iterative 扫到 {i} 条才凑满 {need} 条 -> 过滤选择性决定扫描深度")


if __name__ == "__main__":
    if HAS_PG:
        import os
        if os.environ.get("PG_DSN"):
            print(filtered_search(os.environ["PG_DSN"], [0.0] * 768, "legal"))
        else:
            demo_stdlib()
    else:
        demo_stdlib()
```

**追问一**：什么时候该放弃"向量库 + WHERE"，改用"先元数据过滤再向量检索"？
答：过滤字段选择性极低（如某部门只占 0.1% 文档）且组合条件复杂时，向量索引的过滤回填代价失控；把过滤字段抽出做倒排/关系筛选，得到候选 id 集，再对候选做向量近邻（或干脆检索后精排）。混合检索系统里这是"过滤前置"路线，代价是要维护两套索引的一致性。

**追问二**：`hnsw.ef_search` 调到 200 还是召回不足怎么办？
答：先确认召回不足的判定口径（用标注集算 recall@10，不是肉眼看）；ef 再大不改变图的贪心性质，root cause 常是 embedding 质量或分块问题（查询向量与文档向量不在同一语义空间，比如查询用了不同模型）。图层面升级路径：m 提到 32 重建索引，或换 rerank 补召回。

**背诵要点**：
- 百万级写入频繁选 HNSW（m=16, ef_construction=64, ef_search 60-100），静态数据省内存选 IVFFlat。
- WHERE 过滤是"回填式"：低选择性条件掏空近邻池，靠 iterative scan 或过滤前置解决。
- 算子与索引 ops 必须配对（<=> 配 vector_cosine_ops），错配即 Seq Scan。

**复盘追问**：
- 如何构建一个 200 条的标注集来量化 pgvector 召回率并监控其回归？
- 表从 100 万涨到 5000 万后，HNSW 的内存与构建时间账怎么估？

## 背诵要点
- ef 必须 ≥ limit；ef_search 是召回/延迟旋钮，重建参数是 m/ef_construction。
- 过滤后召回崩 = 选择性问题：iterative_scan、放宽 limit、过滤前置三条出路。
- 排查"索引没生效"：EXPLAIN ANALYZE 看扫描类型 + 核对算子与 ops 配对。

## 复盘追问
- IVFFlat 的 lists/probes 与 HNSW 的 ef 在"召回-延迟"曲线上如何实测对比？
- pgvector 的 HNSW 索引构建期间的写入阻塞如何安排（ CONCURRENTLY 支持）？
