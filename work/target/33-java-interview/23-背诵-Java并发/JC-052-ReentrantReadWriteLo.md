---
title: "[JC-052] 显式锁·ReentrantReadWriteLock（读写锁）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 显式锁 · ReentrantReadWriteLock（读写锁）

- **事实**：ReentrantReadWriteLock 允许读共享写独占且支持写锁降级为读锁
- **原理**：持有写锁时可再获取读锁后释放写（降级安全），升级（持读再取写）会死锁，适合读多写少的缓存场景
- **常见误区**：
  1. 读写锁支持锁升级（错）
  2. 读锁也是互斥的（错）
  3. 降级是指先释放写锁再拿读锁（错）
- **工程用法**：缓存刷新：写锁改数据降级读锁再校验
- **版本锚点**：JDK 文档
