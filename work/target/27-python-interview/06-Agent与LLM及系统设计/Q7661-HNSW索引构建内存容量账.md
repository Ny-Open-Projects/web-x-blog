---
title: [Q7661] HNSW 索引构建内存容量账：1000 万向量要多少内存
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7661 · HNSW 索引构建内存容量账：1000 万向量要多少内存

难度：P6-P7 | 标签：容量规划、向量索引、HNSW

**问**：计划把 1000 万条 768 维向量从暴力检索迁到 HNSW 索引。这条索引的内存账怎么算？为什么"向量本体 30GB"算完，实际进程内存却要 2-3 倍？构建阶段的内存峰值与查询阶段有什么不同？

**答**：结论：HNSW 内存 = 向量本体 + 图结构。向量本体 = N × dim × 4 字节（float32）= 1000 万 × 768 × 4 ≈ 29GB；图结构 = N × M × 层概率叠加 × 8 字节（邻居 ID 指针），M=16 时约 2-4GB。**但进程实际内存是 2-3 倍**，因为构建期还有三笔账：① 构建临时结构（插入时的候选集、已访问集，与 ef_construction 相关）；② 索引从磁盘加载到内存缓冲的瞬时双份；③ 向量本体在应用侧还可能存一份原副本（做 rerank 或存原始 payload），如用 float64 存就是双倍。容量账必须按"构建峰值"而不是"稳态"申请内存。

取舍与实战：
1. 降本三档：量化标量（int8：4 倍省，召回掉 1-3%，Q7616 halfvec 思路同理）；降维（768→384/256，配合检索质量评估）；分层存储（向量在磁盘 + 内存只留导航层，faiss IndexIVF 类、Qdrant quantization）——按"内存预算 ÷ 每 GB 单价"选档。
2. 构建策略：全量构建峰值最高，改成"分批插入 + 定期 rebuild"或用 IVF/HNSW 混合（IVF 先聚类降低候选集）；构建耗时 ≈ N × log(N) × ef_construction，1000 万条单机约数小时，属于"容量事件"要按回溯作业账（Q7158 同构）排窗口。
3. 查询期账单：ef_search 决定候选集大小（内存平稳但延迟上升），容量稳定；Q7590 是查询侧 QPS 账，本卡是构建/驻留内存账，两者分开报。
4. payload 别忘了：真实业务里 payload（文本、元数据）常比向量本身大，向量库只存向量时 payload 在外部存储——账里要写清"索引内存"与"全链路内存"两个口径。

```python
"""HNSW 内存容量账：本体 + 图 + 构建峰值（标准库，可运行）"""

def hnsw_memory_gb(
    n: int, dim: int,
    m: int = 16,                    # 每节点邻居数
    bytes_per_dim: int = 4,         # float32
    layers_avg: float = 1.15,       # 层级概率叠加平均
    build_overhead: float = 2.5,    # 构建期峰值系数（临时结构+双份缓冲）
) -> dict:
    vectors = n * dim * bytes_per_dim / 1024**3
    graph = n * m * layers_avg * 8 / 1024**3        # 邻居 ID int64
    steady = vectors + graph
    peak = steady * build_overhead
    # 降档选项：int8 标量量化
    q = n * dim * 1 / 1024**3 + graph
    return {"向量本体GB": round(vectors, 1), "图结构GB": round(graph, 2),
            "稳态GB": round(steady, 1), "构建峰值GB": round(peak, 1),
            "int8量化稳态GB": round(q, 1)}

r = hnsw_memory_gb(n=10_000_000, dim=768)
for k, v in r.items():
    print(f"{k}: {v}")
assert r["构建峰值GB"] > r["稳态GB"] > r["int8量化稳态GB"]
```

**追问 1**：为什么 M 调大召回变好但内存线性上涨，而 ef_construction 影响的是构建时间不是内存？
**提示**：M 决定每个节点的邻居指针数——内存与图密度直接挂钩；ef_construction 只是插入时搜索的候选队列长度，决定"边连得好不好"（质量/时间），构建完成后不留驻内存。

**追问 2**：int8 量化后为什么还要保留部分 float32 精度（rescoring）？
**提示**：量化引入每维误差，直接用量化距离排序会掉召回；常见做法是量化值做粗筛（近邻候选 top-k），再用原 float 向量对 top-k 精排——内存只需保留原向量的候选子集或从磁盘回捞。

## 背诵要点
- 内存账：N × dim × 4B 向量本体 + N × M × 1.15 × 8B 图结构；构建峰值 = 稳态 × 2-3，按峰值申请。
- 降本三档：int8 标量量化（省 4 倍，召回 -1~3%）、降维、磁盘分层 + rescoring。
- M 挂内存、ef_construction 挂构建时间、ef_search 挂查询延迟，三个参数账各归各。

## 复盘追问
- 如何用一小份样本（10 万条）实测召回-内存曲线，外推全量 1000 万的选型决策？
- 构建期峰值若与线上查询共存同一实例，内存 OOM 风险如何隔离（独立构建机再切换）？
