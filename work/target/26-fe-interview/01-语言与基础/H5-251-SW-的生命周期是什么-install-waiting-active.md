---
title: [H5-251] SW 的生命周期是什么：install-waiting-active
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, PWA]
type: 面试题
---

## H5-251：SW 的生命周期是什么：install → waiting → active

**答**：
- installing：新 SW 下载解析中，install 事件里做预缓存（cache.addAll 全部资源）
- waiting：新 SW 已就绪但要等旧 SW 退出——旧 SW 仍控制着打开的页面，这是「更新不生效」的根源
- activating：旧 SW 的所有页面关闭后（或 skipWaiting 强制），新 SW 激活，activate 事件里清理旧缓存
- 控制范围：注册成功 ≠ 立即控制页面；首个 SW 要等下一次导航才控制（clients.claim 可立即接管）
- 版本强更方案：skipWaiting（跳过等待）+ clients.claim + 通知用户刷新，要权衡「强制更」对进行中操作的影响

```javascript
self.addEventListener('install', (e) => e.waitUntil(cache.addAll(ASSETS)));
self.addEventListener('activate', (e) => e.waitUntil(
  caches.keys().then(keys =>
    Promise.all(keys.filter(k => k !== CACHE_VERSION).map(k => caches.delete(k))))
));
// 主线程强制激活新版本
registration.waiting?.postMessage('SKIP_WAITING');
navigator.serviceWorker.addEventListener('controllerchange', () => location.reload());
```
