---
title: "[JC-105] 虚拟线程·Semaphore（限流）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 虚拟线程 · Semaphore（限流）

- **事实**：虚拟线程并发限流标准做法是 Semaphore
- **原理**：虚拟线程可无限创建，下游（数据库连接池）承受不了无限并发，acquire 许可形成背压，连接池本身就是天然限流器
- **常见误区**：
  1. 限制虚拟线程数量即可限流（错）
  2. Semaphore 与虚拟线程不兼容（错）
  3. 限流只能靠网关（错）
- **工程用法**：虚拟线程 + Semaphore 是官方推荐组合
- **版本锚点**：JDK 文档
