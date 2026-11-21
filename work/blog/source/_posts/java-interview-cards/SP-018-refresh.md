---
title: "[SP-018] 容器·refresh（启动）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 容器 · refresh（启动）

- **事实**：容器启动核心是 AbstractApplicationContext.refresh 的 12 步模板
- **原理**：步骤包括 BeanFactory 准备、BPP 注册与执行、国际化、事件广播器、onRefresh（内嵌容器启动）、finishBeanFactoryInitialization（预实例化）
- **常见误区**：
  1. refresh 每次都会重新创建所有 Bean（错）
  2. 内嵌 Tomcat 在实例化 Bean 之后启动（错）
  3. refresh 只在 XML 容器存在（错）
- **工程用法**：Spring Boot 启动慢分析从 refresh 分步计时入手
- **版本锚点**：Spring 源码
