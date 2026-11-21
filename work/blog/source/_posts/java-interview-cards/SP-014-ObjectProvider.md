---
title: "[SP-014] IoC·ObjectProvider（API）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## IoC · ObjectProvider（API）

- **事实**：ObjectProvider 提供延迟与可选的依赖获取
- **原理**：getIfAvailable、getIfUnique、getObject，解决"依赖可能不存在"与"每次要新实例"两类问题
- **常见误区**：
  1. ObjectProvider 在启动时立刻解析依赖（错）
  2. 它是 @Autowired 的废弃替代（错）
  3. getIfAvailable 找不到会抛异常（错）
- **工程用法**：框架开发与可选依赖场景
- **版本锚点**：Spring 文档
