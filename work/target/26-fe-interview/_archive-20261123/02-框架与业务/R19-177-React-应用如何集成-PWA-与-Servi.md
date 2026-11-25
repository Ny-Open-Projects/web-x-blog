---
title: [R19-177] React 应用如何集成 PWA 与 Service Worker？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-177：React 应用如何集成 PWA 与 Service Worker？
**答**：
- 分工：SW 管资源缓存与离线（构建产物哈希清单交给 vite-plugin-pwa/workbox 生成），React 管"安装引导、更新提示、离线兜底 UI"。
- 更新流：SW 有新版本 -> waiting 状态 -> React 提示条 -> 用户确认 -> `skipWaiting` + `location.reload`，绝不能自动刷新打断用户操作。
- 缓存策略分层：App Shell 用 precache、静态资源 cache-first、API 请求 network-first（带离线回退），不要一刀切。
- React 侧只暴露三个 hook：useRegisterSW（注册+版本检测）、useOnlineStatus（navigator.onLine + 事件）、useInstallPrompt（beforeinstallprompt 捕获）。

```tsx
// pwa.tsx —— React 与 Service Worker 集成
import { useEffect, useState, useSyncExternalStore } from 'react';

// 1. 注册 + 版本检测（配 vite-plugin-pwa：import { registerSW } from 'virtual:pwa-register'）
export function useRegisterSW() {
  const [needRefresh, setNeedRefresh] = useState(false);
  const [waitingWorker, setWaitingWorker] = useState<ServiceWorker | null>(null);

  useEffect(() => {
    if (!('serviceWorker' in navigator)) return;
    navigator.serviceWorker.register('/sw.js').then(reg => {
      reg.addEventListener('updatefound', () => {
        const installing = reg.installing;
        installing?.addEventListener('statechange', () => {
          // 新 SW 安装完成且处于 waiting -> 提示用户更新
          if (navigator.serviceWorker.controller && installing?.state === 'installed') {
            setNeedRefresh(true);
            setWaitingWorker(installing);
          }
        });
      });
    });
    // 检测到 controllerchange（新 SW 接管）时刷新
    let refreshing = false;
    navigator.serviceWorker.addEventListener('controllerchange', () => {
      if (refreshing) return;
      refreshing = true;
      location.reload();
    });
  }, []);

  const update = () => {
    waitingWorker?.postMessage({ type: 'SKIP_WAITING' }); // 用户确认后才切换
  };
  return { needRefresh, update };
}

// 2. 在线状态 hook
function onlineSubscribe(cb: () => void) {
  window.addEventListener('online', cb);
  window.addEventListener('offline', cb);
  return () => {
    window.removeEventListener('online', cb);
    window.removeEventListener('offline', cb);
  };
}
export function useOnlineStatus() {
  return useSyncExternalStore(
    onlineSubscribe,
    () => navigator.onLine,
    () => true,
  );
}

// 3. UI 接线：更新提示条 + 离线横幅
export function PwaBanners() {
  const { needRefresh, update } = useRegisterSW();
  const online = useOnlineStatus();

  return (
    <>
      {needRefresh && (
        <div role="status">
          有新版本可用
          <button onClick={update}>立即更新</button>
        </div>
      )}
      {!online && (
        <div role="alert">当前离线，部分功能不可用</div>
      )}
    </>
  );
}

// 4. sw 缓存策略（vite-plugin-pwa 配置摘要）
// workbox: {
//   navigateFallback: '/index.html',                 // App Shell
//   runtimeCaching: [
//     { urlPattern: /\.(js|css|woff2)$/, handler: 'CacheFirst' },   // 静态资源
//     { urlPattern: /\/api\//, handler: 'NetworkFirst',           // API：在线优先
//       options: { cacheName: 'api', networkTimeoutSeconds: 3 } }, // 超时回退缓存
//   ],
// }
```
## 第二十七章 综合大题（R19-178 ~ R19-200）
