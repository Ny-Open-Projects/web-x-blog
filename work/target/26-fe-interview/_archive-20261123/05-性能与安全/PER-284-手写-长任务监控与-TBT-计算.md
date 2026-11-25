---
title: [PER-284] 笔试题：手写 TBT（Total Blocking Time）计算器（仅统计 FCP 到 TTI 窗口内的长任务）
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-284：手写 TBT（Total Blocking Time）计算器（仅统计 FCP 到 TTI 窗口内的长任务）

**题目**：实现 TBT 计算：① TBT 定义——FCP 到 TTI（这里用"5 秒无长任务且无网络活动"的 quiet window 近似）窗口内，所有 >50ms 任务超出 50ms 部分之和；② 实现 `trackTBT(report)`：监听 FCP 与 longtask，检测 quiet window（5s 内无 longtask 且无进行中的 fetch/资源加载）判定 TTI，到点上报 TBT；③ 若 15s 未达到 quiet window，按当前累计值上报并标记 timeout。

**答**：TBT 是实验室可精确算的指标，RUM 近似关键是窗口定义：FCP 起点 + quiet window 终点。资源加载活动用 PerformanceObserver 的 resource 条目时间判断（近似：记录最后网络活动时间）。

```javascript
function trackTBT(report, { quietMs = 5000, maxWait = 15000 } = {}) {
  let fcp = null, tbt = 0, lastNetwork = 0, reported = false;
  const t0 = performance.now();

  new PerformanceObserver((l) => {
    const e = l.getEntries()[0];
    if (e.name === 'first-contentful-paint') fcp = e.startTime;
  }).observe({ type: 'paint', buffered: true });

  new PerformanceObserver((l) => {
    for (const e of l.getEntries()) {
      lastNetwork = Math.max(lastNetwork, e.startTime + e.duration);
      if (fcp != null && e.startTime >= fcp) tbt += Math.max(0, e.duration - 50);
    }
  }).observe({ type: 'longtask', buffered: true });

  new PerformanceObserver((l) => {                 // 网络活动时间线（近似 TTI 条件）
    for (const e of l.getEntries()) lastNetwork = Math.max(lastNetwork, e.responseEnd);
  }).observe({ type: 'resource', buffered: true });

  const poll = setInterval(() => {
    if (reported) return clearInterval(poll);
    const now = performance.now();
    const quiet = now - Math.max(lastNetwork, lastLongTaskAt) >= quietMs;
    if (fcp != null && quiet) { reported = true; clearInterval(poll);
      report({ type: 'TBT', value: Math.round(tbt), fcp: Math.round(fcp) }); }
    if (now - t0 > maxWait && !reported) { reported = true; clearInterval(poll);
      report({ type: 'TBT', value: Math.round(tbt), timeout: true }); }
  }, 1000);
  let lastLongTaskAt = 0;
  // 注：lastLongTaskAt 需在 longtask 回调中更新：lastLongTaskAt = Math.max(lastLongTaskAt, e.startTime + e.duration)
}
```

**评分点**：
- TBT 语义正确：仅统计 FCP 之后、超 50ms 的部分（不是全部时长）。
- quiet window 双条件：无长任务 + 无网络活动，5s 连续。
- 超时兜底（15s）带 timeout 标记，不无限等待。
- 循环轮询结束条件完整（reported 后 clearInterval，无泄漏）。
