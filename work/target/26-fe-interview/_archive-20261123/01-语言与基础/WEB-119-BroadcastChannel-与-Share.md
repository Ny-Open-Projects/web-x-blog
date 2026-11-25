---
title: [WEB-119] BroadcastChannel 与 SharedWorker 各适合什么跨页通信场景？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-119：BroadcastChannel 与 SharedWorker 各适合什么跨页通信场景？
**答**：
- BroadcastChannel：同源所有标签页广播，API 最简单，一收一发全异步；适合主题切换、登录态同步、多标签互踢。
- SharedWorker：一个工作线程被多个标签页共享，内部可维护状态与连接表，能实现"标签页计数、消息路由中心"；IE/部分老环境不支持，Safari 曾长期缺失。
- 兜底对比：storage 事件兼容性最好但语义绕（必须真的写 localStorage）；Service Worker postMessage 也能做中转。
- 三者都不跨源；跨源只能服务端中转。

```javascript
// BroadcastChannel：多标签页主题同步
const bc = new BroadcastChannel('app-sync');
bc.onmessage = (e) => {
  if (e.data.type === 'theme') applyTheme(e.data.value);
  if (e.data.type === 'logout') location.href = '/login'; // 一处退出处处退出
};
document.querySelector('#theme-btn').onclick = () => {
  const value = 'dark';
  applyTheme(value);
  bc.postMessage({ type: 'theme', value }); // 广播给其他标签页
};
```

```javascript
// shared.js —— SharedWorker：多标签页共享一个连接与状态
const ports = [];                    // worker 全局连接表：所有标签页的 MessagePort
let pages = 0;                       // worker 全局状态：标签页计数
onconnect = (e) => {
  const port = e.ports[0];
  ports.push(port);                  // 必须先登记，否则后续消息无处转发
  port.onmessage = (ev) => {
    pages++; // 占位示例：真实业务在此处理消息
    // 路由中心：一个标签页的消息转发给其余所有标签页
    ports.forEach((p) => { if (p !== port) p.postMessage(ev.data); });
  };
  port.postMessage({ type: 'count', pages });
  port.start();
};
```

```javascript
// main.js —— 每个标签页连一次
const worker = new SharedWorker('/shared.js');
worker.port.onmessage = (e) => console.log('来自共享 worker', e.data);
worker.port.postMessage({ type: 'ping' });
worker.port.start();
```
