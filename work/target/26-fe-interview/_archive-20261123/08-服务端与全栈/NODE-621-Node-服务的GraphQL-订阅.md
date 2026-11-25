---
title: [NODE-621] Node 服务的 GraphQL 订阅（实时推送）如何实现与扩展？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-621：GraphQL 订阅实现与扩展
**答**:
- 实现：PubSub 抽象（订阅解析器发布事件——单机 EventEmitter → 多实例 Redis PubSub/External pubsub（可扩展），NODE-346 水平扩展同构）、订阅协议（WebSocket graphql-ws——连接生命周期与鉴权 NODE-481 对齐）。
- 过滤与权限：订阅参数过滤（server-side filter——订阅时声明过滤条件，事件按条件推送减少带宽）、订阅权限（topic 级权限——订阅授权与数据权限，退权即断订阅 NODE-481）、消息大小治理（事件负载裁剪——只推订阅字段）。
- 可靠性：客户端重连补拉（订阅 gap——重连后拉增量（配合 lastEventId），订阅不保证不丢——协议声明：订阅+查询兜底）、心跳保活（ping/pong——半开连接清理）。
- 性能：订阅扇出（大房间广播——按 topic 分区/聚合推送 NODE-346）、事件负载裁剪（投影字段）、订阅数上限（每连接——防滥用 NODE-393）。
- 取舍：GraphQL 订阅 vs SSE/WS 直推——已有 GraphQL 生态才用（否则简单协议更轻）。
```javascript
// 订阅解析器（Redis PubSub 扩展）
resolvers.Subscription = {
  orderUpdated: { subscribe: withFilter(
    (p, a, ctx) => pubsub.asyncIterator([`order:${ctx.user.id}`]),   // 用户维度 topic
    (payload, vars) => filterByStatus(payload, vars.statuses)),      // 服务端过滤
    resolve: (p) => project(p, { fields: 'sub' }) }
};
// 多实例：pubsub = new RedisPubSub(redis) —— 广播到各实例本地连接
```
