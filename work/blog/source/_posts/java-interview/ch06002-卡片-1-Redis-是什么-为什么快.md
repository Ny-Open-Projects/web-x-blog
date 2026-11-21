---
title: "卡片 1：Redis 是什么，为什么快？"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 概念卡, 33]
type: 概念卡
disableNunjucks: true
---

### 卡片 1：Redis 是什么，为什么快？
单线程内存 KV 数据库（6.0 起网络 IO 多线程，**命令执行仍单线程**）。快的原因四条：
1. 纯内存操作；
2. **IO 多路复用**（epoll，单线程处理万级连接）；
3. 单线程无锁竞争、无上下文切换；
4. 高效数据结构（SDS、跳表、压缩列表等专用优化）。
