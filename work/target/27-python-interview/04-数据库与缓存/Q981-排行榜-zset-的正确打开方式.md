---
title: [Q981] 排行榜: zset 的正确打开方式
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q981 · 排行榜: zset 的正确打开方式

> 难度:★★★☆ | 标签:zset, 排行榜

**问**:实时排行榜用 zset 怎么实现?并列名次与分页翻页怎么处理?

**答**:ZADD 更新分数、ZINCRBY 累加、ZREVRANGE/ZREVRANK 取名次、ZRANGE 按名次分页,全是 O(logN)。两个工程细节:一、并列——同分时业务通常要求"先达成者靠前",把 score 拼成 `主分 * 1e10 + (MAX_TS - 达成时间戳)`,或 score 存主分、member 用 (主分, ts, id) 编码,保证确定序;二、深排名翻页用 `ZRANGEBYSCORE (max, min) LIMIT offset count` 以分数为游标,避免按 index 大偏移;三、亿级用户全量榜不可行,只维护 TopN(如前 1 万),其余用户排名走"分数区间统计 ZCOUNT + 我的分数"推导名次段。更新频率极高时考虑本地聚合 + 批量刷 zset。

```python
# file: code/04_数据库与缓存/q981_leaderboard.py
"""zset 排行榜: 更新 名次 并列时按达成时间排序"""
import bisect

class MiniZSet:
    def __init__(self):
        self.items = []                     # [(score, member)] 降序

    def add(self, member, score):
        self.items = [x for x in self.items if x[1] != member]
        bisect.insort(self.items, (-score, member))   # 负分实现降序
        self.items = self.items[:100]                 # 只维护 TopN

    def top(self, n=5):
        return [(m, -s) for s, m in self.items[:n]]

    def rank(self, member):
        for i, (s, m) in enumerate(self.items):
            if m == member:
                return i + 1
        return None

if __name__ == "__main__":
    lb = MiniZSet()
    for name, sc in [("alice", 95), ("bob", 88), ("carol", 95), ("dave", 70)]:
        lb.add(name, sc)
    print("Top4:", lb.top(4), "<- 同分 95: alice 与 carol 相邻")
    print("dave 名次:", lb.rank("dave"))
    print("未上榜用户用 ZCOUNT 统计分数区间推导名次段")
```

**追问**:
- score 的 double 精度有什么坑?——拼接大数(分*1e10+ts)后超过 2^53 会丢精度,要控制拼接位数或改用两层级联(zset 主分 + member 内时间戳)。
- 榜单数据要持久化吗?——zset 是内存态,重启不丢(RDB/AOF 持久化),但历史榜单(日榜/周榜)按时段切 key + 定期落库归档。

---
