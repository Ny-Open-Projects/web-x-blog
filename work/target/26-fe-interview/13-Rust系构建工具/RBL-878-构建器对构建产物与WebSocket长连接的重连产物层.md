---
title: [RBL-878] 场景题：WebSocket 长连接的产物层——重连退避与心跳的封装边界
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-878：场景题：WebSocket 长连接的产物层——重连退避与心跳封装

**答**:
- WS 长连接的产物层封装：1) **重连退避**（指数退避 + 抖动 jitter——重连风暴防护：服务端重启时全量客户端同时重连 = 二次雪崩）；2) 心跳（ping/pong 保活 + 死链检测——心跳超时判定断线主动重连）；3) 消息队列（断线期间的消息缓冲——重连后重放，幂等键防重复 RBL-640）；4) 页面可见性联动（后台 tab 降频心跳/断开——省电与服务器资源）。
- 构建器的配合：WS 库独立 chunk（聊天/协作页用——RBL-840 策略）；能力检测降级（WS 不可用 → SSE/轮询 RBL-874 降级链的 ws 版）；「连接参数」配置化（退避基数/心跳间隔）不是硬编码——多环境调优需要。
- 封装的边界：重连/心跳/队列是通用层（库），业务语义（消息协议）是应用层——「通用层不认识业务消息」是可测试性的关键（RBL-655 的分层）。
- 页面生命周期：visibilitychange 时的连接策略（hidden → 心跳降频或断开，visible → 立即重连）；unload 的清理（beforeunload 发送 leaving 消息尽力而为）。
- 追问钩子：为什么重连必须加「抖动」？——服务端重启/网络恢复时，所有断线客户端的重连定时器几乎同时到期（指数退避的基数相同）→ 惊群（N 万客户端同时握手 = 服务端二次崩溃）；jitter（退避 × random(0.5, 1.5)）把重连时间打散——「分布式系统的时钟同步是灾难，随机化是解药」，与缓存过期加抖动、任务调度错峰同构。

```javascript
// WS 封装：退避抖动 + 心跳 + 队列
class WsClient {
  #backoff = 1000; #queue = [];
  constructor({ url, heartbeatMs = 30000, onMessage }) { ... }
  #scheduleReconnect() {
    const jitter = 0.5 + Math.random();                  // ×0.5~1.5 抖动
    const delay = Math.min(this.#backoff * jitter, 30000);
    this.#backoff = Math.min(this.#backoff * 2, 30000);
    setTimeout(() => this.connect(), delay);
  }
  #startHeartbeat() {
    this.#hb = setInterval(() => {
      if (Date.now() - this.#lastPong > this.heartbeatMs * 2) return this.reconnect();  // 死链
      this.send({ type: 'ping' });
    }, this.heartbeatMs);
  }
  send(msg) {
    if (this.ws?.readyState === 'open') return this.ws.send(JSON.stringify(msg));
    this.#queue.push(msg);                               // 断线缓冲，重连后重放
  }
}
// 产物配置化
const wsConfig = { backoffBaseMs: 1000, backoffMaxMs: 30000, heartbeatMs: 30000, jitter: true };
```
