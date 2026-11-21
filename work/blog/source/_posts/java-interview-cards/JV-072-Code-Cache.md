---
title: "[JV-072] Code Cache·Code Cache（JIT 缓存）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Code Cache · Code Cache（JIT 缓存）

- **事实**：JIT 编译产物存于 Code Cache，默认上限与保留区随版本变化
- **原理**：大量动态代码（脚本引擎、JSP）可撑满 Code Cache 导致不再编译性能下降，-XX:ReservedCodeCacheSize 可调，分层编译下非方法区可被清理
- **常见误区**：
  1. Code Cache 在堆内（错）
  2. Code Cache 满会 OOM 堆内存（错）
  3. Code Cache 自动无限扩容（错）
- **工程用法**：长跑服务性能逐步下降排查项
- **版本锚点**：HotSpot
