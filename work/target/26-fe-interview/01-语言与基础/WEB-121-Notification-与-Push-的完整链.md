---
title: [WEB-121] Notification 与 Push 的完整链路是什么？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-121：Notification 与 Push 的完整链路是什么？
**答**：
- 链路：用户授权 Notification.requestPermission → SW 注册 → pushManager.subscribe 拿到 endpoint（带 VAPID 公钥）→ 服务端向该 endpoint 发加密推送 → SW 收 push 事件 → showNotification 展示，点击可聚焦/打开页面。
- 关键约束：推送必须经过 Service Worker（页面关闭也能送达）；`userVisibleOnly: true` 强制每条推送都要有可见通知，防静默骚扰。
- VAPID 是自签名的服务器身份，避免依赖各家厂商后台；endpoint 送达依赖浏览器厂商的推送服务（FCM/APNs 系）。
- 权限被拒后 requestPermission 不再弹窗，只能在设置里恢复——授权时机放用户主动点击处。

```javascript
// 前端完整链路
const permission = await Notification.requestPermission(); // 1. 授权（放用户手势里）
if (permission !== 'granted') return;
const reg = await navigator.serviceWorker.register('/sw.js');
const sub = await reg.pushManager.subscribe({               // 2. 订阅拿 endpoint
  userVisibleOnly: true,
  applicationServerKey: urlBase64ToUint8(VAPID_PUBLIC_KEY), // 3. VAPID 公钥
});
await fetch('/api/push-subscribe', {                        // 4. endpoint 交给服务端
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(sub),
});
```

```javascript
// sw.js —— 服务端推送到达与点击处理
self.addEventListener('push', (e) => {
  const data = e.data.json();
  e.waitUntil(self.registration.showNotification(data.title, {
    body: data.body, icon: '/icon.png', tag: 'msg', // tag 合并同类通知
    data: { url: '/inbox' },
  }));
});
self.addEventListener('notificationclick', (e) => {
  e.notification.close();
  e.waitUntil(clients.openWindow(e.notification.data.url));
});
```
