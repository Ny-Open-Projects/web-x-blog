---
title: "[SP-011] 循环依赖·allow-circular-references（Boot 2.6）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 循环依赖 · allow-circular-references（Boot 2.6）

- **事实**：Spring Boot 2.6 起默认禁止循环依赖需显式 allow-circular-references=true 开启
- **原理**：官方认为循环依赖是设计坏味道，禁止它把问题暴露在启动期而不是运行期
- **常见误区**：
  1. Boot 2.6 后循环依赖完全不能用（错）
  2. 开启开关后构造器注入循环依赖也能用（错）
  3. 该开关影响 prototype 注入（错）
- **工程用法**：升级 Boot 2.6 前先解环再加开关
- **版本锚点**：Boot 2.6
