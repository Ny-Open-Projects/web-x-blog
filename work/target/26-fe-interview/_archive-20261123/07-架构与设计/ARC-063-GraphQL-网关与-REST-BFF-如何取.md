---
title: [ARC-063] GraphQL 网关与 REST BFF 如何取舍？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-063：GraphQL 网关与 REST BFF 如何取舍？
**答**：
- GraphQL 适合"页面多、字段需求差异大、客户端类型多"的场景：一次查询精确取字段，天然解决 over/under-fetch。
- REST BFF 适合接口形态稳定、团队 REST 经验深、缓存策略依赖 HTTP 语义（CDN/ETag）的场景。
- 复杂度主要在服务端：dataloader 防 N+1、权限按字段控制、查询深度限制，这些都要有人兜底。

```graphql
# GraphQL 网关：一个查询聚合多域数据，字段级取用
query ProductPage($id: ID!) {
  product(id: $id) {                      # product 域
    title
    price { amount currency }
    stock { state }                       # 只取需要的字段，天然裁剪
  }
  recommendations(productId: $id, limit: 4) {   # 推荐域：同一次请求
    items { id title coverUrl }
  }
}

# 服务端配套（缺了就是事故）：
# 1. DataLoader 按批合并防 N+1
# const batchUsers = new DataLoader(ids => rpc.user.getBatch(ids));
# 2. 查询深度/复杂度限制，防恶意深查询
# depthLimit(8), costAnalysis({ maximumCost: 1000 })
# 3. 字段级权限：未登录 user.phone 直接为 null 并告警
```
