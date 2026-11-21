---
title: [NODE-365] Node 服务的 GraphQL 服务器实践要点有哪些？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-365：Node 服务的 GraphQL 服务器实践
**答**:
- N+1 是第一课：resolver 逐个执行导致下游调用放大——DataLoader 批处理合并（同一 tick 的 key 合并请求 + 缓存去重），配合 dataloader 实例请求级创建（防跨请求缓存泄漏）。
- 安全：深度限制（query depth 防嵌套攻击）、复杂度限制（字段成本计分）、禁 introspection（生产）、分页强制（cursor 连接模式，禁无限列表）、字段级权限（resolver 内判权）。
- 性能：persisted queries（APQ：客户端发哈希，省带宽 + 白名单效果）、查询计划缓存、复杂聚合下沉服务端（GraphQL 不做业务计算）。
- 错误与监控：errors 数组语义（部分成功，data 可空）、错误脱敏（不漏内部堆栈）、按 resolver 维度的耗时追踪（APM 集成）。
- 与 REST 取舍（ARC-063）：聚合与多端差异强 → GraphQL；简单 CRUD → REST/tRPC。
```javascript
// DataLoader 批处理
function createLoaders(svc) {
  return { goods: new DataLoader(async (ids) => {
    const rows = await svc.batchGetGoods(ids);                   // 一次批量查询
    return ids.map(id => rows.find(r => r.id === id));           // 按请求顺序返回
  }, { maxBatchSize: 100 }) };
}
// context 每请求新建 loaders；schema 深度限制 depthLimit(8)
```
