---
title: "[RD-101] 生态·Module（模块）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 生态 · Module（模块）

- **事实**：Redis Module 生态：RedisJSON/RediSearch/RedisBloom/RedisTimeSeries，Redis 8.0 起官方版内置集成
- **原理**：模块以扩展命令补足原生能力（JSON 文档/全文检索/布隆/时序），Redis 8 把官方模块并入开源版免单独部署，选型前先确认版本能力边界
- **常见误区**：
  1. 模块需要商业授权（官方模块开源版 8.0 已内置）（错）
  2. Redis 7 也能用内置模块（需单独装）（错）
  3. 模块影响持久化兼容性（错）
- **工程用法**：Redis 能力边界评估
- **版本锚点**：Redis 8.0
