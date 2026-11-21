---
title: [NODE-293] span 的设计与归因？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-293：span 的设计与归因？
**答**:
- span 粒度：一请求一棵 span 树——HTTP 入口 span、每个下游调用 span、DB 查询 span、MQ 发送 span。粒度原则：覆盖网络 I/O 与可疑热点，本地纯函数不打（span 开销非零）。
- span 属性：路由（低基数）、错误码、重试次数——用于聚合分析；禁止高基数属性（userId/orderId 进 tag 会爆索引）。
- 归因：慢请求看 span 树最慢分支——"P95 慢"的瓶颈通常在树的最深叉（下游 X 占 800ms）。
- span 事件：异常记录为 span event（不是属性），重试记录为 event（保留次数信息）。

```javascript
// 手动 span（OTel）
import { trace, SpanStatusCode } from '@opentelemetry/api';
const tracer = trace.getTracer('bff');
export async function aggregate(req) {
  return tracer.startActiveSpan('aggregate', async (span) => {
    span.setAttribute('route', '/aggregate');          // 低基数
    try {
      const orders = await tracer.startActiveSpan('fetch.orders', async (s) => {
        try { return await fetchOrders(req); }
        catch (e) { s.recordException(e); s.setStatus({ code: SpanStatusCode.ERROR }); throw e; }
        finally { s.end(); }
      });
      span.setAttribute('count', orders.length);
      return orders;
    } finally { span.end(); }
  });
}
```
