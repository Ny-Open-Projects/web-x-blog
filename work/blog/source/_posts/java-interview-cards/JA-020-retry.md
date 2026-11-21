---
title: "[JA-020] Spring AI·retry（可靠性）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · retry（可靠性）

- **事实**：Spring AI 内置重试：spring.ai.retry 前缀配置最大尝试与退避策略
- **原理**：模型服务限流与瞬时故障常见，框架层指数退避兜底，重试耗尽异常上抛由业务降级处理
- **常见误区**：
  1. Spring AI 不做任何重试（错）
  2. 重试无限次直到成功（错）
  3. 重试不需要幂等（对话调用天然幂等可重试）（错）
- **工程用法**：生产可靠性配置
- **版本锚点**：Spring AI 1.0 GA
