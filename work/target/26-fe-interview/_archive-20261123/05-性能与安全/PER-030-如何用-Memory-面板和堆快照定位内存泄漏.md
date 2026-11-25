---
title: [PER-030] 如何用 Memory 面板和堆快照定位内存泄漏？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-030：如何用 Memory 面板和堆快照定位内存泄漏？

**答**：
- 流程：页面加载后拍快照 1 -> 复现可疑操作 -> 快照 2 -> 再操作 -> 快照 3。
- 切到 Comparison 视图对比相邻快照，看新增对象未回收的构造函数；Summary 视图看各类对象总量与 Retained Size。
- Retainers 链显示对象被谁引用住（闭包、全局变量、事件监听、Map），顺着链找持有者即可定位泄漏源头。
- 可以配合 `performance.memory` 做线上粗粒度监控，堆曲线只涨不跌即是疑似泄漏。

```javascript
// 线上粗粒度内存监控：JS 堆持续上涨且 GC 后不回落，基本可判定泄漏
function watchMemory(interval = 10000) {
  const timer = setInterval(() => {
    const mem = performance.memory; // Chrome 专有字段
    console.log('已用堆', Math.round(mem.usedJSHeapSize / 1024 / 1024), 'MB');
    console.log('堆上限', Math.round(mem.jsHeapSizeLimit / 1024 / 1024), 'MB');
    // 上报堆曲线，告警阈值超过上限的 80%
  }, interval);
  return () => clearInterval(timer);
}
watchMemory();

// 本地排查：三张堆快照对比定位泄漏对象
// 快照1 -> 操作可疑交互 -> 快照2 -> 再操作 -> 快照3
// 用 Comparison 视图找新增未释放的构造函数，看 Retainers 找持有链
```
