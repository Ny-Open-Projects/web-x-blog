---
title: [Q6680] 集群MGET跨slot拆分容量账
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6680 · Redis Cluster 下 MGET 跨 slot 拆分：往返成本与容量账

难度：P6 ｜ 标签：容量规划、Redis Cluster、批量命令
基线：Redis Cluster（CRC16 → 16384 slot）；redis-py 5+ 的 `mget_keys`/`mget_nonatomic` 自动拆分。

**问**：单机 Redis 的 `MGET k1..k100` 一条命令搞定，迁到 Cluster 后为什么报 CROSSSLOT 错误？客户端拆分后网络往返从 1 变多少？这次迁移的容量账怎么算？

**答**：**结论**：Cluster 按 key 的 CRC16 映射到 16384 个 slot，多 key 命令要求所有 key 同 slot（`{hash_tag}` 包裹可强制同槽，但会造成数据倾斜）。客户端库的通用做法是**按 slot 分组、每组一次请求**——100 个随机 key 大概率散布在几十个 slot 上，往返数从 1 涨到"slot 数"。容量账的两端：客户端侧 P99 延迟由最慢的一组决定（尾部放大），服务端侧总请求数 = 批量数 × 平均 slot 分组数，QPS 预算要按这个放大系数评估。

**取舍**：三条路线：① hash tag 强制同槽（`{user123}:cart`）——MGET 保住一条往返，代价是同 tag key 全落一个节点，热点与迁移风险；② 客户端按 slot 拆分——无倾斜，代价是往返放大与 P99 尾部；③ Pipeline 打包多组请求——往返数接近 1，但要控制单 pipeline 字节数避免打满缓冲区。热 key 集中场景选 ①，均匀 key 选 ③。

**实战**：迁移前用真实 key 样本算"slot 分组分布"，得出平均组数与 P99 组数，写进容量评审；拆分逻辑自己实现时用 `CRC16 XMODEM` 与 `slot = crc16(key) % 16384`，注意 redis-py 默认对不含 tag 的 key 直接取整 key 哈希。

```python
# Cluster slot 计算与 MGET 拆分的容量账（标准库实现 CRC16-XMODEM）
_CRC_TABLE = []
for _b in range(256):
    _c = _b << 8
    for _ in range(8):
        _c = ((_c << 1) ^ 0x1021) if _c & 0x8000 else (_c << 1)
    _CRC_TABLE.append(_c & 0xFFFF)

def crc16(data: bytes) -> int:
    crc = 0
    for byte in data:
        crc = ((crc << 8) & 0xFFFF) ^ _CRC_TABLE[((crc >> 8) ^ byte) & 0xFF]
    return crc

def slot(key: str) -> int:
    """redis-py 风格：提取 {tag} 内的部分参与哈希。"""
    if "{" in key:
        start = key.index("{") + 1
        end = key.find("}", start)
        if end > start:
            key = key[start:end]
    return crc16(key.encode()) % 16384

def split_by_slot(keys: list[str]) -> dict[int, list[str]]:
    groups: dict[int, list[str]] = {}
    for k in keys:
        groups.setdefault(slot(k), []).append(k)
    return groups

import random
random.seed(7)
keys = [f"product:{i}" for i in range(100)]
groups = split_by_slot(keys)
print(f"100 个 key -> {len(groups)} 个 slot 组，"
      f"往返数 1 -> {len(groups)}（无 pipeline 时）")

# 容量账：服务端 QPS 放大系数 = 平均组数
avg_groups = len(groups)          # 随机 key 接近组数下限=组数≈key 数的分布
tagged = [f"{{user42}}:cart:{i}" for i in range(100)]
tag_groups = split_by_slot(tagged)
print(f"hash tag 后 -> {len(tag_groups)} 组（1 次往返，但同节点倾斜）")

# P99 尾部：总延迟 = max(各组延迟)，组数越多尾部越差
import statistics
lat = lambda g: 2 + len(g) * 0.01      # 每组固定 RTT + 处理耗时
delays = [lat(g) for g in groups.values()]
print(f"单往返延迟 ~2ms；拆分后 P50={statistics.median(delays):.2f}ms "
      f"P99={max(delays):.2f}ms（由最慢组决定）")
```

**追问 1**：为什么 `{tag}` 能让多 key 同槽？它引入的最大风险是什么？
提示：Cluster 只对 `{}` 内内容哈希，同 tag 必同槽；风险是业务把大批 key 挂在同一 tag 上造成单节点热点与 reshard 迁移困难，tag 粒度要按"实体"（user/order）划分而不是全局常量。

**追问 2**：Pipeline 与按 slot 拆分能叠加吗？上限怎么控？
提示：能——按 slot 分组后每组进同一 pipeline 并发发出；上限由节点输出缓冲区与 `maxmemory` 压力决定，实践中单 pipeline 控制在几百 KB 与几千条命令以内。

**追问 3**：如果 key 数扩大到 1 万，纯拆分方案会怎样？
提示：1 万个随机 key ≈ 上千个 slot 组，往返与调度开销超过批量收益；此时应降级为"多次小批量 + 并发"或改用本地缓存/二级索引结构，MGET 本身不再适用。

## 背诵要点
1. Cluster 多 key 命令必须同 slot：CRC16(key) % 16384；`{tag}` 强制同槽但引入倾斜风险，tag 按实体划分。
2. 容量账两端：服务端请求数 × 平均 slot 组数；客户端 P99 由最慢组决定（尾部放大）。
3. 大批量演进路径：按 slot 拆分 → slot 分组 + pipeline 并发 → key 数过大时放弃 MGET 改结构。

## 复盘追问
1. 你从主从迁到 Cluster 时，哪些批量命令踩过 CROSSSLOT？当时的改造记录里有没有留下"slot 组数"这个指标？
2. hash tag 方案上线后如何监控倾斜？什么信号会触发你把 tag 拆细？
