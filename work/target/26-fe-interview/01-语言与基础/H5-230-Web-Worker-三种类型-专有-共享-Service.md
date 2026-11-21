---
title: [H5-230] Web Worker 的三种类型：专有/共享/Service
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, Worker]
type: 面试题
---

## H5-230：Web Worker 的三种类型：专有/共享/Service

**答**：
- Dedicated Worker：`new Worker(url)`，一对一专属，最常用
- Shared Worker：多个同源页面共享同一个 worker 实例（跨 tab 通信的早期方案），现在多被 BroadcastChannel 替代
- Service Worker：代理网络请求的「安装型」worker，生命周期与页面解耦，PWA 核心；注册协议与事件模型完全不同
- 共同限制：无 DOM、无 window（用 self）、同步 API 受限（localStorage 不可用）
- 面试话术：三种 worker 是「三个进程角色」——干活的、共享的、拦截网络的，别混为一谈

```javascript
// Shared Worker 跨 tab 通信示例
const sw = new SharedWorker('shared.js');
sw.port.postMessage('hello from tab1');
sw.port.onmessage = e => console.log('其他 tab 说:', e.data);
// shared.js
const ports = [];
onconnect = ({ ports: [port] }) => {
  ports.push(port);
  port.onmessage = e => ports.forEach(p => p.postMessage(e.data));
};
```
