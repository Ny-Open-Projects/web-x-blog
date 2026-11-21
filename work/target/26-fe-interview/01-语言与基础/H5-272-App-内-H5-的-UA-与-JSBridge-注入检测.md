---
title: [H5-272] App 内 H5 的 UA 与 JSBridge 注入检测
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, 移动端]
type: 面试题
---

## H5-272：App 内 H5 的 UA 与 JSBridge 注入检测

**答**：
- 环境判断双通道：UA 字符串（App 通常附加标识如 `MyApp/3.2`）与 JSBridge 对象探测（`window.AndroidBridge` / `window.webkit.messageHandlers`）
- 时序坑：JSBridge 注入时机不一定在页面加载前——要轮询或监听 `WebViewJavascriptBridgeReady` 事件，不能页面 init 就调用
- UA 的不可靠性：可以伪造、可能被代理改写，关键逻辑别只依赖 UA，用 bridge 存在性做二级校验
- 调用规范：所有 bridge 调用封装成带超时的 Promise（原生可能不回调），统一的错误码回传
- 面试钩子：能说清「UA 判断环境、bridge 判断能力」的分层，比背 UA 正则高级

```javascript
function isNative() { return /MyApp\/\d/.test(navigator.userAgent); }
function callBridge(name, args, timeout = 5000) {
  return new Promise((resolve, reject) => {
    const timer = setTimeout(() => reject(new Error('bridge timeout')), timeout);
    const bridge = window.AndroidBridge || window.webkit?.messageHandlers;
    if (!bridge) { clearTimeout(timer); return reject(new Error('no bridge')); }
    bridge.postMessage(JSON.stringify({ name, args, cb: Date.now() }));
    pendingCbs[cbId] = (res) => { clearTimeout(timer); resolve(res); };
  });
}
```
