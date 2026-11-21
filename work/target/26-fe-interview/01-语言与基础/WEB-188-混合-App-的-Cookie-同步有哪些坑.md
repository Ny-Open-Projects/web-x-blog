---
title: [WEB-188] 混合 App 的 Cookie 同步有哪些坑？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-188：混合 App 的 Cookie 同步有哪些坑？
**答**：
- WebView 与原生网络层是两套 Cookie 存储：登录态在原生层设置后，H5 的 XHR 可能读不到（iOS WKWebView 尤其隔离）。
- iOS 方案：WKHTTPCookieStore.setCookie 显式同步，注意写入时机与响应头 Cookie 的主动搬运；Android 用 CookieManager.setCookie 加 flush。
- 通用坑：跨进程同步是异步的，存在竞态——先发请求后同步 Cookie 会丢登录态。
- 推荐时序：登录完成后由原生统一写 Cookie，再通知 H5 校验就绪后刷新业务。

```javascript
// H5 侧配合：收到原生 cookie-synced 通知后，校验关键 Cookie 可见再初始化
window.addEventListener('native-event', (e) => {
  if (e.detail.type !== 'cookie-synced') return;
  const ready = () => document.cookie.includes('__session=');
  // 轮询等待就绪（pollUntil 为简单轮询工具函数），规避跨进程同步的竞态
  (ready() ? Promise.resolve() : pollUntil(ready, { timeout: 3000 })).then(initApp);
});
// 原生侧对应：iOS 用 WKHTTPCookieStore.setCookie，Android 用 CookieManager.setCookie + flush
```
