---
title: [H5-255] Push API 推送怎么做：服务端与前端配合
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, PWA]
type: 面试题
---

## H5-255：Push API 推送怎么做：服务端与前端配合

**答**：
- 全链路：前端 subscription（含 endpoint + 密钥）→ 存服务端 → 服务端用 web-push 库向推送服务（FCM/Mozilla autopush）发加密消息 → SW 的 push 事件接收 → showNotification 展示
- 关键代码点：`registration.pushManager.subscribe({ userVisibleOnly: true, applicationServerKey: VAPID 公钥 })`
- 必须展示通知：userVisibleOnly: true 是规范要求，推送不显示通知会被浏览器压制订阅
- 权限体验：不要页面加载就弹授权（拒绝率高），在用户主动场景（如开启提醒按钮）触发 Notification.requestPermission
- 失效清理：推送返回 410 Gone 说明订阅失效，服务端要清理该 endpoint

```javascript
// SW 内
self.addEventListener('push', (e) => {
  const data = e.data.json();
  self.registration.showNotification(data.title, { body: data.body, icon: '/icon.png', data });
});
self.addEventListener('notificationclick', (e) => {
  e.notification.close();
  clients.openWindow(e.notification.data.url);
});
```
