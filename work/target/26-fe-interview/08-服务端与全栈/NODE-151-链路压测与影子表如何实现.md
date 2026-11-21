---
title: [NODE-151] 链路压测与影子表如何实现？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-151：链路压测与影子表如何实现？
**答**：
- 核心机制：压测流量全程带标记（`x-load-test: 1`），数据面按标记**改写落点**——SQL 走影子表、缓存 key 加前缀、MQ topic 加后缀，与生产数据物理隔离。
- 标记必须全链路透传：HTTP 头 → RPC metadata → MQ 消息头，断一环就会污染生产数据（事故级）。
- 影子表与生产同构 + 独立清理任务；外部调用（短信/支付/推送）在压测流量下**硬阻断**。
- 与 NODE-091 流量染色同一套机制：染色头既服务灰度也服务压测，网关注入、ALS 透传。

```javascript
// 染色中间件：识别并透传压测标记
app.use(async (ctx, next) => {
  ctx.state.shadow = ctx.get('x-load-test') === '1';
  if (ctx.state.shadow) {
    ctx.state.tableSuffix = '_shadow';
    ctx.state.cachePrefix = 'lt:';
    ctx.state.topicSuffix = '.shadow';
  }
  await next();
});

// ORM 层统一重写 SQL（示意）
function rewriteSql(sql, shadow) {
  return shadow
    ? sql.replace(/\bFROM\s+orders\b/i, 'FROM orders_shadow')
         .replace(/\bINSERT\s+INTO\s+orders\b/i, 'INSERT INTO orders_shadow')
    : sql;
}

// 红线：外部调用硬阻断
function guardExternal(ctx) {
  if (ctx.state.shadow) throw new Error('external call blocked under load test');
}
// 监控：压测流量单独打点（label shadow=1），与生产指标分开看板
```
