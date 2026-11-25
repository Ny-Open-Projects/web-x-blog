---
title: [NODE-270] BFF 面试综述：鉴权与聚合的完整链路？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-270：BFF 面试综述：鉴权与聚合的完整链路？
**答**:
- 综述框架：入口收口（NODE-267 鉴权）→ 编排（268 聚合模式）→ 收敛（269 缓存合批）→ 协议（261-266 GraphQL/tRPC）→ 降级（NODE-052 配合）。
- 完整请求链路一图：前端 cookie → BFF 鉴权（session→user/permCtx）→ 聚合编排（预算+criticality）→ 下游收敛（单飞+合批+TTL）→ 裁剪响应 → trace 透传（NODE-36x）。
- 高频追问："下游挂了怎么办"→ criticality 分级+降级占位；"token 泄漏怎么办"→ token 不出 BFF（HttpOnly）；"怎么防 N+1"→ DataLoader+合批。
- 收束金句："BFF 是前端观点的服务端——它的价值在聚合裁剪与安全收口，不在业务逻辑重算。"

```javascript
// 链路一页纸
// 1) auth middleware: cookie → session → user + permCtx（单飞刷新）
// 2) aggregate: slots(criticality) + budget(AbortSignal.any) + partial-success
// 3) downloader: TTL 缓存 → 单飞 → 合批（DataLoader）
// 4) protocol: GraphQL(APQ+复杂度限制) / tRPC(zod+类型) / REST
// 5) trace: x-trace-id 透传下游 + ALS 自动跟随（NODE-256）
// 6) degrade: 非核心 slot → DEGRADED 占位 + 上报
```
