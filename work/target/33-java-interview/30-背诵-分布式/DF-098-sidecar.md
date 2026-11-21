---
title: "[DF-098] 云原生·sidecar（Mesh）"
date: 2026-11-18
categories: [Java面试, 分布式]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 云原生 · sidecar（Mesh）

- **事实**：Service Mesh（Istio）：把治理（路由/限流/熔断）下沉 sidecar，业务无侵入
- **原理**：sidecar 代理每跳流量（延迟+资源开销），收益：治理与语言解耦（多语言团队）、统一管控面，权衡：复杂度大增（排障跨进程），按团队规模决策
- **常见误区**：
  1. Mesh 无性能代价（错）
  2. Mesh 替代所有框架治理（错）
  3. sidecar 是业务的一部分（错）
- **工程用法**：治理下沉架构
- **版本锚点**：实战共识
