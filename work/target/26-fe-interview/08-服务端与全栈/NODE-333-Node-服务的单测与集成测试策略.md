---
title: [NODE-333] Node 服务的单测与集成测试策略如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-333：Node 服务的单测与集成测试策略如何设计？
**答**:
- 分层：纯逻辑单测（服务函数/工具，mock 依赖注入）、HTTP 集成测试（supertest 起真实 app 实例，mock 下游 HTTP）、契约测试（下游 API stub 按 schema）、E2E 冒烟（部署后健康链路）。BFF 的重心在集成层——业务逻辑薄，风险在编排与边界。
- 依赖注入是可测性前提：DB/MQ/下游客户端通过构造参数传入而非模块内单例，测试替换为内存实现或 msw-node 拦截。
- 数据层测试：用真实 DB 的容器化实例（testcontainers）跑迁移 + 用例，比 mock DB 可信度高一个量级；每用例事务回滚或数据快照复位。
- 时间与随机：注入 clock（避免 sleep 断言）、随机种子固定，防 flaky。
- 覆盖率策略：核心链路（支付/鉴权）行覆盖 90%+，工具代码 80%，模板/配置不追求覆盖率数字。
```javascript
// 依赖注入 + 集成测试
function createApp({ db, downstream }) { /* app 依赖外注入 */ }
test('POST /order 扣减库存', async () => {
  const db = await startPgContainer(); await db.migrate();
  const app = createApp({ db, downstream: stubDownstream() });
  const res = await request(app).post('/order').send({ sku: 'a', qty: 2 });
  expect(res.status).toBe(201);
  expect(await db.query('select stock from sku where id=$1', ['a'])).toEqual({ stock: 8 });
});
```
