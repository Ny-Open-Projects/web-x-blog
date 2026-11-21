---
title: [ARC-366] 前端基建：本地 Mock 与接口仿真体系如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-366：前端基建：本地 Mock 与接口仿真体系如何设计？
**答**:
- Mock 体系三层：开发期本地 mock（MSW 拦截，代码即契约）、联调期代理网关（指向测试环境）、仿真期契约仿真（按 OpenAPI schema 自动生成数据）。
- MSW 的架构优势：Service Worker 层拦截不侵入业务代码；同一套 handlers 可复用于单测（node 环境），实现"开发/测试共用仿真数据"。
- 契约驱动：schema 为唯一事实源，mock 数据从 schema 生成（faker + 约束），后端改契约前端 mock 自动感知，防"mock 与真实接口脱节"。
- 场景仿真：异常态（超时/500/慢响应）、边界态（空列表/超长文案）、灰度态（同一接口不同返回）用场景开关切换。
- 演进：与契约测试（Pact）打通，mock 校验失败即契约破坏预警。
```javascript
// MSW handlers：契约驱动 + 场景开关
import { setupWorker } from 'msw';
import { http, HttpResponse } from 'msw';
const worker = setupWorker(
  http.get('/api/goods', ({ request }) => {
    const scene = new URL(request.url).searchParams.get('__scene');
    if (scene === 'error') return HttpResponse.error();
    if (scene === 'slow') return delayed(3000, goodsList);
    return HttpResponse.json(fromSchema(GoodsListSchema)); // schema 生成
  })
);
worker.start({ onUnhandledRequest: 'warn' });
```
