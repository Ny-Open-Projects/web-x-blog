---
title: [TST-842] 笔试：手写一个「长任务(long task)检测与归因」工具
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-842：笔试：手写一个「长任务(long task)检测与归因」工具
**答**：
- 需求：实现 observeLongTasks(thresholdMs, callback) —— 用 PerformanceObserver 监听 longtask 条目，回调输出时长与归因来源。
- 规则：过滤时长 >= thresholdMs 的任务；归因取 attribution 中最主要的容器名/容器类型；去重连续相同归因。
- 边界：浏览器不支持 PerformanceObserver 时降级为轮询 performance.getEntriesByType('longtask')或直接返回空。

```javascript
function observeLongTasks(thresholdMs = 50, callback) {
  if (typeof PerformanceObserver === 'undefined') {
    callback({ unsupported: true, tasks: [] });
    return () => {};
  }
  const tasks = [];
  let lastAttr = null;
  const observer = new PerformanceObserver(list => {
    for (const entry of list.getEntries()) {
      if (entry.duration < thresholdMs) continue;
      const attr = entry.attribution?.[0];
      const source = attr ? `${attr.containerName || attr.containerType}` : 'unknown';
      if (source === lastAttr) continue; // 去重连续相同归因
      lastAttr = source;
      tasks.push({ duration: Math.round(entry.duration), source, start: entry.startTime });
    }
    callback({ tasks: [...tasks] });
  });
  observer.observe({ entryTypes: ['longtask'] });
  return () => observer.disconnect(); // 返回清理函数
}
const stop = observeLongTasks(50, console.log);
// 页面操作后调用 stop() 断开观察
```
**评分点**：
- 用 PerformanceObserver 监听 longtask 并过滤阈值，技术选型正确。
- 归因到 containerName/containerType，能定位是哪个脚本/iframe 导致卡顿。
- 不支持时降级而非报错，边界健壮。
- 返回 disconnect 清理函数，避免观察者泄漏——加分项。
