---
title: [ENG-247] API 类型契约（schema→类型→mock→测试）怎么打通？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-247：API 契约打通怎么做？
**答**：
- 单源链路：OpenAPI/GraphQL schema → 类型生成（SCN-ENG-231）→ mock server 按 schema 生成数据 → MSW handler 复用同 schema → 契约测试校验 mock 与真实响应一致——四处共享一份契约。
- 变更感知：schema diff 在 PR 里展示（新增字段/删字段/breaking 标记），消费方类型错误 CI 即现。
- mock 一致性：mock 数据由 schema 驱动生成（faker + schema 约束），联调期 mock 与真实服务行为同构。
- 版本演进：API 版本化策略（路径/头）与前端适配层（旧字段兼容层限寿）。
- 追问钩子：为什么「mock 与真实响应同构」是联调质量的关键——mock 随手编的数据在真实环境字段缺失/类型不符时才暴露，联调变事故；schema 驱动的 mock 让前端开发即验证契约。

```typescript
// schema 驱动全链
type User = components['schemas']['User'];          // 生成类型
const mockUser = fakerFromSchema('User');            // schema 驱动 mock
http.get('/user', () => HttpResponse.json(mockUser)); // MSW handler
// 契约测试：真实响应 schema 校验
expect(realResponse).toMatchSchema('User');
```
