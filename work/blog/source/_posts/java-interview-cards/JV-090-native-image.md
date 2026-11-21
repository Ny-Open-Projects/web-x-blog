---
title: "[JV-090] GraalVM·native image（Native）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## GraalVM · native image（Native）

- **事实**：GraalVM native image AOT 编译为本地可执行文件启动毫秒级内存极低
- **原理**：封闭世界假设：反射、动态代理需配置可达性元数据，兼容成本是与 JVM 方案的核心差异，云原生 Serverless 场景价值大
- **常见误区**：
  1. native image 完全兼容所有 Java 特性（错）
  2. native image 运行时还有 JIT（错）
  3. native image 启动与 JVM 一样慢（错）
- **工程用法**：GraalVM 是 AOT 不是更快的 JVM
- **版本锚点**：GraalVM 文档
