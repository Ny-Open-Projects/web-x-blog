---
title: [NODE-701] BFF 与 API Gateway 的分工怎么定？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-701：BFF 与网关怎么分工？
**答**：
- 网关职责：横切基础设施（鉴权粗验/限流/路由/灰度标记/监控注入——与业务无关的全局策略）。
- BFF 职责：面向端的聚合与裁剪（多下游编排/字段裁剪/协议适配——业务感知的组合逻辑）。
- 边界准则：「与端无关的全局策略」进网关，「面向特定端的业务组合」进 BFF——鉴权粗验（token 有效性）在网关，权限细化（资源级授权）在服务。
- 分工的反模式：业务逻辑漏进网关（网关写业务规则——网关成为单点业务债）、BFF 重复实现限流（网关已有限流——重复且口径不一）。
- 追问钩子：为什么「权限细化」不该放网关——资源级授权（这个订单是这个用户的吗）需要业务数据访问，网关只有身份上下文——网关做粗粒度（认证/token 有效性），细粒度授权下沉到拥有数据的服务——「谁拥有数据谁做授权」是权限边界的分配原则。

```javascript
// 网关：全局横切
gateway.use(authenticate(), rateLimit(), grayMark(), tracing());
// BFF：端业务组合
bff.get('/home', async (req) => aggregateForHome(req.user));   // 聚合/裁剪
// 资源授权在服务（数据拥有者）
orderSvc.requireOwnership(req.user.id, orderId);
```
