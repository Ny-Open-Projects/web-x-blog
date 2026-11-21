---
title: "[SP-032] 自动配置·AutoConfiguration.imports（机制）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 自动配置 · AutoConfiguration.imports（机制）

- **事实**：Boot 2.7+ 自动配置清单从 META-INF/spring.factories 迁移到 spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports
- **原理**：Boot 3.0 彻底移除旧机制，自定义 starter 必须用新文件，老 starter 升级 Boot 3 前必须迁移
- **常见误区**：
  1. spring.factories 至今仍是自动配置入口（错）
  2. 自动配置在用户 Bean 之后加载（错）
  3. AutoConfiguration.imports 是注解扫描结果（错）
- **工程用法**：Boot 3 迁移必查项
- **版本锚点**：Boot 2.7/3.0
