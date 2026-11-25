---
title: [WCN-251] Signals 在 SSR 场景（服务端无事件循环 flush）如何处理？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-251：Signals 在 SSR 场景（服务端无事件循环 flush）如何处理？
**答**：
- SSR：信号读取直接求值（无订阅无调度），渲染即纯函数求值。
- 水合：客户端从「服务端值」初始化信号，首帧不重算（值已一致）——避免水合后闪烁。
- 序列化：信号初始值随 HTML 下发（__SIGNALS__ 状态），客户端 restore。
- 禁止项：SSR 期间注册 effect（无意义且可能泄漏）——环境守卫。

```javascript
// SSR：信号作为纯值
const price = signal(props.price);      // 服务端直接读取渲染
// 客户端 restore：初始值来自 HTML，不触发 effect 首跑
hydrateSignals(window.__SIGNALS__);
r
```
