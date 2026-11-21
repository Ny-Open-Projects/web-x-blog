---
title: [Q535] hash 随机化与 PYTHONHASHSEED
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q535 · hash 随机化与 PYTHONHASHSEED

> 难度:★★★★ | 标签:hash, 安全

**问**:为什么 str 的 hash 每次重启进程都不同?这防的是什么攻击?

**答**:自 3.3 起 str/bytes 的哈希默认加盐(hash randomization,可通过 PYTHONHASHSEED=0 关闭):同一进程内哈希一致,跨进程不可预测。防的是哈希碰撞 DoS——攻击者构造大量同哈希的 key 塞进 dict,哈希表退化成 O(n) 链,一个请求打满 CPU;随机盐让攻击者无法离线构造碰撞集。推论:任何「依赖 str 哈希稳定」的逻辑(把 hash 值持久化、跨进程分片路由)都是错的,需要稳定摘要用 hashlib。int 的哈希与数值本身相关(取模质数),不受随机化影响。

```python
# file: code/01_语言核心与底层/q535_hash_randomization.py
import sys

if __name__ == "__main__":
    print("randomization on:", sys.flags.hash_randomization)
    print("hash('python') =", hash("python"), "(differs across runs)")
    print("hash(42) =", hash(42), "(int hash is stable)")
    print("same within this process:", hash("a") == hash("a"))

    d = {}
    for i in range(1000):
        d[f"key{i}"] = i
    print("dict still O(1) on average:", len(d), "keys")

    print("rule: persist digests via hashlib, never via hash()")
```

**追问**:1) PYTHONHASHSEED=0 什么场景下用?——复现哈希相关的 bug、或基准测试要消除盐带来的抖动;生产严禁关闭,等于把 DoS 防线拆掉。2) 为什么要随机化?——防哈希碰撞 DoS:攻击者构造同桶键让 dict/set 操作退化 O(n²);3.3 起每进程随机盐,str/bytes 受影响,int 的哈希是自身不受盐影响。3) 底层算法?——str/bytes 用 SipHash 加进程盐;依赖字符串哈希顺序的遍历序不可复现,tuple 哈希组合元素哈希也不稳定,只有 int 稳定。4) 生产陷阱?——逻辑依赖 set/dict 遍历序(必须 sort);本地复现不了线上顺序问题,其实是盐差异;测试固定 PYTHONHASHSEED 只限测试环境,不要带进部署配置。
