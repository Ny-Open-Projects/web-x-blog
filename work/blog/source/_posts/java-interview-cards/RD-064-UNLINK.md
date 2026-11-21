---
title: "[RD-064] 运维·UNLINK（删除）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 运维 · UNLINK（删除）

- **事实**：大 key 删除用 UNLINK（4.0 lazy-free 异步回收）
- **原理**：UNLINK 从键空间摘除后由后台线程释放内存，DEL 同步释放大对象阻塞主线程，lazyfree-lazy-expire 让过期也异步
- **常见误区**：
  1. UNLINK 与 DEL 等价无区别（错）
  2. 异步删除可能丢数据（错）
  3. lazy-free 默认全开（错）
- **工程用法**：大 key 治理配套命令
- **版本锚点**：Redis 4.0
