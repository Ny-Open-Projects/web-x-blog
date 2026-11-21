---
title: "[SP-033] Boot·@SpringBootApplication（启动）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Boot · @SpringBootApplication（启动）

- **事实**：@SpringBootApplication 是 @Configuration+@EnableAutoConfiguration+@ComponentScan 组合
- **原理**：默认扫描主类所在包及子包，排包错位导致 Bean 扫不到是常见启动失败根因
- **常见误区**：
  1. 它会扫描整个 classpath（错）
  2. 组合注解不可拆开单独使用（错）
  3. 扫描范围默认是主类同包之外（错）
- **工程用法**：主类放包根（com.example.app 的顶层）
- **版本锚点**：Boot 文档
