---
title: [H5-288] PWA 与原生混用：deep link 场景
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, PWA]
type: 面试题
---

## H5-288：PWA 与原生混用：deep link 场景

**答**：
- 混合形态普遍：营销 H5 唤起原生 App、原生 App 内嵌 H5 活动、PWA 装桌面后点通知进特定页面
- 路由一致性：start_url 带 source 参数区分入口（pwa/推送/scheme），统一进页面路由层处理
- 通知深链：PWA push 的 notificationclick 里 `clients.openWindow(url)` 打开指定路由；SW 控制下命中缓存秒开
- 互相跳转边界：PWA 内用 scheme 唤起原生支付/客服，原生返回后 PWA 状态要保持（beforeunload 不触发，靠 visibilitychange 保存）
- 面试话术：混用架构的关键是「入口归因 + 状态保持 + 降级链路」三件事

```javascript
self.addEventListener('notificationclick', (e) => {
  const url = e.notification.data?.deepLink || '/';
  e.waitUntil(clients.matchAll({ type: 'window' }).then(list => {
    const win = list.find(c => c.url.startsWith(self.registration.scope));
    return win ? (win.navigate(url), win.focus()) : clients.openWindow(url); // 复用已开窗口
  }));
});
```
