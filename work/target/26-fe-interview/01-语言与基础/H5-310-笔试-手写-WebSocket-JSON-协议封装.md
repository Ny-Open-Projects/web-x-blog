---
title: [H5-310] 笔试：手写 WebSocket JSON 协议封装
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 笔试题, WebSocket]
type: 笔试题
---

## H5-310：笔试：手写 WebSocket JSON 协议封装

**题目**：实现协议层 `ProtoWS(url)`：消息统一 `{ v: 1, type, id, payload }` 信封；`emit(type, payload)` 返回 Promise（带 id，服务端回 ack/id 匹配，10s 超时 reject）；服务端主动推送（无 id 消息）走 `on(type, cb)` 订阅。

**答**：
```javascript
class ProtoWS {
  #pending = new Map(); // id -> { resolve, reject, timer }
  #subs = new Map();
  constructor(url) {
    this.ws = new WebSocket(url);
    this.ws.onmessage = (e) => {
      let m; try { m = JSON.parse(e.data); } catch { return; }
      if (!m?.type) return;
      if (m.id && this.#pending.has(m.id)) {          // 响应
        const p = this.#pending.get(m.id);
        clearTimeout(p.timer);
        this.#pending.delete(m.id);
        m.error ? p.reject(new Error(m.error)) : p.resolve(m.payload);
      } else {                                        // 服务端推送
        this.#subs.get(m.type)?.forEach(cb => cb(m.payload));
      }
    };
  }
  emit(type, payload) {
    return new Promise((resolve, reject) => {
      const id = crypto.randomUUID();
      const timer = setTimeout(() => {
        this.#pending.delete(id);
        reject(new Error(`timeout: ${type}`));
      }, 10000);
      this.#pending.set(id, { resolve, reject, timer });
      this.#send({ v: 1, type, id, payload });
    });
  }
  on(type, cb) {
    if (!this.#subs.has(type)) this.#subs.set(type, new Set());
    this.#subs.get(type).add(cb);
    return () => this.#subs.get(type).delete(cb); // 退订
  }
  #send(m) { this.ws.readyState === 1 && this.ws.send(JSON.stringify(m)); }
}
// 用法
const p = new ProtoWS('wss://im.example.com');
await p.emit('send', { text: 'hi' });           // 请求-响应
p.on('message', (msg) => console.log(msg));     // 服务端推送
```

**评分点**：
- 请求 id + pending Map 的响应匹配模型（RPC over WS）
- 超时必须清理 pending 项（防 Map 泄漏）
- 响应与推送的分流依据：有无 id——协议设计核心
- on 返回退订函数；JSON 解析容错
