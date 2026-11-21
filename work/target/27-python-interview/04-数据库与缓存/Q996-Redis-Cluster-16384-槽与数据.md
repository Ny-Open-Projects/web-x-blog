---
title: [Q996] Redis Cluster: 16384 槽与数据分片
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q996 · Redis Cluster: 16384 槽与数据分片

> 难度:★★★★ | 标签:Redis Cluster, 分片

**问**:Cluster 怎么决定一个 key 放哪个节点?为什么是 16384 个槽?客户端要注意什么?

**答**:key 经 CRC16 % 16384 得到槽号,槽分配给节点(每节点负责一段),节点间 gossip 协议交换槽位图。为什么 16384:作者解释心跳包里槽位图用 bitmap 压缩,16384 位约 2KB 合适,且集群规模设计上限约 1000 节点,够用且省带宽。多键操作要求所有键同槽——hash tag `{user1000}:orders` 强制同槽。客户端要点:走 MOVED/ASK 重定向或智能客户端(SDK 缓存槽位图直连正确节点);resharding 期间用 ASK 临时重定向; Lua 与事务、MGET 批量同样受同槽约束。扩容是"搬槽":逐槽迁移+双写窗口,业务低峰执行。

```python
# file: code/04_数据库与缓存/q996_cluster_slots.py
"""CRC16 取模映射槽位(教学实现) + hash tag 同槽演示"""

CRC16_TABLE = None

def crc16(data: bytes) -> int:
    """CRC-16/XMODEM, Redis cluster 使用的多项式 0x1021"""
    crc = 0
    for b in data:
        crc ^= b << 8
        for _ in range(8):
            crc = ((crc << 1) ^ 0x1021) if crc & 0x8000 else (crc << 1)
            crc &= 0xFFFF
    return crc

def key_slot(key: str) -> int:
    # hash tag: 取第一个 {..} 内的内容参与计算
    if "{" in key and "}" in key:
        tag = key[key.index("{") + 1:key.index("}")]
        if tag:
            key = tag
    return crc16(key.encode()) % 16384

if __name__ == "__main__":
    nodes = {"nodeA": range(0, 8192), "nodeB": range(8192, 16384)}
    def node_of(key):
        slot = key_slot(key)
        return ("nodeA" if slot in nodes["nodeA"] else "nodeB", slot)

    for k in ("user:1", "user:2", "{user1}:profile", "{user1}:orders"):
        n, s = node_of(k)
        print(f"{k:<18} -> 槽 {s:<5} 节点 {n}")
    print("hash tag 保证 {user1} 系列同槽, 多键操作可用")
```

**追问**:
- MOVED 与 ASK 的区别?——MOVED 是"槽已永久归他人, 更新你的槽位图";ASK 是"槽正在迁移, 本次去新节点问, 但别更新缓存"。
- Cluster 模式下还支持 MULTI 吗?——支持,但只能操作同槽键;跨槽事务放弃,业务改 hash tag 或拆流程。

---
