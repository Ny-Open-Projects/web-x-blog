---
title: [NODE-359] Node 服务的 API 版本管理策略如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-359：API 版本管理策略
**答**:
- 版本策略：URL 路径版本（/v2/goods，路由清晰、缓存友好，主流）优先；header 版本（Accept: application/vnd.api+json; version=2）语义优雅但排障难。不版本化的是内部 BFF（前后端同节奏发布，ARC-162 契约演进代替大版本）。
- 兼容规则：同一大版本内只加不改删——字段新增（消费方忽略未知字段）、错误码只增；破坏性变更升大版本。
- 多版本共存成本：v1/v2 并行期间的代码组织（handler 分层复用 service 层，版本差异收敛在 DTO 转换层）；旧版本 sunset 流程（弃用公告 → 响应头 Deprecation 标注 → 流量监控 → 使用方清零 → 下线）。
- 前端配合：客户端请求带版本头/路径 + 服务端版本能力协商（响应 x-api-version）；灰度期双版本数据兼容（ARC-449）。
- 文档：OpenAPI 按版本生成，版本间 diff 自动出变更说明。
```javascript
// 版本路由组织：service 复用，DTO 差异化
routerV2.get('/goods/:id', async (ctx) => {
  const goods = await svc.getGoods(ctx.params.id);              // 共享 service
  ctx.body = toV2DTO(goods);                                    // 版本差异只在 DTO 层
});
// sunset: res.set('Deprecation', 'true'); res.set('Sunset', 'Sat, 01 Jan 2027');
```
