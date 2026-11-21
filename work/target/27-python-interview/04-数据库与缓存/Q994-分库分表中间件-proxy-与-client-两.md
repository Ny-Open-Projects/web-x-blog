---
title: [Q994] 分库分表中间件: proxy 与 client 两种模式
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q994 · 分库分表中间件: proxy 与 client 两种模式

> 难度:★★★★ | 标签:分库分表, 中间件

**问**:ShardingSphere 的 JDBC 与 Proxy 两种模式怎么选?中间件要解决哪些问题?

**答**:client 模式(JDBC/Sharding-JDBC):应用内嵌 jar 直连分片库,少一跳性能好、运维简单,但每种语言都要接入、升级跟随发版;proxy 模式(Sharding-Proxy/MyCat):独立进程伪装成 MySQL,多语言零改造接入,多一跳网络与运维成本。中间件解决的四大问题:路由(SQL 改写定位到分片)、聚合(跨片 group by/order by/limit 的归并)、分布式主键(接号段/雪花)、分布式事务(弱 XA/BA AT/SAGA 集成)。限制要心里有数:跨片 join 支持有限(常用广播表/绑定表缓解)、不带分片键的查询广播全片、DDL 在线变更需要配套工具。规模小先分库不分表或单库分区,别为了架构而架构。

```python
# file: code/04_数据库与缓存/q994_sharding_proxy.py
"""最小分片中间件: SQL 路由 -> 改写 -> 结果归并"""
import sqlite3

class MiniShardingProxy:
    def __init__(self, shards=4):
        self.shards = shards
        self.conns = [sqlite3.connect(":memory:") for _ in range(shards)]
        for c in self.conns:
            c.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INT, amt REAL)")

    def route(self, user_id):
        return hash(user_id) % self.shards

    def insert(self, user_id, amt):
        idx = self.route(user_id)
        self.conns[idx].execute(
            "INSERT INTO orders (user_id, amt) VALUES (?, ?)", (user_id, amt))
        self.conns[idx].commit()
        return idx

    def query_by_user(self, user_id):              # 带分片键: 单片路由
        idx = self.route(user_id)
        return self.conns[idx].execute(
            "SELECT * FROM orders WHERE user_id = ?", (user_id,)).fetchall()

    def query_all(self):                            # 无分片键: 广播归并
        rows = []
        for c in self.conns:
            rows.extend(c.execute("SELECT * FROM orders").fetchall())
        return sorted(rows)                          # 归并排序

if __name__ == "__main__":
    proxy = MiniShardingProxy()
    for uid, amt in [(1, 10), (5, 20), (9, 30), (1, 40)]:
        print(f"user {uid} 路由到分片 {proxy.insert(uid, amt)}")
    print("带分片键查询:", proxy.query_by_user(1))
    print("广播归并:", proxy.query_all())
```

**追问**:
- 广播查询为什么危险?——N 个分片各执行一次再归并,延迟与压力乘 N,深分页归并更要内存拉平;业务上强制带分片键或走异构索引(ES)。
- 绑定表是什么?——订单表与订单明细表按同一分片键分片,join 时同分片对同分片本地完成,避免跨片 join。

---
