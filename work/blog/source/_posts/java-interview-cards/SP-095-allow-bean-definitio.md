---
title: "[SP-095] Bean·allow-bean-definition-overriding（覆盖）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Bean · allow-bean-definition-overriding（覆盖）

- **事实**：Boot 2.1 起默认禁止 Bean 覆盖（重名即启动失败）
- **原理**：覆盖引发的隐性 Bug 难排查，显式开启（spring.main.allow-bean-definition-overriding=true）才允许，团队规范建议重名直接报错
- **常见误区**：
  1. Boot 默认允许覆盖（错）
  2. 覆盖是配置便利性设计（错）
  3. 开关只对 @Bean 生效（错）
- **工程用法**：升级 Boot 2.1 常见启动报错
- **版本锚点**：Boot 2.1
