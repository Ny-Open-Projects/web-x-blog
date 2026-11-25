---
title: [PER-271] performance.memory 有什么用？如何建立"内存基线"做线上内存回归监控？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-271：performance.memory 有什么用？如何建立"内存基线"做线上内存回归监控？

**答**：
- `performance.memory`（Chrome，需要 enablePreciseMemoryInfo 或默认粗粒度）给 jsHeapSizeLimit / totalJSHeapSize / usedJSHeapSize，是 RUM 侧唯一能拿到的运行时堆水位。粗粒度有量化抖动（约 1MB 桶），只适合趋势不适合绝对值。
- 内存基线做法：页面空闲期（visibility visible + 无 longtask）定时采样 usedJSHeapSize，上报"空闲水位"与"操作后峰值水位"；版本对比——新版本发布后对比同页面同场景的水位分布（p75），台阶上涨即内存回归。
- 判定注意：采样要在 GC 后才准——连续采样多次取最小值近似"GC 后水位"；页面之间不可比（业务不同），必须按模板对比。
- 替代口径：Safari/Firefox 无此 API，只能用堆快照（实验室）或自研 native 探针（如公司级 WebView 监控）；RUM 内存监控是 Chrome-only 的补充项，不能作为唯一依据。

```javascript
// 空闲内存基线采样：取 10 次采样最小值近似 GC 后水位
function sampleHeapBaseline() {
  const m = performance.memory;                    // Chrome only
  if (!m) return null;
  return Math.round(m.usedJSHeapSize / 1048576);   // MB
}
async function collectBaseline() {
  if (document.visibilityState !== 'visible') return;
  const samples = [];
  for (let i = 0; i < 10; i++) {                   // 连续采 10 次
    samples.push(sampleHeapBaseline());
    await new Promise(r => requestIdleCallback?.(r) ?? setTimeout(r, 200));
  }
  const clean = samples.filter(s => s != null);
  if (clean.length) report({ type: 'heap-baseline', mb: Math.min(...clean) }); // 最小值 ≈ GC 后
}
setInterval(collectBaseline, 60000);
// 服务端按 page × version 聚合：新版本 p75 比旧版高 > 30% => 内存回归告警
```
