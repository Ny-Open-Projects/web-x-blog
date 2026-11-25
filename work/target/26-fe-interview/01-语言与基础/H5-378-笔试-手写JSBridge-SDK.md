---
title: [H5-378] 笔试：手写 JSBridge SDK（双端适配 + 回调管理）
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 笔试题, Hybrid]
type: 笔试题
---

## H5-378：笔试：手写 JSBridge SDK

**答**：实现 `JSBridge`：① `call(module, action, params)` 返回 Promise，回调 id 关联 Native 响应；② 双通道适配：优先原生注入对象（window.NativeBridge.postMessage），否则 URL scheme 兜底（协议 myapp://bridge?payload=）；③ 超时 10s reject 且清理回调；④ Native 主动事件：`on(event, handler)` + Native 推送分发；⑤ 白名单校验：仅在授权域名下可用（location 白名单）。写出核心实现。

```javascript
const ALLOWED_HOSTS = ['m.example.com', 'app.example.com'];

class JSBridge {
  constructor() {
    this.cbs = new Map(); this.events = new Map(); this.seq = 0;
    if (!ALLOWED_HOSTS.includes(location.hostname)) return; // 白名单外不启用
    // Native 推送统一入口
    window.__bridgeReceive = (raw) => this._receive(typeof raw === 'string' ? JSON.parse(raw) : raw);
  }
  call(module, action, params = {}, timeout = 10_000) {
    return new Promise((resolve, reject) => {
      const id = `cb_${++this.seq}_${Date.now()}`;
      const timer = setTimeout(() => { this.cbs.delete(id); reject(new Error(`bridge timeout: ${module}.${action}`)); }, timeout);
      this.cbs.set(id, { resolve, reject, timer });
      const payload = JSON.stringify({ id, module, action, params });
      if (window.NativeBridge?.postMessage) window.NativeBridge.postMessage(payload);
      else location.href = `myapp://bridge?payload=${encodeURIComponent(payload)}`;
    });
  }
  _receive({ id, ok, data, event, payload }) {
    if (event) return this.events.get(event)?.forEach(h => h(payload)); // 事件推送
    const cb = this.cbs.get(id);
    if (!cb) return;
    clearTimeout(cb.timer); this.cbs.delete(id);
    ok ? cb.resolve(data) : cb.reject(new Error(data?.message || 'bridge error'));
  }
  on(event, handler) { (this.events.get(event) ||= new Set()).add(handler); return () => this.events.get(event)?.delete(handler); }
}
// Native 侧回调示例: evaluateJavascript("__bridgeReceive('...json...')")
```

**评分点**：
- 回调 id 关联 + 超时清理，无悬挂 Promise
- 双通道适配（注入对象优先，scheme 兜底）与 payload 编码
- Native 事件推送与请求回调共用分发入口区分
- 白名单校验作为安全前置
