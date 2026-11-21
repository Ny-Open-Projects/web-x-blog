---
title: [H5-050] 离线应用如何实现？AppCache 为什么被废弃？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-050：离线应用如何实现？AppCache 为什么被废弃？
**答**：
- 老方案 AppCache（manifest 文件声明缓存清单）已被废弃：声明式、控制力弱、缓存更新规则反直觉、双重缓存问题频发。
- 现行方案：Service Worker + Cache Storage（见 WEB-028），命令式、可编程，配合策略（Cache First/Network First）灵活控制。
- 完整离线应用 = SW 预缓存静态资源 + 接口数据缓存兜底 + 离线队列重放（Background Sync 可选）。
- 离线体验要兜底：离线 fallback 页面、失败提示、恢复后同步。

```html
<!-- 已废弃的 AppCache 写法：仅用于识别旧项目，新项目禁止使用 -->
<!-- <html manifest="offline.appcache"> -->
```

```javascript
// 现行方案：Service Worker 完整离线应用骨架
const VERSION = 'offline-v1';
const CACHE = `shell-${VERSION}`;
const SHELL = ['/', '/index.html', '/app.js', '/app.css', '/offline.html'];

self.addEventListener('install', (event) => {
  event.waitUntil(caches.open(CACHE).then((c) => c.addAll(SHELL)));
});

self.addEventListener('fetch', (event) => {
  const req = event.request;

  if (req.mode === 'navigate') {
    // 页面导航：网络优先，断网回退离线页
    event.respondWith(
      fetch(req).catch(() => caches.match('/offline.html'))
    );
  } else if (req.url.includes('/api/')) {
    // 接口：网络优先 + 缓存兜底，离线也能看到上次数据
    event.respondWith(
      fetch(req)
        .then((res) => {
          const copy = res.clone();
          caches.open(CACHE).then((c) => c.put(req, copy));
          return res;
        })
        .catch(() => caches.match(req))
    );
  } else {
    // 静态资源：缓存优先
    event.respondWith(
      caches.match(req).then((hit) => hit || fetch(req))
    );
  }
});
```

```javascript
// 页面侧：离线写操作排队，恢复后重放（Background Sync 思路的轻量实现）
const pending = JSON.parse(localStorage.getItem('pending-actions') || '[]');

window.addEventListener('online', async () => {
  while (pending.length) {
    const action = pending[0];
    try {
      await fetch(action.url, action.init);
      pending.shift(); // 成功才出队
      localStorage.setItem('pending-actions', JSON.stringify(pending));
    } catch {
      break; // 仍失败，保留队列等下次恢复
    }
  }
});

function submitOfflineSafe(url, init) {
  if (navigator.onLine) return fetch(url, init);
  pending.push({ url, init });
  localStorage.setItem('pending-actions', JSON.stringify(pending));
  toast('当前离线，已加入待同步队列');
}
```

## 十一、语义与结构进阶
