---
title: [NODE-702] 服务间通信选型（REST/gRPC/MQ）怎么定？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-702：通信选型怎么定？
**答**：
- REST：通用/调试友好/生态成熟——外部 API 与低频内部调用；JSON 序列化开销在高频内部调用中显著。
- gRPC：高性能（protobuf——体积/序列化快）、强契约（proto 契约——SCN-ENG-247 单源）、流式——内部高频调用；调试与浏览器支持成本（需 grpc-web）。
- MQ：异步解耦/削峰/事件驱动——不需要即时响应的业务事件（SCN-NODE-653 本地消息表）。
- 混合现实：外部 REST + 内部 gRPC/MQ 混用——统一 tracing/超时语义贯穿（SCN-NODE-670 标记传播在三种协议都要通）。
- 追问钩子：为什么「内部高频调用」的 JSON 序列化开销值得在意——QPS 1000 × 50KB JSON 的序列化消耗 CPU（V8 序列化是热点，SCN-BLD-261 剖析常见）；protobuf 体积减半+解析快 5×——CPU 是 Node 最稀缺资源（单线程），序列化省的 CPU 直接转为吞吐——内部通信的序列化成本是容量账的一部分。

```javascript
// gRPC 强契约 + 高性能
const client = new OrderClient('order-svc:50051');
const resp = await client.getOrder({ id }, { deadline });   // proto deadline 传播
// MQ：事件驱动
await kafka.send('order-events', event);              // 无需即时响应
```
