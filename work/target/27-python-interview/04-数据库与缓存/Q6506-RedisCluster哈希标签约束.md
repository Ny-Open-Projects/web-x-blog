---
title: [Q6506] Redis Cluster hash tag 的批量与事务约束
date: 2026-11-18
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6506 · Redis Cluster hash tag 的批量与事务约束

> 难度:★★★ | 标签:Redis, Cluster, 数据分布

**问**：业务想在 Cluster 里用 MSET/MULTI 一次写用户的一组 key，结果报 CROSSSLOT。hash tag 到底怎么工作？用了 hash tag 之后，又引入了什么新问题？

**答**：结论：Cluster 按 key 的 CRC16 模 16384 分槽，只有 `{...}` 内的部分参与计算（hash tag）。MSET/MULTI/Lua 多 key/SUNION 这类跨 key 原子操作，要求所有 key 落同一槽，否则 CROSSSLOT。hash tag 把 `user:{u100}:profile`、`user:{u100}:orders` 钉到同一槽，换来单用户级的原子性——代价是**数据分布被你接管，热点由 tag 设计决定**。

取舍与实战：
- tag 粒度即热点粒度：tag 越细（按 user）数据越均匀但原子域越小；tag 越粗（按租户）原子域越大但单槽承载过大流量。槽迁移时一个 tag 整体搬移，超大 tag 让 reshard 卡顿。经验：tag 选择"最小的需要原子的业务域"，通常是单实体 id。
- pipeline 不受 CROSSSLOT 限制（客户端按槽分组发送），只有 MULTI/EXEC、Lua 多 key、服务端聚合类命令受限。所以"批量写"优先 pipeline + 客户端分槽，只有"真原子需求"才 hash tag。
- 事故复盘：某团队把 `{tenant_1}` 当 tag，一个大租户 40% 流量砸进一个槽，出现单节点 CPU 90% 而其他节点 10%。修复是拆 tag（原子域收缩到单实体）+ 对该租户写路径去原子化（pipeline + 业务层补偿）。教训：hash tag 是原子性的手段，不是性能优化；用之前先回答"这个原子域业务上真的需要吗"。

```python
# 基线:Python 3.9+ 标准库;模拟 CRC16 分槽与 hash tag 提取(可运行,算法为 Redis 官方 CRC16-CCITT)
def crc16(data: bytes) -> int:
    crc = 0
    for b in data:
        crc ^= b << 8
        for _ in range(8):
            crc = ((crc << 1) ^ 0x1021) & 0xFFFF if crc & 0x8000 else (crc << 1) & 0xFFFF
    return crc

REDIS_CLUSTER_SLOTS = 16384

def keyslot(key: str) -> int:
    """Redis Cluster 分槽:取第一对 {} 内的子串做 CRC16,无 {} 则整个 key。"""
    i = key.find("{")
    if i >= 0:
        j = key.find("}", i + 1)
        if j > i + 1:                       # "{}" 空标签不算
            key = key[i + 1:j]
    return crc16(key.encode()) % REDIS_CLUSTER_SLOTS

def group_by_slot(keys: list[str]) -> dict[int, list[str]]:
    """pipeline 场景:客户端按槽分组发(MULTI 则要求组内单槽)。"""
    g: dict[int, list[str]] = {}
    for k in keys:
        g.setdefault(keyslot(k), []).append(k)
    return g

if __name__ == "__main__":
    same = ["user:{u100}:profile", "user:{u100}:orders", "user:{u100}:cart"]
    print({k: keyslot(k) for k in same})            # 三者同槽
    print(group_by_slot(same + ["order:9"]))        # order:9 被分到别的槽
    try:
        assert len(group_by_slot(same)) == 1
        print("MULTI OK: 全部同槽")
    except AssertionError:
        print("CROSSSLOT")
```

**追问**：
- 一层追问：MULTI 和 pipeline 的原子性区别？——MULTI 是服务端事务（EXEC 原子执行、无回滚，中途错命令继续）；pipeline 只是网络层攒批，命令逐条独立执行，可能被其他客户端插入。要原子用 MULTI+hash tag，要吞吐用 pipeline。
- 二层追问：Lua 脚本在 Cluster 上的 key 约束？——脚本里所有访问的 key 必须与传入 KEYS 同槽，脚本内不允许拼 key 绕过（如用 ARGV 拼 key 再 GET 会 CROSSSLOT），这是很多人从单机迁移过来的坑。
- 三层追问：怎么发现"tag 热点"？——`redis-cli --cluster check` 看槽分布没意义（槽均匀≠流量均匀），要用节点级 QPS/CPU 对比 + `redis-cli monitor` 抽样按 tag 聚合；节点间 CPU 差异 >3 倍基本可判定数据倾斜。
