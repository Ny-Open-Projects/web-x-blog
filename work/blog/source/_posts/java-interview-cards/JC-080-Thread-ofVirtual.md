---
title: "[JC-080] 虚拟线程·Thread.ofVirtual（API）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 虚拟线程 · Thread.ofVirtual（API）

- **事实**：创建虚拟线程的 API 是 Thread.ofVirtual().start() 或 Executors.newVirtualThreadPerTaskExecutor()
- **原理**：与平台线程同一 Thread 抽象，可加名字便于排查，Spring Boot 3.2 开 spring.threads.virtual.enabled 一键切换
- **常见误区**：
  1. 虚拟线程是新的线程类型接口与 Thread 无关（错）
  2. 必须用专门框架才能创建（错）
  3. 开启后所有线程自动变虚拟（错）
- **工程用法**：Tomcat 请求线程与 @Async 池切换虚拟线程
- **版本锚点**：Spring Boot 3.2
