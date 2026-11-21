---
title: [NODE-399] Node 服务的 API 文档与开发者体验（DX）如何建设？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-399：API 文档与开发者体验（DX）
**答**:
- 文档即代码：OpenAPI 从代码/schema 生成（zod → openapi 或装饰器注解），CI 校验文档与实现一致性（文档过期是最常见失败）；示例从测试用例生成（真实可跑）。
- 文档必备：请求/响应 schema + 字段说明、错误码清单（每个接口可能返回的错误）、分页/限流约定、认证方式、可运行示例（curl + 多语言 SDK）。
- DX 设施：沙箱环境（测试账号 + mock 数据）、调试台（浏览器内直接发请求）、变更订阅（OpenAPI diff 推送到 webhook，NODE-397）。
- SDK：官方 SDK 从 OpenAPI 生成（多语言），类型完整；SDK 与 API 版本节奏同步。
- 质量闭环：接入方工单分析（文档缺什么被反复问 → 补文档）、文档满意度调研、首次接入成功耗时度量（开放 API 的核心 DX 指标）。
```javascript
// zod → OpenAPI + CI 一致性校验
const GoodsQuery = z.object({ kw: z.string().optional(), page: z.number().int().min(1).default(1) });
appRegistry.register('GET /goods', { query: GoodsQuery, res: GoodsList, desc: '商品搜索' });
// CI: openapi generate → diff 校验实现与文档一致，不一致阻断合并
```
