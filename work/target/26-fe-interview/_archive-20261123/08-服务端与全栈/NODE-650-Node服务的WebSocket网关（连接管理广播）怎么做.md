---
title: [NODE-650] WebSocket 网关（连接管理/广播/横向扩展）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-650：WebSocket 网关怎么做？
**答**：
- 连接管理：连接注册表（userId → sockets 多端映射）、心跳保活（ping/pong——死连接清理，浏览器半开连接探测）、背压（ws 缓冲区积压检测——慢消费者踢掉或降级，SCN-FIN-558 同源）。
- 广播模型：进程内广播（同实例用户）+ 跨实例广播（pub/sub Redis——发布到频道，各实例订阅后推本地连接）；消息扇出的 fan-out 成本模型（万级连接 × 消息 = 推送风暴，需合并窗口）。
- 横向扩展：连接无状态化（连接归属实例，路由通过 pub/sub 解耦）——sticky 与否的权衡（sticky 让进程内直达高效，非 sticky 用 pub/sub 通用）。
- 可靠性：重要消息的 ACK 与重推（通知类不可靠推送 + 业务侧拉取兜底——推拉结合）。
- 追问钩子：为什么「慢消费者」必须在网关层处理——WebSocket 的 TCP 缓冲会静默积压（send 不报错但 bufferedAmount 涨），慢客户端会让实例内存涨 + 广播延迟拖累全组；监控 bufferedAmount 超阈值 → 踢掉或降级为轮询——广播系统的吞吐由最慢的接收者决定。

```javascript
setInterval(() => wss.clients.forEach(ws => {
  if (ws.bufferedAmount > 1e6) {                       // 1MB 积压：慢消费者
    ws.close(4000, 'SLOW_CONSUMER');                   // 踢掉，客户端转轮询降级
  } else ws.ping();
}), 30_000);
// 跨实例广播
redisSub.on('message', (ch, msg) => localBroadcast(msg));   // 各实例推本地连接
```
