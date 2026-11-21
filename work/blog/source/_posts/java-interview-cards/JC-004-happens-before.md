---
title: "[JC-004] JMM·happens-before（happens-before）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## JMM · happens-before（happens-before）

- **事实**：happens-before 是判断两个操作是否可见的核心规则而非时间先后
- **原理**：A happens-before B 意味着 A 的结果对 B 可见；程序顺序规则、锁的解锁加锁、volatile 写读、线程 start 与 join 都天然构成 happens-before
- **常见误区**：
  1. happens-before 就是代码执行的先后顺序（错）
  2. 没有 happens-before 关系就一定看不到（错）
  3. happens-before 只适用于 volatile（错）
- **工程用法**：并发正确性论证一律用 happens-before 推导
- **版本锚点**：JLS 17.4.5
