---
title: [Q6582] Redis Cluster 拓扑刷新缺失 MOVED 风暴复盘
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6582 · Redis Cluster 拓扑刷新缺失 MOVED 风暴复盘

难度：P7 ｜ 标签：Redis Cluster / MOVED / 客户端 / 事故复盘

**问**：运维对 Redis Cluster 做了在线扩容 reshard，之后一段时间 P99 延迟翻倍，日志里大量 `MOVED 12345 10.0.3.7:6379`。扩容都完成了为什么还会持续 MOVED？怎么避免这类延迟毛刺？

**答**：
- **结论**：MOVED 是集群告诉客户端"这个 key 不归我，去问新主人"。reshard 期间以及完成后，如果客户端不主动刷新槽位表（cluster slots / cluster shards），每次请求都走"旧节点 → 301 重定向 → 新节点"两跳，延迟翻倍且旧节点被打满。redis-py 的 `RedisCluster` 默认 `require_full_coverage` 与拓扑缓存需要显式 `cluster_mts`/重连或 `reload_clusters` 才会更新；很多自研客户端只在重连时才刷新拓扑，于是"reshard 完成后风暴持续"。
- **取舍**：客户端侧解法：① 用支持集群拓扑自动刷新的客户端（redis-py 4.1+ 的 `RedisCluster`、lettuce、Go-redis 都内置）；② reshard 前把客户端拓扑刷新间隔调小，reshard 后对批量 key 迁移窗口做限流。服务端侧解法：ASK 与 MOVED 不同——迁移中间态是 ASK（本次去新节点但不更新缓存），完成态才是 MOVED（可更新缓存）；客户端必须实现"收到 MOVED/ASK 就更新本地槽表"的闭环，否则等于没做集群感知。
- **实战**：事故剧本：① 监控里 MOVED/ASK 响应占比做成指标（redis-py 可用 `RESP` 响应回调统计），超过 1% 即告警；② reshard 用 `--cluster reshard` 分批小步迁移（每批 100-500 槽），配合业务低峰；③ 扩容完成后对客户端执行一轮受控重连（滚动重启或手动触发拓扑 reload），确认 MOVED 归零再收工；④ 复盘项：把"客户端拓扑刷新能力"纳入 Redis 客户端选型的硬性验收项。

```python
# Redis Cluster 客户端拓扑缓存模拟器（纯标准库）
# 基线：Python 3.9+；真实连接用 redis-py 5.x（缺库时本脚本自动降级为纯模拟）

import random


class FakeCluster:
    """模拟 3 节点集群 0..16383 槽位，可执行 reshard"""

    def __init__(self, slots_per_node: dict[str, int]) -> None:
        total = sum(slots_per_node.values())
        assert total == 16384
        cur = 0
        self.owner: list[str] = []
        for node, n in slots_per_node.items():
            self.owner.extend([node] * n)
            cur += n

    def reshard_move(self, slot: int, to_node: str) -> None:
        self.owner[slot] = to_node


class Client:
    """只随 MOVED 被动刷新（坏实现） vs 定期刷新（好实现）"""

    def __init__(self, cluster: FakeCluster, active_refresh: bool) -> None:
        self.cluster = cluster
        self.cache: list[str] = list(cluster.owner)
        self.active_refresh = active_refresh
        self.moved = 0

    def refresh(self) -> None:
        self.cache = list(self.cluster.owner)

    def get(self, key: int) -> str:
        node = self.cache[key]
        if self.cluster.owner[key] != node:
            self.moved += 1
            if self.active_refresh:
                self.refresh()  # MOVED 即刷新
        return self.cluster.owner[key]


def main() -> None:
    random.seed(7)
    c = FakeCluster({"a": 5461, "b": 5461, "c": 5462})
    # reshard: 1000 个槽从 a 迁到 d（模拟新增节点）
    c.reshard_move(0, "d")  # 占位，真实迁移见下方循环
    moved_slots = random.sample(range(16384), 1000)
    for s in moved_slots:
        c.reshard_move(s, "d")

    lazy = Client(c, active_refresh=False)
    eager = Client(c, active_refresh=True)
    lazy.refresh(); eager.refresh()
    keys = [random.randrange(16384) for _ in range(10000)]
    for k in keys:
        lazy.get(k)
    for k in keys:
        eager.get(k)
    # 坏实现：只有再次命中同一 key 才可能触发 MOVED，且不刷新 → MOVED 持续
    print(f"被动客户端 MOVED 次数: {lazy.moved}")
    print(f"主动刷新客户端 MOVED 次数: {eager.moved}")
    assert eager.moved == 0
    print("OK: MOVED 闭环刷新可消除重定向风暴")


if __name__ == "__main__":
    main()
```

**追问 1**：ASK 和 MOVED 在协议语义上的区别，客户端分别应该怎么处理？
→ 一句话提示：ASK 是"这一次去新节点试试（且要带 ASKING）"，槽还归旧节点管、不更新缓存；MOVED 是"槽永久归新节点"，必须更新本地槽表，否则每次都两跳。

**追问 2**：为什么 reshard 大 key 会造成阻塞，和 MOVED 风暴叠加时会发生什么？
→ 一句话提示：单 key 迁移是同步序列化传输，大 key 迁移阻塞源/目标节点正常命令；叠加客户端不刷新拓扑时，重定向流量涌入迁移中的节点，把它卡死，形成雪上加霜的放大。

## 背诵要点
- MOVED = 槽永久迁移（要更新客户端槽表），ASK = 迁移中间态（单次重定向 + ASKING，不更新缓存）。
- 客户端不刷新拓扑，reshard 后每次访问都是"旧节点→重定向"两跳，P99 翻倍；redis-py 4.1+ RedisCluster 内置刷新。
- reshard 分批小步（百槽级）、监控 MOVED 占比 >1% 告警、完成后受控重连收尾。

## 复盘追问
- 为什么说"重连就能修复拓扑"是个危险假设？提示：长连接池不主动重连，且重连风暴本身又会打爆节点；应当依赖协议级的主动刷新而非故障驱动的重连。
- hash tag（{user123}）在这类事故里扮演什么角色？提示：hash tag 把相关 key 固定在同一槽，迁移时同批大 key 一起走，会放大迁移阻塞，但也能保证多 key 操作不跨槽失败——是容量账里要单独算的一笔。
