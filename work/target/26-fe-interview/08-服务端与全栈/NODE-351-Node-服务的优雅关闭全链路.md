---
title: [NODE-351] Node 服务的优雅关闭（Graceful Shutdown）全链路如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-351：Node 服务的优雅关闭全链路
**答**:
- 关闭时序：收到 SIGTERM → 标记不健康（readiness false，LB 摘流）→ server.close() 停止新请求 → 等存量请求完成（超时强杀 30s）→ 关闭下游连接（DB 池/Redis/MQ 消费者 stopFetch）→ flush 内存数据（日志/指标）→ exit。
- 长连接处理：WS/SSE 先发"服务即将重启"让客户端重连到其他实例（ARC-346 优雅下线）；等连接 drain 或超时。
- K8s 配合：terminationGracePeriodSeconds > 关闭超时；preStop sleep 2~5s 给 LB 传播摘流时间；readiness 探针摘流优先于 SIGTERM。
- 中断防护：进行中的异步任务（消息消费）关闭 ack 机制——未 ack 消息回队列重投（幂等保障，ARC-344）；定时任务检查点续跑。
- 信号处理纪律：只处理 SIGTERM/SIGINT；uncaughtException 记录后退出（状态已不可信，不要试图继续服务）。
```javascript
async function shutdown(signal) {
  server.unref?.();
  ready = false;                                                  // 1. 摘流
  await new Promise(r => server.close(r));                        // 2. 停新连
  await Promise.race([drainConnections(), delay(15000)]);         // 3. 等 drain
  await mqConsumer.stop();                                        // 4. 停消费（未 ack 回队）
  await db.end(); redis.quit();                                   // 5. 关下游
  await logger.flush();                                           // 6. flush
  process.exit(0);
}
process.on('SIGTERM', () => shutdown('SIGTERM'));
```
