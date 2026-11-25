---
title: [PER-1030] WebSocket 的性能要点：心跳、背压与压缩
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1030：WebSocket 的性能要点：心跳、背压与压缩

**答**：
- 长连接健康：心跳保活（30s ping/pong）穿透 NAT 超时；断线指数退避重连 + 网络切换立即重连。
- 背压：发送缓冲区检测（bufferedAmount），积压超阈值暂停发送，防止内存膨胀与消息时序错乱。
- 压缩：permessage-deflate 降低带宽但增加 CPU，高频小消息场景评估后开启；二进制协议（protobuf）替代 JSON 更省。
- 监控：RTT（ping-pong 差值）、积压量、重连率作为长连接健康指标。

```javascript
class SafeWS {
  constructor(url) {
    this.ws = new WebSocket(url);
    this.ws.binaryType = 'arraybuffer';
    this.timer = setInterval(() => {
      if (this.ws.readyState === 1) { this.t0 = Date.now(); this.ws.send('ping'); }
    }, 30_000);
    this.ws.onmessage = e => {
      if (e.data === 'pong') this.rtt = Date.now() - this.t0;
      else this.onData?.(e.data);
    };
    this.ws.onclose = () => this.#reconnect();
  }
  send(msg) {
    if (this.ws.bufferedAmount > 1024 * 512) {       // 背压：积压 > 512KB
      report({ type: 'ws-backpressure', buffered: this.ws.bufferedAmount });
      return false;                                  // 拒绝发送，调用方降级
    }
    this.ws.send(msg); return true;
  }
  #reconnect() { /* 指数退避 + jitter，参照 1027 */ }
}
```
