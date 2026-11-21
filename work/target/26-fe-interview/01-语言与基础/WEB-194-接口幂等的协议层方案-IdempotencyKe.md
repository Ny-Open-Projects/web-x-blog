---
title: [WEB-194] 接口幂等的协议层方案（Idempotency-Key）怎么设计？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-194：接口幂等的协议层方案（Idempotency-Key）怎么设计？
**答**：
- 场景：支付/下单类 POST 请求，网络重试或用户重复点击导致重复提交。
- 协议方案：客户端为每个业务操作生成唯一 Idempotency-Key 请求头；服务端首次执行后把 key 与响应绑定缓存（带 TTL），重试直接返回首次结果。
- 状态机细节：处理中收到同 key 请求返回 409 或 202（让客户端稍后再试）；同 key 但 payload 不同返回 422。
- 客户端责任：同一逻辑操作的重试必须复用同一个 key，进入新表单才换新 key。

```http
# 第一次提交：生成唯一 key
POST /api/payments HTTP/1.1
Content-Type: application/json
Idempotency-Key: 8f14e45f-ea0a-4b3f-9f2d-1a2b3c4d5e6f

{"orderId": "A1001", "amount": 9900}

# 网络超时后客户端重试：必须复用同一个 key
POST /api/payments HTTP/1.1
Content-Type: application/json
Idempotency-Key: 8f14e45f-ea0a-4b3f-9f2d-1a2b3c4d5e6f

{"orderId": "A1001", "amount": 9900}

# 服务端命中 key 缓存：返回首次结果，不重复扣款
HTTP/1.1 200 OK
Idempotency-Replayed: true
```
