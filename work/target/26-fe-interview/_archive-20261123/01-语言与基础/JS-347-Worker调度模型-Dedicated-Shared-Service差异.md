---
title: [JS-347] Worker 调度模型：Dedicated/Shared/Service 三类差异
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## JS-347：Worker 调度模型：Dedicated/Shared/Service 三类差异

**答**：
- Dedicated Worker：一对一，页面关闭即终止——重计算/图片处理的默认选择；生命周期跟页面，无状态共享（除 SAB）
- Shared Worker：多页面（同源）共享一个实例——跨 tab 状态聚合（多 tab 聊天连接复用），消息走 port；支持度注意（Safari 现已支持，Chrome 好）
- Service Worker：独立于页面生命周期（可被杀/唤醒），代理网络事件——PWA 核心，事件驱动模型，与 Dedicated 语义完全不同（不是「为页面算东西」而是「接管请求」）
- 调度共性：Worker 与主线程消息异步（postMessage），transferable 避免拷贝；Worker 内也可再嵌 Worker（嵌套线程池）
- 选型速记：算东西用 Dedicated、跨 tab 共享用 Shared、拦网络用 Service——三者职责不可互换

```javascript
// Shared Worker: 多 tab 复用一个 WebSocket
// shared.js:
const ports = new Set();
const ws = new WebSocket('wss://im.example.com');
ws.onmessage = (e) => ports.forEach(p => p.postMessage(e.data));
onconnect = (e) => {
  const port = e.ports[0];
  ports.add(port);
  port.onmessage = ({ data }) => ws.send(data);   // 所有 tab 共享连接
  port.start();
};
```
