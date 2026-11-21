---
title: "[JC-089] 线程基础·yield（yield）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 线程基础 · yield（yield）

- **事实**：yield 只是提示调度器让出当前 CPU 无任何保证
- **原理**：可能立即被再次调度，也不保证让给谁，测试中用于模拟竞争但生产代码不依赖其语义
- **常见误区**：
  1. yield 会释放持有的锁（错）
  2. yield 保证低优先级线程执行（错）
  3. yield 与 sleep 效果相同（错）
- **工程用法**：了解即可不用于业务逻辑
- **版本锚点**：JDK 文档
