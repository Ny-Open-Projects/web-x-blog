---
title: [WCN-278] Worker 中运行信号计算（主线程只渲染）的架构？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-278：Worker 中运行信号计算（主线程只渲染）的架构？
**答**：
- 信号图整体在 Worker：计算/派生/业务逻辑全在子线程；主线程只收「变更补丁」。
- 通信：Worker 广播变更集（signalId → value），主线程代理信号 apply。
- 往返：主线程用户输入 postMessage 给 Worker 写信号。
- 收益：重计算（过滤/排序万条）不阻塞主线程；成本：序列化与延迟（<5ms 可接受）。

```javascript
// worker: 权威信号图
self.onmessage = ({ data }) => { signals[data.id].value = data.v; };
// 主线程：代理信号
const proxySig = { get value() { return cache[id]; },
  set value(v) { worker.postMessage({ id, v }); cache[id] = v; } };  // 乐观写
r
```
