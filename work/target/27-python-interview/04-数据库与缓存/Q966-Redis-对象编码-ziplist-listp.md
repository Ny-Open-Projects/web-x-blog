---
title: [Q966] Redis 对象编码: ziplist / listpack / skiplist
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q966 · Redis 对象编码: ziplist / listpack / skiplist

> 难度:★★★★ | 标签:Redis, 底层结构

**问**:Redis 的 zset 底层是什么?为什么小数据用 ziplist/listpack,大数据才用 skiplist?

**答**:每种类型按数据量动态选编码:小体量时 hash/zset/list 用 ziplist(Redis 7 起为 listpack,紧凑连续内存、省指针),超过阈值(如 zset 128 个元素或单值 64 字节,listpack-max-xxx 配置)转为 skiplist+dict 双结构。zset 的 skiplist 维护按 score 排序的跳表实现范围查询,dict 维护 member->score 实现 O(1) 查分,两者共享元素。意义:小集合全在一段连续内存,缓存友好且省内存;大集合才值得付出多结构代价。面试要点:能说出"编码随阈值切换"与"zset 双结构分工"即可,极端细节(listpack 与 ziplist 的级联更新差异)属于加分项。

```python
# file: code/04_数据库与缓存/q966_encoding.py
"""模拟编码切换阈值 + zset 双结构分工; 有 redis 时打印真实 OBJECT ENCODING"""
import sys

THRESHOLDS = {"list-max-listpack-size": 128, "hash-max-listpack-entries": 128,
              "zset-max-listpack-entries": 128, "zset-max-listpack-value": 64}

class MiniZSet:
    """listpack 阶段: 单列表; 超阈值升级 skiplist+dict 双结构"""
    def __init__(self):
        self.mode = "listpack"
        self.pairs = []          # [(member, score)]
        self.dict = {}           # member -> score

    def add(self, member, score):
        if self.mode == "listpack":
            self.pairs.append((member, score))
            if len(self.pairs) > THRESHOLDS["zset-max-listpack-entries"] or \
               len(member) > THRESHOLDS["zset-max-listpack-value"]:
                self.mode = "skiplist"
                self.dict = dict(self.pairs)
        else:
            self.dict[member] = score

if __name__ == "__main__":
    z = MiniZSet()
    for i in range(THRESHOLDS["zset-max-listpack-entries"] + 1):
        z.add(f"m{i}", i)
    print("元素超阈值后编码:", z.mode, "<- listpack 升级为 skiplist")
    print("skiplist 管 zrangebyscore, dict 管 zscore, 两者共享元素")

    try:
        import redis
        r = redis.Redis(decode_responses=True)
        r.zadd("enc_demo", {"a": 1})
        print("真实编码(小 zset):", r.object("ENCODING", "enc_demo"))
        r.delete("enc_demo")
    except Exception as e:
        print("无可用 redis, 仅演示:", type(e).__name__)
```

**追问**:
- listpack 相比 ziplist 改进了什么?——取消了 prevlen 的连锁更新问题,每项只记自身长度,最坏插入从 O(n方) 降为 O(n)。
- 怎么观察线上对象的真实编码?——`OBJECT ENCODING key` 与 `redis-cli --bigkeys`,大 key 治理前先确认它处在哪个编码阶段。

---
