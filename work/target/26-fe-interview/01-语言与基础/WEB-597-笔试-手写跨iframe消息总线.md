---
title: [WEB-597] 笔试：手写跨 iframe 消息总线（节流 + transferable）
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, 浏览器架构]
type: 笔试题
---

## WEB-597：笔试：手写跨 iframe 消息总线（节流 + transferable）

**答**：实现 `IframeBus`：① 主文档侧按 targetOrigin 白名单过滤 message 事件，拒绝未知来源；② `publish(topic, payload, { throttleMs })`：同 topic 节流合并（保留最后一次）；③ payload 为 ArrayBuffer/TypedArray 时自动 transferable 零拷贝；④ 子 iframe 侧提供对称 API `subscribe(topic, handler)`；⑤ 通道用 MessageChannel 建立点对点连接。写出核心实现与安全注意点。

```javascript
const T = { arr: ['ArrayBuffer', 'SharedArrayBuffer'] };

class IframeBus {
  constructor(win, allowedOrigins) {
    this.win = win; this.allowed = new Set(allowedOrigins);
    this.ch = new MessageChannel();
    this.handlers = new Map();
    this.ch.port1.onmessage = (e) => this._dispatch(e.data);
    this.ch.port1.start();
  }
  attachTo(iframe, targetOrigin) {
    if (!this.allowed.has(targetOrigin)) throw new Error('origin not allowed');
    iframe.contentWindow.postMessage({ __bus: 'hello' }, targetOrigin, [this.ch.port2]);
  }
  publish(topic, payload, { throttleMs = 0, targetOrigin } = {}) {
    if (throttleMs) {
      clearTimeout(this._t?.[topic]);
      this._t ||= {}; this._t[topic] = setTimeout(() => this._send(topic, payload, targetOrigin), throttleMs);
    } else this._send(topic, payload, targetOrigin);
  }
  _send(topic, payload, targetOrigin) {
    const transfer = payload instanceof ArrayBuffer ? [payload] : [];
    this.ch.port1.postMessage({ topic, payload }, transfer);
  }
  subscribe(topic, handler) {
    (this.handlers.get(topic) ||= new Set()).add(handler);
  }
  _dispatch({ topic, payload }) { this.handlers.get(topic)?.forEach(h => h(payload)); }
}
```

**评分点**：
- targetOrigin 白名单强校验，且 message 接收侧校验 e.origin（答案需提及）
- 节流合并保留最后一次值（而非丢弃），语义正确
- ArrayBuffer 自动走 transferable 列表实现零拷贝
- MessageChannel 点对点优于 window 层级广播（避免多 iframe 广播串扰）
