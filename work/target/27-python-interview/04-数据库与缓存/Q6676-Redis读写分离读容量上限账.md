---
title: [Q6676] Redis读写分离读容量上限账
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6676 · Redis 主从读写分离：读容量上限怎么算、到顶怎么办

难度：P6/P7 ｜ 标签：容量规划、Redis、读写分离

**问**：读 QPS 涨到主库扛不住，加从库分摊读流量。从库数量的上限怎么算？为什么"读容量"不是从库数 × 单机读 QPS？

**答**：**结论**：读容量上限受三个硬约束：① **主库写 QPS**——每个写命令要复制到所有从库，从库越多主库复制线程压力越大，主库写 QPS 是全系统上限；② **单从库读上限**——受单核命令处理能力与网络带宽限制；③ **复制延迟容忍**——读从库就有读到旧数据的窗口，延迟敏感的读必须粘主库，实际可分流比例 < 100%。所以真实读容量 ≈ min(主库写预算, N × 从库读上限 × 可分流比例)。

**取舍**：加从库到 4-6 台后收益递减：复制流量线性增长、故障面变大（一台挂 = 瞬间 1/N 读流量转主）。超过拐点后的两条路线：**本地缓存挡读**（app 内 L1，把"读 Redis"降为"读内存"）或 **Redis Cluster 分片**（把读写都按 key 水平拆）。选型的分界是：热点 key 集中 → 本地缓存；整体读多 → 分片。

**实战**：给从库读做容量账：先压测单从库读 QPS 基线（一般几万到十几万），再乘副本数与 0.8 安全系数；监控上 `master_repl_offset - slave_repl_offset` 延迟超 1s 自动把该从库摘出读路由。

```python
# 读容量账：主库写预算约束下的最大可分流读 QPS
def read_capacity(
    master_write_qps: int,      # 主库写 QPS（复制流量的源头）
    replica_read_qps: int,      # 单从库读上限（压测基线）
    replicas: int,
    repl_overhead_per_write: float = 0.02,  # 每写复制开销（从库数比例系数）
    readable_ratio: float = 0.8,  # 延迟敏感读粘主库后可分流比例
) -> dict:
    # 主库写预算：每增加一个从库，写命令多一份复制开销（近似线性）
    repl_cost = master_write_qps * replicas * repl_overhead_per_write
    master_headroom = master_write_qps - repl_cost
    if master_headroom <= 0:
        return {"verdict": "从库过多，复制已拖垮主库写", "max_read": 0}
    # 读容量 = 副本读能力 × 可分流比例，但受主库剩余预算约束的间接上限
    fanout_read = replica_read_qps * replicas * readable_ratio
    return {
        "repl_cost_qps": repl_cost,
        "master_headroom_qps": master_headroom,
        "max_read_qps": fanout_read,
        "verdict": "正常" if fanout_read > master_write_qps * 3
                   else "读容量吃紧：考虑本地缓存或分片",
    }

print(read_capacity(master_write_qps=20000, replica_read_qps=80000,
                    replicas=2))
# repl_cost=800, fanout=128000 -> 正常
print(read_capacity(master_write_qps=20000, replica_read_qps=80000,
                    replicas=8, repl_overhead_per_write=0.02))
# repl_cost=3200 -> 仍正常但故障面大；把 overhead 提到 0.05 会翻转结论
print(read_capacity(master_write_qps=20000, replica_read_qps=80000,
                    replicas=8, repl_overhead_per_write=0.05))
# -> 从库过多，复制已拖垮主库写
```

**追问 1**：为什么"一台从库挂掉"比"读容量少 1/N"更危险？
提示：读路由摘除有探测窗口，窗口内该从库的流量重试/超时打到主库，形成读尖峰，可能触发主库连锁故障——所以摘除要靠客户端探测 + 预留冗余（N+1 原则）。

**追问 2**：本地缓存（L1）加入后，容量账里哪一项变了？
提示：readable_ratio 上升（L1 挡住部分读不再打到 Redis），但引入新变量：L1 失效回源的突发读，回源峰值也要按 QPS 计入账。

**追问 3**：读写分离下如何处理"写后立即读"？
提示：会话粘主库（按用户维度路由）或读写版本号校验（读到旧版本重试读主），成本是主库流量比例上升，容量账要扣这部分。

## 背诵要点
1. 读容量 ≈ min(主库写预算 − 复制开销, N × 从库读上限 × 可分流比例)，不是简单乘法。
2. 从库 4-6 台后收益递减，拐点后的选项：本地缓存挡热点读 / Cluster 分片。
3. 从库故障的真实风险是探测窗口内的读流量冲向主库，按 N+1 预留冗余。

## 复盘追问
1. 你负责的 Redis 读路径上，延迟敏感读占比多少？如何度量"可分流比例"而不是拍脑袋给 0.8？
2. 如果读 QPS 明天翻十倍，你的架构在哪个约束先崩？预算方案是什么？
