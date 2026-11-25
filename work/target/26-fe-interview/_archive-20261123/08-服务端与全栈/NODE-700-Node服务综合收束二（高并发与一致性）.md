---
title: [NODE-700] Node 服务综合收束二：高并发与一致性方法论？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-700：高并发收束
**答**：
- 高并发主线：漏斗削峰（前端限流→排队→预扣→异步落库）/池隔离/请求合并/热点打散（NODE-656/643/691/689）。
- 一致性主线：幂等全景（唯一约束/in-flight）+ 本地消息表 + 对账兜底 + 读己之写（NODE-655/653/682/654）。
- 稳定性主线：熔断+降级框架/超时传播/限流维度化/降级标记可见（NODE-669/642/641/690）。
- 面试答法：高并发三问——「扛不扛得住」（容量模型+漏斗削峰）、「对不对」（幂等+对账）、「挂了怎么办」（熔断降级+预案）——三问全绿才算高并发设计完成。

```javascript
const nodeHcMethodology = {
  throughput: ['funnel-shaping', 'pool-isolation', 'coalescing', 'hotkey-sharding'],
  consistency: ['idempotency-full', 'outbox-pattern', 'reconciliation', 'read-your-write'],
  stability: ['breaker+fallback', 'deadline-propagation', 'rate-limit-dims', 'degraded-marker'],
};
```
