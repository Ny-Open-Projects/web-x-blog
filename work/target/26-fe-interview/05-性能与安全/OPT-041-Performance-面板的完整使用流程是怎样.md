---
title: [OPT-041] Performance 面板的完整使用流程是怎样的？如何从录制到定位再到验证？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-041：Performance 面板的完整使用流程是怎样的？如何从录制到定位再到验证？

**答**：
- 标准四步流：**录制**（选 Machine/CPU 4x slowdown 模拟目标机型）→ **看火焰图**（Main 线程，红色 Layout、紫色 Recalculate Style、黄色 Script）→ **定位**（Bottom-Up 视图按 Self Time 排序找热点函数）→ **验证**（改完同条件重录对比）。
- 录制时打开 Screenshots 和 Memory 轨道，能同时发现强制同步布局与内存抖动。
- 定位技巧：先在 Timings 轨道看 FP/FCP/LCP 标尺，锁定"慢在哪一段"，再去 Main 轨道展开对应时间段，比漫无目的看火焰图高效得多。
- Bottom-Up 比 Call Tree 更适合找"自己贵"的函数，Call Tree 适合看"谁调用出来的"。

```javascript
// 一一对应：用 CDP 脚本化录制 Performance Trace，替代手工面板操作（可进 CI）
// node trace.mjs —— 对目标页面采集 trace 并输出耗时 top 函数
import puppeteer from 'puppeteer';

const browser = await puppeteer.launch({
  args: ['--cpu-throttling-rate=4'], // 等价于面板里的 CPU 4x slowdown
});
const page = await browser.newPage();
await page.tracing.start({ categories: ['devtools.timeline', 'v8.execute'] });
await page.goto('https://example.com', { waitUntil: 'networkidle0' });
const buffer = await page.tracing.stop();

const events = JSON.parse(buffer.toString()).traceEvents;
// 统计 RunTask 长任务与函数级自耗时（用 ProfileChunk 事件近似）
const longTasks = events.filter(
  (e) => e.name === 'RunTask' && e.dur > 50_000 // dur 单位微秒，>50ms 即 Long Task
);
console.log('长任务数量:', longTasks.length);
console.log('最长任务(ms):', (Math.max(...longTasks.map((t) => t.dur)) / 1000).toFixed(1));
await browser.close();
// 改代码后重跑本脚本，对比"长任务数量/最长任务"两个数字即为验证
```
