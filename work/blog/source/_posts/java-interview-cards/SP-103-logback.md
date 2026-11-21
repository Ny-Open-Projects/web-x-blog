---
title: "[SP-103] Boot·logback（日志）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Boot · logback（日志）

- **事实**：Boot 默认 logback 按 spring.profile 加载 logback-spring.xml
- **原理**：生产配置滚动策略（按天+大小）、异步 Appender（AsyncAppender 防日志 IO 拖慢业务）、traceId 进 pattern
- **常见误区**：
  1. Boot 默认 log4j（错）
  2. 异步日志会丢日志（错）
  3. 日志不需要滚动配置（错）
- **工程用法**：日志规范落地
- **版本锚点**：Boot 文档
