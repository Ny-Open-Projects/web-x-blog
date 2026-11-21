---
title: [Q1019] Redis 升级与数据迁移: 平滑换实例
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1019 · Redis 升级与数据迁移: 平滑换实例

> 难度:★★★★ | 标签:迁移, 运维

**问**:Redis 从单机迁到集群(或换大内存实例),怎么做到业务无感?

**答**:迁移四法按停机时间从多到少:一、停机窗口——业务低峰停写,DUMP/RDB 恢复到新实例,改配置切流,分钟级停机,最简单;二、MIGRATE/复制——新实例做旧实例的从库(SLAVEOF 旧主),同步追平后哨兵式切换;三、双写+对账——应用同时写新旧,读旧,对账一致后读新、停旧写(适合结构变化大的迁移,如单机 -> Cluster 分片规则变了);四、proxy 过渡——引入代理层按槽灰度搬迁,业务只对 proxy。升级版本(如 6 -> 7)注意:新版本命令行为变化、AOF/RDB 兼容性(向后兼容可读)、先在预发全量回归。共同纪律:先做回滚方案、迁移期间监控命中率与错误率、切流可一键回退。

```python
# file: code/04_数据库与缓存/q1019_migration.py
"""双写迁移 Redis: 写新读旧 -> 对账 -> 切读 -> 收尾"""
class Cluster:
    def __init__(self):
        self.old, self.new = {}, {}
        self.write_both, self.read_new = False, False

    def write(self, k, v):
        self.old[k] = v
        if self.write_both:
            self.new[k] = v

    def read(self, k):
        return self.new.get(k) if self.read_new else self.old.get(k)

    def reconcile(self):
        missing = {k for k in self.old if self.new.get(k) != self.old[k]}
        for k in missing:                        # 修复后新库才可切读
            self.new[k] = self.old[k]
        return missing

if __name__ == "__main__":
    c = Cluster()
    for i in range(5):
        c.write(f"k{i}", i)
    c.write_both = True
    c.write("k5", 5)
    print("未迁移前差异:", c.reconcile())
    print("对账通过, 切读新库:", (c.__setattr__("read_new", True), c.read("k3"))[1])
    print("收尾: 停旧写 -> 旧实例只读观察 -> 下线")
```

**追问**:
- 单机迁 Cluster 为什么不能直接复制?——分片规则变了,按槽重分布必须逐 key 搬(MIGRATE)或双写重建,纯 RDB 只能灌进一个节点。
- 迁移期间缓存 miss 激增正常吗?——正常,新实例冷缓存会回源 DB,务必预热(Q998)或灰度放量,避免迁移变成 DB 事故。

---
