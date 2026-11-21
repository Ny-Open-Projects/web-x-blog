---
title: [Q7601] embedding 批量入库吞吐与索引构建容量账
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7601 · embedding 批量入库吞吐与索引构建容量账

难度：P6 ｜ 标签：向量库 / embedding / 容量规划

**问**：知识库从 10 万文档涨到 800 万 chunk，首次全量入库跑了一周还没完，增量更新又和查询流量抢资源。embedding 入库的吞吐账怎么算？索引构建（HNSW/IVFFlat）的容量规划要点是什么？

**答**：
- **结论**：入库吞吐的瓶颈链：读取解析 → embedding 调用 → 向量库写入 → 索引构建。四段速率不同，整条链的吞吐 = min(各段吞吐)，而 embedding 通常是最慢的一段：API 限流按 token/分钟计（如 TPM 上限），单条 512 token 时 `理论 QPS = TPM / 512 / 有效利用率`；批量调用（batch size）能省网络往返但受单请求 token 上限约束。索引侧：HNSW 构建时间随向量数超线性增长（构建期内存也随参数 M/ef_construction 膨胀），全量构建与在线查询争抢 CPU/内存——所以"边写入边检索"的大批量入库必须限速，或建临时索引后原子切换。容量账公式：`全量入库时长 = 向量数 / min(解析, embedding, 写入) 速率 + 索引构建时长`，其中索引构建时长要用实测拐点数据外推（不能线性外推）。
- **取舍**：写入吞吐 vs 查询质量的参数交换：HNSW 构建期 `ef_construction` 越大召回越高、构建越慢；IVFFlat 要"先攒数据再 build（lists 数 = sqrt(N) 起步）再 insert"（pgvector 特性），边插边建会形成劣质聚类。限速策略：查询高峰时段入库限速到 20-30%，或干脆错峰；用独立副本专门构建再复制到服务集群。
- **实战**：步骤：① 实测四段单机吞吐，取最小值定 pipeline 并发；② TPM 限额做令牌桶调度，按供应商配额自动伸缩；③ 大规模重建用"影子索引 + 别名切换"（零窗口）；④ 复盘项：入库进度看"段级速率曲线"而不是总进度条——能提前发现最慢段并扩容。

```python
# embedding 入库吞吐与索引构建容量账（纯标准库）
# 基线：Python 3.9+

import math


def emb_throughput_qps(tpm: int, tokens_per_chunk: int,
                       utilization: float = 0.8) -> float:
    """embedding API 吞吐上限（chunk/秒）"""
    return tpm * utilization / tokens_per_chunk / 60


def full_ingest_hours(n_chunks: int, parse_cps: float, emb_cps: float,
                      write_cps: float, index_build_hours: float) -> float:
    """全量入库时长 = 数据量 / 最慢段 + 索引构建"""
    bottleneck = min(parse_cps, emb_cps, write_cps)
    return n_chunks / bottleneck / 3600 + index_build_hours


def ivf_lists(n: int) -> int:
    """IVFFlat lists 经验值 ~ sqrt(N)（pgvector 建议）"""
    return max(1, int(math.sqrt(n)))


def main() -> None:
    # TPM 2M，单 chunk 512 token，利用率 0.8 → ~52 chunk/s
    qps = emb_throughput_qps(2_000_000, 512)
    print(f"embedding 吞吐 ≈ {qps:.1f} chunk/s")
    assert 50 < qps < 55
    # 800 万 chunk，写入与解析都够快，embedding 52/s 是瓶颈
    h = full_ingest_hours(8_000_000, parse_cps=200, emb_cps=qps,
                          write_cps=100, index_build_hours=6)
    print(f"全量入库 ≈ {h:.1f} 小时")
    assert 42 < h < 50  # 8e6/52 ≈ 42.6h + 6h
    assert ivf_lists(1_000_000) == 1000
    print("OK")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么 HNSW 的索引构建时间不能按向量数线性外推？
→ 一句话提示：插入时要在图上做贪心搜索找邻居，图越大搜索路径越长，构建时间超线性（接近 N·logN 到 N^1.x）；容量规划要用两三个实测点拟合指数再外推。

**追问 2**：增量更新频繁时，"定期全量重建"和"持续增量插入"怎么选？
→ 一句话提示：增量插入会让 HNSW 图逐渐劣化（新增节点邻居选择受限）与 IVF 聚类偏移，删除只标记不回收；更新率高、召回要求高的场景用定期重建 + 别名切换，低频更新用增量 + 监控召回率拐点。

## 背诵要点
- 入库吞吐 = min(解析, embedding, 写入)；embedding 受 TPM 限制，QPS = TPM × 利用率 / 单条 token / 60。
- 全量时长 = 数据量 / 最慢段 + 索引构建；HNSW 构建超线性，外推要实测拟合，不能线性算。
- 大重建用影子索引 + 别名切换零窗口；查询高峰期入库限速 20-30% 或错峰；IVFFlat 先攒数据再 build。

## 复盘追问
- embedding 降本（批量 + 缓存重复文本）和 TPM 配额是什么关系？提示：缓存命中不消耗 TPM 但改变有效吞吐结构，容量账要按"缓存命中率"修正 QPS 预算；批量只是省网络与单价，不改 TPM 天花板。
- 入库期间查询召回率下降是什么机制？提示：并发写入触发 HNSW 图重构与 IVF 聚类重算，查询看到的是"构建中间态"；限速与错峰是保护查询 SLA 的直接手段，独立构建副本是彻底解法。
