---
title: [Q967] 大 key 扫描与拆分
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q967 · 大 key 扫描与拆分

> 难度:★★★★ | 标签:Redis, 大 key

**问**:什么是大 key?怎么发现?怎么拆分和删除而不阻塞线上?

**答**:大 key 指 value 过大(如几百万元素的 hash/list、几 MB 的 string),危害是读写慢、阻塞单线程、主从同步与迁移卡顿、内存倾斜。发现手段:`redis-cli --bigkeys`(采样)、SCAN 全量分析内存、RDB 离线分析工具。治理三板斧:一、拆分——hash 按 field 哈希分成 N 个子键(field->field%N),list 按时间分段;二、压缩与瘦身——value 序列化压缩、过期字段清理;三、异步删除——4.0+ 用 UNLINK(后台线程回收)代替 DEL,大批量用 SCAN 分批删除,严禁直接 DEL 千万元素 key。写路径设计阶段就该限制单 key 规模,是"设计问题"不是"清理问题"。

```python
# file: code/04_数据库与缓存/q967_big_key_scan.py
"""SCAN 游标遍历找大 key + hash 分片拆分 + 分批删除"""
import json

def scan_all(store, cursor=0, batch=3):
    """模拟 SCAN: 返回 批内keys, 新cursor; cursor=0 表示结束"""
    keys = sorted(store.keys())
    if cursor >= len(keys):
        return [], 0
    chunk = keys[cursor:cursor + batch]
    nxt = cursor + batch
    return chunk, nxt if nxt < len(keys) else 0

def big_keys(store, limit=20):
    found = []
    c = 0
    while True:
        chunk, c = scan_all(store, c)
        for k in chunk:
            size = len(json.dumps(store[k]).encode())
            if size > limit:
                found.append((k, size))
        if c == 0:
            break
    return found

def split_hash(big_value, shards=4):
    out = {f"hash:{i}": {} for i in range(shards)}
    for field, v in big_value.items():
        out[f"hash:{hash(field) % shards}"][field] = v
    return out

if __name__ == "__main__":
    store = {"user:1": {"name": "a"}, "feed:2": {f"p{i}": "x" * 30 for i in range(50)}}
    print("大 key 扫描:", big_keys(store))
    big = store["feed:2"]
    parts = split_hash(big)
    print("拆分后:", {k: len(v) for k, v in parts.items()})
    print("删除用 UNLINK 分批: 每次 SCAN 取一批 UNLINK, 避免单次 DEL 阻塞")
```

**追问**:
- 为什么不能用 KEYS 找大 key?——KEYS 一次性遍历全库阻塞单线程,生产禁用;SCAN 游标分批、可中断、复杂度仍 O(N) 但摊薄到每次调用。
- hash 拆分后怎么"整体取回"?——应用层聚合 N 个子键(并行 MGET/HGETALL),跨片统计的成本是拆分的代价,设计时要评估读模式。

---
