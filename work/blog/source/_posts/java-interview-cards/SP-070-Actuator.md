---
title: "[SP-070] Boot·Actuator（运维）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Boot · Actuator（运维）

- **事实**：Actuator 提供 /actuator/health、metrics、env 等运维端点
- **原理**：生产暴露 health+info+prometheus 其余关闭（management.endpoints.web.exposure.include），health 可聚合 DB/Redis/MQ 健康度供 K8s 探针
- **常见误区**：
  1. Actuator 默认暴露全部端点（错）
  2. health 端点默认关闭（错）
  3. Actuator 是监控面板替代品（错）
- **工程用法**：K8s liveness/readiness 探针数据源
- **版本锚点**：Boot 文档
