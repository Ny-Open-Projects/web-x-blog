---
title: "[SP-028] Boot·@ConfigurationProperties（配置绑定）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Boot · @ConfigurationProperties（配置绑定）

- **事实**：@ConfigurationProperties 批量绑定前缀下的属性并支持校验与元数据
- **原理**：relaxed binding 支持 kebab-case 与驼峰互转，配合 @Validated 做 JSR-303 校验，IDE 有元数据提示，优于散落的 @Value
- **常见误区**：
  1. @ConfigurationProperties 只能绑定 String（错）
  2. 它需要手动调用 bind 方法（错）
  3. relaxed binding 会模糊匹配任意拼写（错）
- **工程用法**：配置项超过 3 个就建绑定类
- **版本锚点**：Boot 文档
