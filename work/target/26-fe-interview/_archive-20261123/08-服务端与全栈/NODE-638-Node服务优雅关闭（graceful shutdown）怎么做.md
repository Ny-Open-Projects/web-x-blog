---
title: [NODE-638] Node 服务的优雅关闭怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-638：优雅关闭怎么做？
**答**：
- 信号处理：SIGTERM/SIGINT → 停止接受新请求（server.close + 负载均衡摘流）→ 排空在途请求（带超时上限）→ 关闭连接池/消费者 → 退出；K8s 的 preStop 与 readiness 探针配合（先摘流量再 SIGTERM——SCN-OPS 编排）。
- 排空手段：在途请求等待（server.close 回调）+ 长连接处理（WebSocket 主动关/迁移）；超时兜底（排空上限如 30s，超时强杀防僵尸——SIGKILL 兜底）。
- 关闭顺序：先停止「生产新工作」的入口（HTTP/消息消费）→ 等在途完成 → 关下游连接（DB/Redis 池）→ flush 遥测（最后上报不丢）。
- 未捕获异常兜底：uncaughtException/unhandledRejection 记录后决定（不可恢复才退出——退出前也要走优雅流程）。
- 追问钩子：为什么「先摘流量再 SIGTERM」而不是直接 SIGTERM——直接 SIGTERM 时 LB 可能仍把新请求路由到该实例（摘流有传播延迟），新请求在关闭中失败；readiness 探针先置 fail（LB 停止路由）+ preStop sleep（等 LB 传播）再 SIGTERM，排空才真正从空开始——这是 K8s 零停机发布的标准三步。

```javascript
process.on('SIGTERM', async () => {
  server.close();                                      // 停收新请求
  await Promise.race([drainConnections(), sleep(30_000)]);   // 排空 + 超时兜底
  await Promise.all([db.close(), redis.quit()]);
  await flushTelemetry();                              // 最后 flush 遥测
  process.exit(0);
});
// K8s: preStop: sleep 5s + readiness 探针联动
```
