---
title: [NODE-254] Fastify 为什么快：schema 与序列化？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-254：Fastify 为什么快：schema 与序列化？
**答**:
- JSON Schema 编译：请求校验（ajv 编译为函数）与响应序列化（fast-json-stringify 编译为代码）都在启动期完成——运行时零反射，接近手写代码性能。
- 路由压缩：fastify 用 radix tree 路由——长前缀共享，查找 O(路径长)；对比 express 线性遍历正则表。
- 少抽象：不代理 req/res（直接用原生对象），无 ctx 层转发。
- 面试表达："schema 即契约"——校验、文档（swagger 生成）、类型（json-schema-to-ts）一份 schema 三份产出。

```javascript
// fastify schema 示例
const schema = {
  body: {
    type: 'object',
    required: ['sku', 'count'],
    properties: {
      sku: { type: 'string', pattern: '^SKU-\\d+$' },
      count: { type: 'integer', minimum: 1, maximum: 99 },
    },
  },
  response: {
    200: {
      type: 'object',
      properties: { orderId: { type: 'string' }, price: { type: 'number' } },
      // 额外字段被 fast-json-stringify 静态丢弃（白名单序列化）
    },
  },
};
fastify.post('/order', { schema, config: { perm: 'order:create' } }, async (req) => {
  return { orderId: create(req.body), price: calc(req.body), internalSecret: 'x' };  // internalSecret 不会输出
});
```
