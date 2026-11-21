---
title: "[RD-015] 线程模型·epoll（IO）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 线程模型 · epoll（IO）

- **事实**：Redis 用 IO 多路复用（Linux epoll）单线程处理海量连接
- **原理**：事件驱动框架 ae，连接就绪才处理，避免每连接一线程，是单线程高并发的根基
- **常见误区**：
  1. Redis 用 BIO 每连接一线程（错）
  2. epoll 是 Redis 特有（是 OS 能力）（错）
  3. select/poll 与 epoll 无区别（错）
- **工程用法**：网络模型原理题
- **版本锚点**：通用
