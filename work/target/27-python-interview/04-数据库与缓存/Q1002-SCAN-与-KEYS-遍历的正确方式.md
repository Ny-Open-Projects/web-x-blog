---
title: [Q1002] SCAN 与 KEYS: 遍历的正确方式
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1002 · SCAN 与 KEYS: 遍历的正确方式

> 难度:★★★★ | 标签:SCAN, 运维

**问**:SCAN 为什么不阻塞?它保证不漏不重吗?生产遍历的姿势是什么?

**答**:SCAN 用反向二进制迭代:游标是桶位掩码翻转序,遍历中即使 rehash,也能保证"遍历开始时已存在的元素至少返回一次"(可能重复返回,由客户端去重),且每次只处理一个桶的若干元素,O(1) 级,不阻塞单线程;KEYS 一次性全库 O(N) 阻塞,生产禁用。SCAN 语义要点:不保证元素在遍历期间被添加的会返回、可能重复、键在遍历中被删除则可能不返回——它是"尽力快照"。工程姿势:每次 SCAN count 100~500(按键大小调)、客户端 Set 去重、按模式 MATCH 只扫前缀、大集合用 HSCAN/SSCAN/ZSCAN 配合分批删除。

```python
# file: code/04_数据库与缓存/q1002_scan_iterate.py
"""模拟 SCAN 游标遍历 + 客户端去重"""
def scan(store, cursor, count=2):
    keys = sorted(store.keys())                  # redis 真实为桶序, 此处简化
    if cursor >= len(keys):
        return [], 0
    chunk = keys[cursor:cursor + count]
    nxt = (cursor + count) if cursor + count < len(keys) else 0
    return chunk, nxt

def scan_all(store):
    seen, cursor = set(), 0
    while True:
        chunk, cursor = scan(store, cursor)
        seen.update(chunk)
        if cursor == 0:
            return seen

if __name__ == "__main__":
    store = {f"user:{i}": i for i in range(10)}
    all_keys = scan_all(store)
    print("遍历到:", sorted(all_keys))
    print("完整:", all_keys == set(store.keys()))
    print("语义: 可能重复(需去重), 遍历期间新增键不保证返回")
    print("删除大集合: HSCAN 分批取 field -> HDEL 批删, 拒绝一次性 DEL")
```

**追问**:
- SCAN count 是精确数量吗?——不是,是每轮检查的桶数上限,实际返回受键密度影响,空桶多时返回少、游标推进快。
- 集群下怎么全库 SCAN?——每个节点单独 SCAN(客户端聚合),智能客户端提供按节点扫描接口。

---
