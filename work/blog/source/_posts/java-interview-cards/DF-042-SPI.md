---
title: "[DF-042] RPC·SPI（Dubbo）"
date: 2026-11-18
categories: [Java面试, 分布式]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## RPC · SPI（Dubbo）

- **事实**：Dubbo SPI 增强：按 key 加载（@SPI/@Adaptive）、IOC 与 AOP 注入扩展、自适应扩展类
- **原理**：Java 原生 SPI 全量加载低效，Dubbo 按 name 惰性加载+运行时自适应（URL 参数选实现），微内核架构的教科书实现
- **常见误区**：
  1. Dubbo SPI 与 Java SPI 相同（错）
  2. 自适应扩展是编译期固定（错）
  3. SPI 不能注入依赖（错）
- **工程用法**：框架设计能力题
- **版本锚点**：Dubbo 源码
