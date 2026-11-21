---
title: "[SP-038] AOP·proxy-target-class（默认）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## AOP · proxy-target-class（默认）

- **事实**：Spring Boot 2.0 起 AOP 默认强制 CGLIB（proxy-target-class=true）
- **原理**：统一代理避免"有接口用 JDK 无接口用 CGLIB"的类型不一致问题，注入时按具体类型而非接口
- **常见误区**：
  1. Boot 默认 JDK 代理（错）
  2. proxy-target-class 默认 false（错）
  3. 切换 JDK 代理是性能优化（错）
- **工程用法**：Boot 2 迁移说明
- **版本锚点**：Boot 2.0
