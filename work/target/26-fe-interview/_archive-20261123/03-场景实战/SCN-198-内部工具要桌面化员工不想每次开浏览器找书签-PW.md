---
title: [SCN-198] 内部工具要"桌面化"：员工不想每次开浏览器找书签，PWA 桌面化如何落地？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-198：内部工具要"桌面化"：员工不想每次开浏览器找书签，PWA 桌面化如何落地？
**答**：
- PWA 桌面化 = manifest 安装（独立窗口、任务栏图标）+ Service Worker 缓存（内网弱环境可用）+ 系统能力（通知、协议唤起）。Chrome/Edge 支持最好，安装用 `beforeinstallprompt` 捕获引导。
- 缓存策略按资源分层：App shell（框架 HTML/CSS/JS）precache + 版本化更新，接口数据 network-first 带超时回退缓存，静态资源 cache-first。
- 更新体验是重点：SW 检测到新版本不自动刷新（打断工作），提供"有新版本，点击更新"的全局提示条，用户确认后 `skipWaiting` + 刷新。
- 内网特殊问题：证书信任、多子域 Cookie、SW 作用域要提前验证；离线可用范围要明确（工具类缓存最近数据快照即可）。

```javascript
// PWA 桌面化：安装引导 + SW 分层缓存 + 可控更新
// 1. 安装引导：捕获 beforeinstallprompt，在合适时机弹安装按钮
let deferredPrompt = null;
window.addEventListener('beforeinstallprompt', e => {
  e.preventDefault();
  deferredPrompt = e;                                  // 存起来，别让浏览器乱弹
});
export async function installApp() {
  if (!deferredPrompt) return showToast('当前浏览器不支持安装，可用 Chrome/Edge');
  deferredPrompt.prompt();
  const { outcome } = await deferredPrompt.userChoice;
  report({ type: 'pwa-install', outcome });
  deferredPrompt = null;
}

// 2. Service Worker：资源分层缓存
// sw.js
const SHELL_CACHE = 'shell-v12';                       // App shell：版本化
self.addEventListener('install', e => {
  e.waitUntil(caches.open(SHELL_CACHE)
    .then(c => c.addAll(['/', '/app.css', '/app.js'])) // 精确列出 shell 资源
    .then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys =>
    Promise.all(keys.filter(k => k !== SHELL_CACHE).map(k => caches.delete(k)))));
});

self.addEventListener('fetch', e => {
  const { request } = e;
  if (request.method !== 'GET') return;
  const url = new URL(request.url);
  if (url.pathname.startsWith('/api/')) {
    // 接口：network-first 带超时，失败回退缓存快照（工具离线可看最近数据）
    e.respondWith(
      fetch(request).then(res => {
        const clone = res.clone();
        caches.open('api-cache').then(c => c.put(request, clone));  // 顺带更新快照
        return res;
      }).catch(() => caches.match(request))
    );
  } else {
    // 静态资源：cache-first，miss 才网络
    e.respondWith(caches.match(request).then(hit => hit ?? fetch(request)));
  }
});

// 3. 更新提示：新版本就绪后提示用户手动刷新，不打断当前工作
navigator.serviceWorker.register('/sw.js').then(reg => {
  reg.addEventListener('updatefound', () => {
    const sw = reg.installing;
    sw.onstatechange = () => {
      if (sw.state === 'installed' && navigator.serviceWorker.controller) {
        showUpdateBar(() => { sw.postMessage('SKIP_WAITING'); location.reload(); });
      }
    };
  });
});
```
