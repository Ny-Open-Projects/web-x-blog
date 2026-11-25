---
title: [ARC-042] 无界 wujie 的原理是什么？相比 qiankun 的取舍是什么？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-042：无界 wujie 的原理是什么？相比 qiankun 的取舍是什么？
**答**：
- wujie = iframe + Proxy 混合：JS 跑在 iframe 里（原生硬隔离，天然干净），DOM/渲染跑在主应用容器（iframe 内创建的 shadowRoot 被投影到主应用），样式在 iframe 内天然隔离。
- 取舍优点：隔离最强（不再手写沙箱）、子应用切换保活成本低、多实例简单；缺点：弹窗定位/事件冒泡跨 iframe 需要代理修复、路由同步靠 iframe 跳转代理、调试链路更绕。
- 适用：强隔离诉求、老应用接入成本低优先；对事件冒泡和 location 行为有强依赖的复杂应用需评估。

```typescript
// wujie 接入：JS 与 DOM 的分离运行示意
import { startApp } from 'wujie';

startApp({
  name: 'app-legacy',
  url: '//legacy.corp.com',
  el: '#container',            // DOM 渲染在主应用的容器里（shadowRoot 投影）
  // 内部机制：
  // 1. 隐藏 iframe 中执行子应用 JS —— window/document 原生隔离，无需手写沙箱
  // 2. iframe 内 document 上创建 shadowRoot，子应用把 DOM 挂进来
  // 3. shadowRoot 的根节点被“投影”到主应用容器显示
  // 4. 事件冒泡、location 赋值、弹窗定位等跨 iframe 行为由 wujie 代理修复
  sync: true,                  // 路由同步
  alive: true,                 // 保活模式：隐藏 iframe 保留状态
});
```
