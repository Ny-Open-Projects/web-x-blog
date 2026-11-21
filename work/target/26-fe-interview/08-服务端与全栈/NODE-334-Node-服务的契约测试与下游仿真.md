---
title: [NODE-334] Node 服务的契约测试与下游仿真如何落地？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-334：Node 服务的契约测试与下游仿真
**答**:
- 问题：BFF 依赖多个下游服务，联调环境不稳定导致测试 flaky；下游悄悄改接口上线后 BFF 才崩。契约测试把"依赖的稳定性"变成 CI 可验证的资产。
- 消费者驱动契约：BFF 按自己实际使用的字段/行为生成契约文件（Pact），发布到 broker；下游 CI 拉取契约验证实现满足；破坏契约的 MR 被下游 CI 拦截，而不是等线上事故。
- 本地仿真：测试环境用 Pact 的 mock server（按契约生成响应）替代真实下游——集成测试稳定且不依赖联调环境。
- 契约演进：契约版本化；新增字段下游先兼容（消费方未用到不受影响）；移除字段需消费方全部升级后在下个大版本删除。
- 覆盖判定：每个下游交互至少一条契约用例（成功/错误/超时三类响应都定义）。
```javascript
// Pact 消费者测试
const { PactV3 } = require('@pact-foundation/pact');
const provider = new PactV3({ consumer: 'bff-trade', provider: 'svc-inventory' });
it('查询库存', async () => {
  await provider.addInteraction().given('sku a exists').uponReceiving('get stock')
    .withRequest({ method: 'GET', path: '/stock', query: { sku: 'a' } })
    .willRespondWith({ status: 200, body: { sku: 'a', stock: PactV3.Matchers.integer(8) } })
    .executeTest(mockServer => expect(bff.getStock(mockServer.url, 'a')).resolves.toMatchObject({ stock: 8 }));
});
```
