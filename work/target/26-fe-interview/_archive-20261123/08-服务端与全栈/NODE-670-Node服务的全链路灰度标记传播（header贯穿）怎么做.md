---
title: [NODE-670] 全链路灰度标记传播（header 贯穿）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## NODE-670：灰度标记传播怎么做？
**答**：
- 标记链路：入口网关判定（SCN-OPS-216 网关权威）→ Node BFF 消费标记 → 下游调用透传（每跳转发 header）→ MQ 消息携带（消息头）→ 异步任务继承（ALS 上下文——SCN-NODE-645）。
- 强制重写：网关重写标记（不信客户端传值——SCN-OPS-216），BFF 转发时「透传网关给的」而非「透传客户端原始的」。
- 标记与路由：标记决定路由（下一跳路由到灰度实例——服务发现 meta 过滤，SCN-NODE-668 请求级金丝雀）。
- 遗漏审计：链路覆盖检查（哪些调用点没透传标记——入口标记进但出口没出 = 链断，自动化扫描出站调用点）。
- 追问钩子：为什么「MQ 消息也要携带灰度标记」——灰度版本发的消息被稳定版消费者处理（或反向）时，行为组合不可控（新格式消息被旧逻辑解析）；消息头携带标记让消费者按标记路由到对应版本消费者——异步链路的灰度一致性靠消息标记，这是全链路灰度最容易漏的环节。

```javascript
// BFF 透传（ALS 上下文）
als.run({ gray: req.headers['x-gray-bucket'] }, () => next());
axios.interceptors.request.use(cfg => {
  const ctx = als.getStore();
  if (ctx?.gray) cfg.headers['x-gray-bucket'] = ctx.gray;   // 每跳透传
  return cfg;
});
// MQ 携带
mq.publish(topic, payload, { headers: { 'x-gray-bucket': als.getStore().gray } });
```
