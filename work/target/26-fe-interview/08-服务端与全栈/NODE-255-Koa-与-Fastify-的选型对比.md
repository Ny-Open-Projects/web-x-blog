---
title: [NODE-255] Koa 与 Fastify 的选型对比？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-255：Koa 与 Fastify 的选型对比？
**答**:
- Koa：洋葱中间件优雅、生态（Koa 生态偏轻）适合 BFF/自研框架底座（很多公司框架基于 Koa 深度封装）；性能中等；错误处理与类型支持要自己搭。
- Fastify：性能强（schema 编译/radix tree）、契约化（schema 即文档）、hooks 切面精细——适合接口密集的独立服务。
- 团队因素：存量中间件资产（Koa 中间件生态）与团队熟悉度是硬约束；新项目无历史包袱选 Fastify 收益直接。
- 折中路线：自研框架底座（Koa + 公司中间件库）兼容存量，新领域服务用 Fastify（NODE-232 组合思想）。

```javascript
// 选型矩阵
const matrix = [
  { factor: '性能（schema 校验+序列化）', weight: 3, koa: 3, fastify: 5 },
  { factor: '中间件生态/存量兼容', weight: 3, koa: 5, fastify: 3 },
  { factor: '契约与文档自动化', weight: 2, koa: 2, fastify: 5 },
  { factor: '类型安全（TS 集成）', weight: 2, koa: 2, fastify: 4 },
  { factor: '自研框架底座灵活性', weight: 2, koa: 5, fastify: 3 },
];
// koa=34 fastify=41 → 结论：BFF/底座 Koa，领域服务 Fastify
```
