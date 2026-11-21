---
title: [NODE-631] Node 服务的契约测试服务端（Pact provider 端）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-631：契约测试服务端
**答**:
- Provider 端职责：验证实现满足所有消费者的契约（Pact broker 拉取契约 → 起服务 → 逐条交互验证——CI 中运行 NODE-334 消费者端配套）。
- 集成方式：验证流水线（消费者发布契约 → provider CI 拉 pending 契约验证 → 结果回写 broker——can-i-deploy 门禁：部署前检查所有消费者验证通过）、契约状态钩子（given 状态准备：测试数据注入——provider state setup）。
- 一致性与演进：破坏性变更拦截（契约失败 → MR 阻断——消费者未升级不许改）、兼容期管理（双版本并行期间两套契约都验——NODE-449）、未覆盖消费（新调用方接入 → 契约自动出现——依赖关系可见）。
- 与单测边界：契约测"接口行为符合预期"（schema/语义）——不测业务逻辑（那是单测）——分层清晰。
- 观测：契约验证通过率、契约失败归因（实现 bug vs 契约过时——分类处理）。
```javascript
// Pact provider 验证
new PactVerifier({ provider: 'order-svc', providerBaseUrl, pactUrls: broker.pacts,
  stateHandlers: { 'order exists': async () => seedOrder() } })  // 状态钩子
  .verifyProvider();
// CI 门禁: can-i-deploy --pacticipant order-svc --to-environment prod
```
