---
title: [NODE-450] 服务网格（Istio/mesh）时代 Node BFF 的定位与边界如何调整？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-450：mesh 时代 Node BFF 的定位
**答**:
- 职责重划：mesh 接管基础设施横切面（mTLS/重试/熔断/限流/trace 注入——sidecar 统一实现），BFF 专注业务编排——避免双重治理（BFF 里写重试 + mesh 又配重试 = 重试风暴）。
- BFF 保留的职责：页面级聚合（业务编排）、协议适配（前端友好格式）、体验逻辑（降级数据选择/个性化）——业务层的智能不能下沉 mesh。
- 与 mesh 的协作约定：超时/重试预算在 mesh 层配置（声明式），BFF 的 deadline 传播（NODE-377）通过请求头与 mesh 对齐（mesh 按头里的剩余预算收紧自己的重试）。
- 可观测分工：mesh 提供网络层指标（TCP/gRPC 流量），BFF 提供业务语义指标（按页面/业务动作）——两层看板互补。
- 渐进接入：mesh 迁移期双重配置共存（先关 BFF 应用层重试，逐项搬到 mesh VirtualService），每项迁移演练验证（NODE-408）。
```yaml
# mesh 接管重试（BFF 应用层不再写）
apiVersion: networking.istio.io/v1
kind: VirtualService
spec: http:
  - route: [{ destination: { host: order-svc } }]
    timeout: 800ms
    retries: { attempts: 2, perTryTimeout: 300ms, retryOn: "5xx,reset" }
# BFF 约定：应用层只做业务编排，传输韧性交给 mesh；deadline 头 x-deadline-ms 由 BFF 注入
```
