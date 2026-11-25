---
title: [NODE-677] 接口契约测试（provider 侧）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## NODE-677：契约测试怎么做？
**答**：
- 契约流：消费者发布期望（pact 文件——消费者驱动契约）→ provider CI 验证（can-i-deploy——provider 变更是否破坏消费方，SCN-OPS-229 门禁语义）→ broker 协调（契约中心——版本与验证状态）。
- provider 验证的实现：pact mock 数据驱动 provider——每个交互（请求/响应）做真实请求验证（状态机 setup——验证前置状态）。
- 契约版本化：契约随 API 版本演进（breaking 需同步消费方——SCN-OPS-245 通知 ack 联动）；兼容期双契约（新旧并存——SCN-OPS-265 扩展期）。
- 与 schema 校验分工：schema 校验（字段结构——单次请求）vs 契约测试（行为语义——请求组合与状态机）；两者互补。
- 追问钩子：为什么「消费者驱动契约」优于「provider 自测」——provider 自测验证的是「我给的符合我的理解」；消费者驱动验证「我给的符合消费者要的」——语义偏差（字段含义/状态假设）只有消费者能定义；can-i-deploy 让「发布前知道会破坏谁」，把契约破坏从生产事故前移到 CI。

```javascript
// provider 验证（pact）
const verifier = new Verifier({ provider: 'order-svc',
  pactUrls: [brokerUrl], stateHandlers: {
    '存在订单': async () => await seedOrder(testOrder),   // 状态机 setup
  } });
await verifier.verifyProvider();
// CI 门禁：can-i-deploy
pactBroker.canIDeploy({ provider: 'order-svc', version, toTag: 'prod' });
```
