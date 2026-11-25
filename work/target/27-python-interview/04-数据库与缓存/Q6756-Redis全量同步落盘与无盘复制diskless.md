---
title: "[Q6756] 从库上线拖垮主库：RDB 全量同步的落盘与无盘复制 diskless"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6756 · 从库上线拖垮主库：RDB 全量同步的落盘与无盘复制 diskless

难度：P6 ｜ 标签：Redis、主从复制、全量同步、repl-diskless-sync

基线：Python 3.12；用时长与磁盘占用的账面模型对比 diskful 与 diskless 全量同步。

**问**：给 20GB 的 Redis 主库新挂一个从库，主库立刻出现延迟毛刺，磁盘上多出一个几百 MB 的临时 RDB 文件，如果同时挂三个从库更明显。全量同步时主库到底做了什么？`repl-diskless-sync` 开还是不开？为什么这个参数还有个 `repl-diskless-sync-delay` 要配？

**答**：
- **结论**：全量同步时主库要 `bgsave` 出一份 RDB 发给从库。**diskful（默认关 diskless）**：fork 出子进程把 RDB 写到磁盘临时文件，再由主进程分发给所有等待的从库——优点是临时文件可复用（多个从库同一时刻上线只做一次 bgsave），缺点是占一块磁盘空间、写入慢盘时拖长全量窗口。**diskless**：fork 的子进程不走磁盘，直接把 RDB **流式**写进每个从库的网络连接——省磁盘、起量快，但每个从库要单独生成一次 RDB 流，多从库同时上线会 fork 多次，且 `repl-diskless-sync-delay` 会让主库**等几秒**，把同一批上线的从库凑齐再开始，避免串行生成多份。
- **取舍**：① 主库磁盘紧张（容器/small 盘）或用了 tmpfs，选 diskless；② 主库磁盘富裕、但经常**批量增删从库**（弹性扩缩容），diskful + delay 更省 fork 次数；③ diskless 下 `sync_delay` 设 0~5 秒，是从库上线速度与主库 fork 次数的折中；④ 无论哪种，20GB 实例的 bgsave 都要 fork（Q1421 的 COW 连锁反应），全量同步窗口内主库写入要收敛。
- **实战**：① 新从库上线错峰，别和大促重合；② 用 `INFO stats` 的 `sync_full`/`sync_partial_ok` 观察全量/部分同步比例，频繁 `sync_full` 说明 backlog 太小（Q6739）在反复全量；③ diskless 下盯主库网络出口带宽，RDB 流可能把复制带宽打满影响业务流量；④ 从库侧同样有加载 RDB 的窗口，加载完成前从库是空的，读流量切过去会全部回源。

```python
"""全量同步账面模型：diskful(落盘复用) vs diskless(流式多份) 的时长与磁盘占用。"""
DATA_GB = 20
DISK_WRITE_MBPS = 150     # 主库磁盘写 RDB 的速度
NET_MBPS = 600            # 分发/流式带宽
FORK_COST_S = 1.5         # fork + COW 启动开销


def diskful(replicas: int) -> dict:
    gen = FORK_COST_S + DATA_GB * 1024 / DISK_WRITE_MBPS   # 一次 bgsave 落盘
    send = DATA_GB * 1024 / NET_MBPS                       # 临时文件复用，分发一次
    return {"耗时_s": gen + send, "forks": 1,
            "主库磁盘峰值_MB": DATA_GB * 1024}


def diskless(replicas: int, delay_s: float) -> dict:
    if replicas == 0:
        return {"耗时_s": 0, "forks": 0, "主库磁盘峰值_MB": 0}
    # delay 把同一批上线的从库凑齐 -> 一份流式生成，逐路复制
    gen = FORK_COST_S + DATA_GB * 1024 / NET_MBPS
    return {"耗时_s": delay_s + gen, "forks": 1, "主库磁盘峰值_MB": 0}


def staggered_diskless(replicas: int) -> dict:
    """从库分批上线且 delay=0：每批各 fork 一次。"""
    return {"耗时_s": FORK_COST_S + replicas * (DATA_GB * 1024 / NET_MBPS),
            "forks": replicas, "主库磁盘峰值_MB": 0}


if __name__ == "__main__":
    for n in (1, 3):
        d1 = diskful(n)
        d2 = diskless(n, delay_s=2.0)
        d3 = staggered_diskless(n)
        print(f"{n} 个从库同时上线:")
        print(f"  diskful   耗时 {d1['耗时_s']:.0f}s fork {d1['forks']} 次"
              f" 磁盘峰值 {d1['主库磁盘峰值_MB']}MB")
        print(f"  diskless+delay 耗时 {d2['耗时_s']:.0f}s fork {d2['forks']} 次"
              f" 磁盘峰值 {d2['主库磁盘峰值_MB']}MB")
        print(f"  diskless零延迟分批 耗时 {d3['耗时_s']:.0f}s fork {d3['forks']} 次")
    print("\n结论：diskless 省磁盘但不省 fork；delay 的意义是把同批从库凑齐只流式一次")
    print("      diskful 的临时文件在多从库场景是复用资产，单从库场景才是纯开销")
```

**追问一**：全量同步期间主库新写入的数据会丢吗？

→ 解析：不会丢，但会走"全量+增量"接力：bgsave 开始时主库记下复制偏移量，RDB 发送期间的新写命令先堆在复制缓冲区/replication backlog 里，从库加载完 RDB 后再回放这段增量。风险在**缓冲区溢出**：RDB 生成传输太慢、期间写入又猛，客户端输出缓冲区超限会把从库踢掉重连，再触发一次全量，进入"全量风暴"循环。所以大实例挂从库要么收敛写入、要么先调大 `client-output-buffer-limit replica`，让增量窗口撑得住。

**追问二**：为什么大规模集群更推荐"从盘级联复制"？

→ 解析：所有从库都挂在一个主库上，全量同步的 fork、网络出口、COW 内存都压在主库一个点上；级联复制（从库下面再挂从库）把分发树化，主库只服务一层子节点，深层的全量由中间从库承担。代价是链路变长、延迟叠加，且中间节点故障会传染给下游。Redis Sentinel/Cluster 的拓扑设计里，副本数多、实例大的场景（如 20GB+、副本 ≥3）都值得评估两级复制，把"一次上线三从库"的峰值从主库挪走。
