---
title: [NODE-482] Node 服务的多协议网关（HTTP/WS/gRPC 共存）如何统一治理？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-482：多协议网关统一治理
**答**:
- 现实：一个业务域内 HTTP（页面 API）+ WS（实时）+ gRPC（内部）共存——横切面（鉴权/限流/trace/日志）在各协议重复实现是治理灾难。方案：协议适配层——统一"请求/响应/事件"抽象，横切面在抽象层实现一次。
- 抽象设计：统一上下文（身份/trace/租户/灰度标签——各协议入口适配成同一结构，ALS 存 NODE-421）、统一鉴权决策（token 校验结果三协议共享）、统一限流维度（用户级限流跨协议共享计数——防"WS 饶过 HTTP 限流"）。
- 各协议适配：HTTP（网关中间件）、WS（握手鉴权 + 消息框架对齐统一上下文 NODE-481）、gRPC（interceptor 注入/提取 trace 与身份）。
- 观测统一：三协议指标统一模型（按协议打标签）、trace 跨协议续链（gRPC metadata / WS 消息头携带 traceparent NODE-319）。
- 配置统一：路由表/限流规则/鉴权策略一份配置多协议生效（防协议间策略漂移）。
```javascript
// 统一上下文适配
function unifiedCtx(proto, req) {
  return als.run({
    proto, uid: authOf(proto, req), trace: extractTrace(proto, req),
    tenant: tenantOf(proto, req), gray: grayOf(proto, req)
  }, () => dispatch(proto, req));                                // 三协议入口归一
}
// 限流共享：rateLimit.check(uid) 不分协议计数
```
