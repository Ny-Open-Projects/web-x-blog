---
title: "[Q6767] 集群加了副本读更慢还读旧值：Cluster 副本读 READONLY 的语义与一致性"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6767 · 集群加了副本读更慢还读旧值：Cluster 副本读 READONLY 的语义与一致性

难度：P6 ｜ 标签：Redis Cluster、副本读、READONLY、复制延迟、读写分离

基线：Python 3.12；模拟一主两副的 Cluster 读路由，演示副本读的旧值窗口与故障转移时的路由切换，标准库实跑。

**问**：Cluster 集群 QPS 上不去，加了两个副本想把读分散，结果读延迟没降多少，业务还开始报"读到了旧值"。副本读的正确姿势是什么？`READONLY` 命令为什么必须发？写后立刻读的场景怎么办？主挂了副本顶上时，正在副本上的读会怎样？

**答**：
- **结论**：Cluster 里普通 GET 默认发往 key 所属槽的**主节点**；想在副本上读，客户端必须先对副本发 `READONLY`（**连接级开关**，开启后该连接允许读非主节点上的槽）。副本读的价值有限、陷阱明确：① 副本异步复制，读到的数据**落后于主**，写后读场景读到旧值甚至读不到；② 分摊的是主节点的读压力，但每个副本还要同步写流量，扩读能力不等于扩容（Q6666 读副本上限）；③ 主故障转移时副本升主，原来读副本的连接路由全变，客户端要重定向/重建连接（Q6556 的重连风暴）。所以副本读适用的是**容忍旧值的读**（容灾冷读、全量扫描、报表拉数），不适用会话内一致性要求高的读。
- **取舍**：① 副本读 vs 加缓存层：读热点该进应用缓存（Q6633 成本拐点），副本读只解决"主节点 CPU/网络被打满"，不解决延迟；② 一致性分级：写后立即读走主库（客户端按 key 路由到主），普通展示类读走副本，用读写分离策略显式声明而不是全量切；③ 副本数与故障转移平衡：副本越多读分摊越好，但写流量同步越多、故障转移时提升的主越"旧"——`min-replicas-to-write` 之外的另一道可用性账（Q1415 数据丢失窗口）。
- **实战**：① 客户端配置声明三种路由：force_master（写后读）、prefer_replica（容读旧值）、random（无所谓），业务按场景选，别全局一刀切；② 副本读延迟监控：副本 `master_repl_offset` 与主差值超阈值自动把副本读路由切回主（Q6646 延迟摘除思路）；③ 故障转移演练固定项：副本升主后验证读路由收敛时间与 READONLY 状态重建（Q7646 演练思路在 Redis 场景的落地）。

```python
"""Cluster 副本读模拟：路由策略 + 复制延迟窗口 + 故障转移切换。"""
import time


class Node:
    def __init__(self, node_id: str, role: str):
        self.node_id = node_id
        self.role = role                # master / replica
        self.data: dict[str, tuple] = {}    # key -> (value, version)
        self.readonly = False           # READONLY 连接级开关


class Cluster:
    def __init__(self):
        self.master = Node("m1", "master")
        self.replicas = [Node("r1", "replica"), Node("r2", "replica")]
        self.repl_lag = 0.0             # 副本落后主的数据版本差

    def write(self, key: str, value: str, version: int) -> None:
        self.master.data[key] = (value, version)
        self.repl_lag += 1              # 写入先落到主, 副本落后

    def replica_catchup(self, n: int = 1) -> None:
        """副本追 n 个版本。"""
        for r in self.replicas:
            for k, (v, ver) in self.master.data.items():
                r.data[k] = (v, min(ver, version_of(r, k) + n))
        self.repl_lag = max(0, self.repl_lag - n)


def version_of(node: Node, key: str) -> int:
    return node.data.get(key, ("", 0))[1]


def read(client: Cluster, key: str, route: str) -> tuple[str, int, str]:
    """route: master / replica。返回 (值, 版本, 命中节点)。"""
    if route == "master":
        v, ver = client.master.data.get(key, (None, 0))
        return v, ver, client.master.node_id
    r = client.replicas[0]
    if not r.readonly:                  # 未开 READONLY -> 应拒绝/重定向主
        v, ver = client.master.data.get(key, (None, 0))
        return v, ver, client.master.node_id + "(被重定向: 副本未开READONLY)"
    v, ver = r.data.get(key, (None, 0))
    return v, ver, r.node_id


if __name__ == "__main__":
    c = Cluster()
    c.replicas[0].readonly = True       # 只有这条连接开了副本读

    c.write("user:1", "v1", version=1)
    print("写入 user:1 = v1 (版本1), 副本尚未同步\n")

    _, ver_m, node_m = read(c, "user:1", "master")
    print(f"主库读:   版本 {ver_m} @ {node_m}")
    _, ver_r, node_r = read(c, "user:1", "replica")
    print(f"副本读:   版本 {ver_r} @ {node_r}  <- 旧值窗口: 写后立即副本读会读到旧数据")

    c.replica_catchup(1)
    _, ver_r2, _ = read(c, "user:1", "replica")
    print(f"副本追平后读: 版本 {ver_r2}")

    # 未开 READONLY 的新连接: 客户端按 MOVED 语义把读重定向回主
    c.replicas[0].readonly = False
    _, ver_x, node_x = read(c, "user:1", "replica")
    print(f"新连接(未READONLY)副本读: 版本 {ver_x} @ {node_x}")
    c.replicas[0].readonly = True

    # 故障转移: r1 升主
    c.master, c.replicas = c.replicas[0], [c.master, c.replicas[1]]
    c.master.role = "master"
    print(f"\n故障转移: r1 升主, 原读路由全部重定向, 连接需重建")
    print("结论：副本读是会话级 READONLY + 容忍旧值的读; 写后读走主,")
    print("      副本滞后超阈值自动切回主, 故障转移要演练路由收敛")
```

**追问一**：为什么副本读不能解决延迟问题，甚至可能更慢？

→ 解析：副本读省下的只是主节点的 CPU，但**多了一跳**：请求先到客户端路由/代理判断该去哪个副本（或直连副本但仍要确认槽归属），副本还要处理与主同步的复制流。若副本机器规格低于主（常见省成本配法），单副本读能力反而可能更差。真实收益只在"主节点读 QPS 接近瓶颈、且读流量能容忍旧值"时成立。扩读的优先级排序应该是：应用缓存（收益最大）→ 本地 L1（Q975）→ 副本读（兜底）。把副本读当第一手段，通常意味着架构上缓存没做对。

**追问二**：副本升主瞬间，正在进行的副本读会怎样？

→ 解析：三段连锁。第一段：升主瞬间旧连接还指向"前副本"，它已变成 master，原 READONLY 状态对 master 语义失效，客户端收到 MOVED/重定向或直接报错。第二段：客户端连接池要重建（对升主节点重发命令恢复路由表，Q6582 拓扑刷新），这期间读请求排队或失败——所以客户端要有路由刷新与重试。第三段：业务一致性上，若故障转移丢失了最后一段写（异步复制没追上，Q1415），副本读出来的"旧值"就是最后可见值，业务要能接受。演练时重点测收敛时间：从主挂到读路由恢复的 P99，决定这 30 秒内业务是否需要显式降级提示。
