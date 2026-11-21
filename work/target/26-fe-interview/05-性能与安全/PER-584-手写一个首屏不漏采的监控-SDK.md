---
title: [PER-584] 手写一个首屏不漏采的监控 SDK 引导器：预埋钩子 + buffered 补采 + 指标 finalize 时序
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-584：手写一个首屏不漏采的监控 SDK 引导器：预埋钩子 + buffered 补采 + 指标 finalize 时序

**答**：
- 把 583 落成完整代码：预埋阶段收集 error/unhandledrejection；SDK 阶段接管并回放；PerformanceObserver 全 buffered；hidden 时 finalize 指标并停止观察。
- 要点：unhandledrejection 的预埋也要做（Promise 错误走不同通道）；finalize 后的 entry 丢弃（防止 hidden 后统计被污染）；回放预埋错误时打 `late:true` 标记区分时段。
- 边界：SDK 自身加载失败时预埋缓冲要能落地（简单 beacon 兜底）。
- 评分点：双通道预埋（error+rejection）与 finalize 时序。

```javascript

// ---- 第 1 部分：内联 <head> 的预埋（同步执行）----
(function () {
  const log = (window.__pre = { err: [], rej: [] });
  addEventListener('error', e => log.err.push({ msg: e.message, ts: Date.now(), file: e.filename }), true);
  addEventListener('unhandledrejection', e => log.rej.push({ reason: String(e.reason), ts: Date.now() }));
})();
// ---- 第 2 部分：SDK 主体 ----
function bootSdk(report) {
  const obs = [];
  const vital = { lcp: 0, cls: 0 };
  const push = (type, o) => report(type, o);
  obs.push(new PerformanceObserver(l => l.getEntries().forEach(e => { vital.lcp = e.startTime; }))
    .observe({ type: 'largest-contentful-paint', buffered: true }));
  obs.push(new PerformanceObserver(l => l.getEntries().forEach(e => {
    if (!e.hadRecentInput) vital.cls += e.value;
  })).observe({ type: 'layout-shift', buffered: true }));
  // 回放预埋期错误，带 late 标记
  window.__pre.err.forEach(e => push('error', { ...e, late: true }));
  window.__pre.rej.forEach(e => push('rejection', { ...e, late: true }));
  delete window.__pre;
  addEventListener('error', e => push('error', { msg: e.message, ts: Date.now() }), true);
  addEventListener('unhandledrejection', e => push('rejection', { reason: String(e.reason) }));
  const finalize = () => {                                 // hidden 时定稿并停观察
    obs.forEach(o => o.disconnect());
    push('vitals-final', vital);
  };
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'hidden') finalize();
  }, { once: false });
}
```
