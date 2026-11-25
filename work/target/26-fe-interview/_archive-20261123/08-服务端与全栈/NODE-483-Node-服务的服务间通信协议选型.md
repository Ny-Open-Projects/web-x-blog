---
title: [NODE-483] Node 服务间通信协议选型（REST/gRPC/MQ）的决策框架是什么？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-483：服务间通信协议选型
**答**:
- 决策三问：调用模式（同步问答 vs 异步通知）、性能要求（内网低频 vs 高频热点）、契约强度（内部快速迭代 vs 跨团队稳定契约）。
- 选型框架：同步强契约/高频 → gRPC（proto 契约 + 多路复用 + 流式）、同步弱契约/内部迭代快 → REST/JSON（Node 生态友好，BFF↔内部默认）、异步解耦 → MQ（NODE-344）、订阅推送 → gRPC stream/SSE。
- Node 侧现实：gRPC 在 Node 的性能与开发体验（proto 代码生成/流式支持好但调试难于 REST）——BFF 层对外必须 REST/JSON（前端友好），内部可选 gRPC。
- 混合纪律：同一调用链避免协议反复转换（HTTP→gRPC→HTTP 的网状转换增加序列化成本与排障复杂度——按域统一协议方向）；跨语言是 gRPC 的最大理由（NODE-449）。
- 演进：REST 到 gRPC 迁移按域灰度（双写对拍验证 NODE-438）；协议选型记录进 ADR（ARC-184）。
```javascript
// 选型决策表
const commDecision = {
  'BFF→前端': 'REST/JSON + SSE/WS',                              // 前端友好强制
  'BFF→内部同步高频': 'gRPC（proto 契约）',                       // 性能与契约
  'BFF→内部迭代快': 'REST/JSON（OpenAPI 弱契约）',
  '跨服务事件': 'MQ（Kafka/RocketMQ）',
  '规则': '同域协议统一，避免转换链'
};
```
