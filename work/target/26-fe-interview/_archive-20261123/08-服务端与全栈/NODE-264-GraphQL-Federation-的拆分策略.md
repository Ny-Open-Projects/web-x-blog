---
title: [NODE-264] GraphQL Federation 的拆分策略？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-264：GraphQL Federation 的拆分策略？
**答**:
- subgraph 按领域拆（user/order/inventory），网关（router）合并成统一 schema——每个 subgraph 独立部署独立演进（ARC-206 依赖图谱思想）。
- 实体跨域引用：@key 声明实体，网关按 key 拼装（Order.user 引用 User@id）——跨域字段查询由网关分发。
- 治理：schema 注册表（谁改了什么类型）、断网域查询预算（depth/complexity）、subgraph 健康度熔断。
- 反模式：一个 subgraph 拆太碎（跨域查询扇出爆炸）或按团队而非领域拆（schema 边界混乱）。

```graphql
# subgraph: orders
type Order @key(fields: "id") {
  id: ID!
  userId: ID!
}
extend type User @key(fields: "id") {          # 跨域实体扩展
  id: ID! @external
  orders: [Order!]!                            # 网关按 User.id 路由到 orders subgraph
}
# subgraph: users
type User @key(fields: "id") { id: ID! name: String! }
# 网关查询：query { user(id:"1") { name orders { id } } } → 两次内部分发，一次返回
```
