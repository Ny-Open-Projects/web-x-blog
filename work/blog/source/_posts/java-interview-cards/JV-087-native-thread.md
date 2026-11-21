---
title: "[JV-087] OOM·native thread（类型）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## OOM · native thread（类型）

- **事实**：unable to create native thread 根因：线程数撞系统限制或内存不足创建栈失败
- **原理**：排查：线程总数（jcmd Thread.print 统计）、ulimit -u、可用内存；解法：虚拟线程改造或线程池治理
- **常见误区**：
  1. 该 OOM 是堆内存不足（错）
  2. 加大 -Xmx 可以解决（错）
  3. 线程数无上限（错）
- **工程用法**：高并发服务必知故障
- **版本锚点**：实战共识
