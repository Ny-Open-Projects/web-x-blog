---
title: "[JC-100] 误用·volatile 缺失（双重检查）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 误用 · volatile 缺失（双重检查）

- **事实**：无 volatile 的 DCL 在重排下可能发布半初始化对象
- **原理**：new 的引用赋值可能先于构造执行，第二个线程首次判空后直接使用未初始化字段，加 volatile 禁止该重排
- **常见误区**：
  1. DCL 加了 synchronized 就绝对安全（错）
  2. 半初始化问题只在老 JVM 存在（错）
  3. JIT 不会做这种重排（错）
- **工程用法**：review 单例代码必查 volatile
- **版本锚点**：JSR-133
