---
title: [WEB-498] 笔试：手写全局错误上报 SDK
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 笔试题, 监控]
type: 笔试题
---

## WEB-498：笔试：手写全局错误上报 SDK

**题目**：实现 `initErrorReport()`：捕获 window.onerror、unhandledrejection、资源加载错误三类；堆栈脱敏截断；同一错误指纹 1 分钟内只上报一次；上报不阻塞主线程。

**答**：
```javascript
function initErrorReport({ dsn = '/api/error-report' } = {}) {
  const seen = new Map(); // fingerprint -> lastTime
  const seenWindow = 60_000;

  function report(payload) {
    const fp = payload.type + '|' + (payload.message || '').slice(0, 100) + '|' + payload.file;
    const now = Date.now();
    if (seen.get(fp) && now - seen.get(fp) < seenWindow) return; // 去重节流
    seen.set(fp, now);
    requestIdleCallback?.(() => navigator.sendBeacon(dsn, JSON.stringify({
      ...payload, ua: navigator.userAgent, url: location.href,
    })) ?? navigator.sendBeacon(dsn, JSON.stringify(payload)));
  }

  window.addEventListener('error', (e) => {
    if (e.target && (e.target.src || e.target.href)) { // 资源错误走 target
      return report({ type: 'resource', file: e.target.src || e.target.href, message: '资源加载失败' });
    }
    report({ type: 'js', message: e.message, file: e.filename, line: e.lineno, stack: (e.error?.stack || '').slice(0, 2000) });
  }, true); // 资源错误不冒泡，必须捕获阶段监听

  window.addEventListener('unhandledrejection', (e) => {
    report({ type: 'promise', message: String(e.reason?.message || e.reason) });
  });
}
```

**评分点**：
- 三类错误覆盖齐全：JS 错误、Promise 未处理拒绝、资源错误（target.src 判断）
- 资源错误必须捕获阶段监听（不冒泡）——高频判分点
- 错误指纹去重 + 时间窗节流，防错误风暴
- 上报用 sendBeacon/requestIdleCallback，不阻塞主线程
