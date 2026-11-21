---
title: "[JC-065] 并发容器·CopyOnWriteArrayList（COW）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 并发容器 · CopyOnWriteArrayList（COW）

- **事实**：CopyOnWriteArrayList 写时复制整份数组读完全无锁
- **原理**：修改时复制新数组替换引用（volatile 数组），迭代器是快照不支持 remove，适合读极多写极少的小列表（监听器列表）
- **常见误区**：
  1. COW 写性能优于 ArrayList（错）
  2. COW 迭代器支持并发修改（错）
  3. COW 适合大列表高频写（错）
- **工程用法**：监听器注册场景标准选择
- **版本锚点**：JDK 源码
