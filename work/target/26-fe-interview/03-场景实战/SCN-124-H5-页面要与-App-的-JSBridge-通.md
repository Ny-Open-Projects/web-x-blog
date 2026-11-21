---
title: [SCN-124] H5 页面要与 App 的 JSBridge 通信，但线上有 5 个 App 版本接口行为不一致，如何做兼容层？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-124：H5 页面要与 App 的 JSBridge 通信，但线上有 5 个 App 版本接口行为不一致，如何做兼容层？
**答**：
- 建 BridgeAdapter 适配层：按"能力探测"注册（WKWebView messageHandlers / Android addJavascriptInterface / scheme 拦截），而不是按版本号写 if-else——版本会越积越多，能力不会。
- App 注入能力矩阵（bridge capabilities），调用前协商：旧版不支持的方法走前端 fallback（如 setTitle 不支持就用 document.title + 前端 UI）。
- 所有调用 promise 化 + 回调超时，防止原生侧不回调导致业务挂起。

```javascript
// JSBridge 适配器：按能力探测而非按版本写 if-else
class BridgeAdapter {
  handlers = new Map();

  constructor() {
    // 三种宿主探测：WKWebView / Android addJavascriptInterface / scheme
    if (window.webkit?.messageHandlers) this.native = window.webkit.messageHandlers.bridge;
    else if (window.NativeInterface) this.native = window.NativeInterface;
    this.capabilities = window.__BRIDGE_INFO__?.capabilities ?? {};   // App 注入能力矩阵
  }

  call(method, params = {}, { timeout = 5000 } = {}) {
    // 能力协商：旧版 App 不支持的方法走前端 fallback
    if (this.capabilities[method] === false) return this.fallback(method, params);
    const id = crypto.randomUUID();
    return new Promise((resolve, reject) => {
      const timer = setTimeout(() => reject(new Error(`bridge timeout: ${method}`)), timeout);
      this.handlers.set(id, (result) => { clearTimeout(timer); resolve(result); });
      this.native
        ? this.native.postMessage(JSON.stringify({ id, method, params }))
        : this.schemeCall({ id, method, params });
    });
  }
  // 原生回调统一入口
  onNativeMessage({ id, result }) {
    this.handlers.get(id)?.(result);
    this.handlers.delete(id);
  }
  schemeCall(payload) {
    const iframe = document.createElement('iframe');
    iframe.style.display = 'none';
    iframe.src = `myapp://bridge?payload=${encodeURIComponent(JSON.stringify(payload))}`;
    document.body.appendChild(iframe);
    setTimeout(() => iframe.remove(), 100);
  }
  fallback(method, params) {
    // 例：旧版不支持原生 setTitle，前端用 document.title 兜底
    if (method === 'setTitle') document.title = params.title;
    return Promise.resolve({ degraded: true });
  }
}
```
