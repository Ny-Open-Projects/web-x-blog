---
title: "[Q7809] ColBERT 的 late interaction：多向量检索的存储账怎么算"
date: 2026-11-25
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7809 · ColBERT 的 late interaction：多向量检索的存储账怎么算

难度：P7 ｜ 标签：ColBERT、late interaction、多向量、MaxSim、向量存储成本

基线：库知识库外知识卡，用"文档数 × token 数 × 维度 × 字节数"估算单向量与 late interaction 多向量的存储/查询成本。

**问**：团队想用 ColBERT 式 late interaction 替代"单向量 + cross-encoder rerank"，理由是"检索质量接近 cross-encoder，但可以离线建索引"。POC 在 10 万文档上效果很好，扩到 1000 万文档时存储从 30GB 涨到 3.6TB，查询 P99 从 80ms 涨到 900ms。多向量到底贵在哪？MaxSim 的计算量有多大？什么规模下它比"单向量 + rerank"更划算？

**答**：

- **结论**：ColBERT 为**每个 token** 存一个向量（通常 768 维 float32），查询时对每个候选文档做 **MaxSim**：查询的每个 token 与文档的每个 token 算相似度、取最大、再求和。存储是单向量的 `文档 token 数` 倍（120 token → 120 倍），计算是 `查询 token × 文档 token × 候选数` 次点积。10M 文档 × 120 token × 3KB ≈ 3.6TB，是单向量 30GB 的 120 倍；P99 的上涨来自 MaxSim 的乘性计算量与更大的内存带宽压力。它适合"中等规模 + 高质量要求 + 能接受存储"的场景，不适合十亿级全量。
- **取舍**：① 单向量 + cross-encoder rerank：存储最小（30GB），rerank 只算 top-100，计算可控，代价是首轮召回可能漏；② ColBERT 全量：召回质量最好，存储/延迟高，适合候选规模 100 万以内或按租户分片；③ ColBERT 只做 rerank：首轮单向量召回 1000，再用 MaxSim 精排，存储只需为候选文档建多向量（或在线算），折中；④ 量化/PQ：int8 把存储降到 1/4，PQ 更低，但会损失 MaxSim 精度，需要评测。
- **实战**：① 先算三笔账：存储（docs × tokens × dim × bytes）、查询算力（q_tokens × d_tokens × candidates）、内存带宽；② 用"单向量召回 + ColBERT rerank"做基线，对比"全量 ColBERT"的边际收益；③ 按租户/语种分片，避免单索引无限膨胀；④ 监控 token 数分布，长文档（500+ token）会把存储放大 4 倍，先做长度治理；⑤ 量化后必须重跑 recall/MaxSim 精度评测，别只看存储降了。

下面量化单向量、ColBERT 多向量、int8 量化的存储与 MaxSim 计算量。

```python
# ColBERT late interaction: 每 token 一个向量, MaxSim 查询时逐 token 比对
DIM = 768
BYTES = 4                      # float32
TOKENS_PER_DOC = 120
DOCS = 10_000_000
QUERY_TOKENS = 30
CANDIDATES = 100

single_bytes = DIM * BYTES
multi_bytes = single_bytes * TOKENS_PER_DOC
print(f"[1] 单向量/文档={single_bytes / 1024:.1f}KB, 多向量/文档={multi_bytes / 1024:.0f}KB, "
      f"放大={multi_bytes / single_bytes:.0f}x")
assert multi_bytes / single_bytes == TOKENS_PER_DOC

single_total_gb = single_bytes * DOCS / 1e9
multi_total_tb = multi_bytes * DOCS / 1e12
print(f"[2] 1000 万文档: 单向量={single_total_gb:.1f}GB, 多向量={multi_total_tb:.2f}TB")
assert 30 < single_total_gb < 32
assert 3.5 < multi_total_tb < 4.0

# int8 量化: 存储 1/4, 但仍有 30 倍
multi_int8_tb = multi_total_tb / 4
print(f"[3] int8 量化后={multi_int8_tb:.2f}TB, 仍是单向量的 {multi_int8_tb * 1000 / single_total_gb:.0f}x")
assert multi_int8_tb > 0.8

# MaxSim 计算量: 查询 token × 文档 token × 候选数
def maxsim_dots(q_tokens, d_tokens, candidates):
    return q_tokens * d_tokens * candidates


colbert_dots = maxsim_dots(QUERY_TOKENS, TOKENS_PER_DOC, CANDIDATES)
print(f"[4] 100 个候选的 MaxSim 点积次数={colbert_dots:,}")
assert colbert_dots == 360_000

# 单向量首轮: 每个候选一次点积
single_dots = QUERY_TOKENS * CANDIDATES
print(f"[5] 单向量 100 候选的点积次数={single_dots:,}, 是 MaxSim 的 1/{colbert_dots // single_dots}")
assert single_dots == 3_000

# 长文档放大: 500 token 的文档存储再 ×4
long_tokens = 500
long_tb = single_bytes * long_tokens * DOCS / 1e12
print(f"[6] 若平均 500 token: 多向量={long_tb:.1f}TB")
assert long_tb > 15
print("    → 实测 存储与 token 数线性, MaxSim 与 token 数乘性; 先治长度, 再谈全量 ColBERT")
```

**追问一**：ColBERT 的 MaxSim 为什么比单向量慢这么多？—— 单向量是"一次点积得到一个分数"；MaxSim 是"查询每个 token 与文档每个 token 都算一次，再取最大求和"，计算量是 `q × d` 倍。100 个候选、30×120 token 就是 36 万次点积，且每个点积 768 维，内存访问模式也不如矩阵乘连续。它的质量收益来自"词级匹配"，代价是乘性计算。

**追问二**：什么规模适合 ColBERT？—— 经验上：候选规模在百万级、质量要求高（法律/医疗/代码检索）、能按租户/语种分片时值得；十亿级全量更适合"单向量召回 + 小候选 cross-encoder/ColBERT rerank"。不要用"POC 在 10 万文档上很好"直接推到全量，存储和 P99 都是线性/乘性增长的。

## 背诵要点

- ColBERT 每 token 存一个向量，存储是单向量的 `token 数` 倍（120 token → 120x）；10M 文档约 3.6TB vs 30GB。
- MaxSim 计算量 = `q_tokens × d_tokens × candidates`，是单向量点积的 `d_tokens` 倍；P99 上涨来自乘性计算与内存带宽。
- 适合百万级 + 高质量 + 可分片；十亿级用"单向量召回 + ColBERT/cross-encoder rerank"，并先治文档长度。

## 复盘追问

- int8/PQ 量化后，MaxSim 的"取最大"会不会放大量化误差？怎么评测？
- 如果只用 ColBERT 做 rerank，候选文档的多向量是在线算还是离线存？各自的成本拐点在哪？
