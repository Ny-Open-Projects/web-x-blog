---
title: [PER-552] 手写一个页面性能 trace 导出与离线分析工具：从 Performance 面板导出的 trace JSON 里统计长任务与布局抖动
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-552：手写一个页面性能 trace 导出与离线分析工具：从 Performance 面板导出的 trace JSON 里统计长任务与布局抖动

**答**：
- Chrome trace 事件的 关键 channel：`RunTask`/`FireAnimationFrame` 等主线程事件可还原长任务，`Layout`/`UpdateLayoutTree` 事件统计布局开销；分析器解析 JSON 按 tid=主线程过滤。
- 要点：trace 时间戳是微秒（us）；主线程识别取 renderer 进程中事件量最大的线程；输出长任务 top10 与布局耗时占比两个核心数字。
- 边界：trace 文件可达几百 MB，要用流式或分块解析，统计中不要保留完整事件数组。
- 评分点：主线程识别与长任务聚合（相邻 RunTask 小于阈值间隔合并）。

```javascript

const fs = require('fs');
function analyzeTrace(file, { longTaskMs = 50 } = {}) {
  const trace = JSON.parse(fs.readFileSync(file, 'utf8'));
  const evs = trace.traceEvents ?? trace;
  // 识别 renderer 主线程：同 pid 下事件最多的 tid
  const byThread = {};
  evs.forEach(e => { if (e.ph === 'X') (byThread[`${e.pid}:${e.tid}`] ??= []).push(e); });
  const [mainKey, main] = Object.entries(byThread).sort((a, b) => b[1].length - a[1].length)[0];
  // 长任务：相邻 RunTask 合并（间隔 < 1ms 视为同一任务）
  let tasks = [], cur = null;
  for (const e of main.filter(e => e.name === 'RunTask').sort((a, b) => a.ts - b.ts)) {
    if (cur && (e.ts - (cur.ts + cur.dur)) < 1000) cur.dur = e.ts + e.dur - cur.ts; // us
    else { if (cur) tasks.push(cur); cur = { ts: e.ts, dur: e.dur }; }
  }
  if (cur) tasks.push(cur);
  const layoutMs = main.filter(e => e.name === 'Layout' || e.name === 'UpdateLayoutTree')
    .reduce((s, e) => s + e.dur, 0) / 1000;
  const longTasks = tasks.filter(t => t.dur > longTaskMs * 1000)
    .sort((a, b) => b.dur - a.dur).slice(0, 10)
    .map(t => ({ startMs: +((t.ts - evs[0].ts) / 1000).toFixed(1), durMs: +(t.dur / 1000).toFixed(1) }));
  return { thread: mainKey, longTasks, layoutTotalMs: +layoutMs.toFixed(1) };
}
console.log(analyzeTrace(process.argv[2]));
```
