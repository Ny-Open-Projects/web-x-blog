---
title: [NODE-093] Node 服务的测试策略（单测、集成、契约测试）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-093：Node 服务的测试策略（单测、集成、契约测试）？
**答**：
- 金字塔：**单元测试**（service 函数，mock 依赖，快而多）→ **集成测试**（supertest 起 app 打真实路由，DB 用内存/容器，验证中间件链与序列化）→ **契约测试**（Pact/OpenAPI 校验 BFF 与下游接口约定，防下游悄悄改字段）→ 少量 E2E。
- Node 特有注意：异步竞态用 fake timers；时间相关逻辑注入 clock；环境变量隔离（每个测试文件独立 process.env）；测试必须不依赖执行顺序。
- 门禁：覆盖率阈值（增量代码 80%）、PR 跑全量、发布前跑集成+契约。

```javascript
// 单元测试：mock 依赖，验证业务逻辑
const { describe, it, expect, jest } = require('@jest/globals');
const { transfer } = require('../services/transfer');

describe('transfer 转账服务', () => {
  it('余额不足时抛出业务异常且不写库', async () => {
    const dbMock = { execute: jest.fn().mockResolvedValue([{ affectedRows: 0 }]) };
    await expect(transfer(dbMock, 1, 2, 9999))
      .rejects.toMatchObject({ code: 'INSUFFICIENT_BALANCE' });
    expect(dbMock.execute).toHaveBeenCalledTimes(1);   // 未走到第二条 UPDATE
  });
});

// 集成测试：supertest 打真实 app（中间件链全走）
const request = require('supertest');
const app = require('../app');   // app 导出不 listen，由 supertest 控制

describe('POST /api/orders', () => {
  it('未登录返回 401', async () => {
    const res = await request(app).post('/api/orders').send({ sku: 'A1' });
    expect(res.status).toBe(401);
    expect(res.body.code).toBe('AUTH_REQUIRED');
  });

  it('正常下单返回 200 与幂等键回放', async () => {
    const idemKey = crypto.randomUUID();
    const res1 = await request(app).post('/api/orders')
      .set('authorization', `Bearer ${testToken}`)
      .set('idempotency-key', idemKey)
      .send({ sku: 'A1', count: 1 });
    expect(res1.status).toBe(200);

    const res2 = await request(app).post('/api/orders')   // 同 key 重放
      .set('authorization', `Bearer ${testToken}`)
      .set('idempotency-key', idemKey)
      .send({ sku: 'A1', count: 1 });
    expect(res2.body).toEqual(res1.body);                 // 快照一致
    expect(res2.headers['idempotent-replayed']).toBe('true');
  });
});
```
