---
title: [NODE-296] OTel 自动埋点与自定义埋点的边界？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-296：OTel 自动埋点与自定义埋点的边界？
**答**:
- 自动埋点覆盖：http/express/fastify/next、DB client（pg/mysql/mongoose）、redis、kafka/amqp——框架级 I/O 全覆盖，零侵入。
- 需要自定义：业务关键流程（下单链路/风控判定）、非标准库调用（内部 RPC 框架）、本地耗时热点（大 JSON 处理）。
- 边界原则：自动埋点管"标准动作"，自定义管"业务语义"——在自动 span 下层加业务 span（层级语义清晰）。
- 成本控制：自定义 span 只打"值得归因"的段；开启 ignore 匹配（健康检查/静态资源不打 span）。

```javascript
// 自动埋点降噪
getNodeAutoInstrumentations({
  '@opentelemetry/instrumentation-http': { ignoreIncomingPaths: ['/health', '/metrics', '/favicon'] },
});
// 业务 span 装饰器
function traced(name, attrs) {
  return (target, prop, desc) => {
    const orig = desc.value;
    desc.value = async function (...args) {
      return tracer.startActiveSpan(name, async (span) => {
        span.setAttributes(attrs);
        try { return await orig.apply(this, args); }
        finally { span.end(); }
      });
    };
  };
}
class OrderService {
  @traced('order.risk-check', { domain: 'risk' })
  async riskCheck(order) { /* 风控判定：业务关键段 */ }
}
```
