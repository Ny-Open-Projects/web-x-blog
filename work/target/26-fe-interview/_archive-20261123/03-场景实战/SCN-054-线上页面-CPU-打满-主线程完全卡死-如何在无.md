---
title: [SCN-054] 线上页面 CPU 打满、主线程完全卡死，如何在无法打 log 的情况下定位问题代码？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-054：线上页面 CPU 打满、主线程完全卡死，如何在无法打 log 的情况下定位问题代码？
**答**：
- 死循环会阻塞主线程，页面内所有手段（console、监控 SDK 的 JS 执行部分）都失效，必须用"外部观察者"：Web Worker 心跳看门狗。
- 主线程定时向 Worker 喂狗，Worker 发现超过阈值没收到心跳即判定主线程被阻塞，把阻塞时长与最后的行为现场上报。
- 开发期用 Performance 面板长录制找 Long Task 定位具体函数；线上看门狗负责"发现 + 归因到版本/页面/操作路径"。

```javascript
// 主线程看门狗：worker 定时检查心跳，主线程被阻塞时上报最后现场
// watchdog-worker.js —— 独立线程不受主线程阻塞影响
let lastBeat = Date.now();
self.onmessage = (e) => { lastBeat = e.data.time; };
setInterval(() => {
  if (Date.now() - lastBeat > 3000) {
    fetch('/api/monitor', { method: 'POST', body: JSON.stringify({
      type: 'main-thread-blocked',
      blockedMs: Date.now() - lastBeat,   // 阻塞时长，区分长任务与死循环
      lastRoute: lastRoute,               // 主线程每次路由变化时同步给 worker
    }) });
  }
}, 1000);

// 主线程：每秒喂狗 + 同步上下文
const worker = new Worker('watchdog-worker.js');
setInterval(() => worker.postMessage({ time: Date.now(), lastRoute }), 1000);
```
