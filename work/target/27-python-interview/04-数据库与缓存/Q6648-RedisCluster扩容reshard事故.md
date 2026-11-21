---
title: [Q6648] Redis Cluster 扩容 reshard 事故复盘
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6648 · Redis Cluster 扩容 reshard 事故复盘

难度：P7 | 标签：Redis Cluster、扩容、容量规划、事故复盘

**问**：三主 Cluster 内存水位 85%，决定加节点扩容。reshard 期间线上出现超时毛刺，甚至迁移卡死。slot 迁移对线上请求意味着什么？怎么把扩容做成无损操作？

**答**：
- **结论**：slot 处于 MIGRATING/IMPORTING 状态时，客户端请求该 slot 的 key：源节点有则正常返回，没有则返回 ASK 重定向——多一次往返且部分客户端兼容差，表现为该分片延迟毛刺。单个大 key（几十 MB 的 list/hash）迁移要一次性序列化传输，会卡住迁移通道甚至节点，是"reshard 卡死"的第一根因。无损扩容流程：先治理大 key → 小批量迁移 slot（每批 10-50 个）+ 迁移间休眠 → 低峰执行 → 全程监控 ASK/MOVED 比例与节点延迟。
- **取舍**：slot 区间重划时迁移量比一致性哈希大：3 主均分 slots 后加 2 主，即便重划均衡，约半数 key 换主；一致性哈希加节点只迁 1/(N+1)。Redis Cluster 用固定 16384 slot 换来路由表简单、客户端可缓存映射，代价就是扩容迁移量偏大——所以要"预留容量提前扩"，而不是水位打满才扩。
- **实战**：客户端侧：用支持 smart client 的驱动（自动缓存 slots 映射、处理 MOVED/ASK 并更新映射）；`cluster nodes` 拉映射的频率要克制，避免扩容期间全员拉取打爆管理端口。扩容后要重新观察各主内存均衡与热分片 QPS。

```python
# Redis Cluster slot 计算（CRC16/XMODEM，与 redis-cli cluster keyslot 一致）
def crc16(data: bytes) -> int:
    crc = 0
    for b in data:
        crc ^= b << 8
        for _ in range(8):
            crc = ((crc << 1) ^ 0x1021) & 0xFFFF if crc & 0x8000 else (crc << 1) & 0xFFFF
    return crc

def keyslot(key: str) -> int:
    s = key
    if "{" in key:                      # hash tag：取第一个 {} 内的内容
        start = key.index("{")
        end = key.find("}", start + 1)
        if end != -1 and end != start + 1:
            s = key[start + 1:end]
    return crc16(s.encode()) % 16384

def master_of(slot, masters):
    for name, lo, hi in masters:
        if lo <= slot <= hi:
            return name

# 3 主扩容到 4 主：均分重划后按区间看迁移量
old = [("m1", 0, 5460), ("m2", 5461, 10922), ("m3", 10923, 16383)]
new = [("m1", 0, 4095), ("m2", 4096, 8191), ("m3", 8192, 12287), ("m4", 12288, 16383)]

keys = [f"user:{i}:profile" for i in range(1000)] + ["{cart:42}.a", "{cart:42}.b"]
moved = sum(1 for k in keys if master_of(keyslot(k), old) != master_of(keyslot(k), new))
print(f"均分重划 3->4 主，{moved}/{len(keys)} ≈ {moved/len(keys):.0%} 的 key 换主")
print("hash tag 同槽:", keyslot("{cart:42}.a"), keyslot("{cart:42}.b"))
print("结论：区间均分迁移量远大于一致性哈希的 1/(N+1)，扩容要提前做且小批量迁")
```

**追问链**：
1. 追问一层：hash tag 是怎么改变 key 归属的？——取 key 中第一个非空 `{}` 内的子串参与 slot 计算，`{cart:42}.a` 与 `{cart:42}.b` 恒同槽；代价是 tag 内所有 key 集中在一个分片，可能造成热点。
2. 追问二层：扩容期间业务侧出现 MOVED 风暴说明什么？（客户端没更新 slots 映射或映射更新太慢，应升级驱动或提高映射刷新频率）

**背诵要点**：
1. reshard 毛刺来自 ASK 重定向；大 key 是迁移卡死第一根因。
2. 无损扩容：先治大 key，小批量迁 slot，低峰 + 全程监控。
3. slot 区间重划迁移量 ≈ 一致性哈希的两倍，扩容要提前做。

**复盘追问**：
1. reshard 进行到一半因大 key 卡死，怎么恢复？（跳过该 key 的 slot 单独处理，先拆 key 再迁）
2. 为什么"水位 85% 才扩容"本身就是事故预备条件？（迁移周期内可能到 maxmemory 触发淘汰/写入失败）
