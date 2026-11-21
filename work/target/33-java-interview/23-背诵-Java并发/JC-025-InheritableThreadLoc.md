---
title: "[JC-025] ThreadLocal·InheritableThreadLocal（误用）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## ThreadLocal · InheritableThreadLocal（误用）

- **事实**：InheritableThreadLocal 只在子线程创建时拷贝一次在线程池场景失效
- **原理**：线程池线程是复用的不会重新创建，后续任务拿到的是首次创建时的快照，需用阿里开源的 TransmittableThreadLocal 配 TTL 包装线程池
- **常见误区**：
  1. InheritableThreadLocal 能跟随线程池任务传递（错）
  2. TTL 是 JDK 内置类（错）
  3. 子线程修改会同步回父线程（错）
- **工程用法**：跨线程池传递上下文用 TransmittableThreadLocal
- **版本锚点**：开源 TTL
