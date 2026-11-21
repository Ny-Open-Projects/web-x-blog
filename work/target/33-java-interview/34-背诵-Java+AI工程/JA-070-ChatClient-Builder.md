---
title: "[JA-070] Spring AI·ChatClient.Builder（装配）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · ChatClient.Builder（装配）

- **事实**：Spring Boot 自动装配 ChatClient.Builder bean，注入后 .build() 得到 ChatClient
- **原理**：builder 由自动配置预置默认模型与选项，业务注入 builder 即可定制装配，免手写 create(model)
- **常见误区**：
  1. ChatClient.Builder 不存在（错）
  2. 必须手动 create（错）
  3. builder 与 ChatClient 是一回事（错）
- **工程用法**：Spring 环境标准装配
- **版本锚点**：Spring AI 1.0 GA
