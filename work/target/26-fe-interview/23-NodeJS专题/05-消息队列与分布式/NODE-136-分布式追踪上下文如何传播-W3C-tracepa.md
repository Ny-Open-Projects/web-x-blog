---
title: [NODE-136] 分布式追踪上下文如何传播（W3C traceparent）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-136：分布式追踪上下文如何传播（W3C traceparent）？
**答**：
- 标准 header：`traceparent = 00-<32 位 traceId>-<16 位 spanId>-<2 位 flags>`，flags 最低位为 1 表示采样。
- 入站 extract：解析合法则复用 traceId（全链路串联），非法/缺失则生成新 traceId；出站 inject：透传 traceId + 生成新 spanId。
- 跨协议都要透传：HTTP 头、gRPC metadata、MQ 消息头——断一环，这条链路在平台上就断了。
- 与日志打通：把 traceId 同步进 ALS（NODE-106/133），日志与追踪可以互跳。

```javascript
const { randomUUID } = require('crypto');
const HEX32 = /^[0-9a-f]{32}$/, HEX16 = /^[0-9a-f]{16}$/;

// 入站：解析或生成
function extractContext(headers) {
  const raw = headers['traceparent'];
  if (raw) {
    const [version, traceId, spanId, flags] = raw.split('-');
    if (version === '00' && HEX32.test(traceId) && HEX16.test(spanId)) {
      return { traceId, parentSpanId: spanId, sampled: (parseInt(flags, 16) & 1) === 1 };
    }
  }
  return { traceId: randomUUID().replaceAll('-', ''), parentSpanId: null, sampled: true };
}
const newSpanId = () => randomUUID().replaceAll('-', '').slice(0, 16);

// 出站：透传
function injectContext(headers, ctx) {
  headers['traceparent'] = `00-${ctx.traceId}-${newSpanId()}-01`;
}
// 兼容老系统：同时透传 x-trace-id；Zipkin 系的 B3 格式同理做字段映射
```
