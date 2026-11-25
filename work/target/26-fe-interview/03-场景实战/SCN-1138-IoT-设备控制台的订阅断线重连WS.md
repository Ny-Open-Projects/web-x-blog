---
title: [SCN-1138] IoT 设备控制台的订阅断线重连（WS 可靠性）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1138：IoT 设备控制台的订阅断线重连（WS 可靠性）

**答**：
- 可靠性：WS 心跳（30s）+ 断线指数退避重连 + 重连后订阅恢复（topic 重订阅）。
- 补偿：断线期间数据丢失——重连后按 lastTs 拉增量（遥测/告警）。
- 降级：WS 不可用降级轮询（10s）。

```javascript
// 订阅可靠性
class ReliableWS {
  constructor(url, topics) {
    this.topics = topics; this.lastTs = Date.now();
    this.connect();
  }
  connect(attempt = 1) {
    this.ws = new WebSocket(this.url);
    this.ws.onopen = () => {
      this.ws.send(JSON.stringify({ action: 'subscribe', topics: this.topics }));
      this.resync();                                   // 补拉断线期间数据
    };
    this.ws.onclose = () => setTimeout(() =>
      this.connect(Math.min(attempt + 1, 6)), 1000 * 2 ** attempt);
  }
  resync() { return api('/telemetry/since', { ts: this.lastTs }); }
}
```
