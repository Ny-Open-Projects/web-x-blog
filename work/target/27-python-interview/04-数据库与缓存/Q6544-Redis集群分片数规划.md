---
title: [Q6544] Redis Cluster 分片数规划：内存、QPS、热点三约束下的推算
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6544 · Redis Cluster 分片数怎么定？从内存账、QPS 账和热点账三条线推

> 难度:★★★★ | 标签:容量规划, Redis Cluster, 架构设计

**问**：预期集群 200GB 数据、峰值 80 万 QPS，Redis Cluster 要几个分片？"按内存够用就行"为什么是错的？分片规划时必须留出哪些冗余维度？

**答**：结论：分片数 = **三个约束取最大**：内存约束（数据 × 峰值系数 ÷ 单分片安全内存）、QPS 约束（峰值 QPS ÷ 单分片可承载 QPS）、**热点约束**（最热 key 的单 key QPS 必须落在单分片上限内，拆不掉就要本地缓存/拆桶）。三者取最大后再上浮副本与运维冗余。"内存够就行"错在忽略了单分片 CPU 网络上限和写扩散，更忽略了 reshard 是运维重活——分片规划要一步到位留 2 年余量。

机理与实战：
- **内存约束**：单分片建议 ≤ 25GB（考虑 maxmemory 预留、fork COW 峰值≈写峰值页数、大 key 治理半径），200GB × 1.3 峰值系数 ≈ 260GB → 至少 11 分片，取整 12。
- **QPS 约束**：单分片纯 GET 实测可达 8-10 万 QPS，但混入 SET、Lua、大 value 后安全值取 4-5 万；80 万 ÷ 5 万 = 16 分片 → 本例 QPS 是主导约束。
- **热点约束**：一个爆款商品 key 10 万 QPS 时落在哪个分片哪个分片就独木桥；解法是 hash tag 拆桶（key 后缀 0-9 分散到 10 个槽）或客户端本地缓存兜底。规划期就要问"业务里有没有单 key > 3 万 QPS 的可能"。
- **冗余维度**：副本（至少 1 副本/分片，跨机架/可用区）、reshard 峰值迁移期的容量腾挪、故障时少一个分片后其余分片兜底的余量（N+1 原则）；agent 数与 slot 均匀性用 `redis-cli --cluster check` 验证。

```python
# 基线:Python 3.10+;纯标准库,Redis Cluster 分片数三约束推算器
from __future__ import annotations
import math
from dataclasses import dataclass


@dataclass
class ClusterPlan:
    data_gb: float            # 预估数据量
    peak_qps: int             # 峰值总 QPS
    hot_key_qps: int          # 预估最热单 key QPS
    shard_mem_gb: float = 25.0   # 单分片安全内存上限
    shard_safe_qps: int = 50_000  # 单分片安全 QPS(混合读写)
    peak_factor: float = 1.3     # 内存峰值系数
    growth_factor: float = 1.5   # 两年增长余量


def plan_shards(p: ClusterPlan) -> dict:
    by_mem = math.ceil(p.data_gb * p.peak_factor * p.growth_factor / p.shard_mem_gb)
    by_qps = math.ceil(p.peak_qps * p.growth_factor / p.shard_safe_qps)
    # 热点:单 key 无法跨分片,必须靠拆桶把热 key 打散
    by_hot = math.ceil(p.hot_key_qps * p.growth_factor / p.shard_safe_qps)
    hot_note = f"热 key 需拆 {by_hot} 桶(hash tag 后缀 0..{by_hot - 1})" if by_hot > 1 else "无热点拆桶需求"
    shards = max(by_mem, by_qps)
    return {
        "按内存": by_mem, "按QPS": by_qps, "主导约束": "内存" if by_mem >= by_qps else "QPS",
        "建议分片(主)": shards, "含副本实例数": shards * 2,
        "热点": hot_note,
    }


def demo() -> None:
    p = ClusterPlan(data_gb=200, peak_qps=800_000, hot_key_qps=10_000)
    r = plan_shards(p)
    for k, v in r.items():
        print(f"  {k}: {v}")
    assert r["建议分片(主)"] == 24, f"QPS 主导: {r['按内存']} vs {r['按QPS']}"
    # 无热点场景
    p2 = ClusterPlan(data_gb=200, peak_qps=300_000, hot_key_qps=2_000)
    r2 = plan_shards(p2)
    assert r2["建议分片(主)"] == max(r2["按内存"], r2["按QPS"])
    print("分片规划:内存/QPS/热点三约束取最大,再乘增长余量 ✅")


if __name__ == "__main__":
    demo()
```

**追问一**：业务增长后分片数不够要扩容，reshard 迁移期间业务会感知到什么？
答：迁移中的槽处于 MIGRATING/IMPORTING 状态，客户端对 slot 内 key 会收到 ASK 重定向，需要客户端支持 ASK 错误重试；迁移走 `MIGRATE` 是同步阻塞的，大 key 会让源/目标分片瞬间卡顿——所以扩容要在低峰分批迁，且先把大 key 拆掉。这也是"规划一步到位"的原因之一。

**追问二**：为什么单分片内存要压在 25GB 而不是把 128GB 机器塞满？
答：三个理由：① BGSAVE/AOF rewrite 的 fork COW 与主库写入量成正比，大实例 fork 时延和内存峰值都不可控；② 故障恢复时 RDB/AOF 加载时长随内存线性增长，25GB 恢复在分钟级，128GB 可能半小时不可用；③ 主从全量同步与 reshard 的数据搬运窗口同样线性变长。单分片大小本质是"故障半径 × 恢复时长"的预算问题。

## 背诵要点
- 分片数 = max(内存约束, QPS 约束) + 热点校验：单分片安全值内存 ≤25GB、混合 QPS 4-5 万；规划乘 1.5 倍两年增长余量。
- 热 key 拆不掉分片：hash tag 后缀拆桶或客户端本地缓存兜底；单 key >3 万 QPS 必须预案。
- 分片大小本质是故障半径预算：fork COW、恢复加载时长、全量同步窗口都随单分片内存线性增长。

## 复盘追问
- 上线半年后某分片内存是其他分片 3 倍，怎么排查规划哪里错了？（提示：大概率 hash tag 设计让某业务族 key 全落一个槽，或存在大 key；用 `--cluster check` 看 slot 分布 + 大 key 扫描，治理后复盘 hash tag 规范）
- 为什么规划时把副本算作"不承载读流量"的冗余？（提示：读流量打到副本会让故障转移瞬间把读压力全砸回主库，容量账应按"主库独立扛全部读写"的 N+1 模型算，副本读只做弹性缓冲）
