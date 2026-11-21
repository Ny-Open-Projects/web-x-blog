---
title: "[JV-044] OOM·Java heap space（分类）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## OOM · Java heap space（分类）

- **事实**：常见 OOM：Java heap space、GC overhead limit、Metaspace、unable to create native thread、Direct buffer memory
- **原理**：不同区域 OOM 根因与解法不同：堆 OOM 查泄漏或堆小、元空间查动态类生成、native thread 查线程数与系统限制
- **常见误区**：
  1. OOM 都是堆空间不足（错）
  2. Metaspace OOM 不可能发生（错）
  3. 所有 OOM 解法都是加大内存（错）
- **工程用法**：OOM 分诊是排查第一步
- **版本锚点**：实战共识
