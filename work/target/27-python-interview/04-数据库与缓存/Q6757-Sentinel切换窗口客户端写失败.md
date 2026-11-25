---
title: "[Q6757] 主库宕机后 30 秒：Sentinel 切换窗口里客户端在写谁"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6757 · 主库宕机后 30 秒：Sentinel 切换窗口里客户端在写谁

难度：P7 ｜ 标签：Redis、Sentinel、故障转移、客户端切换、写失败窗口

基线：Python 3.12；用状态机模拟主库宕机→Sentinel 仲裁→提升从库→客户端感知的完整时间线。

**问**：Redis 主库硬件故障宕机，Sentinel 配置 `down-after-milliseconds=5000`，实际业务却报了 30 秒左右的写错误，比配置值大了 6 倍。这 30 秒里发生了什么？客户端到底什么时候拿到新主库地址？应用侧怎么把写失败窗口压到最短？

**答**：
- **结论**：切换窗口是几段串行的延迟之和：① **主观下线（SDOWN）**：单个 Sentinel 超过 `down-after` 判主库无响应，约 5 秒；② **客观下线（ODOWN）+ 选举**：quorum 个 Sentinel 确认后，Sentinel 之间先选 leader（Raft 式投票，最多再加几秒）；③ **执行切换**：挑优先级最高/偏移量最新的从库发 `REPLICAOF NO ONE`，等它追平、通知其余从库改指向；④ **客户端感知**：只有订阅了 Sentinel 的 `+switch-master` 事件或重新执行 `SENTINEL get-master-addr` 才拿到新地址——**没订阅、也没重查的客户端会一直敲旧主库的门**，写失败窗口由客户端重连/重查策略决定，常常是全链路里最长的一段。
- **取舍**：① `down-after` 调小切得快，但网络抖动会误切换（切一次就是一次全量同步，见 Q6756 的连锁），不是越小越好；② 客户端必须用支持 Sentinel 的驱动（redis-py 的 `Sentinel` 类），自己缓存 master 地址的封装是事故重灾区；③ 写失败的兜底要区分**可降级**（缓存类写，跳过等恢复）与**不可降级**（关键状态，落库 DB 再回补缓存）；④ `parallel-syncs` 控制其余从库改指向的并发，调大可缩短整体切换时间但给新主更大瞬时压力。
- **实战**：① 客户端订阅 `+switch-master` 事件主动失效连接池，而不是等下一次请求失败被动重连；② 应用侧写失败重试要带"查 Sentinel"步骤（Q6512 的应用侧配合同理）；③ 故障演练定期做，把真实窗口（SDOWN→ODOWN→switch-master→客户端拿到新地址）用埋点量出来；④ Sentinel 节点至少 3 个且跨可用区，quorum=2，避免单点仲裁。

```python
"""Sentinel 切换时间线：SDOWN -> ODOWN/选主 -> 提升 -> 客户端感知。"""
import time

Timeline = list[tuple[float, str]]


def simulate(down_after_s: float, quorum_vote_s: float,
             promote_s: float, client_mode: str) -> tuple[float, int]:
    """client_mode: subscribe=订阅事件 | repoll=每次请求重查 | cache=本地缓存地址。
    返回 (写失败窗口秒数, 失败请求数)。"""
    switch_ready = down_after_s + quorum_vote_s + promote_s
    failed = 0
    if client_mode == "subscribe":
        window = switch_ready                      # 事件一到位立刻切
    elif client_mode == "repoll":
        # 每 5s 重试一次写，失败后重查 Sentinel
        t, step = 0.0, 5.0
        while t < switch_ready:
            failed += 1
            t += step
        window = t
    else:                                          # cache: 固定地址，重连也无用
        t, step = 0.0, 5.0
        while t < switch_ready + 60.0:             # 直到人工介入(分钟级)
            failed += 1
            t += step
        window = t
    return window, failed


if __name__ == "__main__":
    down_after, vote, promote = 5.0, 4.0, 6.0      # 秒
    print(f"服务端切换就绪: {down_after + vote + promote:.0f}s "
          f"(SDOWN {down_after} + 仲裁/选主 {vote} + 提升 {promote})\n")
    for mode, desc in (("subscribe", "订阅 +switch-master 事件"),
                       ("repoll", "失败后重查 Sentinel"),
                       ("cache", "本地写死主库地址")):
        w, f = simulate(down_after, vote, promote, mode)
        print(f"{desc:<18} 写失败窗口 {w:5.1f}s | 失败请求 ~{f} 次")
    print("\n结论：切换慢常常慢在客户端；订阅事件 + 主动失效连接池才能贴住服务端下限")
    print("      down-after 不是越小越好：误切换的代价是一次全量同步")
```

**追问一**：为什么 Sentinel 需要 quorum 个节点确认，一个不行吗？

→ 解析：单个 Sentinel 判断"主库无响应"可能与它自身的网络分区有关（它看不见主库，主库其实活着）；quorum 机制让多数派确认才进入 ODOWN，把"我这边看不见"与"大家都看不见"区分开。同样，Sentinel 内部选 leader 也要多数派投票，所以 Sentinel 节点要奇数个（通常 3 或 5）。若把 quorum 设成 1，任何一台 Sentinel 的网络抖动都可能触发一次不必要的故障转移，而每次转移都伴随全量同步与写窗口。

**追问二**：切换完成后，原主库恢复上线会发生什么？

→ 解析：Sentinel 会把它降级为从库并指向新主库（`REPLICAOF` 新主），若它宕机期间数据落后，会触发一次全量同步。要警惕两个坑：① 原主库是**重启后带旧数据**上线且 Sentinel 尚未接管，客户端（写死地址的）会把写流量打回旧主库，造成双主分叉数据；② 只读模式被人为关掉的旧主库（Q6651 的写从库事故同理）会静默接收写请求。所以恢复上线流程要人工确认 Sentinel 已把它标记为 replica、且应用连接池已刷新，再放回服务。
