---
title: "[JV-006] 对象分配·TLAB（TLAB）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 对象分配 · TLAB（TLAB）

- **事实**：TLAB 是 Eden 内按线程划分的私有分配缓冲区
- **原理**：分配只需移动指针（碰撞指针）无需同步，是快速分配路径，分配失败才退回 Eden 公共区 CAS
- **常见误区**：
  1. TLAB 让对象分配在栈上进行（错）
  2. TLAB 需要加锁分配（错）
  3. TLAB 在老年代内（错）
- **工程用法**：-XX:+UseTLAB 默认开启
- **版本锚点**：HotSpot 实现
