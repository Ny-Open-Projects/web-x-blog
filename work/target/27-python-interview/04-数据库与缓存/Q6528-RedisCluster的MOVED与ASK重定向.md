---
title: [Q6528] Redis Cluster 的 MOVED 与 ASK 重定向
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6528 · Redis Cluster 的 MOVED 与 ASK：reshard 期间客户端到底发生了什么？

> 难度:★★★★ | 标签:Redis, Cluster, 一致性哈希

**问**：集群扩容 reshard 时，业务方观察到延迟毛刺和少量报错。`MOVED` 和 `ASK` 重定向的区别是什么？redis-py 的 RedisCluster 会自动处理吗？为什么 reshard 期间批量管道会大面积失败？

**答**：结论：`MOVED` 是**永久性**重定向——key 所属 slot 已归属新节点，客户端应更新本地 slot 映射后重发；`ASK` 是**临时性**重定向——slot 正在迁移中，该 key 可能已搬到目标节点，客户端本次要带 `ASKING` 标记去目标节点问一次，但**不许**更新 slot 映射（迁移没完成）。redis-py 的 `RedisCluster` 会自动处理这两种重定向并内置 slot 缓存刷新，但只对单 key 命令；跨 slot 的 pipeline/MULTI/Lua 在 reshard 期间会直接抛错，因为协议层面就不保证原子跨越迁移中的 slot。

机理与实战：
- 迁移时序：源节点标 MIGRATING → 目标标 IMPORTING → `CLUSTER GETKEYSINSLOT` 批量搬 key（`MIGRATE COPY` 按需逐 key）→ 搬完后 `CLUSTER SETSLOT` 双端更新 → 集群广播新拓扑。ASK 窗口就存在于"slot 没关闭但部分 key 已搬走"的中间态。
- 客户端坑：MOVED 后的 slot 映射刷新是全量还是增量影响毛刺大小；redis-py 刷新会重建连接池，一次拓扑变化可能抖动一批请求。`cluster_error_retry_attempts` 的默认重试会掩盖重定向成本，P99 毛刺要抓客户端侧指标而不是只看服务端。
- 工程对策：大 key 先治理再 reshard（一个 100MB key 的 MIGRATE 会阻塞双方节点）；业务低峰执行；对 pipeline 依赖重的场景按 slot 分桶组织 key（hash tag），让"一个业务单元"永远同 slot，reshard 时整批同进退。

```python
# 基线:Python 3.9+ / redis-py 4.3+ ;缺库降级:纯标准库模拟 redirect 决策
from dataclasses import dataclass


@dataclass
class Redirect:
    kind: str        # MOVED / ASK / None
    target: str


def handle_redirect(key_slot: int, redirect: Redirect,
                    slot_map: dict[int, str], asking: bool = False) -> tuple[str, dict, bool]:
    """模拟客户端对重定向的处理策略。"""
    if redirect.kind == "MOVED":
        slot_map[key_slot] = redirect.target       # 永久:更新本地映射
        return redirect.target, slot_map, False
    if redirect.kind == "ASK":
        # 临时:本次去目标节点并带 ASKING,但不更新映射
        return redirect.target, slot_map, True
    return redirect.target or "current", slot_map, asking


def demo() -> None:
    slot_map = {1000: "nodeA"}
    # 迁移完成:返回 MOVED
    tgt, m, ask = handle_redirect(1000, Redirect("MOVED", "nodeB"), slot_map)
    print("MOVED ->", tgt, "映射已更新:", m[1000] == "nodeB", "asking:", ask)
    # 迁移中:返回 ASK
    tgt, m, ask = handle_redirect(1000, Redirect("ASK", "nodeB"), slot_map)
    print("ASK ->", tgt, "映射未变:", m[1000] == "nodeB", "asking:", ask)


if __name__ == "__main__":
    demo()
```

**追问一**：为什么 ASK 重定向不许更新本地 slot 映射？
答：迁移中间态下 slot 的"官方归属"仍是源节点，其他 key 可能还在源上；若客户端把整个 slot 映射到目标，后续命中仍在源上的 key 会得到反向 MOVED，造成映射震荡。ASK 是单 key 的一次性旁路。

**追问二**：hash tag `{user1000}` 让业务 key 同 slot，代价是什么？
答：数据分布可能倾斜——热门用户的所有 key 落在同一 slot/节点，失去集群负载均衡；tag 粒度要选"事务/批量单元"而不是"全局用户"，并对倾斜节点做容量冗余或冷热拆分。

**背诵要点**：
- MOVED 永久更新映射，ASK 临时带 ASKING 旁路、不动映射。
- reshard 中间态下 pipeline/MULTI/Lua 跨 slot 必失败，客户端只自动重试单 key 命令。
- reshard 前置条件：大 key 治理、低峰执行、hash tag 按业务单元分桶。

**复盘追问**：
- redis-py slot 缓存刷新的触发条件与成本是什么？如何观测"客户端重定向次数"？
- 一个 100MB 大 key 在 MIGRATE 期间会造成什么阻塞？如何预判？

## 背诵要点
- ASK = 单 key 临时旁路，映射不能改；MOVED = 永久迁移完成。
- 迁移窗口内跨 slot 原子操作必失败，hash tag 分桶是根治手段。
- 大 key MIGRATE 阻塞双方节点，reshard 前必先治理。

## 复盘追问
- 如何用 CLUSTER 指标观测迁移进度并设计"迁移完成"的判定？
- 客户端映射刷新引发连接池重建时，如何做请求平滑（预热新池）？
