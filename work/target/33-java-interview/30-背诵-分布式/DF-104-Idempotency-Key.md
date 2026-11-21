---
title: "[DF-104] 可靠性·Idempotency-Key（接口）"
date: 2026-11-18
categories: [Java面试, 分布式]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 可靠性 · Idempotency-Key（接口）

- **事实**：HTTP 幂等标准实践：客户端生成 Idempotency-Key 头，服务端存储首响应供重放返回
- **原理**：Stripe 式设计：首次处理并缓存响应，同 key 重放返回缓存结果（不重复执行），key 过期回收，支付/订单类 API 的行业标准
- **常见误区**：
  1. 幂等 key 由服务端生成（错）
  2. 重放请求重新执行业务（错）
  3. key 永久保留（错）
- **工程用法**：对外 API 设计规范
- **版本锚点**：Stripe API 设计
