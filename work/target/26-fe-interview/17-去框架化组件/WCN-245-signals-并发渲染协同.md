---
title: [WCN-245] Signals 与框架并发渲染（React Concurrent/Solid transition）如何协同？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-245：Signals 与框架并发渲染（React Concurrent/Solid transition）如何协同？
**答**：
- transition 语义：低优先级更新期间 UI 保持旧值——Signals 需要「双缓冲」（读写分离的版本号）。
- Solid 的 startTransition：把信号写入挂起，transition 结束才对视图可见。
- React 侧（signals 包）：适配 useSyncExternalStore 的 getSnapshot 必须稳定（并发渲染多次调用一致性）。
- 关键约束：并发渲染下「读必须纯」——信号读取不能有副作用（缓存一致性依赖此）。

```javascript
// React 适配层要点
const subscribe = (cb) => onSignalChange(cb);
const getSnapshot = () => sig.value;   // 必须幂等稳定，否则并发渲染无限循环
useSyncExternalStore(subscribe, getSnapshot);
r
```
