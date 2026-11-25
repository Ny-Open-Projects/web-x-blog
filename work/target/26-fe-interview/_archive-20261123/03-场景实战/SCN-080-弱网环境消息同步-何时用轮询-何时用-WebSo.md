---
title: [SCN-080] 弱网环境消息同步，何时用轮询、何时用 WebSocket，如何设计自动切换策略？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-080：弱网环境消息同步，何时用轮询、何时用 WebSocket，如何设计自动切换策略？
**答**：
- 默认 WebSocket；WS 连接失败或频繁断开降级为长轮询（服务端 hold 住请求直到有消息），再失败降级为 30 秒短轮询。
- 用"连续失败次数"驱动降级，"连续成功次数"驱动升级回 WS，形成状态机而不是一次性选择。
- 页面隐藏时统一降为低频轮询省电，恢复可见再升回原通道。

```javascript
// 消息通道自适应：WebSocket -> 长轮询 -> 短轮询，按连续失败自动降级升级
class AdaptiveChannel {
  state = 'ws';
  fails = 0;
  success = 0;

  start() {
    if (this.state === 'ws') return this.startWS();
    if (this.state === 'long-poll') return this.startLongPoll();
    return this.startShortPoll();
  }
  startWS() {
    const ws = new WebSocket('wss://msg.example.com');
    ws.onmessage = (e) => this.onMessage(e.data);
    ws.onclose = () => {
      if (++this.fails >= 2) { this.state = 'long-poll'; this.fails = 0; }   // 降级
      this.start();
    };
  }
  async startLongPoll() {
    try {
      // 服务端 hold 住请求直到有消息或 25 秒超时返回
      const res = await fetch('/api/messages?wait=25', { signal: AbortSignal.timeout(30000) });
      this.onMessage(await res.json());
      this.fails = 0;
    } catch {
      if (++this.fails >= 3) { this.state = 'short-poll'; this.fails = 0; }  // 再降级
    }
    this.start();
  }
  startShortPoll() {
    this.timer = setInterval(async () => {
      try {
        this.onMessage(await api.pollLatest());
        this.fails = 0;
        // 短轮询连续成功 5 次尝试升级回 WebSocket
        if (++this.success >= 5) { this.success = 0; this.state = 'ws'; this.start(); }
      } catch { this.fails++; }
    }, 30000);
  }
}
```
