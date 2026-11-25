---
title: [H5-327] Hybrid JSBridge：通信协议设计与安全
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, Hybrid]
type: 面试题
---

## H5-327：Hybrid JSBridge：通信协议设计与安全

**答**：
- 通信通道双向设计：JS→Native 用拦截 URL scheme（shouldOverrideUrlLoading）或原生注入对象（addJavascriptInterface）；Native→JS 用 evaluateJavascript/ stringByEvaluatingJavaScript 派发回调
- 协议三要素：方法命名空间（module.action）、回调 id（异步结果关联）、参数 JSON 序列化——建议再加版本号与签名（防第三方页面伪造调用）
- 安全是重点：白名单域名才注入桥、敏感方法（支付/登录态）必须校验调用来源（refer + token）、参数大小限制防内存攻击
- iOS WKWebView 差异：不能拦 URL scheme 走应答式，要用 WKScriptMessageHandler（window.webkit.messageHandlers），协议层要抹平两端差异
- 稳定性设计：超时机制（Native 未响应回调）、Native 崩溃降级（H5 功能可独立降级运行）、bridge ready 竞态（JS 先于注入执行）

```javascript
const bridge = {
  cbMap: new Map(), seq: 0,
  call(module, action, params) {
    return new Promise((resolve, reject) => {
      const id = `cb_${++this.seq}`;
      this.cbMap.set(id, { resolve, reject, ts: Date.now() });
      const payload = JSON.stringify({ id, module, action, params, ver: '2.0' });
      // 双端适配
      window.webkit?.messageHandlers?.nativeBridge?.postMessage(payload)
        || (window.NativeBridge?.postMessage?.(payload))
        || (location.href = `jsbridge://${encodeURIComponent(payload)}`);
      setTimeout(() => { // 超时保护
        if (this.cbMap.has(id)) { this.cbMap.delete(id); reject(new Error('bridge timeout')); }
      }, 10_000);
    });
  },
  onNativeResponse({ id, ok, data }) {
    const cb = this.cbMap.get(id);
    if (!cb) return;
    this.cbMap.delete(id);
    ok ? cb.resolve(data) : cb.reject(data);
  },
};
```
