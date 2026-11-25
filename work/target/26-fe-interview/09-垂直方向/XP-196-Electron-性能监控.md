---
title: [XP-196] Electron 性能监控：主进程与渲染进程指标
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 笔试题, 27]
type: 笔试题
---

## XP-196：Electron 性能监控：主进程与渲染进程指标

**答**：
- 题目：Electron 性能监控——主进程 CPU/内存（process.memoryUsage）、渲染进程指标（Chromium metrics）、GPU 进程崩溃、启动耗时分解。
- 思路：主进程 process.memoryUsage()（heap/external）；app.getAppMetrics()（全进程指标含渲染进程）；启动分段（ready 事件前各阶段耗时）；崩溃监听（render-process-gone）。
- 评分点：进程级指标；启动分段；崩溃监听。

```javascript
class ElectronMonitor {
  start() {
    setInterval(() => {                                             // 主进程指标
      const mem = process.memoryUsage();                             // heapUsed/external
      const all = app.getAppMetrics();                               // 全进程（含渲染）
      all.forEach(m => {                                              // 每进程 CPU/内存
        if (m.memory.workingSetSize > 500 * 1024)                     // >500MB 渲染进程
          fire('renderer-memory-high', { pid: m.pid, mb: m.memory.workingSetSize / 1024 });
      });
    }, 30000);
    app.on('render-process-gone', (e, details) => {                    // 渲染进程崩溃
      fire('renderer-crash', { reason: details.reason, exitCode: details.exitCode });
      recoverRenderer(details);                                        // 恢复（重建窗口）
    });
    // 启动分段：main-ready → window-created → dom-ready → first-paint
    const stages = [];                                               // 逐段记录
  }
}
```
