---
title: [NODE-331] Node 服务的 Graceful 全链路？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-331：Node 服务的 Graceful 全链路？
**答**:
- 全链路优雅退出清单：停止收新请求（server.close）→ 停消费 MQ（consumer.pause → grace 期处理完在途）→ 停定时任务 → 刷日志/指标 → 关连接池 → exit；每步超时兜底。
- 编排器模式：shutdown 管理器统一调度各组件的 close（顺序+超时+并行度）。
- 验证：SIGTERM 注入后压测应零错误（NODE-237 reload 联动）。
- 长连接（WS/SSE）：主动通知客户端重连或迁移——连接期 grace 时间要够（PM2 kill_timeout）。

```javascript
// Graceful 编排器
const shutdownManager = new ShutdownManager();
shutdownManager.register({ name: 'http', close: () => server.close(), timeout: 10_000 });
shutdownManager.register({ name: 'mq', close: () => consumer.gracefulStop({ timeout: 5000 }) });
shutdownManager.register({ name: 'db', close: () => pool.end(), timeout: 5000 });
process.on('SIGTERM', () => shutdownManager.run()
  .then(() => process.exit(0))
  .catch(() => process.exit(1)));
class ShutdownManager {
  async run() {
    for (const s of this.items) {                    // 按注册顺序
      await Promise.race([s.close(), sleep(s.timeout)]);   // 超时兜底
    }
  }
}
```
