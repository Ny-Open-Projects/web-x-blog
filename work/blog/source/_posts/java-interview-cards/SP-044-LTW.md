---
title: "[SP-044] AOP·LTW（织入）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## AOP · LTW（织入）

- **事实**：AspectJ 支持编译期与类加载期织入（LTW）能力强于 Spring AOP
- **原理**：可增强 private/final/构造器/字段，需要 -javaagent 加载织入器，全链路监控 agent 就是 LTW 实现
- **常见误区**：
  1. Spring AOP 支持 LTW（错）
  2. LTW 无法拦截构造器（错）
  3. AspectJ 是运行时代理（错）
- **工程用法**：需要跨方法深度增强时用 AspectJ
- **版本锚点**：AspectJ 文档
