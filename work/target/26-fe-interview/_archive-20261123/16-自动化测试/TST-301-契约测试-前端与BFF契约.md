---
title: [TST-301] 前端与 BFF 层的契约测试如何轻量化落地？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-301：前端与 BFF 层的契约测试如何轻量化落地？
**答**：
- MSW handler + OpenAPI schema 双重校验：mock 响应必须符合 schema（mock 即契约）。
- 类型生成（schema → TS）让前端类型与后端定义同源，编译期契约。
- 契约破坏快速发现：CI 中 schema diff 输出 breaking 清单给前端预知。
- 前端不验证 BFF 业务逻辑，只验证「我消费的结构是否还被满足」。

```javascript
// MSW handler 绑定 schema
server.use(http.get('/api/goods/:id', async ({ params }) => {
  const data = await fixture.goods(params.id);
  return HttpResponse.json(GoodsResponseSchema.parse(data)); // 违约即测试红
}));
r
```
