---
title: [H5-241] WebSocket 的 readyState 有哪些，重连要怎么判断
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, WebSocket]
type: 面试题
---

## H5-241：WebSocket 的 readyState 有哪些，重连要怎么判断

**答**：
- 四个状态：CONNECTING(0) / OPEN(1) / CLOSING(2) / CLOSED(3)；发送前必须检查 readyState === 1
- 重连触发点：onclose 事件（区分主动关闭与异常关闭，用标志位）；onerror 只是辅助信号，不等于连接已断
- 状态机设计：连接中 → 已连接 → 断开 → 重连中（指数退避）→ 已停止（手动 close 或超次数）
- 半开问题：TCP 没断但对端死了，readyState 还是 OPEN——必须靠心跳超时主动 close 后重连
- 细节坑：close() 在 CONNECTING 状态调用行为因浏览器而异；重连要重建所有事件监听（新建实例）

```javascript
class ReconnectingWS {
  constructor(url) { this.url = url; this.stopped = false; this.#connect(); }
  #connect() {
    this.ws = new WebSocket(this.url);
    this.ws.onopen = () => { this.retry = 0; };
    this.ws.onclose = () => {
      if (this.stopped) return;
      setTimeout(() => this.#connect(), Math.min(30000, 1000 * 2 ** this.retry++));
    };
  }
  send(m) { if (this.ws.readyState === 1) this.ws.send(m); else this.queue.push(m); }
  stop() { this.stopped = true; this.ws.close(); }
}
```
