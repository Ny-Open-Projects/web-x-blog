---
title: [WEB-614] 笔试：手写基于 storage 事件的跨 tab 通知（含分区兼容）
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, 浏览器架构]
type: 笔试题
---

## WEB-614：笔试：手写基于 storage 事件的跨 tab 通知

**答**：实现 `TabBus`：① `broadcast(type, payload)` 写 localStorage 特定 key（值含自增 seq + type + payload）触发 storage 事件；② 各 tab 监听 storage 事件分发处理，忽略自己写入（storage 事件不触发本 tab，但防御性校验 seq）；③ 乱序防御：按 seq 单调递增过滤旧消息；④ 与 BroadcastChannel 双实现：支持 BroadcastChannel 用之（更高效），否则降级 storage；⑤ 统一 on(type, handler) API。写出核心实现。

```javascript
class TabBus {
  constructor(name) {
    this.name = name; this.seq = 0; this.handlers = new Map();
    if ('BroadcastChannel' in self) {
      this.bc = new BroadcastChannel(name);
      this.bc.onmessage = ({ data }) => this._dispatch(data);
      this.mode = 'bc';
    } else {
      this.key = `__tabbus_${name}`;
      addEventListener('storage', (e) => {
        if (e.key !== this.key || !e.newValue) return;
        try { this._dispatch(JSON.parse(e.newValue)); } catch {}
      });
      this.mode = 'storage';
    }
  }
  broadcast(type, payload) {
    const msg = { type, payload, seq: ++this.seq, ts: Date.now() };
    if (this.bc) this.bc.postMessage(msg);
    else localStorage.setItem(this.key, JSON.stringify(msg));
  }
  on(type, handler) { (this.handlers.get(type) ||= new Set()).add(handler); return () => this.handlers.get(type)?.delete(handler); }
  _dispatch({ seq, type, payload }) {
    if (seq <= (this.lastSeq || 0)) return; // 乱序/重复过滤
    this.lastSeq = seq;
    this.handlers.get(type)?.forEach(h => h(payload));
  }
}
```

**评分点**：
- 双实现优先 BroadcastChannel，storage 为老环境降级
- seq 单调过滤乱序与重复消息
- storage 模式 key 隔离 + 异常 JSON 防御
- 能说明 storage 事件不触发本 tab（天然自过滤），BroadcastChannel 无此语义所以也要 seq
