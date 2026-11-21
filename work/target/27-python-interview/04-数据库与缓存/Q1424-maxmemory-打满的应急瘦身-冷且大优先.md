---
title: [Q1424] maxmemory 打满的应急瘦身: 冷且大优先
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1424 · maxmemory 打满的应急瘦身: 冷且大优先

> 难度:★★★☆ | 标签:Redis, 应急

**问**:告警说 Redis 内存 95%,写入开始报 OOM command not allowed,你手上的应急清单是什么?

**答**:先止血再根治。止血清单按"先冷后热、先大后小"排序:临时与导出类 key(tmp:、export:)直接删,它们天然可再生;过期不淘汰的长尾报表/历史缓存按最后访问时间排序清理;大 value 的可拆分对象(超大 hash/zset)拆小或压缩;会话、购物车这类有状态 key 最后动。根治三件套:确认淘汰策略与业务语义匹配(allkeys-lru 还是 volatile-lru,别用 noeviction 还指望自动腾内存);补容量水位告警提前量(75% 预警而非 95% 才叫);排查膨胀根因——大 key 增长、无 TTL 的 key 堆积(Q1008 的 TTL 纪律)、还是某个上游 bug 在狂写。全程留操作日志,删过的 key 要能对账。

```python
# file: code/04_数据库与缓存/q1424_shrink.py
"""maxmemory 打满的应急瘦身: 冷 且 大 优先"""
# key -> (bytes, seconds_since_last_hit)
usage = {
    "session:u1": (2048, 10),
    "feed:cache:big": (512000, 3600 * 26),
    "report:2023q4": (2000000, 3600 * 24 * 90),
    "hot:goods:1": (10000, 2),
    "cart:u9": (4096, 600),
    "tmp:export:17": (800000, 1800),
}
quota = 1000000

def shrink(usage, quota):
    freed, dropped = 0, []
    for k, (size, age) in sorted(usage.items(), key=lambda x: (-x[1][1], -x[1][0])):
        if freed >= quota:
            break
        freed += size
        dropped.append(k)
    return dropped, freed

dropped, freed = shrink(usage, quota)
for k in dropped:
    usage.pop(k)
print(f"需腾出 {quota} 字节, 实际释放 {freed} 字节, 删除顺序: {dropped}")
print("守则: 临时与导出类优先, 会话购物车谨慎, 全程留日志可对账")
```

**追问**:
- noeviction 下内存打满为什么是写入报错而读正常?——noeviction 拒绝一切会新增内存的命令(写与淘汰均不做),读已有 key 不占新内存所以不受影响,这是它"保护数据、牺牲可用性"的语义。
- allkeys-lru 与 volatile-lru 怎么选?——TTL 纪律严格的缓存选 volatile-lru,保住无 TTL 的关键 key;key 生命周期混乱时 allkeys-lru 更兜底,但等于承认治理缺位。
- 淘汰发生在哪个执行点?——每条命令执行前检查内存水位,超限就在命令路径上同步淘汰腾空间;大 key 淘汰本身耗时,逼近上限时延迟也会抖。
- 生产陷阱?——应急删除不做对账,业务以为数据还在;删 key 前导出清单留日志,事后复盘根因并把 95% 告警提前到 75%。

---
