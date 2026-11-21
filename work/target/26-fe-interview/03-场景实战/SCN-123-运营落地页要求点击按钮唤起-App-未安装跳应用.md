---
title: [SCN-123] 运营落地页要求"点击按钮唤起 App"，未安装跳应用商店，如何设计唤起与兜底？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-123：运营落地页要求"点击按钮唤起 App"，未安装跳应用商店，如何设计唤起与兜底？
**答**：
- 按优先级选通道：iOS 首选 Universal Link（系统级分发、无确认弹窗、未安装自动回退网页）；Android 用 Intent URL（可携带 fallback_url，部分机型免确认）；scheme 覆盖老版本但无法感知是否安装成功。
- scheme 兜底逻辑：触发 scheme 后用 visibilitychange + 计时器（2.5 秒）判定——页面未离开视为唤起失败，跳转应用商店。
- 唤起结果打点（成功/失败/跳商店），持续优化跳转策略与文案。

```javascript
// H5 唤起 App：scheme 尝试 + 超时兜底商店，Universal Link 直接导航
const SCHEME = 'myapp://detail?id=1001';
const STORE = 'https://app.example.com/download';
const isIOS = /iphone|ipad/i.test(navigator.userAgent);
const isAndroid = /android/i.test(navigator.userAgent);

function openApp() {
  if (isIOS && supportsUniversalLink()) {
    // Universal Link：未安装自动回退网页，体验最佳
    location.href = 'https://app.example.com/detail?id=1001';
    return;
  }
  const start = Date.now();
  let left = false;
  document.addEventListener('visibilitychange', () => { if (document.hidden) left = true; });

  if (isAndroid) {
    // intent 协议：未安装时由系统直接走 fallback_url
    location.href = `intent://detail?id=1001#Intent;scheme=myapp;`
      + `package=com.example.app;S.browser_fallback_url=${encodeURIComponent(STORE)};end`;
  } else {
    location.href = SCHEME;
  }
  // 兜底：2.5 秒仍未离开页面说明唤起失败
  setTimeout(() => {
    if (!left && !document.hidden) {
      location.href = STORE;
      track('app-launch-fallback', { cost: Date.now() - start });
    }
  }, 2500);
}

function supportsUniversalLink() {
  // iOS 9.3+ 且 App 已配置 apple-app-site-association 才支持
  const m = navigator.userAgent.match(/OS (\d+)_/);
  return !!m && +m[1] >= 9;
}
```
