---
title: [NODE-376] Node 服务的 API 网关层职责如何划分？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-376：Node 服务的 API 网关层职责
**答**:
- 网关做"横切面"：路由与版本、认证终结（外部 token → 内部身份，NODE-369）、限流熔断（粗粒度）、灰度染色（NODE-370）、审计与访问日志、CORS/安全头、请求体限制。
- 网关不做：业务逻辑、数据聚合（那是 BFF 职责，NODE-147 分工：网关=流量入口横切面，BFF=面向页面的编排层）。
- 认证终结模式：网关校验外部 JWT → 注入可信内部头 + trace；下游服务只信任网关注入（外部流量不可达内部端口，网络策略兜底）。
- 性能与可用性：网关是单点风险——无状态设计 + 多活部署 + 自身也要限流保护；网关故障的爆炸半径最大，变更最谨慎（冻结期）。
- 技术选型：APISIX/Kong（插件生态）、Envoy（mesh 场景）、Node 自研网关（需要深度定制逻辑时，注意性能与维护成本）。
```javascript
// 网关中间件链（Node 自研示意）
app.use(requestId)         // 生成 reqId/traceId
   .use(accessLog)         // 访问日志
   .use(authTerminate)     // JWT 校验 → 注入内部身份
   .use(rateLimit)         // 粗粒度限流
   .use(grayTag)           // 灰度染色
   .use(bodyLimit('1mb'))  // 请求体限制
   .use(proxy(routes));    // 路由转发
```
