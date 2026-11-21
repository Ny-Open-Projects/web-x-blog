---
title: "[SP-069] Boot·RestClient（web）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Boot · RestClient（web）

- **事实**：Spring Boot 3.2 引入 RestClient 同步 API 风格化 HTTP 客户端
- **原理**：RestTemplate 处于维护模式，RestClient 流式 API（get().uri().retrieve().body()），WebClient 仍是响应式场景首选
- **常见误区**：
  1. RestTemplate 是 Boot 3 首选（错）
  2. RestClient 是异步的（错）
  3. RestClient 替代了 WebClient（错）
- **工程用法**：新项目 HTTP 客户端选型
- **版本锚点**：Boot 3.2
