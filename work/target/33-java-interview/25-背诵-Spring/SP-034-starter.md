---
title: "[SP-034] 自定义 starter·starter（步骤）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 自定义 starter · starter（步骤）

- **事实**：自定义 starter：写自动配置类+条件注解+配置绑定+注册到 AutoConfiguration.imports
- **原理**：命名规范官方 x-spring-boot-starter 自家 spring-boot-starter-x，提供 spring-configuration-metadata.json 让 IDE 补全
- **常见误区**：
  1. starter 里要写业务逻辑（错）
  2. 自定义 starter 必须用 @ComponentScan（错）
  3. starter 命名随意（错）
- **工程用法**：公共组件 SDK 化标准方案
- **版本锚点**：Boot 文档
