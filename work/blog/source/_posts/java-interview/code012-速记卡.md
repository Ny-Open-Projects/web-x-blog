---
title: "速记卡"
date: 2026-11-18
categories: [Java面试, 手写代码]
tags: [Java面试, 手写题, 33]
type: 手写题
disableNunjucks: true
---

## 速记卡

1. DCL 三件套：两次检查 + volatile + 私有构造；更优：Holder / 枚举。
2. LRU：LinkedHashMap accessOrder=true；手写版 = HashMap + 双向链表 + 哨兵。
3. 生产消费者：while 判条件、notifyAll、环形数组下标。
4. 交替打印：一个锁 + 条件翻转 或 信号量链。
5. 简易线程池：take 阻塞复用、异常隔离、队列满拒绝、interrupt 关闭。
6. TopK：小顶堆 O(n log k)；静态数据快排 partition 平均 O(n)。
7. 死锁排查：jstack / thread -b；修复靠固定顺序与 tryLock。
8. 布隆：无漏判有误判、不可删；DB 兜底一次。
9. 限流器：单机滑动窗口/LeapArray；分布式 Redis Lua 三连。
10. 白板五字诀：思、界、降、审、并。

---
*返回 [INDEX.md](../../INDEX.md) 选择下一册。*
