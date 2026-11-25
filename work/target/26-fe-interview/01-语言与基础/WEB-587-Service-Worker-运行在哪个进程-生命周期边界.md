---
title: [WEB-587] Service Worker 运行在哪个进程，生命周期边界在哪
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, 浏览器架构]
type: 面试题
---

## WEB-587：Service Worker 运行在哪个进程，生命周期边界在哪

**答**：
- SW 是独立的脚本运行环境：Chrome 中通常在渲染进程内的独立「Service Worker」隔离世界（新架构里有专属的 dedicated 进程形态），与页面主线程分离，但同源
- 关键边界：SW 与页面不共享 JS 内存，只能 postMessage/MessageChannel/跨进程 fetch 事件通信；SW 无 DOM 访问
- 生命周期由浏览器进程侧管理：空闲数十秒即被终止（进程/线程回收），下次 fetch 事件或消息再唤醒——冷启动延迟要计入缓存策略（预热、navigationPreload）
- 多进程关联：SW 控制多个 tab 时，fetch 事件在 SW 世界串行/并行处理，页面跨进程等待 SW 响应——SW 慢会拖慢所有受控页面
- 实战提醒：SW 内不要做重计算（它占的是独立线程但会阻塞页面请求），大计算转 Worker 或后端；`skipWaiting`/`clients.claim` 的更新时序是面试高频坑

```javascript
// SW 冷启动优化: navigationPreload 提前发起网络请求
self.addEventListener('activate', (e) => {
  e.waitUntil(self.registration.navigationPreload.enable());
});
self.addEventListener('fetch', (e) => {
  if (e.request.mode === 'navigate') {
    e.respondWith(e.preloadResponse.then(res => res || fetch(e.request)));
  }
});
// 效果: SW 冷启动期间网络请求已并行进行, 不等 SW 脚本加载完
```
