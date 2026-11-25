---
title: "[Q6787] 两千万个小键撑爆内存：Redis 每键开销与分桶聚合治理"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6787 · 两千万个小键撑爆内存：Redis 每键开销与分桶聚合治理

难度：P6 ｜ 标签：Redis内存、每键开销、分桶聚合、hash-max-listpack、键数估算

基线：Python 3.12；按 Redis 数据结构开销公式估算"百万小键 vs 单 hash 分桶"的内存账，模拟分桶聚合迁移与读写路径改造，全标准库实跑。

**问**：业务把每个用户的每个属性存成一个 string 键（`user:123:name`、`user:123:level`……），两千万个键把 16GB 实例撑爆，但每个键的 value 只有几十字节。为什么 Redis 一个小键的真实内存远大于 value 本身？分桶聚合进 hash 能省多少？改造的读写路径与迁移怎么做？

**答**：
- **结论**：Redis 的每键成本 = **robj 元数据（约 16B）+ SDS 键头（约 3~19B）+ 键字符串本身 + dict entry（约 8B）+ dict 桶摊销 + per-key 过期时间戳（约 8B，若设 TTL）**——一个 20 字节 value 的小键真实占 **100 字节上下**，元数据是 value 的 3~5 倍；两千万小键 ≈ 2GB+ 的纯开销，还没算全局 dict 的 rehash 双表峰值（Q6572）。治理方向是**聚合**：把同前缀/同归属的小键收进一个 hash（`HSET user:123 name x level 9`），hash 在 `hash-max-listpack-entries`（默认 128）与 `hash-max-listpack-value`（默认 64）以内时用紧凑 listpack 存储——**整个 hash 只付一次 robj+dict entry 的开销**，一百万个属性键聚成一万个 hash（每桶 100 字段）内存通常降 60%~80%。与拆分方向（大 hash 拆小键，Q1690/Q6643）是同一枚硬币的两面：键太稀→聚合省元数据，键太稠→拆分避免单键倾斜，分界由每桶字节数决定。
- **取舍**：① 聚合粒度：按"归属对象"（每用户一桶）还是按"数量固定分片"（每 100 个键一桶）——前者读写语义自然但用户键数悬殊会倾斜，后者均匀但需要一次路由查找；② 单桶膨胀风险：listpack 超 128 字段或单值超 64B 会升级为 hashtable，元数据开销回来一部分但仍省（dict 只在桶级），超大的桶要二次拆分；③ 语义损失：分桶后失去单键 TTL（要 7.4 的 HEXPIRE 字段级 TTL，Q6664，或整桶统一 TTL）、单键过期事件、单键 SCAN 定位——按"生命周期相同"的键才聚一桶是铁律；④ 迁移路径：双写（新聚合写 + 旧键只读）→ 离线脚本批量聚合 → 读切聚合 → 旧键批量 UNLINK（Q6776 异步释放），与缓存序列化升级（Q6653）同族的滚动兼容账。
- **实战**：① 键数先于字节数告警：`dbsize` 周环比与内存周环比双曲线，键数暴涨而字节缓涨就是小键泛滥；② 估算先行：改造前用本卡的公式算出收益比与桶分布（多少桶会超出 listpack 上限），收益 <30% 就不值得动；③ 聚合 value 精简：键名里重复的前缀（`user:123:user:level` 这类拼接错误）与长键名都是可瘦身项——键名本身也是 SDS 字节；④ 容量核算时把 per-key 开销常数（≈90B/键 + TTL 8B）写进成本模型（Q1014/Q1960 的内存账家族）。

```python
"""Q6787 Redis 每键开销账: 百万小键 vs hash 分桶聚合的内存对比。"""
ROBJ = 16          # redisObject
SDS_HDR = 9        # sdshdr8 头(键<255B 取小)
DICT_ENTRY = 8     # dictEntry
TTL_META = 8       # expires 表条目(设了 TTL 才有)


def key_cost(key_b: int, value_b: int, with_ttl: bool) -> int:
    """单 string 键的近似真实字节(不含 bucket 摊销/rehash)."""
    cost = ROBJ + SDS_HDR + key_b + 1 + SDS_HDR + value_b + 1 + DICT_ENTRY
    if with_ttl:
        cost += TTL_META
    return cost


def listpack_field_cost(field_b: int, value_b: int) -> int:
    """listpack 内一个字段的紧凑开销: 头+内容+结束字节, 无 per-field dict."""
    return 2 + field_b + 2 + value_b


def hash_bucket_cost(n_fields: int, key_b: int, value_b: int) -> int:
    """一个 hash 桶: 键自身开销一次 + n 个字段紧凑排列."""
    base = key_cost(key_b, 0, True) - DICT_ENTRY - TTL_META
    return base + n_fields * listpack_field_cost(key_b, value_b)


def estimate(n_keys: int, key_b: int, value_b: int, bucket: int) -> dict:
    flat = n_keys * key_cost(key_b, value_b, True)
    n_buckets = -(-n_keys // bucket)          # ceil
    packed = n_buckets * hash_bucket_cost(bucket, key_b, value_b)
    return {"flat_mb": flat / 1e6, "packed_mb": packed / 1e6,
            "n_buckets": n_buckets,
            "save_pct": 1 - packed / flat}


if __name__ == "__main__":
    r = estimate(n_keys=2_000_000, key_b=20, value_b=20, bucket=100)
    print(f"方案A 平铺小键:  {r['flat_mb']:>8.1f} MB  (键数 200万, 每键 ~{key_cost(20,20,True)}B)")
    print(f"方案B 分桶hash:  {r['packed_mb']:>8.1f} MB  ({r['n_buckets']} 桶, 每桶 100 字段)")
    print(f"收益: 节省 {r['save_pct']:.0%}")
    over = hash_bucket_cost(1000, 20, 20)     # 单桶 1000 字段: 超 listpack 上限
    print(f"风险检查: 单桶 1000 字段(超 128 上限)仍需 {over/1e3:.0f}KB -> 应二次拆桶")
    ok = (r["save_pct"] > 0.5 and key_cost(20, 20, True) > 3 * 20
          and r["n_buckets"] == 20000)
    print(f"校验: 元数据主导 + 聚合收益 + 桶数正确 -> {'通过' if ok else '异常'}")
    print("结论：小键的真实内存大头是 per-key 元数据不是 value;")
    print("      同生命周期小键聚合进 hash(listpack) 可省 60%+, 分界是 listpack 上限")
```

**追问一**：为什么 listpack 能把 per-field 开销压到几乎没有？它升级成 hashtable 的边界条件背后的账是什么？

→ 解析：listpack（7.0 前的 ziplist）是**连续内存的紧凑编码**：每个字段就是"头(类型+长度) + 内容 + 结束标记"，没有指针、没有 dict entry、没有 robj——定位靠"上一个字段头里记着总长度"的线性回退，本质是用 CPU 换内存。它的边界条件就是换算账：`hash-max-listpack-entries=128` / `hash-max-listpack-value=64` 两个默认值意味着"字段数 × 字段字节 ≤ 约 10KB 且访问是 O(N) 可接受"——128 个字段线性查找最坏也就几千次字节比较，远快于一次网络往返，但到 10 万字段时每次 HGET 都 O(N) 就是灾难，所以**超上限升级为 hashtable：O(1) 访问回归，同时每字段付回 dict entry + robj 的开销**。工程含义：分桶不是越密越好，桶内字段数贴近 listpack 上限是甜点区（本卡取 100）；value 超 64B 的字段会把整个桶踢出紧凑编码，长文本（如用户简介）不该混进高密度聚合桶。这也是为什么"读多写多"的桶要更保守：hashtable 升级在首次超限时发生，之后即使删字段也不会降回（rehash 双表还有峰值账），升级是不可逆的。

**追问二**：聚合迁移期间怎么保证旧键与新桶的一致性？读路径切换的灰度怎么做？

→ 解析：一致性方案与缓存序列化升级（Q6653）同构：① **写路径先行**：应用同时写旧键与新桶（双写期），写桶成功但写旧键失败要能容忍（旧键已进入只读淘汰轨道）；② **读路径灰度**：读优先走新桶，miss 回读旧键（兼容期兜底），观察命中率曲线稳定后摘除旧键回读；③ **存量迁移**：离线脚本 SCAN 旧键按桶聚合写新桶——注意迁移期与双写期的并发：脚本写桶用 HSETNX 或带版本值，避免覆盖双写的新数据；幂等重跑靠"键值指纹"比对（Q7155 指纹失效账同族）；④ **收尾清理**：旧键按前缀批量 UNLINK（异步释放避免主线程卡顿，Q6776），分批执行并配合 TTL 巡检（Q6785）确认无残留；⑤ **回滚预案**：保留旧键前缀的只读快照（或 RDB 版本），新桶出问题可立即切回读旧键——灰度不是单向门。最容易翻车的点：**双写期的 TTL 语义**——旧键各自的 TTL 不同，聚桶后整桶统一 TTL，等于改变了部分键的生命周期；聚合前必须按"生命周期相同"重分组，这条纪律在选型取舍里就是第一性的。
