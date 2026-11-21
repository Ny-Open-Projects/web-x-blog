---
title: [SCN-055] 线上 WebSocket 频繁断连重连，如何排查？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-055：线上 WebSocket 频繁断连重连，如何排查？
**答**：
- 分层归因：网络层（网关空闲超时断开）、代理层（CDN/企业代理不支持 ws Upgrade）、应用层（服务端主动踢或崩溃），抓包看 close code：1006 异常断开多为网关超时。
- 最常见根因是网关 proxy_read_timeout 默认 60 秒无数据即断，心跳间隔必须小于该值；排查时先核对心跳周期与网关配置。
- 修复要同时防"重连风暴"：指数退避 + 随机抖动，否则网关恢复瞬间海量客户端同时重连会打挂服务端。

```javascript
// 带心跳、指数退避与抖动的 WebSocket 管理
class ResilientWS {
  constructor(url) {
    this.url = url;
    this.retry = 0;
    this.connect();
  }
  connect() {
    this.ws = new WebSocket(this.url);
    this.ws.onopen = () => {
      this.retry = 0;
      // 心跳间隔必须小于网关 proxy_read_timeout（默认 60s），这里 30s
      this.heartbeat = setInterval(() => this.ws.send('{"t":"ping"}'), 30000);
    };
    this.ws.onclose = (e) => {
      clearInterval(this.heartbeat);
      // close code：1000 正常关闭不重连；1006 异常断开多为网关超时或网络问题
      if (e.code !== 1000) this.reconnect();
    };
  }
  reconnect() {
    // 指数退避 + 随机抖动，防止海量客户端同一时刻重连打挂服务端
    const backoff = Math.min(30000, 1000 * 2 ** this.retry);
    const delay = backoff / 2 + Math.random() * (backoff / 2);
    this.retry++;
    setTimeout(() => this.connect(), delay);
  }
}
```
