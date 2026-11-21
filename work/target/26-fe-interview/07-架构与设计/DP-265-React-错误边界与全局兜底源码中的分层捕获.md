---
title: [DP-265] 源码识别：错误捕获分层源码（边界/全局/上报）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-265：源码识别：错误捕获分层源码（边界/全局/上报）？
**答**:
- 分层职责链：组件层 ErrorBoundary（渲染错误）→ 全局 window.onerror/unhandledrejection（兜底异步）→ 顶层上报管道——每层处理自己管辖的错误，未处理逐层上抛。
- 观察者：三路错误源都汇入统一 emitter，归因（是否 React 渲染错误/资源错误/接口错误）后进 DP-264 管线。
- 状态机：错误处理状态（捕获 → 归因 → 降级决策 → 上报），降级决策是策略（重试/隐藏模块/整页兜底）。
- 识别要点：能说清"onerror 收不到 promise rejection（后者要 unhandledrejection）"与跨域脚本 error 的 Script error. 问题（crossorigin + CORS 头）。

```javascript
// 统一错误入口（源码级简化）
const errorBus = new Emitter();
window.addEventListener('error', e => {
  if (e.target instanceof HTMLElement) return errorBus.emit('resource', e.target.src ?? e.target.href); // 资源错误
  errorBus.emit('runtime', { msg: e.message, stack: e.error?.stack, lineno: e.lineno });
});
window.addEventListener('unhandledrejection', e => errorBus.emit('promise', { reason: String(e.reason) }));
// ErrorBoundary：componentDidCatch(e, info) → errorBus.emit('react', { e, componentStack: info.componentStack })
errorBus.on('*', ({ type, ...err }) => {
  const classified = classify(type, err);     // 归因策略
  pipeline.reduce((d, stage) => stage(d), classified);   // 采样/聚合/脱敏/上报（DP-264）
});
// Script error. 问题：<script src="..." crossorigin="anonymous"> + 响应头 Access-Control-Allow-Origin
```
