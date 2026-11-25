---
title: [PER-519] 手写一个一次性采集 FCP/LCP/CLS/INP/长任务的全指标探针，并在页面卸载前可靠上报
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-519：手写一个一次性采集 FCP/LCP/CLS/INP/长任务的全指标探针，并在页面卸载前可靠上报

**答**：
- 一个探针覆盖"加载三指标 + 交互两指标 + 长任务"：用 PerformanceObserver 分别订阅 `paint/largest-contentful-paint/layout-shift/event/longtask`。
- 关键坑：LCP 在 unload 时可能还没定型，要在 `visibilitychange` 到 hidden 时停止观察并定稿；INP 要在交互结束后从 event entries 里取最差的 input delay+processing 组合。
- 上报用 `sendBeacon`（unload 可靠），带兜底 fetch keepalive。
- 评分点：hidden 时 finalize 的处理，这是 Web Vitals 上报正确性的分水岭。

```javascript

function vitalsProbe(report) {
  const data = { fcp: 0, lcp: 0, cls: 0, inp: 0, longTasks: 0 };
  const finalize = () => { report(JSON.stringify(data)); done = true; };
  let done = false;
  new PerformanceObserver(l => {
    if (done) return;
    const [e] = l.getEntries(); data.fcp = e.startTime;
  }).observe({ type: 'paint', buffered: true });
  new PerformanceObserver(l => {
    if (done) return;
    data.lcp = l.getEntries().at(-1).startTime;   // 取最后一个 LCP 候选
  }).observe({ type: 'largest-contentful-paint', buffered: true });
  new PerformanceObserver(l => {
    if (done) return;
    data.cls += l.getEntries().filter(e => !e.hadRecentInput)
                 .reduce((s, e) => s + e.value, 0); // 剔除 500ms 内有输入的偏移
  }).observe({ type: 'layout-shift', buffered: true });
  new PerformanceObserver(l => {
    if (done) return;
    l.getEntries().forEach(e => {
      const t = e.duration;                        // INP：取最差交互时长
      if (t > data.inp) data.inp = t;
    });
  }).observe({ type: 'event', buffered: true, durationThreshold: 40 });
  new PerformanceObserver(l => {
    data.longTasks += l.getEntries().length;
  }).observe({ type: 'longtask', buffered: true });

  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'hidden' && !done) finalize(); // 定稿时机
  });
  addEventListener('pagehide', () => { if (!done) finalize(); });   // 兜底
}
vitalsProbe(payload => {
  navigator.sendBeacon('/vitals', payload);         // unload 场景唯一可靠通道
});
```
