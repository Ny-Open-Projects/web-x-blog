---
title: [OPT-030] Service Worker 更新如何安全发布？skipWaiting 有什么坑？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-030：Service Worker 更新如何安全发布？skipWaiting 有什么坑？

**答**：
- 浏览器在导航/24h 检测到 sw.js **字节差异**后触发新 SW install；新 SW 默认等待（waiting）直到所有旧控制页面关闭才 activate。
- 直接 `skipWaiting + clients.claim` 会让新 SW 立即接管——但页面里运行的是旧代码、 precache 里是新清单，可能出现"新缓存 + 旧资源引用"的错配（懒加载 chunk 404）。
- 安全做法：skipWaiting 后提示用户刷新，或在 `controllerchange` 时统一 reload 一次；旧缓存必须在 activate 阶段清理。
- 灰度发布：服务端按比例下发不同版本的 precache manifest，出问题可快速回滚。

```javascript
// 一一对应：安全更新流程 —— 提示刷新 + 旧缓存清理
// main.js：检测到 waiting 的 SW 时提示用户
navigator.serviceWorker.register('/sw.js').then((reg) => {
  if (reg.waiting) notifyUpdate(); // 已有新版本在等待
  reg.addEventListener('updatefound', () => {
    const nw = reg.installing;
    nw?.addEventListener('statechange', () => {
      if (nw.state === 'installed' && navigator.serviceWorker.controller) notifyUpdate();
    });
  });
});
function notifyUpdate() {
  if (confirm('发现新版本，立即刷新？')) reg.waiting?.postMessage({ type: 'SKIP_WAITING' });
}
// 新 SW 接管后统一刷新，避免新旧资源错配
navigator.serviceWorker.addEventListener('controllerchange', () => location.reload());

// sw.js：用户确认后才跳过等待
self.addEventListener('message', (e) => {
  if (e.data?.type === 'SKIP_WAITING') self.skipWaiting();
});

// activate 阶段清理旧版本缓存，防止缓存无限膨胀
self.addEventListener('activate', (event) => {
  const keep = new Set([CACHE_NAME]);
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => !keep.has(k)).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});
```

## 六、运行时性能优化
