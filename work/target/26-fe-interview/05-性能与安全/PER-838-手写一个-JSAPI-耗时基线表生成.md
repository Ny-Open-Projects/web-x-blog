---
title: [PER-838] 手写一个 JSAPI 耗时基线表生成器：批量跑分各 API 耗时输出基线与超时标注
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-838：手写一个 JSAPI 耗时基线表生成器：批量跑分各 API 耗时输出基线与超时标注

**答**：
- 需求：输入跑分记录 [{api, ms}]（每 API 多次采样），生成基线表：每 API 的 p50/p75/p95、样本数；p95 超 100ms 的标注 heavy；样本 < 10 的标注 insufficient；输出按 p95 降序。另提供 compare(current, baseline) 找出比基线劣化 > 50% 的 API 回归项。
- 边界：异常值（负数/超 30s）剔除；同 API 记录聚合；heavy 阈值可配置。
- 评分点：分位数计算；insufficient 与 heavy 双标注；回归对比逻辑。

```javascript
function apiBaseline(records, { heavyMs = 100, minSample = 10 } = {}) {
  const clean = records.filter(r => r.ms > 0 && r.ms < 30000);   // 异常剔除
  const by = {};
  for (const r of clean) (by[r.api] ??= []).push(r.ms);
  const pct = (a, p) => { const s = [...a].sort((x, y) => x - y); return s[Math.min(s.length - 1, Math.floor(s.length * p))]; };
  return Object.entries(by).map(([api, arr]) => ({
    api, n: arr.length,
    p50: +pct(arr, 0.5).toFixed(1), p75: +pct(arr, 0.75).toFixed(1), p95: +pct(arr, 0.95).toFixed(1),
    heavy: pct(arr, 0.95) > heavyMs,
    insufficient: arr.length < minSample,
  })).sort((a, b) => b.p95 - a.p95);
}
function compare(current, baseline, { regTh = 0.5 } = {}) {
  const base = Object.fromEntries(baseline.map(b => [b.api, b.p95]));
  return current.filter(c => base[c.api] && c.p95 > base[c.api] * (1 + regTh))
    .map(c => ({ api: c.api, baseP95: base[c.api], nowP95: c.p95,
      regression: +((c.p95 / base[c.api] - 1) * 100).toFixed(1) + '%' }));
}
```
