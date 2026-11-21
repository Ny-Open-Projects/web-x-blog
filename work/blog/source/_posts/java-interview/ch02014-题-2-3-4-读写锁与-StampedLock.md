---
title: "题 2.3.4：读写锁与 StampedLock？"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 面试题, 进阶题, 33]
type: 面试题
disableNunjucks: true
---

### 题 2.3.4：读写锁与 StampedLock？

**【参考回答（可背）】**
- ReentrantReadWriteLock：state 高 16 位读、低 16 位写；读共享写独占；支持锁降级（写→读）不支持升级（死锁风险）；适合读多写少且读持有时间较长。
- 缺点：读线程多时写线程可能饥饿。
- StampedLock（JDK8）：**乐观读**——tryOptimisticRead 拿个 stamp（不加锁），读完 validate 校验期间有没有写；失败再升级悲观读锁。读性能显著高于 RWL；但不可重入、不支持 Condition，用错难排查。

**【P10 加分项】**
举真实用例：配置中心客户端本地缓存（读极多写极少）用 StampedLock 乐观读，压测 QPS 提升 30%+；同时讲"什么时候不用"——读持有时间长时乐观读反复 validate 失败反而更差。

---
