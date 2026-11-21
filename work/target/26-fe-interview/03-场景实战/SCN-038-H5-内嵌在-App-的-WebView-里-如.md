---
title: [SCN-038] H5 内嵌在 App 的 WebView 里，如何与 App 互相调用能力？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-038：H5 内嵌在 App 的 WebView 里，如何与 App 互相调用能力？
**答**：
- 约定 JSBridge 协议：H5 调 App 能力（定位、拍照、关页面）走 bridge.call(method, params)，App 主动推事件给 H5 用注册回调。
- Android 用 addJavascriptInterface 注入对象，iOS 用 WKScriptMessageHandler，H5 侧封装统一入口抹平差异。
- 工程细节：每次调用生成唯一回调名并挂 window，调用加超时兜底；bridge 全链路打日志，出问题能快速界定责任方。

```javascript
// 统一 JSBridge：抹平 Android / iOS 差异，返回 Promise
const bridge = {
  call(method, params = {}) {
    return new Promise((resolve, reject) => {
      const cbName = `__cb_${Date.now()}_${Math.random().toString(36).slice(2)}`;
      window[cbName] = (result) => {           // App 处理完后回调此函数
        delete window[cbName];
        result.code === 0 ? resolve(result.data) : reject(result);
      };
      const payload = JSON.stringify({ method, params, cbName });
      const ua = navigator.userAgent;
      if (/android/i.test(ua)) {
        window.NativeBridge?.postMessage(payload);                    // Android 注入对象
      } else if (/iphone|ipad/i.test(ua)) {
        window.webkit?.messageHandlers.native?.postMessage(payload);  // iOS handler
      } else {
        reject({ code: -1, msg: '非 WebView 环境' });
      }
      setTimeout(() => reject({ code: -2, msg: `${method} 调用超时` }), 10000); // 兜底
    });
  },
};
// 使用：const pos = await bridge.call('getLocation')；await bridge.call('closeWebView')
```

## 十、实时通信
