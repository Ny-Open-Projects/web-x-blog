---
title: [NODE-310] Koa/Fastify 深水区：错误边界与进程稳定性？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-310：Koa/Fastify 深水区：错误边界与进程稳定性？
**答**:
- 错误分层：可预期业务错误（4xx 带码）→ 框架兜底（5xx）→ 未捕获异常（uncaughtException = 进程级事件）→ 不可恢复（OOM 被 PM2 拉起）。
- uncaughtException 策略：记录 + 告警 + 优雅退出（让 PM2 reload 拉起）——继续运行状态不可信（Node 官方立场）；unhandledRejection 记录但可观察处理。
- 每请求隔离：中间件 try/catch 保证单请求错误不影响进程（Koa/Fastify 内建）——但同步抛错在非 promise 路径（如注册回调）会逃逸。
- 定期演练：注入 uncaughtException 验证"记录→告警→拉起"链路完整（NODE-264 演练纪律）。

```javascript
// 进程级错误策略
process.on('uncaughtException', async (err) => {
  log.fatal({ err }, 'uncaught'); monitor.alert('process-crash', err);
  process.exit(1);                                 // 让 PM2 拉起（状态不可信）
});
process.on('unhandledRejection', (err) => {
  log.error({ err }, 'unhandledRejection');        // 记录不退出（观察版本修复情况）
  monitor.inc('unhandled_rejection');
});
// 框架兜底验证：任何 handler throw → 500 + 上报，进程不死（可注入测试路由验证）
app.get('/__boom', () => { throw new Error('test crash'); });
```
