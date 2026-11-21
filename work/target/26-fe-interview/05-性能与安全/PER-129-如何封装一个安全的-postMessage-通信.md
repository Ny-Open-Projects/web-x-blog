---
title: [PER-129] 如何封装一个安全的 postMessage 通信模块？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-129：如何封装一个安全的 postMessage 通信模块？

**答**：
- 四要素：**出向 targetOrigin 明确**（禁止 `'*'`）、**入向 e.origin 精确比对**、**消息带协议名与递增序号**（防重放）、**payload 进业务前再过一次 schema 校验**。
- 消息体不裸传业务数据，统一 `{ protocol, type, seq, payload }` 信封；类型不认识的直接丢弃。
- 序号单调递增，收到比已处理序号小的消息视为重放丢弃。
- 发送方持有对端 window 的引用要随 iframe 重载重建，通信模块要暴露销毁方法防泄漏。

```javascript
// 安全 postMessage 封装：双向 origin 校验 + 协议信封 + 防重放
const PROTOCOL = 'app.bridge/v1';
const PEER_ORIGIN = 'https://widget.partner.com'; // 发送与校验都用精确 origin，禁止 '*'

export class SafeChannel {
  constructor(win, { origin = PEER_ORIGIN } = {}) {
    this.win = win;
    this.origin = origin;
    this.seq = 0;
    this.lastSeq = 0;
    this.handlers = new Map();
    window.addEventListener('message', (e) => {
      if (e.origin !== this.origin) return;      // 入向：来源必须精确匹配
      const msg = e.data;
      if (msg?.protocol !== PROTOCOL) return;    // 协议不符直接丢弃
      if (typeof msg.seq !== 'number' || msg.seq <= this.lastSeq) return; // 防重放
      this.lastSeq = msg.seq;
      this.handlers.get(msg.type)?.(msg.payload);
    });
  }
  send(type, payload) {
    this.win.postMessage({ protocol: PROTOCOL, type, seq: ++this.seq, payload }, this.origin); // 出向显式 targetOrigin
  }
  on(type, fn) { this.handlers.set(type, fn); }
  destroy() { this.handlers.clear(); this.win = null; }
}

// 用法：子页只响应自己认识的 type，payload 用前再做 schema 校验
const frame = document.getElementById('widget');
const ch = new SafeChannel(frame.contentWindow);
ch.on('resize', ({ height }) => { frame.style.height = `${Number(height) || 0}px`; });
```
