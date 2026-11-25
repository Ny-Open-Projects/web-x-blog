---
title: [ARC-128] 契约测试（前后端契约 / Pact 思想）如何落地？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-128：契约测试（前后端契约 / Pact 思想）如何落地？
**答**：
- 契约测试思想：消费者（前端）声明"我调用什么接口、期望什么结构"，提供者（后端）在自己的 CI 里验证契约——双方不联调也能发现破坏性变更。
- 落地形态：轻量方案用 OpenAPI schema 作为契约，前端 CI 用 schema 做类型生成 + mock，后端 CI 用 dredd/schemathesis 对 schema 验证实现；重量方案用 Pact（消费者驱动，broker 管理契约与验证结果）。
- 解决的真实问题：接口字段悄悄改名/类型变更在 provider 部署时就被拦截，而不是前端联调时才发现；mock 数据永远与契约一致（handler 即契约）。
- 边界：契约测试保证"结构正确"，不保证业务语义正确——业务正确性仍靠集成测试。

```typescript
// Pact 思想的前端消费者测试（用 @pact-foundation/pact）
import { PactV3, MatchersV3 } from '@pact-foundation/pact-v3';
const { like, integer } = MatchersV3;

const provider = new PactV3({ consumer: 'mall-web', provider: 'order-service' });

describe('订单服务契约', () => {
  it('GET /orders/:id 返回消费者期望的结构', async () => {
    await provider
      .given('订单 ord_1 存在')                                  // provider state
      .uponReceiving('查询订单详情')
      .withRequest({ method: 'GET', path: '/orders/ord_1' })
      .willRespondWith({
        status: 200,
        body: like({
          id: 'ord_1',
          amount: integer(9900),           // 类型匹配器：字段改名/类型变化即契约失败
          status: like('PAID'),
        }),
      })
      .executeTest(async (mockServer) => {
        const order = await fetchOrder(mockServer.url);
        expect(order.status).toBe('PAID');
      });
  });
});
// 流程：前端 CI 生成契约 JSON → 推到 Pact Broker → 后端 CI 拉取契约验证实现
// can-i-deploy：发布前查询 broker 判断该版本是否与所有已上线消费者兼容
```

**追问**：

1. provider state 需要后端准备数据，共享测试环境经常抖，怎么落地？ → provider 侧用独立测试库加事务回滚，state 由代码预置而不是依赖环境里恰好有的数据。
2. 只做消费者驱动契约，会不会漏掉后端新增字段但前端没适配的问题？ → 契约只保证消费者用到的部分不被破坏；新增字段的兼容性另靠 schema 的向后兼容检查（如 buf breaking）覆盖。
3. can-i-deploy 卡住了紧急发版怎么办？ → 允许带记录的 override，但必须事后补验证并把这个消费者的契约修复提到最高优先级，不能把 override 变成常态。
